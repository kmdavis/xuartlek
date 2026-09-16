/**
 * Base-path fix for the TTRPG Tools: Maps Quartz plugin.
 *
 * Upstream builds every image URL as root-absolute:
 *
 *     url: "/" + destRel.split("/").map(encodeURIComponent).join("/")
 *     -- src/transformer.ts, resolveImageRef()
 *
 * That is correct only when the site is served from the root of a domain. This
 * vault deploys to https://kmdavis.github.io/xuartlek/, so every map asked for
 * /setting/places/... instead of /xuartlek/setting/places/... and got a 404.
 * The failure is badly disguised: the runtime's image onerror handler calls
 * renderError("invalid-markers"), so a missing image reports itself as
 * "Marker data is corrupted" and sends you looking at the wrong file.
 *
 * This walks the emitted map config and re-prefixes each URL with the path
 * component of `baseUrl`. It is a shim, not a fix -- the real fix belongs
 * upstream in resolveImageRef, which should consult ctx.cfg.configuration.
 *
 * It lives here rather than as a patch to .quartz/plugins because that
 * directory is gitignored and CI rebuilds it from GitHub on every deploy, so a
 * local edit works locally and vanishes the moment it matters.
 *
 * Remove this once upstream honours baseUrl. It is a no-op when baseUrl has no
 * path component, so leaving it in place costs nothing but noise.
 */

/** Pull "/xuartlek" out of "kmdavis.github.io/xuartlek". */
export function basePathOf(baseUrl) {
  if (!baseUrl) return ""
  // baseUrl is a host plus optional path, with no scheme. Adding one lets the
  // URL parser do the splitting rather than guessing at slashes.
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

export const TTRPGMapBasePath = () => ({
  name: "TTRPGMapBasePath",
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
})

export default TTRPGMapBasePath
