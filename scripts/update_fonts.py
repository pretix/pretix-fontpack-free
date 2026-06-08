import argparse
import json
import requests
import sys
from collections import namedtuple
from pathlib import Path

Font = namedtuple(
    "Font",
    ["family_name", "display_name", "sample", "pdf_only"],
    defaults=[None, None, None, False],
)

FONTS = [
    Font(
        family_name="Noto Sans",
        display_name="Noto Sans",
        sample="Съешь же ещё этих мягких французских булок да выпей чаю.<br>Ταχίστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός",
    ),
    Font(family_name="Roboto", display_name="Roboto"),
    Font(family_name="Roboto Condensed", display_name="Roboto Condensed"),
    Font(family_name="Fira Sans", display_name="Fira Sans"),
    Font(family_name="Lato", display_name="Lato"),
    Font(family_name="Oswald", display_name="Oswald"),
    Font(family_name="Montserrat", display_name="Montserrat"),
    Font(family_name="Vollkorn", display_name="Vollkorn"),
    Font(family_name="Tajawal", display_name="Tajawal"),
    Font(family_name="Poppins", display_name="Poppins"),
    Font(family_name="Almarai", display_name="Almarai"),
    Font(family_name="Ubuntu", display_name="Ubuntu"),
    Font(family_name="Space Mono", display_name="Space Mono"),
    Font(
        family_name="Noto Sans JP",
        display_name="Noto Sans Japanese",
        sample="あなたに会えて光栄です。",
    ),
    Font(
        family_name="Noto Sans SC",
        display_name="Noto Sans Simplified Chinese",
        sample="真是难以置信！",
    ),
    Font(
        family_name="Noto Sans TC",
        display_name="Noto Sans Traditional Chinese",
        sample="我真歡喜佮你熟似",
    ),
    Font(
        family_name="Noto Sans Thai",
        display_name="Noto Sans Thai",
        sample="สุนัขจิ้งจอกสีม่วง",
    ),
    # Slightly arbitraty list based on Googles Noto FAQ
    Font(family_name="Noto Sans Adlam", display_name="Noto Sans Adlam", pdf_only=True),
    Font(family_name="Noto Sans Arabic", display_name="Noto Sans Arabic", pdf_only=True),
    Font(family_name="Noto Sans Armenian", display_name="Noto Sans Armenian", pdf_only=True),
    Font(family_name="Noto Sans Bengali", display_name="Noto Sans Bengali", pdf_only=True),
    Font(family_name="Noto Sans Cherokee", display_name="Noto Sans Cherokee", pdf_only=True),
    Font(family_name="Noto Sans Ethiopic", display_name="Noto Sans Ethiopic", pdf_only=True),
    Font(family_name="Noto Sans Georgian", display_name="Noto Sans Georgian", pdf_only=True),
    Font(family_name="Noto Sans Gujarati", display_name="Noto Sans Gujarati", pdf_only=True),
    Font(family_name="Noto Sans Gurmukhi", display_name="Noto Sans Gurmukhi", pdf_only=True),
    Font(family_name="Noto Sans Hebrew", display_name="Noto Sans Hebrew", pdf_only=True),
    Font(family_name="Noto Sans Kannada", display_name="Noto Sans Kannada", pdf_only=True),
    Font(family_name="Noto Sans Khmer", display_name="Noto Sans Khmer", pdf_only=True),
    Font(family_name="Noto Sans KR", display_name="Noto Sans Korean", pdf_only=True),
    Font(family_name="Noto Sans Lao", display_name="Noto Sans Lao", pdf_only=True),
    Font(family_name="Noto Sans Malayalam", display_name="Noto Sans Malayalam", pdf_only=True),
    Font(family_name="Noto Sans Myanmar", display_name="Noto Sans Myanmar", pdf_only=True),
    Font(family_name="Noto Sans Oriya", display_name="Noto Sans Oriya", pdf_only=True),
    Font(family_name="Noto Sans Sinhala", display_name="Noto Sans Sinhala", pdf_only=True),
    Font(family_name="Noto Sans Tamil", display_name="Noto Sans Tamil", pdf_only=True),
    Font(family_name="Noto Sans Telugu", display_name="Noto Sans Telugu", pdf_only=True),
]


CATALOG_NAME = "catalog.json"
VARIANTS = {
    "regular": "regular",
    "bold": "700",
    "italic": "italic",
    "bolditalic": "700italic",
}
REQUIRED_VARIANT = "regular"
FORMATS = {
    "truetype": {"ending": "ttf"},
    "woff2": {"ending": "woff2", "params": {"capability": "woff2"}},
}


def generate_catalog(out_dir: Path, api_key: str):
    catalog = {}
    name_mapping = {}
    for font in FONTS:
        catalog[font.display_name] = {"pdf_only": font.pdf_only}
        if font.sample:
            catalog[font.display_name]["sample"] = font.sample
        name_mapping[font.family_name] = font.display_name

    for format, options in FORMATS.items():
        resp = requests.get(
            "https://webfonts.googleapis.com/v1/webfonts",
            params={"key": api_key, **options.get("params", {})},
        )
        resp.raise_for_status()

        for family in resp.json()["items"]:
            if family["family"] not in name_mapping:
                continue

            display_name = name_mapping[family["family"]]

            for variant, google_name in VARIANTS.items():
                if google_name not in family["variants"]:
                    if variant == REQUIRED_VARIANT:
                        print("Missing Variant:", display_name, variant)
                    continue

                outname = f"{family['family'].replace(" ", "-")}_{family['version']}_{variant}.{options['ending']}"
                catalog[display_name].setdefault(variant, {})
                catalog[display_name][variant][format] = outname

                url = family["files"][google_name]
                assert url.endswith("." + options["ending"])
                if not (out_dir / outname).exists():
                    req = requests.get(url)
                    req.raise_for_status()
                    with open(out_dir / outname, "wb") as f:
                        f.write(req.content)
    return catalog


def get_font_files(catalog):
    files = set()
    for variants in catalog.values():
        for formats in variants.values():
            if isinstance(formats, dict):
                files |= set(formats.values())
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("api_key")
    parser.add_argument("--keep-old", action="store_true")
    args = parser.parse_args()

    out_dir = args.output_dir
    out_dir.mkdir(exist_ok=True)
    api_key = args.api_key

    catalog = generate_catalog(out_dir, api_key)

    missing_scripts = [k for k, v in catalog.items() if REQUIRED_VARIANT not in v]
    if missing_scripts:
        print(f"[ERROR] Missing scripts: {', '.join(missing_scripts)}; Aborting")
        sys.exit(1)

    catalog_file = out_dir / CATALOG_NAME

    if not args.keep_old:
        with open(catalog_file, "r") as f:
            old_catalog = json.load(f)

        old_files = get_font_files(old_catalog)
        new_files = get_font_files(catalog)
        outdated_files = old_files - new_files
        if outdated_files:
            print(f"Found {len(outdated_files)} outdated font files. Deleting...")
            for file in outdated_files:
                path: Path = out_dir / file
                print(path)
                path.unlink(missing_ok=True)

    with open(catalog_file, "w") as f:
        json.dump(catalog, f)
