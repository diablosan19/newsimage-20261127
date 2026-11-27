// news-image-20261127 entry: copy the front-page image to the output dir.
// Node stdlib only. No network. Deterministic: the same bytes every run.
import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function fail(message: string): never {
  console.error("entry failed: " + message);
  process.exit(1);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR;
if (!outDir) {
  fail("MAKEFUN_OUTPUT_DIR is not set");
}

const source = path.join(path.dirname(fileURLToPath(import.meta.url)), "entry.png");
let data: Buffer;
try {
  data = fs.readFileSync(source);
} catch (err) {
  fail("cannot read entry.png: " + String(err));
}

if (data.length < 8 || !data.subarray(0, 8).equals(PNG_MAGIC)) {
  fail("entry.png is not a PNG file");
}
if (data.length > 1048576) {
  fail("entry.png is over 1 MiB: " + data.length + " bytes");
}

fs.mkdirSync(outDir, { recursive: true });
const target = path.join(outDir, "entry.png");
fs.writeFileSync(target, data);
console.log("wrote " + target + " (" + data.length + " bytes)");
