# MARIE 位图文字渲染器

[English](README.md)

这是一个课程结束后重新实现的低层图形项目，用于展示 **MARIE 汇编、间接寻址、指针、子程序、位图字体以及 16×16 memory-mapped framebuffer**。

> 本仓库是基于 FIT1047 中学到的概念重新实现的独立项目，**不是原始 assessment submission**，也不包含 Monash 的作业模板、题目或提交答案。

## 核心原理

MARIE 风格显示器将 `0x0F00`–`0x0FFF` 共 256 个 memory word 映射成 16×16 framebuffer。一个 4×8 字符包含 32 个像素，因此字符渲染本质上是通过指针把 font data 拷贝到显示内存。

每写完 4 个像素后，目标指针额外前进 12 个 word，从而跳到下一条 16 像素 framebuffer 行中相同的横向位置。

## 内容

- `assembly/renderer.mas`：独立的 MARIE 核心示例，清屏并通过间接寻址绘制字符；
- `font/glyphs.json`：重新设计的 4×8 A–Z 位图字体；
- `src/reference_renderer.py`：Python reference model，可在 16×16 framebuffer 上排版 6 个字符；
- `scripts/generate_font_data.py`：将 JSON 字体生成 MARIE `HEX` 数据；
- `scripts/render_demo.py`：生成 `HELLO` 的确定性 framebuffer；
- unit tests 与 GitHub Actions CI。

## 运行

```bash
PYTHONPATH=. python scripts/render_demo.py
PYTHONPATH=. python scripts/generate_font_data.py
python -m unittest discover -s tests -v
```

## 展示的低层知识

- memory-mapped I/O；
- pointer arithmetic；
- `LoadI` / `StoreI` 间接寻址；
- 子程序与返回地址；
- row-major 位图；
- 二维坐标到线性内存地址的映射；
- font data 与 renderer 的分离；
- 用高层 reference model 验证低层逻辑。

## 来源说明

本项目是在 Monash University **FIT1047 Introduction to Computer Systems, Networks and Security** 学习 MARIE 与计算机体系结构基础后重新实现的公开作品集项目。仓库不会公开课程 assessment material 或原始答案。
