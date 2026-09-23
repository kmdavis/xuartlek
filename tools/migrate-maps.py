#!/usr/bin/env python3
"""Import planet maps and orbit animations from the old atlas.

Each world in the legacy app carried two images:

  simple.svg  a Azgaar-style surface map, vector with two embedded rasters
  orbit.gif   a 166px animation of the world's path around its primary

The SVG is copied as the vector original, and also rasterised to a 4096px WebP
which is what the interactive map actually loads. That is not redundancy: the
zoom-map plugin warns that large SVG bases stutter in DOM mode and suggests a
WebP export, and the Quartz port has no canvas fallback to escape to. The
raster is also *smaller* than the vector here -- 0.48MB against 0.76MB -- since
these SVGs carry embedded bitmaps anyway.

The GIF becomes an animated WebP, about 60% smaller across the set with no
visible loss: at 596 frames of 166 square, the size is frame count rather than
resolution. Orbits stay a plain embed -- an animation is not a map to pan.

Assets land beside the world note as "{World} map.svg", "{World} map.webp" and
"{World} orbit.webp", matching the atlas convention of prefixing an asset with
its note name.

Idempotent: skips any image already present, so a re-run after adding one world
does not re-encode the other eleven. Run from the repo root.
"""
import json
import pathlib
import shutil
import subprocess
import sys

SRC = pathlib.Path.home() / "src/github.com/kmdavis/xuartlek-foundry/bazaar/app/data/atlas/systems"
DST = pathlib.Path("content/setting/places/systems")

# Legacy slug -> (System, World) as the vault spells them.
WORLDS = {
    ("archaelon", "profugae"):   ("Archaelon", "Profugae"),
    ("belcanto", "tertara"):     ("Belcanto", "Tertara"),
    ("calderon", "langsevain"):  ("Calderon", "Langsevain"),
    ("eirion", "hrimgard"):      ("Eirion", "Hrimgard"),
    ("lumiere", "emerraine"):    ("Lumiere", "Emerraine"),
    ("shamsara", "khashayar"):   ("Shamsara", "Khashayar"),
    ("shenzhou", "qigang"):      ("Shenzhou", "Qigang"),
    ("strathis", "strafmack"):   ("Strathis", "Strafmack"),
    ("sylvoria", "arborisle"):   ("Sylvoria", "Arborisle"),
    ("tessara", "myrrhina"):     ("Tessara", "Myrrhina"),
    ("tyros", "shubae"):         ("Tyros", "Shubae"),
    ("umbra", "mortuus-rex"):    ("Umbra", "Mortuus Rex"),
}

# One script, two modes. .cjs because package.json sets "type": "module".
ENCODE = """
const sharp = require('sharp');
const [, , mode, src, dst] = process.argv;
(async () => {
  let buf;
  if (mode === 'gif') {
    buf = await sharp(src, { animated: true }).webp({ quality: 78, effort: 4 }).toBuffer();
  } else if (mode === 'raster') {
    buf = await sharp(src).resize({ width: 4096, withoutEnlargement: true })
      .webp({ quality: 82 }).toBuffer();
  } else {
    // density scales the SVG rasteriser; without it sharp renders at the
    // nominal 1512px and the upscale is a blurry mess.
    const WIDTH = 4096, NOMINAL = 1512;
    buf = await sharp(src, { density: Math.round(72 * WIDTH / NOMINAL) })
      .resize({ width: WIDTH }).webp({ quality: 82 }).toBuffer();
  }
  require('fs').writeFileSync(dst, buf);
})().catch(e => { console.error(e.message); process.exit(1); });
"""


# minZoom has to be below the fit-to-view scale or the map opens zoomed in.
# The plugin calls fitToView() on load, which wants min(vw/imgW, vh/imgH) --
# about 0.17 for a 4096px base in a 700px column, and less on a phone -- but
# applyTransform() then clamps that up to minZoom. Setting minZoom to 0.5
# meant every map opened at 3x the fit scale, showing one corner.
MAP_BLOCK = """
## Maps

```zoommap
image: {path}
minZoom: 0.05
maxZoom: 6
height: 560px
width: 100%
panClamp: true
```

[Full vector map]({svg}) if you would rather zoom in your own viewer.

An orbital view of the world:

![[{world} orbit.webp]]
"""


def embed(note: pathlib.Path, world: str, rel_dir: str) -> bool:
    """Replace or add the map block on a world note.

    The path is written from the vault root, which is the repository root, so
    it starts with content/. That is what Obsidian resolves, and therefore
    where Obsidian writes the marker sidecar when you place a pin.

    Quartz needs the same file named from content/ instead. The local
    quartz-ttrpg-basepath plugin strips the prefix before the upstream
    transformer parses the fence, so one string serves both tools and the
    sidecar Obsidian writes is the sidecar Quartz reads.
    """
    text = note.read_text(encoding="utf-8")
    marker = "\n## Maps\n"
    if marker in text:
        text = text[: text.index(marker)].rstrip() + "\n"
    block = MAP_BLOCK.format(path=f"{rel_dir}/{world} map.webp",
                             svg=f"{world} map.svg".replace(" ", "%20"),
                             world=world)
    note.write_text(text.rstrip() + "\n" + block, encoding="utf-8")
    return True


