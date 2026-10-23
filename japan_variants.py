"""Ten distinct, editable Japan partnership card concepts (1600 × 900)."""

from __future__ import annotations

from pathlib import Path
from shutil import copyfile
from zipfile import ZIP_DEFLATED, ZipFile

import cairosvg
from PIL import Image, ImageDraw, ImageFont

from generate import icon


ROOT = Path(__file__).resolve().parent
DEST = ROOT / "japan-variants"
SVG = DEST / "svg"
PNG = DEST / "png"
NAVY = "#123E4A"
RED = "#BC002D"
CREAM = "#F5F2EA"


def flag(x: int, y: int, w: int, h: int, *, border: str = "#dfe6e4") -> str:
    """Japan flag, 3:2 aspect ratio and red disc at 3/5 of flag height."""
    assert w * 2 == h * 3
    return f'''<g>
      <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff"
            stroke="{border}" stroke-width="2"/>
      <circle cx="{x+w/2:g}" cy="{y+h/2:g}" r="{h*0.3:g}" fill="{RED}"/>
    </g>'''


def lockup(x: int, y: int, *, scale: float = 1, color: str = NAVY,
           marker: bool = True) -> str:
    mark = icon(x, y, int(82 * scale)) if marker else ""
    tx = x + (104 if marker else 0) * scale
    return f'''{mark}<g font-family="Arial, sans-serif" font-weight="800" fill="{color}">
      <text x="{tx:g}" y="{y+34*scale:g}" font-size="{32*scale:g}" letter-spacing="1.6">FREE</text>
      <text x="{tx:g}" y="{y+73*scale:g}" font-size="{32*scale:g}" letter-spacing="1.6">RECRUITERS</text>
    </g>'''


def line(x: int, y: int, words: str, size: int, color: str, *,
         family: str = "Arial, sans-serif", weight: int = 400,
         anchor: str = "start", spacing: int = 0) -> str:
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{spacing}" fill="{color}">{words}</text>')


