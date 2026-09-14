# -*- coding: utf-8 -*-
"""
render_pdf.py

Renders Class_07_Operators_and_Expressions.pptx to a PDF by
replaying the exact same slide-building calls from
generate_presentation.py against a lightweight in-memory shim (instead
of python-pptx's real Presentation object), then rasterizing each slide
with Pillow into one multi-page PDF.

WHY THIS EXISTS
----------------
This environment has no working PowerPoint COM automation or LibreOffice
available for .pptx -> PDF conversion (the same finding documented in
Class 01's PRESENTATION_README.md §9 for visual QA rendering, and
re-verified for Classes 03-06: PowerPoint COM instantiates but
returns a broken proxy with no interactive desktop session available,
and no LibreOffice/unoconv/docx2pdf install exists on this machine).
This script is the pure-Python fallback used instead, identical in
approach to Class 06's `03_Presentation/render_pdf.py`.

It is geometry-accurate rather than a re-interpretation of the design:
every shape, position, color, and text run rendered here comes from
literally running the same slide-builder functions
(`generate_presentation.SLIDE_BUILDERS`) that produce the real .pptx —
just against a shim object graph that records primitives instead of
writing OOXML. There is exactly one source of truth for slide content;
this file only adds a rasterizer.

Fonts: substitutes Calibri for Aptos/Aptos Display (not installed on
this machine), matching Class 01's documented QA substitution. Sizes,
weights, colors, and positions are exact; the saved .pptx itself still
specifies Aptos/Aptos Display and will render in those fonts on any
machine that has them.

Usage:
    python render_pdf.py

Re-run whenever generate_presentation.py changes — this script imports
it directly, so there is nothing to keep in sync by hand.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

import generate_presentation as gp

# ============================================================================
# Scale / fonts
# ============================================================================

DPI = 150
EMU_PER_INCH = 914400


def emu_to_px(v):
    return v * DPI / EMU_PER_INCH


def pt_to_px(pt):
    return pt * DPI / 72.0


FONT_DIR = r"C:\Windows\Fonts"
FONT_FILES = {
    (False, False): "calibri.ttf",
    (True, False): "calibrib.ttf",
    (False, True): "calibrii.ttf",
    (True, True): "calibriz.ttf",
}
_font_cache = {}


def get_font(size_px, bold=False, italic=False):
    key = (round(size_px), bool(bold), bool(italic))
    if key not in _font_cache:
        path = os.path.join(FONT_DIR, FONT_FILES[(bool(bold), bool(italic))])
        _font_cache[key] = ImageFont.truetype(path, max(1, round(size_px)))
    return _font_cache[key]


def rgb_tuple(color):
    if color is None:
        return None
    return (color[0], color[1], color[2])


# ============================================================================
# Shim: the minimal slice of the python-pptx object model used by
# generate_presentation.py's low-level helpers (add_rect, add_text,
# add_line, add_triangle, add_oval, new_slide, set_notes). Every shim
# object records geometry/style instead of writing OOXML, so the exact
# same slide-builder functions run unmodified against either backend.
# ============================================================================

class _ColorHolder:
    def __init__(self):
        self.rgb = None


class _Fill:
    def __init__(self):
        self.kind = None  # "solid" | "none" | None (inherited/unset)
        self._fore_color = _ColorHolder()

    def solid(self):
        self.kind = "solid"

    def background(self):
        self.kind = "none"

    @property
    def fore_color(self):
        return self._fore_color


class _Line:
    def __init__(self):
        self.fill = _Fill()
        self._color = _ColorHolder()
        self.width = 0

    @property
    def color(self):
        return self._color


class _Shadow:
    def __init__(self):
        self.inherit = True


class _Font:
    def __init__(self):
        self.size = None
        self.bold = False
        self.italic = False
        self.name = None
        self._color = _ColorHolder()

    @property
    def color(self):
        return self._color


class _Run:
    def __init__(self):
        self.text = ""
        self.font = _Font()


class _Paragraph:
    def __init__(self):
        self.alignment = None
        self.line_spacing = 1.0
        self.runs = []

    def add_run(self):
        r = _Run()
        self.runs.append(r)
        return r


class _TextFrame:
    def __init__(self):
        self.word_wrap = True
        self.vertical_anchor = None
        self.margin_left = 0
        self.margin_right = 0
        self.margin_top = 0
        self.margin_bottom = 0
        self.auto_size = None
        self._paragraphs = [_Paragraph()]

    @property
    def paragraphs(self):
        return self._paragraphs

    def add_paragraph(self):
        p = _Paragraph()
        self._paragraphs.append(p)
        return p


class _Shape:
    def __init__(self, kind, left, top, width, height, shape_type=None):
        self.kind = kind  # "auto" | "text" | "line"
        self.shape_type = shape_type
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.fill = _Fill()
        self.line = _Line()
        self.rotation = 0
        self.adjustments = [0.0]
        self.text_frame = _TextFrame()
        self.shadow = _Shadow()
        self.x1 = self.y1 = self.x2 = self.y2 = None


class _Shapes:
    def __init__(self, slide):
        self._slide = slide

    def add_shape(self, shape_type, x, y, w, h):
        shp = _Shape("auto", x, y, w, h, shape_type=shape_type)
        self._slide.shape_list.append(shp)
        return shp

    def add_textbox(self, x, y, w, h):
        shp = _Shape("text", x, y, w, h)
        self._slide.shape_list.append(shp)
        return shp

    def add_connector(self, connector_type, x1, y1, x2, y2):
        left, top = min(x1, x2), min(y1, y2)
        width, height = abs(x2 - x1), abs(y2 - y1)
        shp = _Shape("line", left, top, width, height)
        shp.x1, shp.y1, shp.x2, shp.y2 = x1, y1, x2, y2
        self._slide.shape_list.append(shp)
        return shp


class _Background:
    def __init__(self):
        self.fill = _Fill()


class _NotesTextFrame:
    def __init__(self):
        self.text = ""


class _NotesSlide:
    def __init__(self):
        self.notes_text_frame = _NotesTextFrame()


class _Slide:
    def __init__(self):
        self.shape_list = []
        self.shapes = _Shapes(self)
        self.background = _Background()
        self.notes_slide = _NotesSlide()


class _Slides:
    def __init__(self, deck):
        self._deck = deck

    def add_slide(self, layout):
        s = _Slide()
        self._deck.slide_list.append(s)
        return s


class RenderPresentation:
    """Stands in for pptx.Presentation() during rasterization."""

    def __init__(self):
        self.slide_width = 0
        self.slide_height = 0
        self.slide_list = []
        self.slides = _Slides(self)
        self.slide_layouts = [None] * 7


# ============================================================================
# Rasterizer
# ============================================================================

def wrap_text(text, font, max_width, draw):
    if not text:
        return [""]
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        trial = (cur + " " + word).strip() if cur else word
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def render_text(draw, shp, x, y, w, h):
    tf = shp.text_frame
    max_w = max(1.0, w)
    entries = []  # (line_text, font, color, align, line_spacing, size_px)
    for p in tf.paragraphs:
        if not p.runs:
            continue
        text = "".join(r.text for r in p.runs)
        r0 = p.runs[0]
        size_pt = r0.font.size.pt if r0.font.size is not None else 18
        size_px = pt_to_px(size_pt)
        font = get_font(size_px, bold=bool(r0.font.bold), italic=bool(r0.font.italic))
        color = rgb_tuple(r0.font.color.rgb) or (0, 0, 0)
        align = p.alignment
        line_spacing = p.line_spacing or 1.0
        wrapped = wrap_text(text, font, max_w, draw) if tf.word_wrap else [text]
        for ln in wrapped:
            entries.append((ln, font, color, align, line_spacing, size_px))
    if not entries:
        return

    line_heights = [size_px * line_spacing * 1.22
                     for (_, _, _, _, line_spacing, size_px) in entries]
    total_h = sum(line_heights)
    anchor = tf.vertical_anchor
    if anchor == MSO_ANCHOR.MIDDLE:
        cy = y + max(0.0, (h - total_h) / 2)
    elif anchor == MSO_ANCHOR.BOTTOM:
        cy = y + max(0.0, h - total_h)
    else:
        cy = y

    for (ln, font, color, align, _ls, size_px), lh in zip(entries, line_heights):
        bbox = draw.textbbox((0, 0), ln, font=font)
        tw = bbox[2] - bbox[0]
        if align == PP_ALIGN.CENTER:
            tx = x + (w - tw) / 2
        elif align == PP_ALIGN.RIGHT:
            tx = x + (w - tw)
        else:
            tx = x
        ty = cy + (lh - size_px * 1.15) / 2
        draw.text((tx, ty), ln, font=font, fill=color)
        cy += lh


def draw_triangle(draw, x, y, w, h, rotation, color):
    """Apex-up triangle rotated clockwise by `rotation` degrees around its
    own center - matches generate_presentation.add_triangle's convention
    (90=right, 180=down, 270=left, 0=up)."""
    cx, cy = x + w / 2, y + h / 2
    pts = [(cx, y), (x, y + h), (x + w, y + h)]
    rad = math.radians(rotation)
    cos_r, sin_r = math.cos(rad), math.sin(rad)

    def rot(px, py):
        dx, dy = px - cx, py - cy
        return (cx + dx * cos_r - dy * sin_r, cy + dx * sin_r + dy * cos_r)

    draw.polygon([rot(px, py) for px, py in pts], fill=color)


def render_shape(draw, shp):
    if shp.kind == "line":
        x1, y1 = emu_to_px(shp.x1), emu_to_px(shp.y1)
        x2, y2 = emu_to_px(shp.x2), emu_to_px(shp.y2)
        color = rgb_tuple(shp.line.color.rgb) or (0, 0, 0)
        lw = max(1, round(emu_to_px(shp.line.width or 0)))
        draw.line([(x1, y1), (x2, y2)], fill=color, width=lw)
        return

    x, y = emu_to_px(shp.left), emu_to_px(shp.top)
    w, h = emu_to_px(shp.width), emu_to_px(shp.height)

    if shp.kind == "auto":
        fill = rgb_tuple(shp.fill.fore_color.rgb) if shp.fill.kind == "solid" else None
        has_line = shp.line.fill.kind != "none" and shp.line.color.rgb is not None
        outline = rgb_tuple(shp.line.color.rgb) if has_line else None
        lw = max(1, round(emu_to_px(shp.line.width or 0))) if outline else 0

        if shp.shape_type == MSO_SHAPE.OVAL:
            draw.ellipse([x, y, x + w, y + h], fill=fill, outline=outline,
                          width=lw)
        elif shp.shape_type == MSO_SHAPE.ISOSCELES_TRIANGLE:
            draw_triangle(draw, x, y, w, h, shp.rotation, fill or (0, 0, 0))
        else:
            radius = 0.0
            if shp.shape_type == MSO_SHAPE.ROUNDED_RECTANGLE and shp.adjustments:
                radius = (shp.adjustments[0] or 0.0) * min(w, h)
            if radius > 1:
                draw.rounded_rectangle([x, y, x + w, y + h], radius=radius,
                                         fill=fill, outline=outline, width=lw)
            else:
                draw.rectangle([x, y, x + w, y + h], fill=fill,
                                 outline=outline, width=lw)

    render_text(draw, shp, x, y, w, h)


def render_slide(slide, slide_w_emu, slide_h_emu):
    W = max(1, round(emu_to_px(slide_w_emu)))
    H = max(1, round(emu_to_px(slide_h_emu)))
    bg = shp_bg = None
    if slide.background.fill.kind == "solid" and slide.background.fill.fore_color.rgb:
        bg = rgb_tuple(slide.background.fill.fore_color.rgb)
    img = Image.new("RGB", (W, H), bg or (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for shp in slide.shape_list:
        render_shape(draw, shp)
    return img


# ============================================================================
# Main
# ============================================================================

def main():
    prs = RenderPresentation()
    prs.slide_width = gp.SLIDE_W
    prs.slide_height = gp.SLIDE_H
    for i, builder in enumerate(gp.SLIDE_BUILDERS, start=1):
        slide = builder(prs)
        if i != 1:
            gp.add_page_number(slide, i)

    images = [render_slide(s, prs.slide_width, prs.slide_height)
               for s in prs.slide_list]

    here = os.path.dirname(os.path.abspath(__file__))
    out_pdf = os.path.join(here, "Class_07_Operators_and_Expressions.pdf")
    images[0].save(out_pdf, save_all=True, append_images=images[1:])
    print(f"Rendered {len(images)} slides -> {out_pdf}")


if __name__ == "__main__":
    main()
