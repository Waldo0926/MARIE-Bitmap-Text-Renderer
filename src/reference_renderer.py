from __future__ import annotations

import json
from pathlib import Path

DISPLAY_WIDTH = 16
DISPLAY_HEIGHT = 16
GLYPH_WIDTH = 4
GLYPH_HEIGHT = 8


def load_glyphs(path: str | Path) -> dict[str, list[str]]:
    glyphs = json.loads(Path(path).read_text(encoding="utf-8"))
    for letter, rows in glyphs.items():
        if len(rows) != GLYPH_HEIGHT or any(len(row) != GLYPH_WIDTH for row in rows):
            raise ValueError(f"{letter}: expected {GLYPH_WIDTH}x{GLYPH_HEIGHT} glyph")
        if any(set(row) - {"0", "1"} for row in rows):
            raise ValueError(f"{letter}: glyph must contain only 0/1")
    return glyphs


def normalise_text(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalpha() and ch.upper() <= "Z")


def blank_frame() -> list[list[int]]:
    return [[0 for _ in range(DISPLAY_WIDTH)] for _ in range(DISPLAY_HEIGHT)]


def paint_glyph(frame: list[list[int]], rows: list[str], x: int, y: int) -> None:
    if x < 0 or y < 0 or x + GLYPH_WIDTH > DISPLAY_WIDTH or y + GLYPH_HEIGHT > DISPLAY_HEIGHT:
        raise ValueError("glyph would exceed framebuffer")
    for dy, row in enumerate(rows):
        for dx, bit in enumerate(row):
            frame[y + dy][x + dx] = int(bit)


def render_text(text: str, glyphs: dict[str, list[str]]) -> list[list[int]]:
    """Render up to six letters on a 16x16 framebuffer, three per 8-pixel row."""
    frame = blank_frame()
    text = normalise_text(text)[:6]
    slots = [(0, 0), (5, 0), (10, 0), (0, 8), (5, 8), (10, 8)]
    for ch, (x, y) in zip(text, slots):
        paint_glyph(frame, glyphs[ch], x, y)
    return frame


def frame_to_ascii(frame: list[list[int]]) -> str:
    return "\n".join("".join("#" if pixel else "." for pixel in row) for row in frame)


def framebuffer_addresses(frame: list[list[int]], base: int = 0x0F00) -> dict[int, int]:
    """Map the 16x16 frame to MARIE display-memory addresses."""
    result: dict[int, int] = {}
    for y, row in enumerate(frame):
        for x, pixel in enumerate(row):
            result[base + y * DISPLAY_WIDTH + x] = pixel
    return result
