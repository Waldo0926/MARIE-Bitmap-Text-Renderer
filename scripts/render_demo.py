from pathlib import Path

from src.reference_renderer import frame_to_ascii, load_glyphs, render_text

ROOT = Path(__file__).resolve().parents[1]
glyphs = load_glyphs(ROOT / "font/glyphs.json")
frame = render_text("HELLO", glyphs)
(ROOT / "results/demo.txt").write_text(frame_to_ascii(frame) + "\n", encoding="utf-8")
print(frame_to_ascii(frame))
