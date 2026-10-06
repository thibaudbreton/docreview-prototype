"""Builds the web copies of the Alstom brand typeface into fonts/.

    python3 build_fonts.py "/path/to/Alstom Font"

The brand ships desktop TrueType files (2006-2007, all rights reserved by
Alstom). They are licensed, so neither they nor anything built from them is
versioned — fonts/ ignores font files, see fonts/README.md. This script only
turns the desktop files into what a browser should load:

- WOFF 1.0 (zlib) instead of raw TTF: about half the size. WOFF2 would need
  Brotli, which the standard library doesn't have; WOFF is enough here.
- Without the tables a browser never needs: the 1-bit bitmap strikes
  (EBDT/EBLC/EBSC — the Regular carries hand-tuned bitmaps from 9 to 18 px,
  which Chrome on Windows can pick over the outlines at exactly those sizes,
  i.e. jagged 13 px body text) and the GDI device-metric caches
  (hdmx/VDMX/LTSH). Outlines, hinting, kerning and ligatures are kept.

Standard library only, so it runs wherever build_merge.py runs.
"""
import struct
import sys
import zlib
from pathlib import Path

# The weights the prototype uses — see the @font-face rules in each screen.
WEIGHTS = {"Regular": "Alstom Regular.ttf", "Medium": "Alstom Medium.ttf", "Bold": "Alstom Bold.ttf"}
DROP = {b"EBDT", b"EBLC", b"EBSC", b"hdmx", b"VDMX", b"LTSH"}
OUT_DIR = Path("fonts")


def checksum(data):
    data += b"\0" * (-len(data) % 4)
    return sum(struct.unpack(">%dI" % (len(data) // 4), data)) & 0xFFFFFFFF


def read_tables(sfnt):
    flavor, num = struct.unpack(">IH", sfnt[:6])
    tables = {}
    for i in range(num):
        tag, _, off, length = struct.unpack(">4sIII", sfnt[12 + 16 * i:28 + 16 * i])
        tables[tag] = sfnt[off:off + length]
    return flavor, tables


def strip(sfnt):
    """The same font without the DROP tables, head.checkSumAdjustment recomputed."""
    flavor, tables = read_tables(sfnt)
    tables = {t: d for t, d in tables.items() if t not in DROP}
    head = bytearray(tables[b"head"])
    head[8:12] = b"\0\0\0\0"
    tables[b"head"] = bytes(head)
    tags = sorted(tables)
    n = len(tags)
    es = max(i for i in range(17) if 2 ** i <= n)
    out = bytearray(struct.pack(">IHHHH", flavor, n, 16 * 2 ** es, es, 16 * n - 16 * 2 ** es))
    offset = 12 + 16 * n
    body = bytearray()
    for tag in tags:
        data = tables[tag]
        out += struct.pack(">4sIII", tag, checksum(data), offset + len(body), len(data))
        body += data + b"\0" * (-len(data) % 4)
    font = bytearray(out + body)
    head_off = struct.unpack(">I", font[12 + 16 * tags.index(b"head") + 8:12 + 16 * tags.index(b"head") + 12])[0]
    font[head_off + 8:head_off + 12] = struct.pack(">I", (0xB1B0AFBA - checksum(bytes(font))) & 0xFFFFFFFF)
    return bytes(font)


def to_woff(sfnt):
    flavor, tables = read_tables(sfnt)
    tags = sorted(tables)
    n = len(tags)
    total_sfnt = 12 + 16 * n + sum(len(d) + (-len(d) % 4) for d in tables.values())
    directory, body = bytearray(), bytearray()
    offset = 44 + 20 * n
    for tag in tags:
        data = tables[tag]
        packed = zlib.compress(data, 9)
        if len(packed) >= len(data):
            packed = data
        directory += struct.pack(">4sIIII", tag, offset + len(body), len(packed), len(data), checksum(data))
        body += packed + b"\0" * (-len(packed) % 4)
    length = 44 + len(directory) + len(body)
    header = struct.pack(">4sIIHHIHHIIIII", b"wOFF", flavor, length, n, 0, total_sfnt, 1, 0, 0, 0, 0, 0, 0)
    return header + bytes(directory) + bytes(body)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    OUT_DIR.mkdir(exist_ok=True)
    for weight, name in WEIGHTS.items():
        ttf = (src / name).read_bytes()
        woff = to_woff(strip(ttf))
        target = OUT_DIR / f"Alstom-{weight}.woff"
        target.write_bytes(woff)
        print(f"{target}: {len(ttf) // 1024} KB TTF -> {len(woff) // 1024} KB WOFF")


if __name__ == "__main__":
    main()
