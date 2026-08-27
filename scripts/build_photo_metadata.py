#!/usr/bin/env python3
"""Refresh machine-derived Photography metadata from embedded EXIF.

The live site consumes only ``data/photo-metadata.js``. This maintenance
utility scans the flat ``img/interests/photography/`` directory, refreshes
capture metadata, and preserves the human-maintained fields already stored in
the JavaScript data file. Filesystem timestamps are never used as photograph
capture dates.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from fractions import Fraction
from pathlib import Path

from PIL import ExifTags, Image


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}
STYLE_KEYS = {"nature-landscape", "city-architecture", "night-atmosphere"}
DATA_HEADER = """// Photography metadata for gallery.html.
//
// USER EDITABLE:
// - location.en / location.zh
// - locationStatus / locationNote
// - styleTags / styleStatus
// - comment.en / comment.zh
// - pinnedOrder (positive integer to pin; null to leave in the archive)
//
// EXIF / MACHINE DERIVED (refresh with scripts/build_photo_metadata.py):
// - dateTaken / year / month / exifSource / rawCaptureTime
// - camera / lens / focalLength / aperture / shutter / iso / aspectRatio
//
// Style tags control Gallery filters only. They never control file storage.
"""


def ratio_text(value, suffix=""):
    if value in (None, ""):
        return ""
    number = float(value)
    if number.is_integer():
        return f"{int(number)}{suffix}"
    return f"{number:.1f}".rstrip("0").rstrip(".") + suffix


def shutter_text(value):
    if value in (None, ""):
        return ""
    number = float(value)
    if number <= 0:
        return ""
    if number >= 1:
        return ratio_text(number, " s")
    fraction = Fraction(number).limit_denominator(8000)
    return f"{fraction.numerator}/{fraction.denominator} s"


def camera_text(make, model):
    make = str(make or "").strip()
    model = str(model or "").strip()
    if not model:
        return make
    if make and model.upper().startswith(make.split()[0].upper()):
        return model
    return " ".join(part for part in (make, model) if part)


def capture_datetime(ifd0, exif_ifd):
    # Genuine embedded photographic timestamps only; never use Path.stat().
    for key, source, label in (
        (36867, exif_ifd, "DateTimeOriginal"),
        (36868, exif_ifd, "DateTimeDigitized"),
        (306, ifd0, "DateTime"),
    ):
        raw = source.get(key)
        if not raw:
            continue
        try:
            captured = datetime.strptime(str(raw).strip(), "%Y:%m:%d %H:%M:%S")
            return captured, str(raw).strip(), label
        except ValueError:
            continue
    return None, "", ""


def load_existing(path):
    if not path.exists():
        return {}
    try:
        text = path.read_text(encoding="utf-8")
        payload = text.split("=", 1)[1].rsplit(";", 1)[0]
        records = json.loads(payload)
        return {item["file"]: item for item in records}
    except (IndexError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        print("Warning: existing manual metadata could not be read.")
        return {}


def bilingual(value):
    if isinstance(value, dict):
        return {"en": str(value.get("en", "")), "zh": str(value.get("zh", ""))}
    if isinstance(value, str):
        return {"en": value, "zh": ""}
    return {"en": "", "zh": ""}


def extract(path, previous):
    with Image.open(path) as image:
        width, height = image.size
        ifd0 = image.getexif()
        exif_ifd = ifd0.get_ifd(ExifTags.IFD.Exif)

    captured, raw_captured, exif_source = capture_datetime(ifd0, exif_ifd)
    previous_tags = previous.get("styleTags")
    if isinstance(previous_tags, list):
        style_tags = [tag for tag in previous_tags if tag in STYLE_KEYS]
    elif previous.get("category") in STYLE_KEYS:
        # One-time compatibility with the pre-flat metadata schema.
        style_tags = [previous["category"]]
    else:
        style_tags = []

    location = bilingual(previous.get("location"))
    comment = bilingual(previous.get("comment"))
    previous_pinned_order = previous.get("pinnedOrder")
    pinned_order = (
        previous_pinned_order
        if isinstance(previous_pinned_order, int)
        and not isinstance(previous_pinned_order, bool)
        and previous_pinned_order > 0
        else None
    )
    return {
        "file": path.name,
        "src": f"img/interests/photography/{path.name}",
        "dateTaken": captured.isoformat() if captured else "",
        "year": captured.year if captured else None,
        "month": captured.month if captured else None,
        "location": location,
        "locationStatus": str(previous.get("locationStatus", "unconfirmed")),
        "locationNote": str(previous.get("locationNote", "")),
        "styleTags": style_tags,
        "styleStatus": str(previous.get("styleStatus", "classified" if style_tags else "unclassified")),
        "pinnedOrder": pinned_order,
        "aspectRatio": round(width / height, 6) if height else None,
        "camera": camera_text(ifd0.get(271), ifd0.get(272)),
        "lens": str(exif_ifd.get(42036, "")).strip(),
        "focalLength": ratio_text(exif_ifd.get(37386), " mm"),
        "aperture": f"f/{ratio_text(exif_ifd.get(33437))}" if exif_ifd.get(33437) else "",
        "shutter": shutter_text(exif_ifd.get(33434)),
        "iso": str(exif_ifd.get(34855, "")).strip(),
        "comment": comment,
        "exifSource": exif_source,
        "rawCaptureTime": raw_captured,
    }


def main():
    parser = argparse.ArgumentParser()
    project_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "photo_root",
        nargs="?",
        type=Path,
        default=project_root / "img/interests/photography",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=project_root / "data/photo-metadata.js",
    )
    args = parser.parse_args()

    nested = [path for path in args.photo_root.rglob("*") if path.is_file() and path.parent != args.photo_root and path.suffix.lower() in SUPPORTED]
    if nested:
        raise SystemExit("Photography storage is not flat; move images into the Photography root before refreshing metadata.")

    existing = load_existing(args.output)
    paths = sorted(
        path for path in args.photo_root.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    if len({path.name for path in paths}) != len(paths):
        raise SystemExit("Duplicate Photography filenames detected; metadata was not written.")

    records = [extract(path, existing.get(path.name, {})) for path in paths]
    pinned_orders = [item["pinnedOrder"] for item in records if item["pinnedOrder"] is not None]
    if len(pinned_orders) != len(set(pinned_orders)):
        raise SystemExit("Duplicate pinnedOrder values detected; metadata was not written.")
    payload = json.dumps(records, ensure_ascii=False, indent=2)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        DATA_HEADER + f"window.PHOTO_METADATA = {payload};\n",
        encoding="utf-8",
    )

    readable = sum(bool(item["dateTaken"] or item["camera"] or item["lens"]) for item in records)
    print(f"Wrote {len(records)} records; {readable} contain readable photographic EXIF.")


if __name__ == "__main__":
    main()