def wrap(body: str, number: int, name: str, bg: str) -> str:
    footer = line(80, 868, f"DESIGN CONCEPT  /  JAPAN  /  {number:02d} OF 10",
                  16, "#82908F", weight=700, spacing=2)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900"
      viewBox="0 0 1600 900" role="img"
      aria-label="Japan in partnership with Free Recruiters — {name}">
      <defs>
        <filter id="shadow"><feDropShadow dx="0" dy="14" stdDeviation="20"
          flood-color="#081F29" flood-opacity=".18"/></filter>
        <linearGradient id="sky" x2="1" y2="1"><stop stop-color="#d9f2f0"/>
          <stop offset="1" stop-color="#eef4ff"/></linearGradient>
      </defs>
      <rect width="1600" height="900" fill="{bg}"/>
      {body}
      {footer}
    </svg>'''


def concept_01() -> str:
    body = f'''
      <rect x="74" y="66" width="1452" height="744" fill="#FFFEFA"/>
      <rect x="74" y="66" width="12" height="744" fill="{RED}"/>
      {line(132,145,'INTERNATIONAL PARTNERSHIP',20,NAVY,weight=700,spacing=4)}
      {line(132,350,'Japan',165,NAVY,family='Georgia,serif')}
      <path d="M137 390H735" stroke="{RED}" stroke-width="5"/>
      {line(132,467,'In partnership with',35,'#5D7778')}
      {line(132,530,'Free Recruiters',58,NAVY,weight=700)}
      {lockup(132,659,scale=.88)}
      <rect x="875" y="151" width="560" height="520" rx="16" fill="#F3F5F1"/>
      <g filter="url(#shadow)">{flag(902,220,510,340)}</g>
      {line(903,713,'01 — EDITORIAL',21,'#658280',weight=700,spacing=3)}
    '''
    return wrap(body, 1, "Editorial", CREAM)


def concept_02() -> str:
    body = f'''
      <circle cx="1330" cy="110" r="340" fill="#8A1732" opacity=".65"/>
      <circle cx="1500" cy="620" r="270" fill="#183A54"/>
      <path d="M83 91H1515" stroke="#486B76" stroke-width="2"/>
      {line(90,135,'GLOBAL ALLIANCES',20,'#86D2C9',weight=700,spacing=5)}
      <g filter="url(#shadow)">{flag(92,246,600,400,border='#fff')}</g>
      {line(807,333,'JAPAN',108,'#FFFFFF',weight=800,spacing=3)}
      <rect x="811" y="375" width="110" height="6" fill="#EAAE95"/>
      {line(811,448,'IN PARTNERSHIP WITH',26,'#9FDAD3',weight=700,spacing=2)}
      {line(811,518,'FREE RECRUITERS',48,'#FFFFFF',weight=700)}
      {lockup(811,635,scale=.85,color='#FFFFFF')}
    '''
    return wrap(body, 2, "Midnight", "#0B2230")


def concept_03() -> str:
    body = f'''
      <rect width="675" height="900" fill="{RED}"/>
      <rect x="675" width="925" height="900" fill="#FAFAF7"/>
      {line(75,139,'COUNTRY SERIES  /  03',20,'#FFE4E6',weight=700,spacing=3)}
      <g filter="url(#shadow)">{flag(80,190,465,310,border='#ffffff')}</g>
      {line(73,665,'JAPAN',105,'#FFFFFF',weight=800,spacing=6)}
      {line(80,718,'PARTNERSHIP CONCEPT',24,'#FFE4E6',weight=700,spacing=2)}
      {lockup(783,176,scale=1.1)}
      <rect x="785" y="376" width="650" height="2" fill="#D3DCDA"/>
      {line(785,488,'In partnership',66,NAVY,family='Georgia,serif')}
      {line(785,568,'with Free Recruiters',52,NAVY,family='Georgia,serif')}
      {line(785,679,'CONNECTING TALENT ACROSS BORDERS',21,'#63817F',weight=700,spacing=2)}
    '''
    return wrap(body, 3, "Split", "#FAFAF7")


def concept_04() -> str:
    body = f'''
      <path d="M75 85H1525 M75 813H1525" stroke="#161C1D" stroke-width="3"/>
      {line(78,151,'FREE RECRUITERS',19,'#1B2628',weight=700,spacing=5)}
      {line(1524,151,'COUNTRY / 027',19,'#1B2628',weight=700,anchor='end',spacing=3)}
      {line(800,280,'J A P A N',130,'#151C1D',family='Georgia,serif',anchor='middle')}
      <path d="M320 320H1280" stroke="#DADADA" stroke-width="2"/>
      {flag(590,369,420,280)}
      {line(800,734,'JAPAN IN PARTNERSHIP WITH FREE RECRUITERS',29,'#151C1D',weight=700,anchor='middle',spacing=2)}
      {icon(782, 754, 36)}
    '''
    return wrap(body, 4, "Museum", "#FDFDFB")


def concept_05() -> str:
    body = f'''
      <rect x="280" y="43" width="1040" height="770" fill="#F6E9D8"/>
      <circle cx="1060" cy="271" r="174" fill="{RED}"/>
      <path d="M280 650Q620 557 912 655T1320 619V813H280Z" fill="#1A4E56"/>
      <path d="M280 716Q670 621 934 734T1320 694V813H280Z" fill="#0B343D"/>
      <rect x="342" y="107" width="298" height="200" fill="#fff" filter="url(#shadow)"/>
      {flag(342,107,300,200,border='#fff')}
      {line(350,415,'Japan',113,NAVY,family='Georgia,serif')}
      {line(353,479,'IN PARTNERSHIP WITH',25,NAVY,weight=700,spacing=3)}
      {line(353,537,'FREE RECRUITERS',48,NAVY,weight=800)}
      {lockup(353,696,scale=.72,color='#FFFFFF')}
      {line(1248,760,'05',42,'#F2D8C4',anchor='end',weight=700)}
    '''
    return wrap(body, 5, "Travel poster", "#E9D5C0")


def concept_06() -> str:
    body = f'''
      <path d="M0 0H1010L563 900H0Z" fill="#0A3347"/>
      <path d="M1086 0H1600V900H647Z" fill="#238E87"/>
      <path d="M1490 0H1600V900H1162Z" fill="#1E6B73"/>
      {line(83,127,'FR / GLOBAL SERIES',21,'#82D8CB',weight=700,spacing=4)}
      {line(80,341,'JAPAN',116,'#FFFFFF',weight=800,spacing=3)}
      {line(88,416,'IN PARTNERSHIP WITH',26,'#92D9CD',weight=700,spacing=2)}
      {line(88,480,'FREE RECRUITERS',46,'#FFFFFF',weight=700)}
      {lockup(89,641,scale=.82,color='#FFFFFF')}
      <rect x="897" y="183" width="606" height="459" rx="28" fill="#fff" filter="url(#shadow)"/>
      {flag(926,211,546,364,border='#fff')}
      {line(1199,615,'JAPAN  /  JP',19,NAVY,weight=700,anchor='middle',spacing=4)}
    '''
    return wrap(body, 6, "Diagonal", NAVY)


def concept_07() -> str:
    body = f'''
      <rect width="1600" height="900" fill="url(#sky)"/>
      <circle cx="65" cy="685" r="345" fill="none" stroke="#B2D3DB" stroke-width="2"/>
      <circle cx="1529" cy="80" r="280" fill="none" stroke="#B2D3DB" stroke-width="2"/>
      <rect x="120" y="123" width="1360" height="637" rx="45" fill="#FFFFFF" opacity=".88" filter="url(#shadow)"/>
      <rect x="169" y="175" width="615" height="533" rx="29" fill="#EAF2F2"/>
      {flag(206,244,540,360,border='#fff')}
      {line(206,671,'COUNTRY SPOTLIGHT',18,'#6297A1',weight=700,spacing=4)}
      {lockup(854,190,scale=.92)}
      {line(850,422,'Japan',99,NAVY,family='Georgia,serif')}
      <rect x="855" y="458" width="92" height="8" rx="4" fill="{RED}"/>
      {line(855,535,'In partnership with',32,'#517D84')}
      {line(855,602,'Free Recruiters',50,NAVY,weight=700)}
    '''
    return wrap(body, 7, "Airy glass", "#E6F1F3")


def concept_08() -> str:
    body = f'''
      {lockup(95,78,scale=.9)}
      {line(1508,134,'GLOBAL PARTNERSHIPS',20,'#456D72',weight=700,anchor='end',spacing=3)}
      <path d="M0 243H1600V515H0Z" fill="{RED}"/>
      <path d="M1340 243l-92 136 92 136" fill="#8F0729"/>
      {line(101,402,'JAPAN',123,'#FFFFFF',weight=800,spacing=4)}
      {line(111,464,'IN PARTNERSHIP WITH FREE RECRUITERS',30,'#FFF0F1',weight=700,spacing=2)}
      <rect x="890" y="382" width="527" height="381" rx="10" fill="#FFFFFF" filter="url(#shadow)"/>
      {flag(910,399,480,320,border='#fff')}
      {line(100,650,'A shared visual language',57,NAVY,family='Georgia,serif')}
      {line(102,710,'for global collaboration.',38,'#5C7E7D',family='Georgia,serif')}
    '''
    return wrap(body, 8, "Ribbon", "#F8F6F1")


def concept_09() -> str:
    body = f'''
      <path d="M800 0V900 M0 451H1600" stroke="#E4E8E6" stroke-width="3"/>
      {icon(77, 77, 55)}
      {line(150,116,'FREE RECRUITERS',21,NAVY,weight=800,spacing=1)}
      {line(742,132,'09 / 10',17,'#829497',weight=700,anchor='end',spacing=3)}
      {line(66,402,'JP',290,RED,weight=800,spacing=-12)}
      {line(874,142,'JAPAN',31,NAVY,weight=700,spacing=5)}
      {flag(890,179,525,350)}
      {line(82,561,'A partnership',52,NAVY,family='Georgia,serif')}
      {line(82,629,'in focus.',52,NAVY,family='Georgia,serif')}
      {line(866,616,'JAPAN',47,NAVY,weight=800,spacing=2)}
      {line(866,676,'IN PARTNERSHIP WITH',25,'#479489',weight=700,spacing=2)}
      {line(866,731,'FREE RECRUITERS',36,NAVY,weight=700)}
    '''
    return wrap(body, 9, "Swiss grid", "#FFFFFF")


def concept_10() -> str:
    body = f'''
      <rect x="62" y="53" width="1476" height="767" rx="6" fill="none" stroke="#BCA77B" stroke-width="3"/>
      <rect x="76" y="67" width="1448" height="739" rx="2" fill="none" stroke="#D8C9A8" stroke-width="1.5"/>
      {line(800,154,'GLOBAL PARTNERSHIP SERIES',21,'#82775F',weight=700,anchor='middle',spacing=5)}
      {flag(665,194,270,180,border='#D7CCB2')}
      <path d="M570 418H1030" stroke="#BCA77B" stroke-width="2"/>
      {line(800,539,'Japan',102,NAVY,family='Georgia,serif',anchor='middle')}
      {line(800,611,'IN PARTNERSHIP WITH',25,'#8A7960',weight=700,anchor='middle',spacing=3)}
      {line(800,671,'Free Recruiters',50,NAVY,family='Georgia,serif',anchor='middle')}
      <path d="M583 721H1017" stroke="#BCA77B" stroke-width="2"/>
      {icon(774, 729, 49)}
      {line(800,796,'DESIGN STUDY  •  2026',17,'#8A7960',weight=700,anchor='middle',spacing=3)}
    '''
    return wrap(body, 10, "Certificate", "#FAF7F0")


CONCEPTS = [
    ("01-editorial", concept_01), ("02-midnight", concept_02),
    ("03-split", concept_03), ("04-museum", concept_04),
    ("05-travel-poster", concept_05), ("06-diagonal", concept_06),
    ("07-airy-glass", concept_07), ("08-ribbon", concept_08),
    ("09-swiss-grid", concept_09), ("10-certificate", concept_10),
]


def main() -> None:
    SVG.mkdir(parents=True, exist_ok=True)
    PNG.mkdir(parents=True, exist_ok=True)
    previews = []
    for stem, make in CONCEPTS:
        source = make()
        svg_path, png_path = SVG / f"{stem}.svg", PNG / f"{stem}.png"
        svg_path.write_text(source, encoding="utf-8")
        cairosvg.svg2png(bytestring=source.encode(), write_to=str(png_path))
        copyfile(png_path, ROOT / f"japan-{stem}.png")
        previews.append((stem, png_path))

    sheet = Image.new("RGB", (1640, 2490), "#E6EBE9")
    draw = ImageDraw.Draw(sheet)
    for i, (stem, path) in enumerate(previews):
        with Image.open(path) as im:
            thumb = im.convert("RGB")
            thumb.thumbnail((780, 439))
        x, y = 20 + (i % 2) * 820, 15 + (i // 2) * 496
        sheet.paste(thumb, (x, y))
        draw.text((x + 8, y + 446), stem.replace("-", " ").upper(), fill=NAVY)
    sheet.save(ROOT / "japan-10-variants.jpg", quality=92)

    with ZipFile(ROOT / "japan-10-variants.zip", "w", ZIP_DEFLATED) as archive:
        for path in sorted(DEST.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT))
    print(f"Generated {len(CONCEPTS)} concepts in {DEST}")


if __name__ == "__main__":
    main()
