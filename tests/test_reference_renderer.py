import unittest
from pathlib import Path

from src.reference_renderer import framebuffer_addresses, load_glyphs, normalise_text, render_text

ROOT = Path(__file__).resolve().parents[1]


class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.glyphs = load_glyphs(ROOT / "font/glyphs.json")

    def test_font_has_full_alphabet(self):
        self.assertEqual(set(self.glyphs), set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_normalisation(self):
        self.assertEqual(normalise_text("He11o, world!"), "HEOWORLD")

    def test_frame_is_16_by_16(self):
        frame = render_text("HELLO", self.glyphs)
        self.assertEqual(len(frame), 16)
        self.assertTrue(all(len(row) == 16 for row in frame))

    def test_text_is_limited_to_six_slots(self):
        frame_a = render_text("ABCDEF", self.glyphs)
        frame_b = render_text("ABCDEFGH", self.glyphs)
        self.assertEqual(frame_a, frame_b)

    def test_address_mapping_covers_display_memory(self):
        addresses = framebuffer_addresses(render_text("A", self.glyphs))
        self.assertEqual(min(addresses), 0x0F00)
        self.assertEqual(max(addresses), 0x0FFF)
        self.assertEqual(len(addresses), 256)


if __name__ == "__main__":
    unittest.main()
