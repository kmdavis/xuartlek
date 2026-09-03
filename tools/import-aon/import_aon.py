#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "requests>=2.31"]
# ///
"""
Import Pathfinder 2E Remaster rules from Archives of Nethys into Obsidian markdown.

Source of truth: https://2e.aonprd.com/Rules.aspx
Scope: the five Remaster "Core" books.

Two passes, because correct wikilinks need the full ID map before any conversion:
  1. Fetch the rules index, walk every section, cache each page, and record
     every heading ID found (including subsections the index does not list).
  2. Convert cached HTML to markdown, resolving AoN links against that map.

Pages are cached on disk. Re-running only fetches what is missing unless
--refresh is passed.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

from books import ALL_BOOKS, REMASTER_RULEBOOKS
from linkmap import LinkMap

BASE = "https://2e.aonprd.com"
INDEX_URL = f"{BASE}/Rules.aspx"

# Matched against the <summary> text in the index. Two books in the shared list
# (Monster Core 2, Secrets of the Unlit Star) have no Rules sections at all and
# are simply absent here; that is expected, not a failure.
CORE_BOOKS = ALL_BOOKS

# Short citation codes, mirroring the pre-Remaster SRD's "<sup>CRB p. 7</sup>".
BOOK_CODES = REMASTER_RULEBOOKS

USER_AGENT = "xuartlek-srd-importer/1.0 (personal Obsidian vault; contact via github.com/kmdavis)"


# --------------------------------------------------------------------------
# Index model
# --------------------------------------------------------------------------


@dataclass
class Entry:
    """One index-listed rule that gets its own markdown file."""

    aon_id: int
    title: str
    book: str
    chapter_id: int | None  # None when this entry *is* the chapter
    path: Path = field(init=False)

    @property
    def is_chapter(self) -> bool:
        return self.chapter_id is None


def slugify(text: str) -> str:
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def parse_index(index_html: str, books: list[str]) -> list[Entry]:
    """Walk the index.

    The markup nests badly (``<b><u><a>...</a></b></u>``), so rather than trust a
    parsed tree we scan each book's raw HTML in document order and track whether
    we are inside a ``<ul>``. Anchors outside a list are chapters; anchors inside
    one are sections of the most recent chapter.
    """
    entries: list[Entry] = []
    book_blocks = re.findall(
        r"<details>\s*<summary class='hd-1'>(.*?)</summary>(.*?)</details>",
        index_html,
        re.S,
    )
    if not book_blocks:
        raise SystemExit("Could not find any <details> book blocks in the index.")

    found_books = set()
    token = re.compile(
        r"(?P<ul_open><ul>)|(?P<ul_close></ul>)|"
        r'<a href="Rules\.aspx\?ID=(?P<id>\d+)[^"]*">(?P<title>.*?)</a>',
        re.S,
    )

    for raw_name, block in book_blocks:
        name = html.unescape(re.sub(r"<[^>]+>", "", raw_name)).strip()
        found_books.add(name)
        if name not in books:
            continue

        depth = 0
        current_chapter: int | None = None
        for m in token.finditer(block):
            if m.group("ul_open"):
                depth += 1
                continue
            if m.group("ul_close"):
                depth = max(0, depth - 1)
                continue

            aon_id = int(m.group("id"))
            title = html.unescape(re.sub(r"<[^>]+>", "", m.group("title"))).strip()
            if not title:
                continue

            if depth == 0:
                current_chapter = aon_id
                entries.append(Entry(aon_id, title, name, None))
            else:
                entries.append(Entry(aon_id, title, name, current_chapter))

    missing = [b for b in books if b not in found_books]
    if missing:
        print(f"  note: no Rules sections for: {', '.join(missing)}", file=sys.stderr)
    return entries


def assign_paths(entries: list[Entry], root: Path) -> None:
    """Give every entry an output path.

    A chapter with sections becomes ``book/chapter/index.md`` so Quartz and
    Obsidian both treat it as the folder's landing page. A chapter with no
    sections is just ``book/chapter.md``.
    """
    by_id = {e.aon_id: e for e in entries}
    has_children = {e.chapter_id for e in entries if e.chapter_id is not None}

    for e in entries:
        book_dir = root / slugify(e.book)
        if e.is_chapter:
            if e.aon_id in has_children:
                e.path = book_dir / slugify(e.title) / "index.md"
            else:
                e.path = book_dir / f"{slugify(e.title)}.md"
        else:
            chapter = by_id.get(e.chapter_id)
            chapter_slug = slugify(chapter.title) if chapter else "misc"
            e.path = book_dir / chapter_slug / f"{slugify(e.title)}.md"


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------


class Fetcher:
    def __init__(self, cache_dir: Path, delay: float, refresh: bool):
        self.cache_dir = cache_dir
        self.delay = delay
        self.refresh = refresh
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._fetched = 0

    def get(self, url: str, key: str) -> str:
        path = self.cache_dir / f"{key}.html"
        if path.exists() and not self.refresh:
            return path.read_text(encoding="utf-8")
        if self._fetched:
            time.sleep(self.delay)
        resp = self.session.get(url, timeout=30)
        resp.raise_for_status()
        self._fetched += 1
        # AoN serves CRLF. The repo is eol=lf with core.safecrlf set, so git
        # refuses to add a file containing CR. Normalise at the boundary.
        text = normalise_newlines(resp.text)
        path.write_text(text, encoding="utf-8")
        return text

    @property
    def network_calls(self) -> int:
        return self._fetched


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------

SKIP_CLASSES = {"sibling-navigation", "hide-on-print", "rule-related"}


def rule_body(page_html: str) -> Tag | None:
    """Return the outermost div.rule, which holds the section and its children."""
    soup = BeautifulSoup(page_html, "html.parser")
    main = soup.find("div", id="main") or soup
    return main.find("div", class_="rule")


def heading_id(rule: Tag) -> int | None:
    h = rule.find(re.compile(r"^h[1-6]$"), class_="title", recursive=False)
    if not h:
        return None
    a = h.find("a", href=re.compile(r"Rules\.aspx\?ID=\d+"))
    if not a:
        return None
    return int(re.search(r"ID=(\d+)", a["href"]).group(1))


def collect_headings(rule: Tag, out: dict[int, str], own_file_ids: set[int], depth: int = 0) -> None:
    """Record every ``ID -> heading text`` that this page is responsible for.

    Chapter pages inline their whole subtree, so descending blindly would make a
    chapter claim anchors that belong to its sections' own files. Stop at any
    nested rule that has a file of its own.
    """
    h = rule.find(re.compile(r"^h[1-6]$"), class_="title", recursive=False)
    if h:
        a = h.find("a", href=re.compile(r"Rules\.aspx\?ID=\d+"))
        if a:
            aon_id = int(re.search(r"ID=(\d+)", a["href"]).group(1))
            out[aon_id] = a.get_text(strip=True)

    for child in rule.find_all("div", class_="rule", recursive=True):
        # Only direct rule descendants, not grandchildren already covered.
        if child.find_parent("div", class_="rule") is not rule:
            continue
        cid = heading_id(child)
        if depth >= 0 and cid in own_file_ids:
            continue
        collect_headings(child, out, own_file_ids, depth + 1)


class Converter:
    """Recursive HTML-to-markdown pass with AoN-specific handling."""

    def __init__(
        self,
        *,
        link_map: dict[int, tuple[Path, str]],
        anchor_map: dict[int, tuple[Path, str]],
        own_file_ids: set[int],
        current: Path,
        vault_root: Path,
        external_links: bool,
        links=None,
    ):
        self.link_map = link_map
        self.anchor_map = anchor_map
        self.own_file_ids = own_file_ids
        self.current = current
        self.vault_root = vault_root
        self.external_links = external_links
        self.source: str | None = None
        self.unresolved = 0
        self.resolved_external = 0
        self.links = links
        self.skipped_children: list[int] = []

    # -- links -----------------------------------------------------------

    def _wikilink_target(self, path: Path, anchor: str | None) -> str:
        rel = path.relative_to(self.vault_root).with_suffix("")
        # Keep "/index": Quartz resolves either form, Obsidian needs the file.
        target = str(rel)
        return f"{target}#{anchor}" if anchor else target

    def resolve_link(self, href: str, text: str) -> str:
        text = text.strip()
        if not text:
            return ""

        m = re.search(r"Rules\.aspx\?ID=(\d+)", href)
        if m:
            aon_id = int(m.group(1))
            if aon_id in self.link_map:
                path, title = self.link_map[aon_id]
                if path == self.current:
                    return text
                target = self._wikilink_target(path, None)
                return f"[[{target}|{text}]]"
            if aon_id in self.anchor_map:
                path, anchor = self.anchor_map[aon_id]
                if path == self.current:
                    return f"[[#{anchor}|{text}]]"
                target = self._wikilink_target(path, anchor)
                return f"[[{target}|{text}]]"

        # Other AoN databases (Spells, Equipment, Conditions, ...) resolve
        # through the shared map once the compendium and bestiary exist.
        if self.links is not None:
            m2 = re.search(r"/?(\w+)\.aspx\?ID=(\d+)", href)
            if m2:
                target = self.links.lookup(m2.group(1), int(m2.group(2)))
                if target:
                    self.resolved_external += 1
                    return f"[[{target}|{text}]]"

        self.unresolved += 1
        if self.external_links:
            url = href if href.startswith("http") else f"{BASE}/{href.lstrip('/')}"
            return f"[{text}]({url})"
        return text

    # -- dispatch --------------------------------------------------------

    def convert(self, node, depth: int = 0) -> str:
        if isinstance(node, NavigableString):
            return re.sub(r"\s+", " ", str(node))
        if not isinstance(node, Tag):
            return ""

        classes = set(node.get("class", []))
        if classes & SKIP_CLASSES:
            return ""

        name = node.name

        if name == "div":
            if "sources" in classes:
                self._capture_source(node)
                return ""
            if "sidebars" in classes:
                return self._sidebars(node, depth)
            if "rule" in classes:
                return self._nested_rule(node, depth)
            return self.children(node, depth)

        if name == "span" and "action" in classes:
            # AoN already embeds a literal token, e.g. "[one-action]".
            return node.get_text(strip=True)

        if re.fullmatch(r"h[1-6]", name):
            return self._heading(node, depth)
        if name == "table":
            return self._table(node)
        if name in ("ul", "ol"):
            return self._list(node, name == "ol", depth)
        if name == "a":
            return self.resolve_link(node.get("href", ""), node.get_text())
        if name in ("b", "strong"):
            inner = self.children(node, depth).strip()
            return f"**{inner}**" if inner else ""
        if name in ("i", "em"):
            inner = self.children(node, depth).strip()
            return f"*{inner}*" if inner else ""
        if name == "br":
            return "\n"
        if name == "hr":
            return "\n\n---\n\n"
        if name == "p":
            return "\n\n" + self.children(node, depth).strip() + "\n\n"
        if name in ("script", "style", "input", "button"):
            return ""

        return self.children(node, depth)

    def children(self, node: Tag, depth: int) -> str:
        return "".join(self.convert(c, depth) for c in node.children)

    # -- element handlers ------------------------------------------------

    def _capture_source(self, node: Tag) -> None:
        if self.source:
            return
        a = node.find("a")
        if a:
            self.source = a.get_text(strip=True)

    def _heading(self, node: Tag, depth: int) -> str:
        level = int(node.name[1])
        text = node.get_text(" ", strip=True)
        if not text:
            return ""
        return f"\n\n{'#' * min(level, 6)} {text}\n\n"

    def _nested_rule(self, node: Tag, depth: int) -> str:
        # The page's own rule div is unwrapped by the caller, so anything we meet
        # here is a child. Children with their own file are linked, not inlined.
        rid = heading_id(node)
        if rid is not None and rid in self.own_file_ids:
            self.skipped_children.append(rid)
            return ""
        return self.children(node, depth + 1)

    def _sidebars(self, node: Tag, depth: int) -> str:
        out = []
        for box in node.find_all("div", class_="sidebar-nofloat"):
            title_el = box.find(re.compile(r"^h[1-6]$"))
            title = title_el.get_text(" ", strip=True) if title_el else "Sidebar"
            content_el = box.find("div", class_="sidebar-content")
            body = self.children(content_el, depth) if content_el else ""
            body = clean_text(body)
            quoted = "\n".join(f"> {line}" if line else ">" for line in body.split("\n"))
            out.append(f"\n\n> [!pf2-sidebar] {title.upper()}\n>\n{quoted}\n\n")
        return "".join(out)

    def _list(self, node: Tag, ordered: bool, depth: int) -> str:
        items = []
        for i, li in enumerate(node.find_all("li", recursive=False), 1):
            body = clean_text(self.children(li, depth)).replace("\n", " ")
            if body:
                items.append(f"{i}. {body}" if ordered else f"- {body}")
        return "\n\n" + "\n".join(items) + "\n\n" if items else ""

    def _table(self, node: Tag) -> str:
        rows: list[list[str]] = []
        for tr in node.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            if not cells:
                continue
            rows.append(
                [
                    clean_text(self.children(c, 0)).replace("\n", " ").replace("|", "\\|")
                    for c in cells
                ]
            )
        if not rows:
            return ""

        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header, *body = rows
        lines = [
            "| " + " | ".join(header) + " |",
            "|" + "|".join([" --- "] * width) + "|",
        ]
        lines += ["| " + " | ".join(r) + " |" for r in body]
        return "\n\n" + "\n".join(lines) + "\n\n"


def normalise_newlines(text: str) -> str:
    """CRLF and lone CR -> LF."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def clean_text(text: str) -> str:
    text = normalise_newlines(text)
    text = html.unescape(text)
    text = text.replace("\u00a0", " ")
    # "Click here to see ..." only meant something as a hyperlink to a page we
    # do not import; as plain text it instructs the reader to click nothing.
    text = re.sub(r"[^.\n]*\bClick here\b[^.\n]*\.?", "", text, flags=re.I)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# --------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------


