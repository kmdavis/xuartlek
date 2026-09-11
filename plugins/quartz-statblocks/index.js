/**
 * Pathfinder 2e statblocks for Quartz.
 *
 * Renders the ```statblock fences written for the Obsidian fantasy-statblocks
 * plugin (obsidian-ttrpg-community/fantasy-statblocks). Every statblock in this
 * vault uses "Basic Pathfinder 2e Layout", so that is the only layout handled;
 * anything else is left as a code block rather than rendered wrongly.
 *
 * Like the spoiler plugin, this is a text transform rather than an mdast one.
 * The `desc` values are full of wikilinks and __bold__:
 *
 *     desc: "[[.../skills/acrobatics|Acrobatics]] +5, ..."
 *
 * Emitting markdown means Quartz's own pipeline resolves those links. Emitting
 * HTML would leave 1,300 pages of dead wikilink text.
 *
 * The container is an HTML block separated by blank lines, which is the
 * CommonMark rule for embedding markdown inside a div: the opening tag's block
 * ends at the blank line, the markdown is parsed normally, and the closing tag
 * starts a new HTML block.
 */
import { parse as parseYaml } from "yaml"

const DEFAULT_OPTIONS = {
  /** Layouts this plugin knows how to render. */
  layouts: ["Basic Pathfinder 2e Layout"],
  /** Drop ```encounter-table fences, which drive an Obsidian VTT plugin. */
  hideEncounterTables: true,
  /** Ability score column headings, in abilityMods order. */
  abilityNames: ["Str", "Dex", "Con", "Int", "Wis", "Cha"],
}

const ABILITY_KEYS = ["abilityMods"]
/** Section keys in the order the layout renders them. */
const SECTIONS = [
  ["perception", null],
  ["languages", "Languages"],
  ["skills", null],
  ["__abilities__", null],
  ["abilities_top", null],
  ["armorclass", null],
  ["health", null],
  ["__rule__", null],
  ["abilities_mid", null],
  ["speed", "Speed"],
  ["attacks", null],
  ["spellcasting", null],
  ["abilities_bot", null],
]

function signed(n) {
  const v = Number(n)
  if (Number.isNaN(v)) return String(n)
  return v >= 0 ? `+${v}` : `${v}`
}

/** `[{name, desc}]` renders as "**Name** desc" lines. A bare string renders as-is. */
function renderEntries(value, label) {
  if (value == null || value === "") return []
  if (typeof value === "string") {
    return label ? [`**${label}** ${value}`] : [value]
  }
  if (!Array.isArray(value)) return []
  return value
    .filter((e) => e && (e.name || e.desc))
    .map((e) => (e.name ? `**${e.name}** ${e.desc ?? ""}`.trim() : String(e.desc ?? "")))
}

function traits(sb) {
  const out = []
  if (sb.size) out.push({ cls: "sb-trait sb-size", text: sb.size })
  for (let i = 1; i <= 9; i++) {
    const t = sb[`trait_0${i}`]
    if (t) out.push({ cls: "sb-trait", text: String(t) })
  }
  // PC statblocks reuse rare_03/rare_04 for class and background
  for (const k of ["rare_03", "rare_04"]) {
    if (sb[k]) out.push({ cls: "sb-trait sb-trait-alt", text: String(sb[k]) })
  }
  return out
}

export function renderStatblock(sb, opts) {
  const L = []
  L.push(`<div class="pf2e-statblock" data-statblock-name="${escapeAttr(sb.name ?? "")}">`)
  L.push("")
  L.push(
    `<span class="sb-name">${sb.name ?? ""}</span>` +
      (sb.level ? `<span class="sb-level">${sb.level}</span>` : ""),
  )
  L.push("")

  const tr = traits(sb)
  if (tr.length) {
    L.push(tr.map((t) => `<span class="${t.cls}">${t.text}</span>`).join(""))
    L.push("")
  }

  for (const [key] of SECTIONS) {
    if (key === "__rule__") {
      L.push("<hr class='sb-rule'/>", "")
      continue
    }
    if (key === "__abilities__") {
      const mods = sb[ABILITY_KEYS[0]]
      if (Array.isArray(mods) && mods.length) {
        L.push(`| ${opts.abilityNames.join(" | ")} |`)
        L.push(`|${":-:|".repeat(opts.abilityNames.length)}`)
        L.push(`| ${mods.map(signed).join(" | ")} |`)
        L.push("")
      }
      continue
    }
    const label = SECTIONS.find(([k]) => k === key)[1]
    for (const line of renderEntries(sb[key], label)) {
      L.push(line, "")
    }
  }

  if (sb.sourcebook) L.push(`<span class="sb-source">Source: ${sb.sourcebook}</span>`, "")
  L.push("</div>")
  L.push("")
  return L.join("\n")
}

function escapeAttr(s) {
  return String(s).replace(/"/g, "&quot;").replace(/</g, "&lt;")
}

const FENCE = /^(\s*)(`{3,}|~{3,})\s*([^\s`~]*)\s*$/

export function rewriteStatblocks(src, options = {}) {
  const opts = { ...DEFAULT_OPTIONS, ...options }
  const lines = src.split("\n")
  const out = []
  let i = 0

  while (i < lines.length) {
    const m = lines[i].match(FENCE)
    if (!m) {
      out.push(lines[i])
      i++
      continue
    }
    const [, , marker, lang] = m
    const kind = lang.toLowerCase()
    if (kind !== "statblock" && kind !== "encounter-table") {
      out.push(lines[i])
      i++
      while (i < lines.length && !isCloser(lines[i], marker)) out.push(lines[i++])
      if (i < lines.length) out.push(lines[i++])
      continue
    }

    const body = []
    const open = lines[i]
    i++
    while (i < lines.length && !isCloser(lines[i], marker)) body.push(lines[i++])
    i++

    if (kind === "encounter-table") {
      if (!opts.hideEncounterTables) out.push(open, ...body, marker)
      continue
    }

    let sb
    try {
      sb = parseYaml(body.join("\n"))
    } catch {
      sb = null
    }
    // Unknown layout or unparseable YAML: leave the source block untouched
    // rather than render something misleading.
    if (!sb || typeof sb !== "object" || !opts.layouts.includes(sb.layout)) {
      out.push(open, ...body, marker)
      continue
    }
    out.push(renderStatblock(sb, opts))
  }
  return out.join("\n")
}

function isCloser(line, marker) {
  const t = line.trim()
  return t.startsWith(marker[0]) && /^(`{3,}|~{3,})\s*$/.test(t)
}

export const Statblocks = (userOpts) => {
  const opts = { ...DEFAULT_OPTIONS, ...userOpts }
  return {
    name: "Statblocks",
    textTransform(_ctx, src) {
      return src.includes("```statblock") || src.includes("```encounter-table")
        ? rewriteStatblocks(src, opts)
        : src
    },
  }
}

export default Statblocks
