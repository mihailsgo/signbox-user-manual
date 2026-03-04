#!/usr/bin/env python3
"""Sanitize sensitive text in screenshots based on YAML spec.

Usage:
    python scripts/sanitize_screenshots.py specs/redactions.yml
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def load_font(size: int) -> ImageFont.ImageFont:
    for candidate in ("arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sample_fill_color(image: Image.Image, x: int, y: int, w: int, h: int) -> tuple[int, int, int]:
    """Approximate background color around the redaction region."""
    px = image.load()
    width, height = image.size
    samples: list[tuple[int, int, int]] = []

    for xx in range(max(0, x - 2), min(width, x + w + 2)):
        if y - 2 >= 0:
            samples.append(tuple(px[xx, y - 2][:3]))
        if y + h + 1 < height:
            samples.append(tuple(px[xx, y + h + 1][:3]))

    for yy in range(max(0, y - 2), min(height, y + h + 2)):
        if x - 2 >= 0:
            samples.append(tuple(px[x - 2, yy][:3]))
        if x + w + 1 < width:
            samples.append(tuple(px[x + w + 1, yy][:3]))

    if not samples:
        return (245, 245, 245)

    channels = list(zip(*samples))
    return tuple(int(statistics.median(channel)) for channel in channels)


def draw_redaction(draw: ImageDraw.ImageDraw, image: Image.Image, region: dict[str, Any], font: ImageFont.ImageFont) -> None:
    x, y, w, h = region["rect"]
    text = str(region.get("text", "REDACTED"))
    text_color = tuple(region.get("text_color", [65, 65, 65]))

    blur_radius = int(region.get("blur_radius", 0))
    if blur_radius > 0:
        crop = image.crop((x, y, x + w, y + h))
        crop = crop.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        image.paste(crop, (x, y))
        if not text:
            return

    fill_color = tuple(region.get("fill_color", sample_fill_color(image, x, y, w, h)))
    draw.rectangle([x, y, x + w, y + h], fill=fill_color)

    tb = draw.textbbox((0, 0), text, font=font)
    tw = tb[2] - tb[0]
    th = tb[3] - tb[1]
    tx = x + max(4, (w - tw) // 2)
    ty = y + max(2, (h - th) // 2)
    draw.text((tx, ty), text, fill=text_color, font=font)


def process_image(repo_root: Path, image_spec: dict[str, Any], font: ImageFont.ImageFont) -> None:
    input_path = repo_root / image_spec["input"]
    output_path = repo_root / image_spec["output"]

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    image = Image.open(input_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    for region in image_spec.get("regions", []):
        draw_redaction(draw, image, region, font)

    image.save(output_path)
    print(f"Sanitized: {output_path}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/sanitize_screenshots.py specs/redactions.yml")
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

    font = load_font(int(spec.get("default_font_size", 20)))
    for image_spec in images:
        process_image(repo_root, image_spec, font)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
