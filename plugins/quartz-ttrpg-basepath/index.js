/**
 * Two fixes for the TTRPG Tools: Maps Quartz plugin, which does not know that
 * a vault root and a content root can be different directories.
 *
 * This vault has Obsidian open at the repository root, so non-published
 * folders can live outside content/. Quartz's content root is content/. Every
 * path in a note is therefore ambiguous unless something reconciles the two,
 * and the upstream plugin reconciles nothing.
 *
 * 1. textTransform -- vault path to content path
 *
 *    Notes write the path Obsidian needs:
 *
 *        image: content/setting/places/systems/Tyros/Shubae/Shubae map.webp
 *
 *    which is what Obsidian resolves, and therefore where Obsidian writes the
 *    sidecar when you drop a pin. Quartz needs the same file named from
 *    content/, so the leading segment is stripped before the upstream
 *    transformer sees the fence.
 *
 *    A bare filename would look like the obvious answer and does not work:
 *    upstream builds its note-relative candidate with
 *    path.resolve(contentDir, file.data.filePath), but Quartz hands it a
 *    repo-root-relative filePath, so that candidate is always
 *    content/content/... and never matches. Only the content-root candidate
 *    resolves.
 *
 * 2. htmlPlugins -- baseUrl prefix
 *
 *    Upstream builds image URLs as root-absolute:
 *
 *        url: "/" + destRel.split("/").map(encodeURIComponent).join("/")
 *
 *    correct only at a domain root. This site is served from
 *    https://kmdavis.github.io/xuartlek/, so every map 404'd. The failure is
 *    disguised: the runtime's image onerror calls renderError("invalid-markers"),
 *    so a missing image reports itself as "Marker data is corrupted".
 *
 * Both belong upstream. They live here because .quartz/plugins is gitignored
 * and CI rebuilds it from GitHub on every deploy, so a local patch works
 * locally and vanishes exactly when it matters.
 */

const DEFAULT_OPTIONS = {
  /** Fence language the upstream plugin claims. */
  language: "zoommap",
  /** Vault-root prefix to strip so paths resolve from Quartz's content root. */
  contentPrefix: "content/",
}

/** Keys in a zoommap fence whose value is a vault path. */
const PATH_KEYS = ["image", "markers", "path", "viewportFrame", "stickerPath"]

/**
 * Strip the content/ prefix from path values inside zoommap fences.
 *
 * Only touches the fence body, so prose mentioning content/ is left alone, and
 * only the keys that hold paths, so a tooltip saying "content/..." survives.
 */
export function rewriteMapPaths(src, options = {}) {
  const opts = { ...DEFAULT_OPTIONS, ...options }
  if (!src.includes(opts.language)) return src

  const fence = new RegExp(
    String.raw`(^|\n)([ \t]*)(\`{3,}|~{3,})${opts.language}[ \t]*\n([\s\S]*?)\n[ \t]*\3`,
    "g",
  )
  const keys = PATH_KEYS.join("|")
  const pathLine = new RegExp(String.raw`^([ \t]*-?[ \t]*(?:${keys}):[ \t]*)(.+)$`, "gm")

  return src.replace(fence, (match, lead, indent, ticks, body) => {
    const fixed = body.replace(pathLine, (line, head, value) => {
      const trimmed = value.trim()
      if (!trimmed.startsWith(opts.contentPrefix)) return line
      return head + trimmed.slice(opts.contentPrefix.length)
    })
    return `${lead}${indent}${ticks}${opts.language}\n${fixed}\n${indent}${ticks}`
  })
}

/** Pull "/xuartlek" out of "kmdavis.github.io/xuartlek". */
export function basePathOf(baseUrl) {
  if (!baseUrl) return ""
  let pathname
  try {
    pathname = new URL(`https://${String(baseUrl).replace(/^https?:\/\//, "")}`).pathname
  } catch {
    return ""
  }
  const trimmed = pathname.replace(/\/+$/, "")
  return trimmed === "/" ? "" : trimmed
}

/** Prefix one map config's image URLs. Returns true when something changed. */
export function prefixMapConfig(cfg, basePath) {
  if (!basePath || !cfg || !Array.isArray(cfg.resolvedImageUrls)) return false
  let changed = false
  for (const ref of cfg.resolvedImageUrls) {
    if (typeof ref?.url !== "string") continue
    // Idempotent: a rerun, or an upstream fix landing, must not double-prefix.
    if (ref.url.startsWith(`${basePath}/`)) continue
    if (!ref.url.startsWith("/")) continue
    ref.url = basePath + ref.url
    changed = true
  }
  return changed
}

function visit(node, fn) {
  if (!node || typeof node !== "object") return
  fn(node)
  for (const child of node.children ?? []) visit(child, fn)
}

export const TTRPGMapBasePath = (userOpts) => {
  const opts = { ...DEFAULT_OPTIONS, ...userOpts }
  return {
    name: "TTRPGMapBasePath",
    textTransform(_ctx, src) {
      return rewriteMapPaths(src, opts)
    },
    htmlPlugins(ctx) {
      const basePath = basePathOf(ctx?.cfg?.configuration?.baseUrl)
      if (!basePath) return []
      return [
        () => (tree) => {
          visit(tree, (node) => {
            const raw = node.properties?.dataQzTtrpgMapCfg
            if (typeof raw !== "string") return
            let cfg
            try {
              cfg = JSON.parse(raw)
            } catch {
              return
            }
            if (prefixMapConfig(cfg, basePath)) {
              node.properties.dataQzTtrpgMapCfg = JSON.stringify(cfg)
            }
          })
        },
      ]
    },
  }
}

export default TTRPGMapBasePath
