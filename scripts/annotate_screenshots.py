#!/usr/bin/env python3
"""Generate annotated screenshots from a YAML specification.

Usage:
    python scripts/annotate_screenshots.py specs/annotations.yml
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.ImageFont:
    """Load a readable sans-serif font with fallback."""
    for candidate in ("arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: tuple[int, int, int, int],
) -> None:
    """Draw a line arrow from start to end."""
    draw.line([start, end], fill=color, width=5)

    sx, sy = start
    ex, ey = end
    dx, dy = ex - sx, ey - sy
    if dx == 0 and dy == 0:
        return

    angle = math.atan2(dy, dx)
    size = 14
    left = (
        int(ex - size * math.cos(angle - math.pi / 6)),
        int(ey - size * math.sin(angle - math.pi / 6)),
    )
    right = (
        int(ex - size * math.cos(angle + math.pi / 6)),
        int(ey - size * math.sin(angle + math.pi / 6)),
    )
    draw.polygon([end, left, right], fill=color)


def draw_annotation(
    draw: ImageDraw.ImageDraw,
    annotation: dict[str, Any],
    label_font: ImageFont.ImageFont,
    badge_font: ImageFont.ImageFont,
) -> None:
    """Draw one annotation unit: highlight + badge + label + arrow."""
    step = str(annotation.get("step", "?"))
    label = str(annotation.get("label", ""))
    x, y, w, h = annotation["rect"]

    # Tight semi-transparent control highlight.
    draw.rectangle(
        [x, y, x + w, y + h],
        fill=(230, 0, 0, 48),
        outline=(220, 0, 0, 235),
        width=3,
    )

    # Step badge in top-left corner near highlighted control.
    badge_radius = 16
    badge_x = x - badge_radius - 8
    badge_y = y - badge_radius - 8
    draw.ellipse(
        [badge_x, badge_y, badge_x + 2 * badge_radius, badge_y + 2 * badge_radius],
        fill=(210, 0, 0, 245),
        outline=(255, 255, 255, 230),
        width=2,
    )

    bbox = draw.textbbox((0, 0), step, font=badge_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text(
        (badge_x + badge_radius - text_w / 2, badge_y + badge_radius - text_h / 2),
        step,
        fill=(255, 255, 255, 255),
        font=badge_font,
    )

    # Label block. Default position: above highlighted control.
    label_padding = 8
    label_bbox = draw.textbbox((0, 0), label, font=label_font)
    label_w = label_bbox[2] - label_bbox[0]
    label_h = label_bbox[3] - label_bbox[1]

    lx = max(8, x)
    ly = y - (label_h + label_padding * 2 + 8)
    if ly < 8:
        ly = y + h + 8

    draw.rounded_rectangle(
        [lx, ly, lx + label_w + label_padding * 2, ly + label_h + label_padding * 2],
        radius=8,
        fill=(20, 20, 20, 192),
        outline=(255, 255, 255, 215),
        width=1,
    )
    draw.text(
        (lx + label_padding, ly + label_padding),
        label,
        fill=(255, 255, 255, 255),
        font=label_font,
    )

    # Arrow starts at label and points to highlight center.
    arrow_start = (
        lx + (label_w + label_padding * 2) // 2,
        ly + (label_h + label_padding * 2),
    )
    arrow_end = (x + w // 2, y + h // 2)
    draw_arrow(draw, arrow_start, arrow_end, (220, 0, 0, 235))


def process_image(
    repo_root: Path,
    image_spec: dict[str, Any],
    label_font: ImageFont.ImageFont,
    badge_font: ImageFont.ImageFont,
) -> None:
    input_path = repo_root / image_spec["input"]
    output_path = repo_root / image_spec["output"]

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    base = Image.open(input_path).convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for annotation in image_spec.get("annotations", []):
        draw_annotation(draw, annotation, label_font, badge_font)

    out = Image.alpha_composite(base, overlay).convert("RGB")
    out.save(output_path)
    print(f"Generated: {output_path}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/annotate_screenshots.py specs/annotations.yml")
        return 1

    repo_root = Path(__file__).resolve().parents[1]
    spec_path = repo_root / sys.argv[1]
    if not spec_path.exists():
        print(f"Spec file not found: {spec_path}")
        return 1

    with spec_path.open("r", encoding="utf-8") as handle:
        spec = yaml.safe_load(handle)

    images = spec.get("images", [])
    if not images:
        print("No images configured in spec.")
        return 1

    label_font = load_font(20)
    badge_font = load_font(20)

    for image_spec in images:
        process_image(repo_root, image_spec, label_font, badge_font)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
