#!/usr/bin/env python3
"""Generate annotated screenshots from a YAML spec.

Usage:
  python scripts/annotate_screenshots.py specs/annotations.yml
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont
import yaml


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in ["arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _draw_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: tuple[int, int, int, int]) -> None:
    draw.line([start, end], fill=color, width=5)
    ex, ey = end
    sx, sy = start
    dx, dy = ex - sx, ey - sy
    if dx == 0 and dy == 0:
        return
    # Simple arrow head
    import math

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


def _annotate_image(root: Path, item: dict[str, Any], label_font: ImageFont.ImageFont, badge_font: ImageFont.ImageFont) -> None:
    inp = root / item["input"]
    out = root / item["output"]

    if not inp.exists():
        raise FileNotFoundError(f"Input image not found: {inp}")

    out.parent.mkdir(parents=True, exist_ok=True)

    img = Image.open(inp).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for ann in item.get("annotations", []):
        step = str(ann.get("step", "?"))
        label = str(ann.get("label", ""))
        x, y, w, h = ann["rect"]

        # Semi-transparent highlight
        draw.rectangle([x, y, x + w, y + h], fill=(255, 0, 0, 60), outline=(255, 0, 0, 220), width=4)

        # Badge (step number)
        badge_r = 18
        bx = x - badge_r - 10
        by = y - badge_r - 10
        draw.ellipse([bx, by, bx + 2 * badge_r, by + 2 * badge_r], fill=(220, 0, 0, 240), outline=(255, 255, 255, 230), width=2)
        tw, th = draw.textbbox((0, 0), step, font=badge_font)[2:4]
        draw.text((bx + badge_r - tw / 2, by + badge_r - th / 2), step, fill=(255, 255, 255, 255), font=badge_font)

        # Label box above or below depending on space
        lx = max(10, x)
        ly = y - 44 if y > 60 else y + h + 8
        tb = draw.textbbox((0, 0), label, font=label_font)
        lw, lh = tb[2], tb[3]
        pad = 8
        draw.rounded_rectangle([lx, ly, lx + lw + 2 * pad, ly + lh + 2 * pad], radius=8, fill=(0, 0, 0, 180), outline=(255, 255, 255, 200), width=1)
        draw.text((lx + pad, ly + pad), label, fill=(255, 255, 255, 255), font=label_font)

        # Arrow from label to highlighted area center
        start = (lx + (lw // 2), ly + lh + 2 * pad)
        end = (x + w // 2, y + h // 2)
        _draw_arrow(draw, start, end, (255, 0, 0, 230))

    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(out)
    print(f"Generated: {out}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/annotate_screenshots.py specs/annotations.yml")
        return 1

    repo_root = Path(__file__).resolve().parents[1]
    spec_path = repo_root / sys.argv[1]

    if not spec_path.exists():
        print(f"Spec file not found: {spec_path}")
        return 1

    with spec_path.open("r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    images = spec.get("images", [])
    if not images:
        print("No images configured in spec.")
        return 1

    label_font = _load_font(20)
    badge_font = _load_font(20)

    for item in images:
        _annotate_image(repo_root, item, label_font, badge_font)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
