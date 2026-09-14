# -*- coding: utf-8 -*-
"""
generate_presentation.py

Generates Class_07_Operators_and_Expressions.pptx for
Bong Study Hub - Foundation Batch 2026.

Source of truth (do not redesign the lesson when editing this script):
  01_Master_Instructor_Guide/Class_07_Master_Instructor_Guide.md
  02_Student_Notes/Class_07_Student_Notes.md

This deck is a VISUAL TEACHING AID for a live instructor, not the
Student Notes placed onto slides. Slides carry diagrams, short
statements, questions, and live code the instructor points to and talks
around - never paragraphs read aloud.

Design system, component library, and file structure follow the
convention established in Classes 01-06's generate_presentation.py (same
palette, fonts, canvas, and shape-drawing primitives). Unlike every
class since 05, this one needs **no new diagram shapes** - the code
card, output/error console, side-by-side code+output comparison,
vertical flow, and word grid built up across Classes 05-06 already cover
everything an operators-and-expressions class needs (the print(name) vs.
print("name") comparison shape from Class 06, for instance, is exactly
the right shape for 2 + 3 * 4 vs. (2 + 3) * 4, and for = vs. ==).

Structure of this file:
  1. Theme configuration (colors, fonts, spacing)
  2. Low-level utility functions (shapes, text, arrows)
  3. Reusable slide-layout components (title, question, diagram, ...)
  4. Content-aware diagram builders (pipeline, vertical flow, code, ...)
  5. Slide-specific builders (slide_01 .. slide_22)
  6. Main generation function
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

# ============================================================================
# 1. THEME CONFIGURATION
# ============================================================================

# -- Colors ---------------------------------------------------------------
# Same palette as Classes 01-06, for cross-class brand consistency.
NAVY = RGBColor(0x1E, 0x3A, 0x72)
BLUE = RGBColor(0x2A, 0x5C, 0xB8)
CYAN = RGBColor(0x22, 0xC7, 0xE0)
INK = RGBColor(0x1F, 0x27, 0x33)
MUTED = RGBColor(0x64, 0x70, 0x85)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BG = RGBColor(0xF7, 0xF9, 0xFC)
CARD_BG = RGBColor(0xEE, 0xF3, 0xFB)
CARD_BORDER = RGBColor(0xC7, 0xD6, 0xEC)
CYAN_BG = RGBColor(0xE4, 0xF9, 0xFB)
CYAN_BORDER = RGBColor(0x9F, 0xE6, 0xEE)

# Carried over from Classes 05-06: an error/warning accent. Not used for
# an actual runtime error this class - kept only because the shared
# draw_output_card/draw_code_and_output helpers accept it.
ERROR_RED = RGBColor(0xB8, 0x3A, 0x3A)
ERROR_BG = RGBColor(0xFC, 0xEC, 0xEC)
ERROR_BORDER = RGBColor(0xEE, 0xB9, 0xB9)

# -- Fonts ------------------------------------------------------------------
FONT_DISPLAY = "Aptos Display"
FONT_BODY = "Aptos"
# Carried over from Class 05: a monospace face for literal Python source
# code or program output.
FONT_MONO = "Consolas"

# -- Canvas -----------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN

FOOTER_TEXT = "Bong Study Hub  ·  Foundation Batch 2026  ·  Class 07"


# ============================================================================
# 2. LOW-LEVEL UTILITIES
# ============================================================================

def new_slide(prs, bg=LIGHT_BG):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = bg
    return slide


def _i(v):
    return int(round(v))


def _no_shadow(shape):
    try:
        shape.shadow.inherit = False
    except Exception:
        pass


def add_rect(slide, x, y, w, h, fill=WHITE, line=None, line_w=Pt(1),
             radius=0.06, shadow=False):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, _i(x), _i(y), _i(w), _i(h))
    if radius:
        try:
            shp.adjustments[0] = radius
        except Exception:
            pass
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = line_w
    if not shadow:
        _no_shadow(shp)
    shp.text_frame.margin_left = 0
    shp.text_frame.margin_right = 0
    shp.text_frame.margin_top = 0
    shp.text_frame.margin_bottom = 0
    return shp


def add_oval(slide, x, y, w, h, fill=WHITE, line=None, line_w=Pt(1)):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, _i(x), _i(y), _i(w), _i(h))
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = line_w
    _no_shadow(shp)
    return shp


def add_text(slide, x, y, w, h, text, size=18, color=INK, bold=False,
             italic=False, align=PP_ALIGN.LEFT, font=FONT_BODY,
             anchor=MSO_ANCHOR.TOP, line_spacing=1.08, wrap=True,
             shrink=False):
    box = slide.shapes.add_textbox(_i(x), _i(y), _i(w), _i(h))
    tf = box.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    if shrink:
        tf.auto_size = MSO_AUTO_SIZE.NONE
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.name = font
        run.font.color.rgb = color
    return box


def add_line(slide, x1, y1, x2, y2, color=BLUE, width=Pt(1.5)):
    conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, _i(x1), _i(y1),
                                        _i(x2), _i(y2))
    conn.line.color.rgb = color
    conn.line.width = width
    _no_shadow(conn)
    return conn


def add_triangle(slide, cx, cy, size, color, rotation):
    s = _i(size)
    shp = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE,
                                  _i(cx) - s // 2, _i(cy) - s // 2, s, s)
    shp.rotation = rotation
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    _no_shadow(shp)
    return shp


def add_arrow_h(slide, x1, y, x2, color=BLUE, width=Pt(1.5)):
    tip_gap = Emu(90000)
    add_line(slide, x1, y, x2 - tip_gap, y, color=color, width=width)
    add_triangle(slide, x2 - Emu(45000), y, Emu(160000), color, rotation=90)


def add_arrow_v(slide, x, y1, y2, color=BLUE, width=Pt(1.5)):
    tip_gap = Emu(90000)
    add_line(slide, x, y1, x, y2 - tip_gap, color=color, width=width)
    add_triangle(slide, x, y2 - Emu(45000), Emu(160000), color, rotation=180)


def add_footer(slide):
    add_text(slide, MARGIN, SLIDE_H - Inches(0.42), Inches(7.5), Inches(0.3),
              FOOTER_TEXT, size=9.5, color=MUTED, font=FONT_BODY)


def add_page_number(slide, number):
    add_text(slide, SLIDE_W - Inches(1.1), SLIDE_H - Inches(0.42),
              Inches(0.5), Inches(0.3), str(number), size=9.5, color=MUTED,
              align=PP_ALIGN.RIGHT, font=FONT_BODY)


def add_kicker(slide, x, y, w, text, color=BLUE):
    add_text(slide, x, y, w, Inches(0.4), text.upper(), size=13, color=color,
              bold=True, font=FONT_BODY)


def set_notes(slide, purpose=None, say=None, question=None, expected=None,
               board=None, transition=None, timing=None, markers=None):
    lines = []
    if markers:
        lines.append("[" + "] [".join(markers) + "]")
    if timing:
        lines.append(f"TIME: {timing}")
    if purpose:
        lines.append(f"Purpose: {purpose}")
    if say:
        lines.append(f"Say: {say}")
    if question:
        lines.append(f"Ask: {question}")
    if expected:
        lines.append(f"Expected: {expected}")
    if board:
        lines.append(f"Board: {board}")
    if transition:
        lines.append(f"Transition: {transition}")
    slide.notes_slide.notes_text_frame.text = "\n".join(lines)


# ============================================================================
# 3. REUSABLE SLIDE-LAYOUT COMPONENTS
# ============================================================================

def layout_title(prs, kicker, title_lines, subtitle):
    slide = new_slide(prs, bg=NAVY)
    add_rect(slide, MARGIN, Inches(2.15), Inches(1.2), Inches(0.06), fill=CYAN)
    add_kicker(slide, MARGIN, Inches(1.75), Inches(10), kicker, color=CYAN)
    y = Inches(2.4)
    for line in title_lines:
        add_text(slide, MARGIN, y, Inches(11.5), Inches(1.1), line, size=50,
                  color=WHITE, bold=True, font=FONT_DISPLAY)
        y += Inches(1.0)
    add_text(slide, MARGIN, y + Inches(0.15), Inches(10.5), Inches(0.6),
              subtitle, size=20, color=RGBColor(0xB9, 0xCC, 0xEE),
              italic=True, font=FONT_BODY)
    add_text(slide, MARGIN, SLIDE_H - Inches(0.9), Inches(6), Inches(0.5),
              "Bong Study Hub\nFoundation Batch 2026", size=13,
              color=RGBColor(0x8F, 0xA6, 0xD1), font=FONT_BODY,
              line_spacing=1.15)
    return slide


def layout_section_divider(prs, kicker, title, subtitle=None, title_size=40):
    slide = new_slide(prs, bg=NAVY)
    add_rect(slide, MARGIN, Inches(3.05), Inches(1.0), Inches(0.06), fill=CYAN)
    if kicker:
        add_kicker(slide, MARGIN, Inches(2.65), Inches(10), kicker, color=CYAN)
    add_text(slide, MARGIN, Inches(3.25), Inches(11.8), Inches(2.4), title,
              size=title_size, color=WHITE, bold=True, font=FONT_DISPLAY,
              line_spacing=1.15)
    if subtitle:
        add_text(slide, MARGIN, Inches(5.6), Inches(10.5), Inches(0.8),
                  subtitle, size=18, color=RGBColor(0xB9, 0xCC, 0xEE),
                  font=FONT_BODY, italic=True)
    add_text(slide, MARGIN, SLIDE_H - Inches(0.42), Inches(7.5), Inches(0.3),
              FOOTER_TEXT, size=9.5, color=RGBColor(0x6B, 0x82, 0xAE))
    return slide


def _content_header(slide, kicker, title, title_size=32):
    if kicker:
        add_kicker(slide, MARGIN, Inches(0.5), CONTENT_W, kicker, color=BLUE)
        title_y = Inches(0.86)
    else:
        title_y = Inches(0.6)
    add_text(slide, MARGIN, title_y, CONTENT_W, Inches(0.9), title,
              size=title_size, color=NAVY, bold=True, font=FONT_DISPLAY)
    add_rect(slide, MARGIN, title_y + Inches(0.85), Inches(0.85),
              Inches(0.045), fill=CYAN)
    return title_y + Inches(1.15)


def layout_big_question(prs, kicker, question, note=None, size=38):
    slide = new_slide(prs, bg=LIGHT_BG)
    if kicker:
        add_kicker(slide, MARGIN, Inches(1.5), CONTENT_W, kicker, color=BLUE)
    add_text(slide, Inches(1.0), Inches(2.3), Inches(11.3), Inches(2.9),
              question, size=size, color=NAVY, bold=True, font=FONT_DISPLAY,
              align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
              line_spacing=1.15)
    if note:
        add_text(slide, Inches(1.0), Inches(5.5), Inches(11.3), Inches(0.5),
                  note, size=15, color=MUTED, align=PP_ALIGN.CENTER,
                  italic=True)
    add_footer(slide)
    return slide


def layout_two_column(prs, kicker, title, left, right, connector_label=None,
                       connector_symbol=None):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, kicker, title)
    col_w = (CONTENT_W - Inches(0.6)) / 2
    card_h = Inches(2.7)
    card_y = y + Inches(0.4)
    for i, card in enumerate((left, right)):
        x = MARGIN + i * (col_w + Inches(0.6))
        fill = CARD_BG if i == 0 else CYAN_BG
        border = CARD_BORDER if i == 0 else CYAN_BORDER
        add_rect(slide, x, card_y, col_w, card_h, fill=fill, line=border,
                  line_w=Pt(1.25), radius=0.05)
        if card.get("tag"):
            add_text(slide, x + Inches(0.35), card_y + Inches(0.3),
                      col_w - Inches(0.7), Inches(0.4), card["tag"],
                      size=13, color=(BLUE if i == 0 else NAVY), bold=True)
        add_text(slide, x + Inches(0.35), card_y + Inches(0.75),
                  col_w - Inches(0.7), Inches(0.7), card["title"],
                  size=card.get("title_size", 25), color=NAVY, bold=True,
                  font=card.get("title_font", FONT_DISPLAY))
        add_text(slide, x + Inches(0.35), card_y + Inches(1.55),
                  col_w - Inches(0.7), Inches(1.0), card["sub"], size=16,
                  color=INK, line_spacing=1.2)
    mid_y = card_y + card_h / 2
    gap_x1 = MARGIN + col_w
    gap_x2 = gap_x1 + Inches(0.6)
    if connector_symbol:
        add_text(slide, gap_x1, mid_y - Inches(0.35), gap_x2 - gap_x1,
                  Inches(0.7), connector_symbol, size=30, color=NAVY,
                  bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                  font=FONT_DISPLAY)
    else:
        add_arrow_h(slide, gap_x1 + Inches(0.08), mid_y, gap_x2 - Inches(0.08),
                    color=BLUE, width=Pt(2))
        if connector_label:
            add_text(slide, gap_x1, mid_y - Inches(0.55), Inches(0.6),
                      Inches(0.35), connector_label, size=11, color=MUTED,
                      align=PP_ALIGN.CENTER)
    add_footer(slide)
    return slide


def layout_diagram(prs, kicker, title, diagram_fn, caption=None,
                    title_size=32):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, kicker, title, title_size=title_size)
    area_y = y + Inches(0.25)
    area_h = SLIDE_H - area_y - Inches(0.75)
    if caption:
        area_h -= Inches(0.5)
    diagram_fn(slide, MARGIN, area_y, CONTENT_W, area_h)
    if caption:
        add_text(slide, MARGIN, SLIDE_H - Inches(1.05), CONTENT_W,
                  Inches(0.4), caption, size=13, color=MUTED, italic=True,
                  align=PP_ALIGN.CENTER)
    add_footer(slide)
    return slide


def layout_full_screen_visual(prs, kicker, title, diagram_fn, caption=None):
    slide = new_slide(prs, bg=LIGHT_BG)
    add_kicker(slide, MARGIN, Inches(0.45), CONTENT_W, kicker, color=BLUE)
    if title:
        add_text(slide, MARGIN, Inches(0.8), CONTENT_W, Inches(0.7), title,
                  size=26, color=NAVY, bold=True, font=FONT_DISPLAY)
    diagram_fn(slide, MARGIN, Inches(1.55), CONTENT_W,
                SLIDE_H - Inches(1.55) - Inches(1.15))
    if caption:
        add_text(slide, MARGIN, SLIDE_H - Inches(1.0), CONTENT_W, Inches(0.4),
                  caption, size=13, color=MUTED, italic=True,
                  align=PP_ALIGN.CENTER)
    add_footer(slide)
    return slide


def layout_activity(prs, kicker, title, prompt_lines, sub=None, tag="ACTIVITY"):
    slide = new_slide(prs, bg=LIGHT_BG)
    add_rect(slide, Inches(0.9), Inches(0.55), Inches(1.5), Inches(0.42),
              fill=CYAN_BG, line=CYAN_BORDER, line_w=Pt(1))
    add_text(slide, Inches(0.9), Inches(0.55), Inches(1.5), Inches(0.42),
              tag, size=13, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
              anchor=MSO_ANCHOR.MIDDLE)
    add_kicker(slide, Inches(2.6), Inches(0.62), Inches(9), kicker,
                color=BLUE)
    add_text(slide, Inches(0.9), Inches(1.25), Inches(11.5), Inches(1.0),
              title, size=30, color=NAVY, bold=True, font=FONT_DISPLAY)
    y = Inches(2.5)
    for line in prompt_lines:
        add_text(slide, Inches(0.9), y, Inches(11.5), Inches(0.85), line,
                  size=24, color=INK, font=FONT_BODY, line_spacing=1.15)
        y += Inches(0.8)
    if sub:
        add_text(slide, Inches(0.9), y + Inches(0.15), Inches(11.0),
                  Inches(0.6), sub, size=15, color=MUTED, italic=True)
    add_footer(slide)
    return slide


# ============================================================================
# 4. CONTENT-AWARE DIAGRAM BUILDERS
# ============================================================================

def draw_vertical_flow(items, highlight_indices=None, box_w=Inches(4.6),
                        font_size=16):
    highlight_indices = highlight_indices or set()

    def _fn(slide, x, y, w, h):
        n = len(items)
        box_h = min(Inches(0.75), h / (n * 1.35))
        gap = (h - n * box_h) / (n - 1) if n > 1 else Inches(0)
        gap = max(Inches(0.1), min(gap, Inches(0.5)))
        total_h = n * box_h + (n - 1) * gap
        cy = y + max(Inches(0), (h - total_h) / 2)
        bx = x + w / 2 - box_w / 2
        for i, label in enumerate(items):
            is_hl = i in highlight_indices
            fill = CYAN_BG if is_hl else CARD_BG
            border = CYAN_BORDER if is_hl else CARD_BORDER
            add_rect(slide, bx, cy, box_w, box_h, fill=fill, line=border,
                      line_w=Pt(1.4 if is_hl else 1.1), radius=0.14)
            add_text(slide, bx, cy, box_w, box_h, label, size=font_size,
                      color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
            if i < n - 1:
                add_arrow_v(slide, x + w / 2, cy + box_h + Inches(0.03),
                            cy + box_h + gap - Inches(0.03), color=BLUE,
                            width=Pt(1.75))
            cy += box_h + gap
    return _fn


def draw_pipeline(items, height=Inches(1.3), font_size=15,
                   highlight_indices=None, gap=Inches(0.55)):
    highlight_indices = highlight_indices or set()

    def _fn(slide, x, y, w, h):
        n = len(items)
        box_w = (w - gap * (n - 1)) / n
        box_y = y + (h - height) / 2
        cx = x
        for i, (label, sub) in enumerate(items):
            is_hl = i in highlight_indices
            fill = CYAN_BG if is_hl else CARD_BG
            border = CYAN_BORDER if is_hl else CARD_BORDER
            add_rect(slide, cx, box_y, box_w, height, fill=fill,
                      line=border, line_w=Pt(1.25), radius=0.09)
            label_y = box_y + (height / 2 - Inches(0.32) if sub
                                else height / 2 - Inches(0.24))
            add_text(slide, cx, label_y, box_w, Inches(0.5), label,
                      size=font_size, color=NAVY, bold=True,
                      align=PP_ALIGN.CENTER, font=FONT_BODY)
            if sub:
                add_text(slide, cx, label_y + Inches(0.42), box_w,
                          Inches(0.35), sub, size=font_size - 4, color=MUTED,
                          align=PP_ALIGN.CENTER)
            if i < n - 1:
                add_arrow_h(slide, cx + box_w + Inches(0.06), box_y + height / 2,
                            cx + box_w + gap - Inches(0.06), color=BLUE,
                            width=Pt(1.75))
            cx += box_w + gap
    return _fn


def draw_word_grid(words, cols=4, highlight_indices=None, font_size=20):
    highlight_indices = highlight_indices or set()

    def _fn(slide, x, y, w, h):
        n = len(words)
        rows = (n + cols - 1) // cols
        gap = Inches(0.3)
        cell_w = (w - gap * (cols - 1)) / cols
        cell_h = min(Inches(1.0), (h - gap * (rows - 1)) / rows) if rows else h
        grid_h = rows * cell_h + (rows - 1) * gap
        top = y + max(Inches(0), (h - grid_h) / 2)
        for i, word in enumerate(words):
            r, c = divmod(i, cols)
            last_row = (r == rows - 1)
            items_in_row = cols if (not last_row or n % cols == 0) else n % cols
            row_w = items_in_row * cell_w + (items_in_row - 1) * gap
            row_x0 = x + (w - row_w) / 2
            cx = row_x0 + c * (cell_w + gap)
            cy = top + r * (cell_h + gap)
            is_hl = i in highlight_indices
            fill = CYAN_BG if is_hl else CARD_BG
            border = CYAN_BORDER if is_hl else CARD_BORDER
            add_rect(slide, cx, cy, cell_w, cell_h, fill=fill, line=border,
                      line_w=Pt(1.25), radius=0.14)
            add_text(slide, cx, cy, cell_w, cell_h, word, size=font_size,
                      color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE, font=FONT_BODY)
    return _fn


def draw_definition(term, definition, term_size=72, def_size=28):
    def _fn(slide, x, y, w, h):
        add_text(slide, x, y, w, h * 0.42, term, size=term_size, color=NAVY,
                  bold=True, font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE)
        rule_y = y + h * 0.46
        add_rect(slide, x + w / 2 - Inches(0.5), rule_y, Inches(1.0),
                  Inches(0.04), fill=CYAN)
        add_text(slide, x, rule_y + Inches(0.25), w, h * 0.5 - Inches(0.25),
                  definition, size=def_size, color=INK, bold=True,
                  align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP,
                  line_spacing=1.2, font=FONT_BODY)
    return _fn


def draw_statement(text, size=40, color=NAVY):
    def _fn(slide, x, y, w, h):
        add_text(slide, x, y, w, h, text, size=size, color=color, bold=True,
                  font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
    return _fn


# -- Carried over from Classes 05-06: code / output shapes ------------------

def draw_code_block(lines, font_size=22):
    """A dark 'editor' card holding monospace Python source, one string per
    line. The small cyan dot in the corner reads as a window/tab marker."""
    def _fn(slide, x, y, w, h):
        n = max(1, len(lines))
        card_h = min(h, Inches(0.62) * n + Inches(0.55))
        top = y + max(Inches(0), (h - card_h) / 2)
        add_rect(slide, x, top, w, card_h, fill=NAVY, radius=0.06)
        add_oval(slide, x + Inches(0.32), top + Inches(0.28), Inches(0.14),
                  Inches(0.14), fill=CYAN, line=None)
        line_h = (card_h - Inches(0.55)) / n
        ty = top + Inches(0.48)
        for i, line in enumerate(lines):
            add_text(slide, x + Inches(0.62), ty + i * line_h,
                      w - Inches(0.95), line_h, line, size=font_size,
                      color=WHITE, font=FONT_MONO, anchor=MSO_ANCHOR.MIDDLE)
    return _fn


def draw_output_card(lines, is_error=False, font_size=20, label=None):
    """A light 'console' card for program output, or an error-tinted card
    when is_error is True (unused this class, kept for shape parity)."""
    def _fn(slide, x, y, w, h):
        fill = ERROR_BG if is_error else CARD_BG
        border = ERROR_BORDER if is_error else CARD_BORDER
        bar = ERROR_RED if is_error else CYAN
        text_color = ERROR_RED if is_error else INK
        add_rect(slide, x, y, w, h, fill=fill, line=border, line_w=Pt(1.25),
                  radius=0.05)
        add_rect(slide, x, y, Inches(0.09), h, fill=bar, radius=None)
        lab = label or ("ERROR" if is_error else "OUTPUT")
        add_text(slide, x + Inches(0.35), y + Inches(0.16),
                  w - Inches(0.6), Inches(0.32), lab, size=12.5,
                  color=(ERROR_RED if is_error else MUTED), bold=True)
        n = max(1, len(lines))
        body_y = y + Inches(0.55)
        body_h = h - Inches(0.7)
        add_text(slide, x + Inches(0.35), body_y, w - Inches(0.6), body_h,
                  "\n".join(lines), size=font_size, color=text_color,
                  font=FONT_MONO, anchor=MSO_ANCHOR.TOP, line_spacing=1.3)
    return _fn


def draw_code_and_output(code_lines, output_lines, is_error=False,
                          code_font=22, output_font=18, output_label=None):
    """Editor card on top, console result beneath it."""
    def _fn(slide, x, y, w, h):
        gap = Inches(0.35)
        code_h = h * 0.54
        out_h = h - code_h - gap
        draw_code_block(code_lines, font_size=code_font)(slide, x, y, w, code_h)
        draw_output_card(output_lines, is_error=is_error,
                          font_size=output_font, label=output_label)(
            slide, x, y + code_h + gap, w, out_h)
    return _fn


def draw_two_code_examples(left, right, font_size=17, output_font=15):
    """Two side-by-side code+output panels - the exact shape used in Class
    06 for print(name) vs. print("name"), reused here for 2+3*4 vs.
    (2+3)*4 (Section 13) and = vs. == (Section 16)."""
    def _fn(slide, x, y, w, h):
        gap = Inches(0.55)
        col_w = (w - gap) / 2
        for i, spec in enumerate((left, right)):
            cx = x + i * (col_w + gap)
            draw_code_and_output(
                spec["code"], spec["output"], is_error=spec.get("is_error", False),
                code_font=font_size, output_font=output_font,
                output_label=spec.get("label"))(slide, cx, y, col_w, h)
    return _fn


# ============================================================================
# 5. SLIDE-SPECIFIC BUILDERS
# ============================================================================

def slide_01_title(prs):
    slide = layout_title(
        prs, "Bong Study Hub · Foundation Batch 2026 · Class 07",
        ["Operators &", "Expressions"],
        "Class 01's LOGIC, Made Literal")
    set_notes(slide, timing="2 min",
              purpose="Set tone; do not read the slide aloud.",
              say="Open with the live 'add these two prices' "
                  "demonstration (Guide §8) before this slide is even "
                  "shown, if possible.",
              transition="Now that we can store values, how do we "
                          "actually compute, compare, and combine "
                          "them?")
    return slide


def slide_02_big_question(prs):
    slide = layout_big_question(
        prs, "The Big Question",
        "Now that we can store values,\nhow do we actually compute,\n"
        "compare, and combine them?", size=32)
    set_notes(slide, markers=["ASK", "PAUSE", "DO NOT ANSWER YET"],
              timing="(closes Guide §8)",
              purpose="Land the central question right after the live "
                      "'can't add two prices yet' demonstration.",
              board="None.",
              transition="Let's go back to exactly where Class 06 left "
                          "off — and to something even older.")
    return slide


def slide_03_callback(prs):
    slide = layout_two_column(
        prs, "Two Boxes Reopened", "Reopening Two Boxes",
        {"tag": "CLASS 06 LEFT OPEN", "title": "No Way to Compute",
         "sub": "We can print numbers, but we haven't done any math "
                "with them, or compared two values."},
        {"tag": "CLASS 01 REOPENED", "title": "LOGIC",
         "sub": "“Reasoning about how to solve a problem” — "
                "never once shown as real code, since Week 1."},
        connector_symbol="+")
    set_notes(slide, markers=["ASK"], timing="5 min (Guide §9)",
              purpose="Reopen Class 06's unresolved hook and Class 01's "
                      "LOGIC box together - both get answered today.",
              question="What did Class 06 leave unanswered? What did "
                        "Class 01's LOGIC box actually mean, "
                        "concretely?",
              expected="How to compute/compare values. Most will admit "
                        "it was always a bit abstract.",
              board="None.",
              transition="Let's name the toolkit that does both.")
    return slide


def slide_04_what_is_an_operator(prs):
    slide = layout_diagram(
        prs, "Naming the Toolkit", "What Is an Operator?",
        draw_definition("OPERATOR", "A SYMBOL THAT ACTS ON VALUES\n\n"
                          "VARIABLES ARE THE NOUNS —\nOPERATORS ARE THE "
                          "VERBS", term_size=64, def_size=24))
    set_notes(slide, timing="5 min (Guide §10)",
              purpose="Name the toolkit and the word 'operand' before "
                      "meeting any specific operator.",
              say="Today we'll meet three families: arithmetic "
                  "(math), comparison (true/false questions), and "
                  "logical (combining true/false answers).",
              question="What is an operator, in your own words?",
              expected="A symbol that acts on values to produce a new "
                        "one.",
              board="None.",
              transition="Let's start with the family you already know "
                          "from math class.")
    return slide


def slide_05_arithmetic_basics(prs):
    slide = layout_diagram(
        prs, "Computing a New Value", "Arithmetic: The Basics",
        draw_code_and_output(
            ["price1 = 50", "price2 = 30", "total = price1 + price2",
             "print(total)"],
            ["80"], code_font=19, output_font=24))
    set_notes(slide, markers=["LIVE"], timing="4 min (part of Guide "
              "§11) — NON-NEGOTIABLE",
              purpose="A variable can now hold the RESULT of a "
                      "computation, not just something typed in "
                      "directly - this is genuinely new.",
              say="+ computed a brand-new value from two variables, "
                  "and we stored that new value in total.",
              board="Live screen.",
              transition="Three more arithmetic operators work exactly "
                          "the way you'd expect from math class.")
    return slide


def slide_06_arithmetic_rest(prs):
    slide = layout_diagram(
        prs, "The Rest of the Family", "Subtraction, Multiplication, Division",
        draw_code_and_output(
            ["print(10 - 3)", "print(4 * 5)", "print(9 / 2)"],
            ["7", "20", "4.5"], code_font=20, output_font=20,
            output_label="OUTPUT — notice / always gives a float"))
    set_notes(slide, markers=["TYPE-ALONG"], timing="4 min (closes "
              "Guide §11) — NON-NEGOTIABLE",
              purpose="Predict each result before running. Land the "
                      "precision point: / always gives a float, even "
                      "10 / 2.",
              question="What data type does / always produce?",
              expected="A float.",
              board="Live screen.",
              transition="Two more arithmetic operators exist, and they "
                          "behave a little differently from what you're "
                          "used to.")
    return slide


def slide_07_floor_mod(prs):
    slide = layout_diagram(
        prs, "Two Special Operators", "// and %",
        draw_code_and_output(
            ["print(9 // 2)", "print(9 % 2)"], ["4", "1"],
            code_font=24, output_font=26))
    set_notes(slide, timing="7 min (Guide §12) — NON-NEGOTIABLE",
              purpose="// floors division to a whole number; % gives "
                      "the remainder. Both behave differently from / "
                      "and *.",
              say="number % 2 == 0 is exactly how programs check "
                  "whether a number is even - we're not writing that "
                  "check today, that's Class 08, but now you know "
                  "where the tool comes from.",
              question="What does // do? What does % give you?",
              expected="Keeps only the whole-number part. The "
                        "remainder.",
              board="Live screen.",
              transition="What happens when an expression uses more "
                          "than one operator at once?")
    return slide


def slide_08_order_question(prs):
    slide = layout_big_question(
        prs, "Predict Before You Reveal",
        "Is  2 + 3 * 4  equal to\n20, or 14?", size=36)
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(opens Guide "
              "§13)",
              purpose="Let guesses happen before revealing - many will "
                      "guess 20 (adding first).",
              board="None.",
              transition="Let's actually run it and see.")
    return slide


def slide_09_order_reveal(prs):
    slide = layout_diagram(
        prs, "Order of Operations", "Multiplication Before Addition",
        draw_two_code_examples(
            {"code": ["print(2 + 3 * 4)"], "output": ["14"],
             "label": "NO PARENTHESES"},
            {"code": ["print((2 + 3) * 4)"], "output": ["20"],
             "label": "PARENTHESES FORCE ORDER"},
        ))
    set_notes(slide, timing="(closes Guide §13)",
              purpose="Python follows the same order of operations as "
                      "math class - multiplication/division before "
                      "addition/subtraction, unless parentheses say "
                      "otherwise.",
              say="When in doubt, use parentheses to make your intent "
                  "explicit, even where they aren't strictly required.",
              board="Live screen.",
              transition="Let's name what all of these lines actually "
                          "are.")
    return slide


def slide_10_expressions(prs):
    slide = layout_diagram(
        prs, "Naming It", "Expressions",
        draw_statement("AN EXPRESSION IS ANY\nPIECE OF CODE THAT\n"
                        "PRODUCES A VALUE", size=34))
    set_notes(slide, timing="6 min (Guide §14)",
              purpose="Name what's been happening all along - price1 + "
                      "price2, 9 // 2, and (2+3)*4 are all expressions.",
              say="subtotal = price1 + price2, then tax = subtotal * "
                  "0.1, then total = subtotal + tax - each line's "
                  "expression can use the result of a previous line.",
              question="What is an expression, in your own words?",
              expected="Any piece of code that produces a value.",
              board="Live screen.",
              transition="So far every expression has produced a "
                          "number. Let's meet a family whose "
                          "expressions always produce a boolean.")
    return slide


def slide_11_comparison_operators(prs):
    slide = layout_diagram(
        prs, "Asking True/False Questions", "Comparison Operators",
        draw_code_and_output(
            ["age = 18", "print(age == 18)", "print(age > 21)",
             "print(age != 20)"],
            ["True", "False", "True"], code_font=17, output_font=19))
    set_notes(slide, markers=["LIVE", "ASK"], timing="8 min (Guide "
              "§15) — NON-NEGOTIABLE",
              purpose="Every comparison produces a boolean - exactly "
                      "the data type from Class 06.",
              say="== equal to, != not equal to, < less than, > "
                  "greater than, <= less than or equal to, >= greater "
                  "than or equal to.",
              question="What data type does every comparison produce?",
              expected="A boolean.",
              board="Live screen.",
              transition="Look very closely at the first line I typed "
                          "— count the equals signs.")
    return slide


def slide_12_equals_trap(prs):
    slide = layout_diagram(
        prs, "The Most Important Contrast Today", "=  vs.  ==",
        draw_two_code_examples(
            {"code": ["age = 18", "print(age)"], "output": ["18"],
             "label": "ONE = STORES A VALUE"},
            {"code": ["age = 18", "print(age == 18)"], "output": ["True"],
             "label": "TWO == ASKS A QUESTION"},
        ))
    set_notes(slide, markers=["TYPE-ALONG", "ASK"], timing="6 min "
              "(Guide §16) — NON-NEGOTIABLE",
              purpose="The single most important guardrail in the "
                      "class - they look almost identical and mean "
                      "completely different things.",
              say="This mix-up is so common that even experienced "
                  "programmers still catch themselves doing it.",
              question="Do = and == ever mean the same thing?",
              expected="No — never.",
              board="Live screen.",
              transition="Sometimes one true/false question isn't "
                          "enough.")
    return slide


def slide_13_logical_operators(prs):
    slide = layout_diagram(
        prs, "Combining True/False Answers", "and, or, not",
        draw_code_and_output(
            ["age = 16", "print(age >= 13 and age <= 19)",
             "print(age < 13 or age > 19)", "print(not (age == 16))"],
            ["True", "False", "False"], code_font=14.5, output_font=17))
    set_notes(slide, markers=["TYPE-ALONG"], timing="9 min (Guide "
              "§17) — NON-NEGOTIABLE",
              purpose="and gives True only if both sides are true; or "
                      "gives True if at least one side is true; not "
                      "flips a boolean.",
              question="When does and give True? When does or give "
                        "True?",
              expected="Only when both sides are true. When at least "
                        "one side is true.",
              board="Live screen.",
              transition="Let's build something that actually feels "
                          "like a real rule.")
    return slide


def slide_14_combining(prs):
    slide = layout_diagram(
        prs, "A Real-Feeling Rule", "Combining Comparisons and Logic",
        draw_code_and_output(
            ["is_weekend = True", "is_raining = False",
             "print(is_weekend and not is_raining)"],
            ["True"], code_font=19, output_font=22,
            output_label='OUTPUT — "is it the weekend AND NOT raining?"'))
    set_notes(slide, timing="7 min (Guide §18)",
              purpose="This reads almost like English - a real rule a "
                      "real program might check, built from nothing but "
                      "variables and operators from the last two "
                      "classes.",
              question="Using age, write a condition for 'is a "
                        "teenager' — 13 through 19, inclusive.",
              expected="age >= 13 and age <= 19",
              board="Live screen.",
              transition="Let's connect this whole idea to something "
                          "from Week 1.")
    return slide


def slide_15_class01_callback(prs):
    slide = layout_diagram(
        prs, "Reconnecting to Week 1", "LOGIC, Made Literal",
        draw_vertical_flow(
            ["LOGIC  (Class 01 — reasoning about a problem)",
             "OPERATORS & EXPRESSIONS  (today — that reasoning, in code)"],
            highlight_indices={1}, box_w=Inches(8.2), font_size=17))
    set_notes(slide, timing="6 min (Guide §19)",
              purpose="Every time you've ever reasoned 'this AND that "
                      "must both be true,' you were doing exactly what "
                      "today's operators do.",
              question="What did Class 01's LOGIC box actually mean? "
                        "What does today's class turn that reasoning "
                        "into?",
              expected="Reasoning about how to solve a problem. Real "
                        "code — operators and expressions.",
              board="None.",
              transition="Let's put the entire day's reasoning on one "
                          "board — starting all the way back at Class "
                          "01.")
    return slide


def slide_16_full_bridge(prs):
    items = ["PROBLEM", "LOGIC", "ALGORITHM", "PYTHON CODE", "VARIABLES",
             "EXPRESSIONS", "RUN", "OUTPUT / RESULT"]
    slide = layout_full_screen_visual(
        prs, "The Hero Diagram", None,
        draw_vertical_flow(items, highlight_indices={5}, box_w=Inches(5.0),
                            font_size=15.5),
        caption="Cyan = new today  ·  Card = already known — and LOGIC "
                "finally connects all the way down to EXPRESSIONS")
    set_notes(slide, markers=["LIVE"], timing="7 min (Guide §20) — "
              "NON-NEGOTIABLE, HERO MOMENT",
              purpose="Build this top to bottom, one line at a time - "
                      "never reveal it finished. EXPRESSIONS isn't just "
                      "new, it's the literal, coded-up version of "
                      "LOGIC at the very top.",
              board="Whiteboard - the one non-screen drawing before the "
                    "activity.",
              transition="Time to try this yourselves.")
    return slide


def slide_17_activity_intro(prs):
    slide = layout_activity(
        prs, "Try It Yourself", "Level Up Your Profile Card",
        ["Add one arithmetic expression,", "one comparison, and one "
         "logical expression", "to your Class 06 Profile Card."],
        sub="Predict each result before you run it.")
    set_notes(slide, markers=["ACTIVITY"], timing="15 min (Guide §21) "
              "— NON-NEGOTIABLE, HERO ACTIVITY",
              purpose="Every student extends their own Class 06 "
                      "program with real computation for the first "
                      "time. Circulate constantly.",
              say="Stuck? What's a number you could multiply or divide "
                  "from your card? What's a true/false question about "
                  "your own age or height?",
              board="Circulate and read screens rather than calling on "
                    "students verbally.",
              transition="Here's a template if you want a starting "
                          "point.")
    return slide


def slide_18_activity_template(prs):
    slide = layout_diagram(
        prs, "A Starting Point (Optional)", "Level Up — Template",
        draw_code_block(
            ["age_in_months = age * 12", "is_adult = age >= 18",
             "is_teenager = age >= 13 and age <= 19", "",
             "print(age_in_months)", "print(is_adult)",
             "print(is_teenager)"],
            font_size=16.5))
    set_notes(slide, timing="(support for Guide §21)",
              purpose="A worked template for students who want a "
                      "starting point - not the only correct answer, "
                      "and not required.",
              board="None.",
              transition="Let a few students share one new line and "
                          "its result with the room.")
    return slide


def slide_19_activity_question(prs):
    slide = layout_big_question(
        prs, "Reflect",
        "If you wrote = when you\nmeant ==, would Python\nnecessarily "
        "tell you?", size=32,
        note="Often not — that's exactly why this mix-up is so risky.")
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(closes Guide "
              "§21)",
              purpose="Re-confirm Section 16's lesson using the "
                      "student's own program as the example.",
              board="None.",
              transition="Let's check a couple of misconceptions "
                          "before we close.")
    return slide


def slide_20_recap(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Quick Recap", "Quick Recap")
    draw_word_grid(["OPERATOR", "EXPRESSION", "// AND %", "COMPARISON",
                     "= VS ==", "AND / OR / NOT"], cols=6, font_size=12)(
        slide, MARGIN, y + Inches(0.1), CONTENT_W, Inches(1.1))
    draw_pipeline(
        [("PROBLEM", None), ("LOGIC", None), ("ALGORITHM", None),
         ("PYTHON\nCODE", None), ("VARIABLES", None), ("EXPRESSIONS", None),
         ("RUN", None), ("OUTPUT/\nRESULT", None)],
        height=Inches(1.15), font_size=9.5, gap=Inches(0.2))(
        slide, MARGIN, y + Inches(1.7), CONTENT_W, Inches(1.4))
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="4 min (Guide §23) — "
              "NON-NEGOTIABLE",
              purpose="One visual summary of every keyword and the "
                      "full bridged chain.",
              question="What's the difference between / and //? What "
                        "does % give you? What data type does a "
                        "comparison produce? What's the difference "
                        "between = and ==? When does and give True?",
              board="None.",
              transition="One question to leave you with.")
    return slide


def slide_21_bridge_forward(prs):
    slide = layout_big_question(
        prs, "A Question for Next Time",
        "Every comparison and logical result\njust gets printed right "
        "now — it doesn't\nchange what the program does next.\nWhat if "
        "it needed to?", size=27)
    set_notes(slide, markers=["DO NOT ANSWER"], timing="(Guide §24)",
              purpose="Leave this open as a deliberate hook into Class "
                      "08 (Making Decisions: if/elif/else).",
              board="None.",
              transition="Class ends on the final takeaway.")
    return slide


def slide_22_final_takeaway(prs):
    slide = layout_section_divider(
        prs, "Final Takeaway",
        "“For six classes, LOGIC was just\na word on a board. Today, "
        "it has a\nshape: operators that compute, compare,\nand "
        "combine. Every rule you will ever\nteach a computer to "
        "follow starts\nwith exactly these tools.”",
        title_size=25)
    set_notes(slide, timing="1 min",
              purpose="Close the class on this exact line, said slowly.",
              board="None.",
              transition="Class ends.")
    return slide


# ============================================================================
# 6. MAIN GENERATION FUNCTION
# ============================================================================

SLIDE_BUILDERS = [
    slide_01_title, slide_02_big_question, slide_03_callback,
    slide_04_what_is_an_operator, slide_05_arithmetic_basics,
    slide_06_arithmetic_rest, slide_07_floor_mod, slide_08_order_question,
    slide_09_order_reveal, slide_10_expressions,
    slide_11_comparison_operators, slide_12_equals_trap,
    slide_13_logical_operators, slide_14_combining,
    slide_15_class01_callback, slide_16_full_bridge,
    slide_17_activity_intro, slide_18_activity_template,
    slide_19_activity_question, slide_20_recap, slide_21_bridge_forward,
    slide_22_final_takeaway,
]


def build_presentation(output_path):
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    for i, builder in enumerate(SLIDE_BUILDERS, start=1):
        slide = builder(prs)
        if i != 1:
            add_page_number(slide, i)
    prs.save(output_path)
    return len(SLIDE_BUILDERS)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "Class_07_Operators_and_Expressions.pptx")
    n = build_presentation(out)
    print(f"Generated {n} slides -> {out}")
