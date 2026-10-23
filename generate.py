"""Generate an original Free Recruiters partnership card series.

Install the pinned flag-icons package with ``npm install`` first. The SVG
flags are embedded into each card; outputs do not depend on external URLs.
"""

from __future__ import annotations

import html
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
FLAGS = ROOT / "node_modules" / "flag-icons" / "flags" / "4x3"

# The supplied brief repeats Vietnam. Keep the 48 unique countries in its order.
COUNTRIES = [
    ("Colombia", "co"), ("Chile", "cl"), ("Paraguay", "py"),
    ("Argentina", "ar"), ("Brazil", "br"), ("Uruguay", "uy"),
    ("Bolivia", "bo"), ("Venezuela", "ve"), ("Ecuador", "ec"),
    ("Peru", "pe"), ("Nigeria", "ng"), ("South Africa", "za"),
    ("Rwanda", "rw"), ("Liberia", "lr"), ("Ghana", "gh"),
    ("Burkina Faso", "bf"), ("Algeria", "dz"), ("Angola", "ao"),
    ("Morocco", "ma"), ("Egypt", "eg"), ("China", "cn"),
    ("Nepal", "np"), ("Malaysia", "my"), ("Thailand", "th"),
    ("India", "in"), ("Indonesia", "id"), ("Japan", "jp"),
    ("South Korea", "kr"), ("Vietnam", "vn"), ("Pakistan", "pk"),
    ("Philippines", "ph"), ("Finland", "fi"), ("Germany", "de"),
    ("Austria", "at"), ("Hungary", "hu"), ("France", "fr"),
    ("Italy", "it"), ("Denmark", "dk"), ("Netherlands", "nl"),
    ("Greece", "gr"), ("Poland", "pl"), ("San Marino", "sm"),
    ("Liechtenstein", "li"), ("Moldova", "md"),
    ("North Macedonia", "mk"), ("Bosnia and Herzegovina", "ba"),
    ("Kiribati", "ki"), ("Guyana", "gy"),
]


def icon(x: int, y: int, size: int) -> str:
    """A custom two-person / connection mark, without third-party branding."""
    return f'''<g transform="translate({x} {y}) scale({size / 108})">
      <rect width="108" height="108" rx="30" fill="#123E4A"/>
      <circle cx="35" cy="35" r="10" fill="#7CD6C0"/>
      <circle cx="73" cy="35" r="10" fill="#E8C58B"/>
      <path d="M24 75c1-15 9-24 21-24 8 0 14 4 18 11"
            fill="none" stroke="#7CD6C0" stroke-width="10" stroke-linecap="round"/>
      <path d="M84 75c-1-15-9-24-21-24-8 0-14 4-18 11"
            fill="none" stroke="#E8C58B" stroke-width="10" stroke-linecap="round"/>
      <path d="M42 76h24" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
    </g>'''


def flag_svg(code: str) -> str:
    source = FLAGS / f"{code}.svg"
    if not source.is_file():
        raise FileNotFoundError(f"Flag not found: {source}")
    root = ET.parse(source).getroot()
    # Preserve the flag's intrinsic viewBox (including the unusual Nepal shape).
    root.set("x", "143")
    root.set("y", "255")
    root.set("width", "560")
    root.set("height", "420")
    root.set("preserveAspectRatio", "xMidYMid meet")
    return ET.tostring(root, encoding="unicode")


