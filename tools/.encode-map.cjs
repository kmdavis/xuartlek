
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
