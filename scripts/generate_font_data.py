from pathlib import Path

from src.reference_renderer import load_glyphs

ROOT = Path(__file__).resolve().parents[1]
glyphs = load_glyphs(ROOT / "font/glyphs.json")
lines = ["/ Generated 4x8 bitmap font data. 0000=background, F00F=foreground."]
for letter in sorted(glyphs):
    lines.append(f"Glyph{letter}, HEX 0000 / marker for {letter}; data starts on next word")
    for row in glyphs[letter]:
        for bit in row:
            lines.append(f"    HEX {'F00F' if bit == '1' else '0000'}")
(ROOT / "assembly/generated_font_data.mas").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("generated assembly/generated_font_data.mas")