def card(name: str, code: str, number: int) -> str:
    safe_name = html.escape(name)
    country_size = 82 if len(name) < 18 else 65
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900"
      role="img" aria-label="{safe_name} in partnership with Free Recruiters">
      <defs>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="160%">
          <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#0D343C" flood-opacity=".13"/>
        </filter>
      </defs>
      <rect width="1600" height="900" fill="#EEF3F1"/>
      <path d="M0 0h1600v14H0z" fill="#123E4A"/>
      <text x="79" y="91" font-family="Arial,sans-serif" font-size="20" font-weight="700"
            letter-spacing="4" fill="#2B6B72">GLOBAL PARTNERSHIPS</text>
      <text x="1521" y="91" text-anchor="end" font-family="Arial,sans-serif" font-size="19"
            letter-spacing="2" fill="#5B777B">{number:02d} / {len(COUNTRIES):02d}</text>
      <rect x="65" y="139" width="1470" height="676" rx="38" fill="#FFFFFF" filter="url(#shadow)"/>
      <rect x="95" y="169" width="650" height="616" rx="28" fill="#F5F8F7"/>
      <rect x="120" y="229" width="600" height="471" rx="18" fill="#FFFFFF"
            stroke="#DEE9E6" stroke-width="2"/>
      {flag_svg(code)}
      <text x="145" y="745" font-family="Arial,sans-serif" font-size="19" font-weight="700"
            letter-spacing="3" fill="#5B777B">{code.upper()} · INTERNATIONAL COLLABORATION</text>
      {icon(798, 218, 100)}
      <text x="927" y="259" font-family="Arial,sans-serif" font-size="35" font-weight="800"
            letter-spacing="1.5" fill="#123E4A">FREE</text>
      <text x="927" y="301" font-family="Arial,sans-serif" font-size="35" font-weight="800"
            letter-spacing="1.5" fill="#123E4A">RECRUITERS</text>
      <rect x="800" y="378" width="76" height="7" rx="3.5" fill="#59BDA6"/>
      <text x="795" y="496" font-family="Arial,sans-serif" font-size="{country_size}" font-weight="700"
            fill="#153D48">{safe_name}</text>
      <text x="800" y="559" font-family="Arial,sans-serif" font-size="27" font-weight="700"
            letter-spacing="2.6" fill="#248F83">IN PARTNERSHIP WITH</text>
      <text x="800" y="623" font-family="Arial,sans-serif" font-size="39" font-weight="700"
            fill="#123E4A">Free Recruiters</text>
      <path d="M800 681h660" stroke="#D9E8E4" stroke-width="2"/>
      <text x="800" y="727" font-family="Arial,sans-serif" font-size="21"
            fill="#647E80">Connecting people. Creating opportunity.</text>
      <text x="80" y="863" font-family="Arial,sans-serif" font-size="17"
            letter-spacing="1.5" fill="#6E898B">DESIGN CONCEPT · ORIGINAL BRAND MARK</text>
    </svg>'''


def brand_svg() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="280" viewBox="0 0 900 280"
      role="img" aria-label="Free Recruiters logo concept">
      <rect width="900" height="280" rx="34" fill="#EEF3F1"/>
      {icon(64, 65, 150)}
      <text x="252" y="128" font-family="Arial,sans-serif" font-size="56" font-weight="800"
            letter-spacing="2" fill="#123E4A">FREE</text>
      <text x="252" y="193" font-family="Arial,sans-serif" font-size="56" font-weight="800"
            letter-spacing="2" fill="#123E4A">RECRUITERS</text>
    </svg>'''


def contact_sheet(files: list[Path]) -> None:
    cols, tile_w, tile_h = 4, 400, 255
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), "#e6eeeb")
    draw = ImageDraw.Draw(sheet)
    for i, file in enumerate(files):
        with Image.open(file) as src:
            preview = src.convert("RGB")
            preview.thumbnail((tile_w - 24, tile_h - 44))
        x = (i % cols) * tile_w + 12
        y = (i // cols) * tile_h + 12
        sheet.paste(preview, (x, y))
        draw.text((x, y + 218), file.stem.replace("-", " ").title(), fill="#123E4A")
    sheet.save(OUT / "contact-sheet.jpg", quality=90)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "svg").mkdir(exist_ok=True)
    (OUT / "png").mkdir(exist_ok=True)
    logo = brand_svg()
    (OUT / "free-recruiters-logo.svg").write_text(logo, encoding="utf-8")
    cairosvg.svg2png(bytestring=logo.encode(), write_to=str(OUT / "free-recruiters-logo.png"))
    previews = []
    for index, (name, code) in enumerate(COUNTRIES, 1):
        stem = name.lower().replace(" ", "-")
        svg = card(name, code, index)
        svg_file = OUT / "svg" / f"{stem}.svg"
        png_file = OUT / "png" / f"{stem}.png"
        svg_file.write_text(svg, encoding="utf-8")
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(png_file))
        previews.append(png_file)
    contact_sheet(previews)
    print(f"Generated {len(COUNTRIES)} original partnership cards in {OUT}")


if __name__ == "__main__":
    main()
