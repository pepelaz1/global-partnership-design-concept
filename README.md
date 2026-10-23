# Free Recruiters · Global Partnership Concept

An **independent portfolio concept** for an international recruiting brand. It contains an original logo mark and a consistent 1600 × 900 partnership card for each unique country in a sample brief. The Toptal logo shown in the supplied reference is not used.

![Japan partnership card](japan.png)

[View the overview of all 48 cards](contact-sheet.jpg) · [Download the complete SVG and PNG series](free-recruiters-design-concept.zip)

## Ten directions for Japan

The [comparison sheet](japan-10-variants.jpg) shows ten different layouts. Each now has its own original, code-drawn mark matched to its visual style; compare the marks on the [icon sheet](japan-10-icons.jpg). All cards use an accurately proportioned Japanese flag. [Download all ten as SVG and PNG](japan-10-variants.zip).

[Download the review package](japan-design-concepts-for-review.zip) for all ten PNG previews, editable SVG files, both comparison sheets, and a short guide. These are initial concepts for feedback; the layouts, icons, colors, and fonts can be refined before producing the remaining country cards.

|  |  |  |  |
|---|---|---|---|
| [01 Editorial](japan-01-editorial.png) | [02 Midnight](japan-02-midnight.png) | [03 Split](japan-03-split.png) | [04 Museum](japan-04-museum.png) |
| [05 Travel poster](japan-05-travel-poster.png) | [06 Diagonal](japan-06-diagonal.png) | [07 Airy glass](japan-07-airy-glass.png) | [08 Ribbon](japan-08-ribbon.png) |
| [09 Swiss grid](japan-09-swiss-grid.png) | [10 Certificate](japan-10-certificate.png) | | |

Run `python japan_variants.py` to regenerate this set after installing the dependencies below.

## Deliverables

- `output/free-recruiters-logo.svg` and `.png` — original brand concept
- `output/svg/` — 48 editable, self-contained SVG cards
- `output/png/` — matching PNG cards at 1600 × 900 pixels
- `output/contact-sheet.jpg` — overview of the series

The source list contained **49 entries but 48 unique countries**, because Vietnam was listed twice. Two additional countries would need to be specified to reach 50 distinct versions.

## Build

Install the flag source package and run the generator:

```powershell
npm install
python -m pip install -r requirements.txt
python generate.py
```

The generated cards embed the flag artwork directly and do not fetch images from a server when opened. The flag artwork comes from [flag-icons](https://github.com/lipis/flag-icons), copyright Panayiotis Lipiridis and contributors, under the MIT license; see `THIRD_PARTY_LICENSES.md`.

This is a design demonstration, not an assertion of any actual partnership between Free Recruiters and the listed countries or governments. Brand names are used solely to illustrate the requested layout.
