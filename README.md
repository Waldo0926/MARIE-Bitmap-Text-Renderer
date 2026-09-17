# MARIE Bitmap Text Renderer

[![Type](https://img.shields.io/badge/Type-Coursework-2563eb?style=for-the-badge)](#)
[![Tech](https://img.shields.io/badge/Tech-MARIE_%C2%B7_Python-7c3aed?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-16a34a?style=for-the-badge)](LICENSE)


**English** · [中文](README.zh-CN.md)

A post-course low-level graphics project demonstrating **MARIE assembly, indirect addressing, pointers, subroutines, bitmap fonts, and a memory-mapped 16×16 framebuffer**.

> This repository is a new implementation inspired by concepts learned in FIT1047. It is **not the original assessment submission**, and it does not contain the Monash assessment template, specification, or submitted solution.

## Core idea

A MARIE-style display exposes 256 memory words (`0x0F00`–`0x0FFF`) as a 16×16 framebuffer. A 4×8 bitmap glyph therefore contains 32 pixels. Rendering becomes a pointer-copy problem:

```text
4x8 glyph data
     |
     | LoadI source pointer
     v
accumulator
     |
     | StoreI framebuffer pointer
     v
16x16 memory-mapped display
```

At the end of each four-pixel glyph row, the destination pointer advances another 12 words to reach the same x-position on the next 16-pixel framebuffer row.

## What's included

- `assembly/renderer.mas` — a clean, standalone MARIE core example that clears the display and paints a glyph using indirect addressing;
- `font/glyphs.json` — an original 4×8 A–Z bitmap font;
- `src/reference_renderer.py` — executable Python reference model for six-character, two-row text layout;
- `scripts/generate_font_data.py` — converts the JSON font into MARIE `HEX` data words;
- `scripts/render_demo.py` — renders `HELLO` as a deterministic ASCII framebuffer;
- unit tests and GitHub Actions CI.

## Demo

`results/demo.txt` contains the 16×16 framebuffer produced by the Python reference model for `HELLO`. `#` means foreground and `.` means background.

```text
#..#.####.#.....
#..#.#....#.....
#..#.#....#.....
####.###..#.....
...
```

The complete deterministic 16×16 frame is stored in `results/demo.txt`.

## Run the reference model

```bash
PYTHONPATH=. python scripts/render_demo.py
PYTHONPATH=. python scripts/generate_font_data.py
python -m unittest discover -s tests -v
```

## Low-level concepts demonstrated

- memory-mapped I/O;
- pointer arithmetic;
- indirect `LoadI` / `StoreI` addressing;
- subroutine calls and return-address storage;
- row-major bitmap representation;
- translating 2-D coordinates into linear addresses;
- separation between font data and rendering logic;
- using a high-level reference model to test low-level behaviour.

## Origin

This project was rebuilt after learning MARIE and computer-architecture fundamentals in **FIT1047 Introduction to Computer Systems, Networks and Security** at Monash University. The public repository intentionally avoids publishing assessment materials or a reusable answer to the original task.
