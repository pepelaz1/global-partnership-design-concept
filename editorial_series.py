"""Render all 48 supplied countries in the selected Editorial / Orbit direction."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image, ImageDraw, ImageFont

from generate import COUNTRIES
import japan_variants as design

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "editorial-series"
NS = "{http://www.w3.org/2000/svg}"


def serif(size: int) -> ImageFont.FreeTypeFont:
    candidates = [os.environ.get("EDITORIAL_FONT", ""),
                  "/System/Library/Fonts/Supplemental/Georgia.ttf",
                  "C:/Windows/Fonts/georgia.ttf", "Georgia.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]
    for name in candidates:
        if name:
            try:
                return ImageFont.truetype(name, size)
            except OSError:
                pass
    raise RuntimeError("Install Georgia or set EDITORIAL_FONT to a serif .ttf file")


def title(name: str) -> str:
    # Keep short names at the approved size; wrap long names inside the left panel.
    max_width = 603
    size = 165
    while size > 95 and serif(size).getlength(name) > max_width:
        size -= 1
    if serif(size).getlength(name) <= max_width:
        lines = [name]
    else:
        words = name.split()
        splits = [(" ".join(words[:i]), " ".join(words[i:]))
                  for i in range(1, len(words))]
        lines = min(splits, key=lambda pair: max(serif(110).getlength(t) for t in pair))
        size = 110
        while max(serif(size).getlength(t) for t in lines) > max_width:
            size -= 1
    # Give descenders more space above the red rule. On two-line titles keep
    # the first line clear of the small heading while lifting the lower line.
    step = size
    y = 338 if len(lines) == 1 else 342 - (len(lines) - 1) * step
    return "".join(design.line(132, y + i * step, html.escape(text),
                              size, design.NAVY, family="Georgia,serif")
                   for i, text in enumerate(lines))


def flag(code: str) -> str:
    if code == "jp":
        return design.flag(902, 220, 510, 340)
    node = ET.parse(ROOT / "assets" / "flags" / f"{code}.svg").getroot()
    node.attrib.update(x="902", y="220", width="510", height="340",
                       preserveAspectRatio="xMidYMid meet")
    return ('<rect x="902" y="220" width="510" height="340" fill="#fff" '
            'stroke="#dfe6e4" stroke-width="2"/>'
            + ET.tostring(node, encoding="unicode"))


def card(name: str, code: str, index: int) -> str:
    svg = design.concept_01()
    svg = svg.replace(design.line(132, 350, 'Japan', 165, design.NAVY,
                                 family='Georgia,serif'), title(name))
    svg = svg.replace(design.flag(902, 220, 510, 340), flag(code))
    svg = svg.replace('Japan in partnership with Free Recruiters — Editorial',
                      html.escape(name) + ' in partnership with Free Recruiters — Editorial')
    svg = svg.replace(design.line(903, 713, '01 — EDITORIAL', 21, '#658280',
                                  weight=700, spacing=3), '')
    svg = svg.replace(design.line(80, 868, 'DESIGN CONCEPT  /  JAPAN  /  01 OF 10',
                                  16, '#82908F', weight=700, spacing=2), '')
    return '\n'.join(line.rstrip() for line in svg.splitlines())


def main() -> None:
    for folder in ['svg', 'png', 'previews']:
        (OUT / folder).mkdir(parents=True, exist_ok=True)
    previews = []
    for i, (name, code) in enumerate(COUNTRIES, 1):
        stem = name.lower().replace(' ', '-')
        svg = card(name, code, i)
        ET.fromstring(svg)
        (OUT / 'svg' / f'{stem}.svg').write_text(svg, encoding='utf-8')
        png = OUT / 'png' / f'{stem}.png'
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(png))
        with Image.open(png) as image:
            if image.size != (1600, 900):
                raise RuntimeError(f'Unexpected image size: {name}')
            previews.append((name, image.convert('RGB').copy()))
    # Three readable pages, plus one overview of the complete set.
    for page in range(3):
        sheet = Image.new('RGB', (1600, 1000), '#e6eeeb')
        draw = ImageDraw.Draw(sheet)
        for j, (name, image) in enumerate(previews[page * 16:(page + 1) * 16]):
            image.thumbnail((376, 212))
            x, y = 12 + j % 4 * 400, 12 + j // 4 * 250
            sheet.paste(image, (x, y))
            draw.text((x, y + 218), name, fill=design.NAVY)
        sheet.save(OUT / 'previews' / f'overview-{page + 1}.jpg', quality=93)
    all_sheet = Image.new('RGB', (1600, 3000), '#e6eeeb')
    for i in range(3):
        with Image.open(OUT / 'previews' / f'overview-{i + 1}.jpg') as page:
            all_sheet.paste(page, (0, i * 1000))
    all_sheet.save(OUT / 'contact-sheet.jpg', quality=93)
    manifest = [{'country': n, 'code': c,
                 'png': 'png/' + n.lower().replace(' ', '-') + '.png',
                 'svg': 'svg/' + n.lower().replace(' ', '-') + '.svg'} for n, c in COUNTRIES]
    (OUT / 'countries.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    (OUT / 'README.txt').write_text(
        'Free Recruiters — Editorial country series\n\n'
        '48 unique countries from the supplied list, in the selected first design: '
        'Editorial layout with the Orbit mark.\n'
        'PNG: 1600 x 900 pixels. SVG: editable, self-contained vector artwork.\n'
        'Text uses Georgia and Arial; SVG font appearance depends on installed fonts.\n'
        'See contact-sheet.jpg or previews/overview-1.jpg through overview-3.jpg.\n'
        'Vietnam was repeated in the brief. Two more country names are needed '
        'if 50 distinct countries are required.\n'
        'Flag artwork: flag-icons, MIT; see THIRD_PARTY_LICENSES.md.\n', encoding='utf-8')
    with ZipFile(ROOT / 'free-recruiters-editorial-48-countries.zip', 'w', ZIP_DEFLATED) as z:
        for path in sorted(OUT.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(OUT))
        z.write(ROOT / 'THIRD_PARTY_LICENSES.md', 'THIRD_PARTY_LICENSES.md')
    print('Generated 48 PNG + 48 SVG, three overview pages, and the complete ZIP.')


if __name__ == '__main__':
    main()