def yaml_escape(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_page(entry: Entry, body: str, source: str | None, contents: list[str] | None = None) -> str:
    code = BOOK_CODES.get(entry.book, entry.book)
    fm = [
        "---",
        f"title: {yaml_escape(entry.title)}",
        f"aliases: [{yaml_escape(entry.title)}]",
        "cssclasses:",
        "  - pf2e",
        "  - pf2e-book",
        "tags:",
        f"  - srd/pf2e/{slugify(entry.book)}",
        f"source: {yaml_escape(entry.book)}",
        f"aon_id: {entry.aon_id}",
        f"aon_url: {yaml_escape(f'{BASE}/Rules.aspx?ID={entry.aon_id}')}",
    ]
    if source:
        fm.append(f"citation: {yaml_escape(source)}")
    fm.append("---")

    parts = ["\n".join(fm), "", f"# {entry.title}", ""]
    if source:
        page = re.search(r"pg\.\s*(\d+)", source)
        if page:
            parts.append(f"<sup>{code} p. {page.group(1)}</sup>")
            parts.append("")
    parts.append(body)
    if contents:
        parts.append("")
        parts.append("## Contents")
        parts.append("")
        parts.extend(contents)
    return "\n".join(parts).rstrip() + "\n"


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    default_out = Path(__file__).resolve().parents[2] / "content" / "srd" / "pf2e" / "books"
    ap.add_argument("--out", type=Path, default=default_out, help="output directory")
    ap.add_argument("--cache", type=Path, default=Path(__file__).parent / ".cache", help="HTML cache directory")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between network fetches")
    ap.add_argument("--refresh", action="store_true", help="ignore the cache and refetch")
    ap.add_argument("--limit", type=int, help="only process the first N entries (for testing)")
    ap.add_argument("--books", nargs="+", default=CORE_BOOKS, help="books to import")
    ap.add_argument(
        "--external-links",
        action="store_true",
        help="keep links to other AoN databases as external URLs instead of plain text",
    )
    ap.add_argument("--dry-run", action="store_true", help="fetch and convert but write nothing")
    args = ap.parse_args()

    vault_root = args.out.parents[2]  # .../content
    fetcher = Fetcher(args.cache, args.delay, args.refresh)

    links = LinkMap(vault_root)
    if links.load(args.cache.parent / ".snapshot" / "linkmap.json"):
        print(f"Loaded {len(links)} link targets")
    else:
        links = None
        print("No linkmap.json -- run build_linkmap.py first", file=sys.stderr)

    # --- Pass 1: index -------------------------------------------------
    print("Fetching rules index...")
    index_html = fetcher.get(INDEX_URL, "index")
    entries = parse_index(index_html, args.books)
    if args.limit:
        entries = entries[: args.limit]
    assign_paths(entries, args.out)

    by_book: dict[str, int] = {}
    for e in entries:
        by_book[e.book] = by_book.get(e.book, 0) + 1
    print(f"Index: {len(entries)} sections across {len(by_book)} books")
    for b, n in by_book.items():
        print(f"  {b:16} {n}")

    # --- Pass 2: fetch every page, build the full ID map ---------------
    print(f"\nFetching {len(entries)} pages (cache: {args.cache})...")
    pages: dict[int, str] = {}
    subsections: dict[int, tuple[Path, str]] = {}
    own_file_ids = {e.aon_id for e in entries}
    link_map = {e.aon_id: (e.path, e.title) for e in entries}

    for i, e in enumerate(entries, 1):
        url = f"{BASE}/Rules.aspx?ID={e.aon_id}&NoRedirect=1"
        try:
            page = fetcher.get(url, str(e.aon_id))
        except requests.RequestException as exc:
            print(f"  [{i}/{len(entries)}] FAILED {e.aon_id} {e.title}: {exc}", file=sys.stderr)
            continue
        pages[e.aon_id] = page

        rule = rule_body(page)
        if rule is None:
            print(f"  [{i}/{len(entries)}] no rule body: {e.aon_id} {e.title}", file=sys.stderr)
            continue
        headings: dict[int, str] = {}
        collect_headings(rule, headings, own_file_ids)
        for hid, htext in headings.items():
            if hid not in own_file_ids and hid not in subsections:
                subsections[hid] = (e.path, htext)

        if i % 25 == 0 or i == len(entries):
            print(f"  [{i}/{len(entries)}] {fetcher.network_calls} fetched, {len(pages)} cached")

    print(f"Discovered {len(subsections)} subsections not listed in the index")

    # --- Pass 3: convert ------------------------------------------------
    print(f"\nConverting to {args.out}...")
    written = 0
    unresolved_total = 0
    resolved_external_total = 0
    for e in entries:
        page = pages.get(e.aon_id)
        if not page:
            continue
        rule = rule_body(page)
        if rule is None:
            continue

        conv = Converter(
            link_map=link_map,
            anchor_map=subsections,
            own_file_ids=own_file_ids,
            current=e.path,
            vault_root=vault_root,
            external_links=args.external_links,
            links=links,
        )
        # Skip the section's own <h1 class="title">; it becomes the page title.
        body_parts = []
        for child in rule.children:
            if isinstance(child, Tag) and re.fullmatch(r"h[1-6]", child.name or "") and "title" in child.get("class", []):
                continue
            body_parts.append(conv.convert(child, 0))
        body = clean_text("".join(body_parts))
        unresolved_total += conv.unresolved
        resolved_external_total += conv.resolved_external

        contents = None
        if e.is_chapter:
            kids = [k for k in entries if k.chapter_id == e.aon_id]
            contents = [
                f"- [[{str(k.path.relative_to(vault_root).with_suffix('')).removesuffix('/index')}|{k.title}]]"
                for k in kids
            ]
        out = render_page(e, body, conv.source, contents)
        if not args.dry_run:
            e.path.parent.mkdir(parents=True, exist_ok=True)
            e.path.write_text(normalise_newlines(out), encoding="utf-8")
        written += 1

    manifest = {
        "books": args.books,
        "entries": [
            {"aon_id": e.aon_id, "title": e.title, "book": e.book, "path": str(e.path.relative_to(args.out))}
            for e in entries
        ],
    }
    if not args.dry_run:
        (args.out / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nDone. {written} files{' (dry run)' if args.dry_run else ''}, {fetcher.network_calls} network fetches.")
    print(f"Cross-links into compendium/bestiary: {resolved_external_total} resolved")
    print(f"Links left as plain text: {unresolved_total}")
    if not args.external_links and unresolved_total:
        print("  (re-run with --external-links to keep them as clickable AoN URLs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
