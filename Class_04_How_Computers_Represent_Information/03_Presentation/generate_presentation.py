# -*- coding: utf-8 -*-
"""
generate_presentation.py

Generates Class_04_How_Computers_Represent_Information.pptx for
Bong Study Hub - Foundation Batch 2026.

Source of truth (do not redesign the lesson when editing this script):
  01_Master_Instructor_Guide/Class_04_Master_Instructor_Guide.md
  02_Student_Notes/Class_04_Student_Notes.md

This deck is a VISUAL TEACHING AID for a live instructor, not the
Student Notes placed onto slides. Slides carry diagrams, short
statements, and questions the instructor points to and talks around -
never paragraphs read aloud.

Design system, component library, and file structure follow the
convention established in Class 01's and Class 03's
generate_presentation.py (same palette, fonts, canvas, and
shape-drawing primitives), reusing Class 03's diagram-builder toolkit
directly wherever the shape fits, and adding only the few new diagram
shapes Class 04 actually needs (a continuous-range-vs-two-states
contrast, and a stacked "growth pattern" list).

Structure of this file:
  1. Theme configuration (colors, fonts, spacing)
  2. Low-level utility functions (shapes, text, arrows)
  3. Reusable slide-layout components (title, question, diagram, ...)
  4. Content-aware diagram builders (pipeline, table, word grid, ...)
  5. Slide-specific builders (slide_01 .. slide_25)
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
# Same palette as Classes 01-03, for cross-class brand consistency.
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

# -- Fonts ------------------------------------------------------------------
FONT_DISPLAY = "Aptos Display"
FONT_BODY = "Aptos"

# -- Canvas -----------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN

FOOTER_TEXT = "Bong Study Hub  ·  Foundation Batch 2026  ·  Class 04"


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
                  col_w - Inches(0.7), Inches(0.7), card["title"], size=25,
                  color=NAVY, bold=True, font=FONT_DISPLAY)
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


def layout_recap(prs, kicker, title, items, numbered=False):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, kicker, title)
    yy = y + Inches(0.3)
    row_h = (SLIDE_H - Inches(0.9) - yy) / len(items)
    row_h = min(row_h, Inches(0.9))
    for i, item in enumerate(items):
        if numbered:
            add_rect(slide, MARGIN, yy + Inches(0.03), Inches(0.4),
                      Inches(0.4), fill=NAVY, radius=0.5)
            add_text(slide, MARGIN, yy + Inches(0.03), Inches(0.4),
                      Inches(0.4), str(i + 1), size=15, color=WHITE,
                      bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
            text_x = MARGIN + Inches(0.58)
        else:
            add_rect(slide, MARGIN, yy + Inches(0.16), Inches(0.14),
                      Inches(0.14), fill=CYAN, radius=0.5)
            text_x = MARGIN + Inches(0.4)
        add_text(slide, text_x, yy, CONTENT_W - Inches(0.6), row_h, item,
                  size=20, color=INK, anchor=MSO_ANCHOR.MIDDLE,
                  line_spacing=1.1)
        yy += row_h
    add_footer(slide)
    return slide


# ============================================================================
# 4. CONTENT-AWARE DIAGRAM BUILDERS
# ============================================================================

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


def draw_table(headers, rows, highlight_cols=None, font_size=18):
    highlight_cols = highlight_cols or set()

    def _fn(slide, x, y, w, h):
        ncols = len(headers)
        nrows = len(rows)
        row_h = min(Inches(0.85), h / (nrows + 1))
        total_h = row_h * (nrows + 1)
        top = y + max(Inches(0), (h - total_h) / 2)
        col_w = w / ncols
        for c, htext in enumerate(headers):
            cx = x + c * col_w
            add_rect(slide, cx + Inches(0.03), top + Inches(0.03),
                      col_w - Inches(0.06), row_h - Inches(0.06), fill=NAVY,
                      radius=0.08)
            add_text(slide, cx, top, col_w, row_h, htext, size=font_size,
                      color=WHITE, bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
        for r, row in enumerate(rows):
            ry = top + (r + 1) * row_h
            for c, val in enumerate(row):
                cx = x + c * col_w
                is_hl = c in highlight_cols
                fill = CYAN_BG if is_hl else (WHITE if r % 2 == 0 else CARD_BG)
                border = CYAN_BORDER if is_hl else CARD_BORDER
                add_rect(slide, cx + Inches(0.03), ry + Inches(0.03),
                          col_w - Inches(0.06), row_h - Inches(0.06),
                          fill=fill, line=border, line_w=Pt(1), radius=0.06)
                add_text(slide, cx, ry, col_w, row_h, str(val),
                          size=font_size, color=INK, align=PP_ALIGN.CENTER,
                          anchor=MSO_ANCHOR.MIDDLE)
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


def draw_three_words_cards(cards):
    def _fn(slide, x, y, w, h):
        gap = Inches(0.4)
        n = len(cards)
        card_w = (w - gap * (n - 1)) / n
        card_h = min(Inches(2.3), h)
        top = y + max(Inches(0), (h - card_h) / 2)
        for i, card in enumerate(cards):
            cx = x + i * (card_w + gap)
            add_rect(slide, cx, top, card_w, card_h, fill=WHITE,
                      line=CARD_BORDER, line_w=Pt(1), radius=0.07)
            add_rect(slide, cx, top, card_w, Inches(0.09), fill=CYAN, radius=None)
            add_text(slide, cx + Inches(0.25), top + Inches(0.35),
                      card_w - Inches(0.5), Inches(0.6), card["title"],
                      size=21, color=NAVY, bold=True, font=FONT_DISPLAY,
                      align=PP_ALIGN.CENTER)
            add_text(slide, cx + Inches(0.25), top + Inches(1.1),
                      card_w - Inches(0.5), card_h - Inches(1.35), card["sub"],
                      size=17, color=INK, line_spacing=1.25,
                      align=PP_ALIGN.CENTER)
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


def draw_two_row_pipelines(rows_spec):
    def _fn(slide, x, y, w, h):
        label_w = Inches(1.9)
        chain_x = x + label_w
        chain_w = w - label_w
        n_rows = len(rows_spec)
        row_h = min(Inches(1.0), h / (n_rows * 1.6))
        gap = (h - n_rows * row_h) / (n_rows - 1) if n_rows > 1 else Inches(0)
        gap = max(Inches(0.25), min(gap, Inches(0.7)))
        total_h = n_rows * row_h + (n_rows - 1) * gap
        cy = y + max(Inches(0), (h - total_h) / 2)
        for row_label, items, hl in rows_spec:
            hl = hl or set()
            add_text(slide, x, cy, label_w - Inches(0.2), row_h, row_label,
                      size=15, color=NAVY, bold=True,
                      anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
            n = len(items)
            box_gap = Inches(0.3)
            box_w = (chain_w - box_gap * (n - 1)) / n
            cx = chain_x
            for i, label in enumerate(items):
                is_hl = i in hl
                fill = CYAN_BG if is_hl else CARD_BG
                border = CYAN_BORDER if is_hl else CARD_BORDER
                add_rect(slide, cx, cy, box_w, row_h, fill=fill, line=border,
                          line_w=Pt(1), radius=0.12)
                add_text(slide, cx, cy, box_w, row_h, label, size=13.5,
                          color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                          anchor=MSO_ANCHOR.MIDDLE)
                if i < n - 1:
                    add_arrow_h(slide, cx + box_w + Inches(0.04), cy + row_h / 2,
                                cx + box_w + box_gap - Inches(0.04),
                                color=BLUE, width=Pt(1.4))
                cx += box_w + box_gap
            cy += row_h + gap
    return _fn


def draw_continuous_vs_discrete():
    """Slide 7's visual contrast: a smooth continuous range (a gradient-
    like bar with a sliding marker) vs. two clear, separate states
    (a hollow circle and a filled circle)."""
    def _fn(slide, x, y, w, h):
        col_w = (w - Inches(0.8)) / 2
        left_x = x
        right_x = x + col_w + Inches(0.8)
        cy = y + h / 2

        add_text(slide, left_x, y, col_w, Inches(0.5), "CONTINUOUS RANGE",
                  size=16, color=MUTED, bold=True, align=PP_ALIGN.CENTER)
        bar_y = cy - Inches(0.06)
        add_rect(slide, left_x + Inches(0.4), bar_y, col_w - Inches(0.8),
                  Inches(0.12), fill=CARD_BG, line=CARD_BORDER,
                  line_w=Pt(1), radius=0.5)
        marker_x = left_x + col_w * 0.42
        add_oval(slide, marker_x, cy - Inches(0.14), Inches(0.28),
                  Inches(0.28), fill=MUTED, line=None)
        add_text(slide, left_x, cy + Inches(0.35), col_w, Inches(0.4),
                  "could be anywhere along here", size=12, color=MUTED,
                  italic=True, align=PP_ALIGN.CENTER)

        add_text(slide, right_x, y, col_w, Inches(0.5), "TWO CLEAR STATES",
                  size=16, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
        dot_size = Inches(0.55)
        gap = Inches(0.6)
        total_w = dot_size * 2 + gap
        dx = right_x + (col_w - total_w) / 2
        add_oval(slide, dx, cy - dot_size / 2, dot_size, dot_size,
                  fill=WHITE, line=NAVY, line_w=Pt(2.5))
        add_oval(slide, dx + dot_size + gap, cy - dot_size / 2, dot_size,
                  dot_size, fill=NAVY, line=NAVY, line_w=Pt(2.5))
        add_text(slide, right_x, cy + Inches(0.35), col_w, Inches(0.4),
                  "always clearly one or the other", size=12, color=MUTED,
                  italic=True, align=PP_ALIGN.CENTER)

        mid_x = left_x + col_w + Inches(0.4)
        add_text(slide, mid_x - Inches(0.3), cy - Inches(0.3), Inches(0.6),
                  Inches(0.6), "vs.", size=18, color=MUTED, italic=True,
                  align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return _fn


def draw_growth_rows(rows):
    """rows: list of (label, value) - e.g. ("1 BIT", "2 COMBINATIONS").
    Stacked, large, center-aligned - the doubling pattern, felt rather
    than calculated."""
    def _fn(slide, x, y, w, h):
        n = len(rows)
        row_h = h / n
        for i, (label, value) in enumerate(rows):
            ry = y + i * row_h
            is_last = (i == n - 1)
            color = CYAN if is_last else BLUE
            size = 30 + i * 4
            add_text(slide, x, ry, w, row_h,
                      f"{label}  →  {value}", size=size, color=NAVY,
                      bold=True, font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
            if not is_last:
                add_rect(slide, x + w / 2 - Inches(0.35),
                          ry + row_h - Inches(0.02), Inches(0.7),
                          Inches(0.025), fill=CARD_BORDER)
    return _fn


# ============================================================================
# 5. SLIDE-SPECIFIC BUILDERS
# ============================================================================

def slide_01_title(prs):
    slide = layout_title(
        prs, "Bong Study Hub · Foundation Batch 2026 · Class 04",
        ["How Computers", "Represent Information"],
        "From Information → Bits → Binary")
    set_notes(slide, timing="2 min",
              purpose="Set tone; do not read the slide aloud.",
              say="Briefly connect back to Class 03 in one sentence before "
                  "starting.",
              transition="If computers work with information like text, "
                          "images, and sound, how do they actually "
                          "represent that information?")
    return slide


def slide_02_big_question(prs):
    slide = layout_big_question(
        prs, "The Big Question",
        "If computers work with information\nlike text, images, and "
        "sound, how do\nthey actually represent that information?",
        size=32)
    set_notes(slide, markers=["ASK", "PAUSE", "DO NOT ANSWER YET"],
              timing="2 min (Guide §8)",
              purpose="Open the central question of the whole class - do "
                      "not resolve it here.",
              board="None.",
              transition="Let's back up to exactly where we left off "
                          "last class.")
    return slide


def slide_03_look_back(prs):
    slide = layout_diagram(
        prs, "Look Back — Class 03", "What Happens Next?",
        draw_vertical_flow(["REAL WORLD", "OBSERVATION", "DATA"],
                            box_w=Inches(5.2), font_size=22))
    set_notes(slide, markers=["ASK"], timing="6 min (Guide §9)",
              purpose="Re-anchor Class 03's chain before extending it - "
                      "create continuity, not a new lecture.",
              question="What is data, from last class? Did we ever ask "
                        "how that information sits inside a computer?",
              expected="\"Recorded information about something.\" Most "
                        "will realize we never asked the second question.",
              board="None.",
              transition="That's exactly today's question.")
    return slide


def slide_04_data_needs_representation(prs):
    slide = layout_diagram(
        prs, "The Next Step", "Data Needs a Representation",
        draw_vertical_flow(["DATA", "REPRESENTATION"], box_w=Inches(5.2),
                            font_size=22),
        caption="Before a computer can store or process information, it "
                "needs a form of that information it can work with.")
    set_notes(slide, markers=["ASK"], timing="9 min (Guide §10)",
              purpose="Establish that a computer can't 'just understand' "
                      "a real-world thing.",
              question="Can a computer just 'look at' a photograph the "
                        "way you do? What does it need instead?",
              expected="No; some kind of stored representation.",
              board="None.",
              transition="How can one machine represent so many "
                          "different kinds of things?")
    return slide


def slide_05_many_kinds(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "The Puzzle", "Many Kinds of Information")
    words = ["NUMBER", "TEXT", "IMAGE", "SOUND", "VIDEO"]
    draw_word_grid(words, cols=5, font_size=19)(slide, MARGIN, y + Inches(0.15),
                                                  CONTENT_W, Inches(1.2))
    add_text(slide, MARGIN, y + Inches(1.9), CONTENT_W, Inches(1.0),
              "How can the same kind of computer\nwork with all of these?",
              size=28, color=NAVY, bold=True, font=FONT_DISPLAY,
              align=PP_ALIGN.CENTER, line_spacing=1.15)
    add_footer(slide)
    set_notes(slide, markers=["ASK", "DO NOT ANSWER YET"],
              timing="(part of Guide §10)",
              purpose="Bank the big puzzle the class will spend the rest "
                      "of the day resolving.",
              board="None.",
              transition="Let's not start with computers at all. Let's "
                          "start with a light switch.")
    return slide


def slide_06_two_states(prs):
    cards = [
        {"title": "LIGHT", "sub": "OFF   |   ON"},
        {"title": "DOOR", "sub": "CLOSED   |   OPEN"},
        {"title": "QUESTION", "sub": "NO   |   YES"},
    ]
    slide = layout_diagram(
        prs, "Everyday Examples", "A Simple Idea: Two States",
        draw_three_words_cards(cards))
    set_notes(slide, markers=["ASK"], timing="8 min (Guide §11)",
              purpose="Ground 'digital' in familiar two-state systems "
                      "before naming anything technical.",
              question="How many states does a light switch have? Name "
                        "another everyday two-state system.",
              expected="Two; yes/no, open/closed, heads/tails.",
              board="Drawing #1 — a two-state switch (OFF ↔ ON).",
              transition="Computers are built from exactly this idea.")
    return slide


def slide_07_digital(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Naming the Idea", "Digital")
    add_text(slide, MARGIN, y, CONTENT_W, Inches(0.6),
              "Information represented using distinct, clearly "
              "distinguishable states.", size=20, color=INK,
              align=PP_ALIGN.CENTER)
    draw_continuous_vs_discrete()(slide, MARGIN, y + Inches(0.85), CONTENT_W,
                                    Inches(2.6))
    add_footer(slide)
    set_notes(slide, timing="6 min (part of Guide §11)",
              purpose="Name 'digital' only after the two-state intuition "
                      "is built. No electronics or signal-processing "
                      "detail.",
              say="This doesn't mean everything in reality is naturally "
                  "two-state — a dimmer switch isn't. Computers *build* "
                  "complex representations out of many simple, reliable "
                  "two-state pieces.",
              board="None.",
              transition="There's a name for one of these two-state "
                          "units inside a computer.")
    return slide


def slide_08_bit(prs):
    slide = layout_diagram(
        prs, "The Key Building Block", "Bit",
        draw_definition("BIT", "BINARY DIGIT\n\nONE OF TWO POSSIBLE STATES",
                          term_size=76, def_size=26))
    set_notes(slide, timing="6 min (Guide §12) — NON-NEGOTIABLE",
              purpose="Name the building block clearly, only after the "
                      "intuition is built. A bit is not a special kind "
                      "of number.",
              say="0 and 1 are just the conventional symbols for the two "
                  "states — we could just as easily call them off/on.",
              board="Drawing #2 — one bit: 0 | 1.",
              transition="But why two states, instead of ten like our "
                          "normal counting system?")
    return slide


def slide_09_one_bit(prs):
    slide = layout_diagram(
        prs, "Starting Small", "One Bit",
        draw_definition("ONE BIT", "0   |   1\n\ntwo possible states",
                          term_size=56, def_size=26))
    set_notes(slide, markers=["ASK"], timing="5 min (Guide §14) — "
              "NON-NEGOTIABLE",
              purpose="One bit gives exactly two possibilities - land "
                      "this before adding a second bit.",
              question="If we only have one switch, how many different "
                        "messages can we send with it?",
              expected="Two.",
              board="Reuse Drawing #2.",
              transition="What if we only have one switch — how many "
                          "different messages can we send?")
    return slide


def slide_10_one_switch_question(prs):
    slide = layout_big_question(
        prs, "Think About It",
        "If one switch has two states,\nhow many different messages\ncan "
        "it represent?", size=32,
        note="A real yes/no answer only needs two options, too.")
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(bridges Guide "
              "§14 → §15)",
              purpose="Let the limitation of one bit be felt before "
                      "adding a second.",
              board="None.",
              transition="Let's try adding a second switch and see what "
                          "happens.")
    return slide


def slide_11_two_bits(prs):
    slide = layout_diagram(
        prs, "Building Live", "Two Bits",
        draw_word_grid(["00", "01", "10", "11"], cols=4, font_size=30),
        caption="Four possible combinations — not two more, but double "
                "the one-bit case.")
    set_notes(slide, markers=["LIVE", "ASK"], timing="7 min (Guide §15) "
              "— NON-NEGOTIABLE",
              purpose="Build the four combinations live, one at a time - "
                      "let students call them out rather than revealing "
                      "the finished list.",
              question="List every possible combination of two bits. "
                        "How many did we find?",
              expected="00, 01, 10, 11 — four.",
              board="Drawing #3 — two bits: 00/01/10/11.",
              transition="Notice — we didn't just add two more options, "
                          "we doubled them. What happens with a third "
                          "bit?")
    return slide


def slide_12_growth_pattern(prs):
    rows = [("1 BIT", "2"), ("2 BITS", "4"), ("3 BITS", "8")]
    slide = layout_diagram(
        prs, "Predict Before You Reveal", "Binary Combinations",
        draw_growth_rows(rows),
        caption="Each extra bit roughly doubles the number of possible "
                "combinations.")
    set_notes(slide, markers=["ASK", "PREDICT"], timing="8 min "
              "(Guide §16) — NON-NEGOTIABLE",
              purpose="Install the doubling pattern intuitively - do NOT "
                      "drill this as a formula or write 2ⁿ on the board.",
              question="If two bits give four combinations, how many do "
                        "you think three bits will give?",
              expected="Eight — reveal by building the list, or by "
                        "extending the visual pattern.",
              board="Drawing #4 — 1→2, 2→4, 3→8.",
              transition="More bits give more combinations. But "
                          "combinations of what? '01' doesn't mean "
                          "anything on its own yet.")
    return slide


def slide_13_representation_system(prs):
    slide = layout_diagram(
        prs, "The Core Reframe", "Binary Is a Representation System",
        draw_statement("A BIT PATTERN IS NOT\n\"THE THING ITSELF.\"\nIT "
                        "REPRESENTS INFORMATION.", size=34))
    set_notes(slide, timing="7 min (Guide §17) — NON-NEGOTIABLE",
              purpose="Land the class's central reframe before surveying "
                      "what bits can represent.",
              board="None.",
              transition="Remember Class 03's canteen example?")
    return slide


def slide_14_class03_callback(prs):
    slide = layout_two_column(
        prs, "Same Idea, Class 03", "Representation, Not the Real Thing",
        {"tag": "CLASS 03", "title": "“80% Full”",
         "sub": "Represents a crowded canteen — it is not the canteen "
                "itself."},
        {"tag": "CLASS 04", "title": "A Bit Pattern",
         "sub": "Represents information for a computer — it is not the "
                "information itself."},
        connector_symbol="≈")
    set_notes(slide, timing="(part of Guide §17)",
              purpose="Explicit callback — one of the strongest "
                      "connective threads in the class.",
              say="The canteen being crowded is a real, physical fact. "
                  "'80% full' is just our recorded representation of "
                  "that fact. Binary works exactly the same way.",
              board="None.",
              transition="So bits represent things. But what kinds of "
                          "things — just numbers?")
    return slide


def slide_15_full_circle(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Closing the Puzzle",
                          "Same Building Block, Every Time")
    words = ["NUMBER", "TEXT", "IMAGE", "SOUND", "VIDEO"]
    draw_word_grid(words, cols=5, font_size=18)(slide, MARGIN, y + Inches(0.1),
                                                  CONTENT_W, Inches(1.1))
    add_arrow_v(slide, SLIDE_W / 2, y + Inches(1.35), y + Inches(1.85),
                color=BLUE, width=Pt(2))
    add_rect(slide, SLIDE_W / 2 - Inches(1.6), y + Inches(1.95),
              Inches(3.2), Inches(0.95), fill=CYAN_BG, line=CYAN_BORDER,
              line_w=Pt(1.5), radius=0.14)
    add_text(slide, SLIDE_W / 2 - Inches(1.6), y + Inches(1.95),
              Inches(3.2), Inches(0.95), "BITS", size=36, color=NAVY,
              bold=True, font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
              anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, MARGIN, y + Inches(3.15), CONTENT_W, Inches(0.6),
              "Very different information — the same underlying building "
              "block.", size=15, color=MUTED, italic=True,
              align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="8 min (Guide §18) — "
              "NON-NEGOTIABLE",
              purpose="Survey the breadth of what bits can represent — "
                      "no encoding mechanisms.",
              question="Could a number be represented with bits? A "
                        "letter or word? A photograph?",
              expected="Yes to all — the photograph stays a little "
                        "mysterious, and that's fine.",
              board="Drawing #6 — many information types → bits.",
              transition="If the same bit pattern could theoretically be "
                          "a number or a letter, how do we know which it "
                          "actually is?")
    return slide


def slide_16_photograph_question(prs):
    slide = layout_big_question(
        prs, "Still a Little Mysterious",
        "How could millions of tiny\nbinary decisions possibly\ndescribe "
        "an image?", size=32)
    set_notes(slide, markers=["ASK", "LET IT STAY UNRESOLVED"],
              timing="(part of Guide §18)",
              purpose="A curiosity-generating question — it's fine to "
                      "leave this a little unresolved on purpose.",
              board="None.",
              transition="Does a sequence of bits carry its meaning by "
                          "itself?")
    return slide


def slide_17_same_bits_interpretation(prs):
    slide = layout_two_column(
        prs, "One More Idea", "Same Marks, Different Meaning",
        {"tag": "CONTEXT A", "title": "“S O S”",
         "sub": "→ a distress signal"},
        {"tag": "CONTEXT B", "title": "“S O S”",
         "sub": "→ just someone's initials"},
        connector_symbol="=")
    set_notes(slide, markers=["ASK"], timing="7 min (Guide §19)",
              purpose="Meaning requires an agreed interpretation — the "
                      "marks themselves didn't change.",
              question="What matters more — the bits themselves, or how "
                        "we interpret them?",
              expected="Both matter, but interpretation is what turns a "
                        "pattern into meaning.",
              board="None.",
              transition="Let's put the entire day's reasoning on one "
                          "board.")
    return slide


def slide_18_meaning_statement(prs):
    slide = layout_diagram(
        prs, "Say It Plainly", "Where Meaning Comes From",
        draw_statement("MEANING COMES FROM\nINTERPRETATION —\nNOT FROM "
                        "THE BITS THEMSELVES.", size=32))
    set_notes(slide, timing="(closes Guide §19)",
              purpose="One clean, quotable statement to close the "
                      "interpretation discussion.",
              board="None.",
              transition="Let's put the entire day's reasoning on one "
                          "board — starting all the way back at Class "
                          "03.")
    return slide


def slide_19_full_bridge(prs):
    items = ["REAL WORLD", "OBSERVATION", "DATA", "REPRESENTATION", "BITS",
             "COMPUTER PROCESSING"]
    slide = layout_full_screen_visual(
        prs, "The Hero Diagram", None,
        draw_vertical_flow(items, highlight_indices={3, 4, 5},
                            box_w=Inches(5.2), font_size=18),
        caption="Cyan = new today  ·  Card = already known from Class 03")
    set_notes(slide, markers=["LIVE"], timing="6 min (Guide §20) — "
              "NON-NEGOTIABLE, HERO MOMENT",
              purpose="Build this top to bottom, one line at a time - "
                      "never reveal it finished. The top three lines are "
                      "exactly Class 03's chain; today extended it.",
              board="Drawing #5 — the full bridge, built live.",
              transition="Time to try this yourselves.")
    return slide


def slide_20_activity_intro(prs):
    slide = layout_activity(
        prs, "Try It Yourself", "Design a Tiny Binary Communication System",
        ["You have 2 bits — four combinations:", "00   01   10   11"],
        sub="Invent a meaning for each one.")
    set_notes(slide, markers=["ACTIVITY"], timing="10 min (Guide §21) "
              "— NON-NEGOTIABLE, HERO ACTIVITY",
              purpose="Let students invent meaning themselves, then "
                      "realize the meaning came from them, not the "
                      "bits.",
              say="If a group is stuck, offer a theme: four colors, four "
                  "moods, a tiny traffic-light-style signal.",
              board="Record 2–3 different student inventions side by "
                    "side.",
              transition="Here's one possible invention.")
    return slide


def slide_21_activity_example(prs):
    slide = layout_diagram(
        prs, "One Possible Invention", "Example: A Tiny Color Code",
        draw_table(["Bits", "Meaning"],
                    [["00", "Red"], ["01", "Green"], ["10", "Blue"],
                     ["11", "Yellow"]], font_size=22))
    set_notes(slide, timing="(part of Guide §21)",
              purpose="A worked example for groups that are stuck — not "
                      "the only correct answer.",
              board="None.",
              transition="Now the key question.")
    return slide


def slide_22_activity_question(prs):
    slide = layout_big_question(
        prs, "The Key Question",
        "Did the bits themselves\ncontain the meaning?", size=36)
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(closes Guide "
              "§21)",
              purpose="Land the realization the whole activity was "
                      "built for.",
              expected="No — the meaning came from the system each "
                        "student agreed on.",
              board="None.",
              transition="Let's check a few misconceptions before we "
                          "close.")
    return slide


def slide_23_recap(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Quick Recap", "Quick Recap")
    draw_word_grid(["INFORMATION", "REPRESENTATION", "BIT", "BINARY",
                     "INTERPRETATION"], cols=5, font_size=14)(
        slide, MARGIN, y + Inches(0.1), CONTENT_W, Inches(1.15))
    draw_pipeline(
        [("REAL WORLD", None), ("OBSERVATION", None), ("DATA", None),
         ("REPRESENTATION", None), ("BITS", None),
         ("COMPUTER\nPROCESSING", None)],
        height=Inches(1.15), font_size=11.5, gap=Inches(0.28))(
        slide, MARGIN, y + Inches(1.75), CONTENT_W, Inches(1.4))
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="4 min (Guide §23) — "
              "NON-NEGOTIABLE",
              purpose="One visual summary of every keyword and the full "
                      "chain.",
              question="Why does a computer need a representation? What "
                        "is a bit? How many combinations do 2 bits give? "
                        "3 bits?",
              board="None.",
              transition="One question to leave you with.")
    return slide


def slide_24_bridge_forward(prs):
    slide = layout_big_question(
        prs, "A Question for Next Time",
        "If the same building blocks can\nrepresent numbers, text, "
        "images,\nand sound — what determines\nwhat those bits actually "
        "mean?", size=28)
    set_notes(slide, markers=["DO NOT ANSWER"], timing="(Guide §24)",
              purpose="Leave this open as a deliberate hook into a "
                      "future class.",
              board="None.",
              transition="Class ends on the final takeaway.")
    return slide


def slide_25_final_takeaway(prs):
    slide = layout_section_divider(
        prs, "Final Takeaway",
        "“Computers do not need a different\nkind of machine for "
        "every kind of\ninformation. They can build many kinds\nof "
        "digital information from the same\nbasic building block: "
        "bits.”",
        title_size=30)
    set_notes(slide, timing="1 min",
              purpose="Close the class on this exact line, said slowly.",
              board="None.",
              transition="Class ends.")
    return slide


# ============================================================================
# 6. MAIN GENERATION FUNCTION
# ============================================================================

SLIDE_BUILDERS = [
    slide_01_title, slide_02_big_question, slide_03_look_back,
    slide_04_data_needs_representation, slide_05_many_kinds,
    slide_06_two_states, slide_07_digital, slide_08_bit, slide_09_one_bit,
    slide_10_one_switch_question, slide_11_two_bits,
    slide_12_growth_pattern, slide_13_representation_system,
    slide_14_class03_callback, slide_15_full_circle,
    slide_16_photograph_question, slide_17_same_bits_interpretation,
    slide_18_meaning_statement, slide_19_full_bridge,
    slide_20_activity_intro, slide_21_activity_example,
    slide_22_activity_question, slide_23_recap, slide_24_bridge_forward,
    slide_25_final_takeaway,
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
    out = os.path.join(here, "Class_04_How_Computers_Represent_Information.pptx")
    n = build_presentation(out)
    print(f"Generated {n} slides -> {out}")
