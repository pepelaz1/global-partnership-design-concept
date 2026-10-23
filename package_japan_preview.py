"""Package the ten Japan design directions for client review."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "japan-design-concepts-for-review.zip"


def main() -> None:
    files = [(ROOT / "JAPAN_PREVIEW_README.md", "README.md")]
    files += [
        (ROOT / "japan-10-variants.jpg", "preview/japan-10-variants.jpg"),
        (ROOT / "japan-10-icons.jpg", "preview/japan-10-icons.jpg"),
    ]
    for folder in ("png", "svg"):
        files += [(path, f"{folder}/{path.name}")
                  for path in sorted((ROOT / "japan-variants" / folder).glob(f"*.{folder}"))]

    if len(files) != 23:
        raise RuntimeError(f"Expected 23 files, found {len(files)}")
    with ZipFile(OUT, "w", ZIP_DEFLATED) as archive:
        for path, name in files:
            archive.write(path, name)
    print(f"Created {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
