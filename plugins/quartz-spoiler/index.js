/**
 * Spoiler blocks for Quartz.
 *
 * Matches the Obsidian spoiler plugin's syntax:
 *
 *     ```spoiler
 *     ### Anything
 *     - including markdown, [[wikilinks]] and ![[images]]
 *     ```
 *
 * The fence is rewritten to a collapsed Obsidian callout before the markdown is
 * parsed:
 *
 *     > [!spoiler]- Spoiler
 *     > ### Anything
 *     > - including markdown, [[wikilinks]] and ![[images]]
 *
 * Doing it as a text transform rather than an mdast transform is deliberate.
 * Everything inside the block then goes through Quartz's normal pipeline, so
 * wikilinks, embeds, nested code blocks and callouts all work with no extra
 * handling, and the collapse behaviour is the callout collapse that already
 * ships with Quartz.
 *
 * This hides content behind a click. It is not access control: the text is in
 * the HTML. For material that must not reach the site, use `draft: true`.
 */

const DEFAULT_OPTIONS = {
  /** Enable inline spoilers written as ||hidden||. */
  inline: true,
  /** Class applied to an inline spoiler. */
  inlineClass: "spoiler-inline",
  /** Fence languages treated as spoilers. */
  languages: ["spoiler"],
  /** Title shown on the closed block when the fence gives none. */
  defaultTitle: "Spoiler",
  /** Callout type, so the styling hook is `[data-callout="spoiler"]`. */
  calloutType: "spoiler",
}

const FENCE = /^(\s*)(`{3,}|~{3,})\s*([^\s`~]*)\s*(.*)$/

/**
 * Rewrite spoiler fences, leaving every other fence alone.
 *
 * Walks line by line and tracks fence state, because a spoiler may itself
 * contain fenced code. A nested fence is only treated as the closer when its
 * marker is at least as long and of the same character, which is the CommonMark
 * rule.
 */
export function rewriteSpoilers(src, options = {}) {
  const opts = { ...DEFAULT_OPTIONS, ...options }
  const langs = new Set(opts.languages.map((l) => l.toLowerCase()))
  const lines = src.split("\n")
  const out = []

  let i = 0
  while (i < lines.length) {
    const m = lines[i].match(FENCE)
    if (!m) {
      out.push(opts.inline ? rewriteInlineSpoilers(lines[i], opts) : lines[i])
      i++
      continue
    }

    const [, indent, marker, lang, rest] = m
    if (!langs.has(lang.toLowerCase())) {
      // Some other fence. Copy it through verbatim to its closer so that a
      // ```spoiler shown as an example inside a code block is not rewritten.
      out.push(lines[i])
      i++
      while (i < lines.length && !isCloser(lines[i], marker)) {
        out.push(lines[i])
        i++
      }
      if (i < lines.length) {
        out.push(lines[i])
        i++
      }
      continue
    }

    // Collect the body up to the matching closer.
    const body = []
    i++
    while (i < lines.length && !isCloser(lines[i], marker)) {
      body.push(lines[i])
      i++
    }
    i++ // step over the closer, if there was one

    const title = rest.trim() || opts.defaultTitle
    out.push(`${indent}> [!${opts.calloutType}]- ${title}`)
    // Every line needs the marker, blank ones included, or the blockquote ends.
    for (const line of body) {
      const l = opts.inline ? rewriteInlineSpoilers(line, opts) : line
      out.push(l.trim() === "" ? `${indent}>` : `${indent}> ${l}`)
    }
    out.push("")
  }

  return out.join("\n")
}

/**
 * Inline spoilers: ||hidden|| becomes a span, so surrounding and nested inline
 * markdown still parses. **||bold||** gives <strong><span>bold</span></strong>.
 *
 * Two things must never be touched:
 *   - table rows, because "| a || b |" is an empty cell, not a spoiler, and the
 *     SRD really does contain one
 *   - inline code, because `a || b` is an operator
 */
export function rewriteInlineSpoilers(line, opts) {
  const trimmed = line.trim().replace(/^>+\s*/, "")
  if (!trimmed.includes("||")) return line

  // A markdown table row is pipe-delimited end to end, and "| a || b |" is an
  // empty cell rather than a spoiler; the SRD contains exactly that. A line
  // opening with "||" is a spoiler, not a row, so it is exempt.
  //
  // Known limit: an inline spoiler as the first thing in a table cell is not
  // detected. Put it later in the cell, or use a block spoiler.
  const looksLikeTableRow = /^\|.*\|\s*$/.test(trimmed) && !trimmed.startsWith("||")
  if (looksLikeTableRow) return line

  // split on inline code so the operator case is left alone
  return line
    .split(/(`+[^`]*`+)/)
    .map((part) =>
      part.startsWith("`")
        ? part
        : part.replace(
            /\|\|(?!\s)((?:[^|]|\|(?!\|))+?)(?<!\s)\|\|/g,
            (_m, inner) => `<span class="${opts.inlineClass}" tabindex="0">${inner}</span>`,
          ),
    )
    .join("")
}

function isCloser(line, marker) {
  const t = line.trim()
  return t.startsWith(marker[0].repeat(marker.length)) && /^(`{3,}|~{3,})\s*$/.test(t)
}

export const SpoilerBlocks = (userOpts) => {
  const opts = { ...DEFAULT_OPTIONS, ...userOpts }
  return {
    name: "SpoilerBlocks",
    textTransform(_ctx, src) {
      return rewriteSpoilers(src, opts)
    },
  }
}

export default SpoilerBlocks