def main() -> int:
    if not SRC.exists():
        print(f"source atlas not found: {SRC}", file=sys.stderr)
        return 1
    # Must live in the repo: node resolves sharp from node_modules by
    # walking up from the script, and /tmp has no ancestor with it.
    # .cjs, not .js: package.json sets "type": "module", so a bare .js
    # here is parsed as an ES module and require() is undefined.
    script = pathlib.Path("tools/.encode-map.cjs")
    script.write_text(ENCODE)

    copied = converted = linked = 0
    saved_before = saved_after = 0
    for (sys_slug, world_slug), (system, world) in sorted(WORLDS.items()):
        src_dir = SRC / sys_slug / world_slug / "images"
        dst_dir = DST / system / world
        note = dst_dir / f"{world}.md"
        if not note.exists():
            print(f"  !! no note for {world} at {note}")
            continue

        svg_src, svg_dst = src_dir / "simple.svg", dst_dir / f"{world} map.svg"
        if svg_src.exists() and not svg_dst.exists():
            shutil.copy2(svg_src, svg_dst)
            copied += 1

        # Raster base for the interactive map.
        png_dst = dst_dir / f"{world} map.webp"
        if svg_dst.exists() and not png_dst.exists():
            r = subprocess.run(["node", str(script), "svg", str(svg_dst), str(png_dst)],
                               capture_output=True, text=True)
            if r.returncode:
                # libvips dies with SIGILL on at least one of these SVGs
                # (Khashayar), so fall back to librsvg, which renders it fine.
                # rsvg-convert has no WebP output, hence the PNG hop.
                tmp_png = pathlib.Path("/tmp") / f"{world}.png"
                fb = subprocess.run(
                    ["rsvg-convert", "-w", "4096", "-o", str(tmp_png), str(svg_dst)],
                    capture_output=True, text=True)
                if fb.returncode == 0:
                    subprocess.run(["node", str(script), "raster",
                                    str(tmp_png), str(png_dst)],
                                   capture_output=True, text=True)
                    tmp_png.unlink(missing_ok=True)
                    print(f"  .. {world} raster via rsvg-convert "
                          f"(libvips exit {r.returncode})")
                else:
                    # Khashayar's SVG defeats libvips and librsvg both. The old
                    # app shipped a 1881px PNG of the same map, so use that --
                    # lower resolution than the 4096 the others get, but a
                    # working interactive map beats a perfect missing one.
                    png_src = src_dir / "simple.png"
                    if png_src.exists():
                        subprocess.run(["node", str(script), "raster",
                                        str(png_src), str(png_dst)],
                                       capture_output=True, text=True)
                        print(f"  .. {world} raster from simple.png "
                              f"(both SVG renderers fail on this file)")
                    else:
                        print(f"  !! {world} raster failed: {fb.stderr.strip()}")

        gif_src, webp_dst = src_dir / "orbit.gif", dst_dir / f"{world} orbit.webp"
        if gif_src.exists() and not webp_dst.exists():
            r = subprocess.run(["node", str(script), "gif", str(gif_src), str(webp_dst)],
                               capture_output=True, text=True)
            if r.returncode:
                print(f"  !! {world} orbit: {r.stderr.strip()}")
            else:
                saved_before += gif_src.stat().st_size
                saved_after += webp_dst.stat().st_size
                converted += 1

        # The plugin treats the marker sidecar as mandatory, not optional: with
        # no {image}.markers.json beside the base it renders "Map failed to
        # load / Marker data not found" and never requests the image at all.
        # An empty layer and marker set is valid and is what Obsidian writes
        # into on the first pin, so this is a seed rather than a placeholder.
        markers = dst_dir / f"{world} map.webp.markers.json"
        if not markers.exists():
            markers.write_text(json.dumps({"layers": [], "markers": []},
                                          indent=1) + "\n", encoding="utf-8")

        if embed(note, world, str(dst_dir)):
            linked += 1
        print(f"  {world:14} svg={'ok' if svg_dst.exists() else '--':3} "
              f"webp={'ok' if png_dst.exists() else '--':3} "
              f"orbit={'ok' if webp_dst.exists() else '--':3}")

    print(f"\n  {copied} maps copied, {converted} orbits converted, {linked} notes linked")
    if saved_before:
        print(f"  orbit animations {saved_before/1048576:.1f}MB -> "
              f"{saved_after/1048576:.1f}MB "
              f"({100 - 100*saved_after//saved_before}% smaller)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
