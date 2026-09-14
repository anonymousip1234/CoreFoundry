# -*- coding: utf-8 -*-
"""
generate_presentation.py

Generates Class_05_Your_First_Python_Program.pptx for
Bong Study Hub - Foundation Batch 2026.

Source of truth (do not redesign the lesson when editing this script):
  01_Master_Instructor_Guide/Class_05_Master_Instructor_Guide.md
  02_Student_Notes/Class_05_Student_Notes.md

This deck is a VISUAL TEACHING AID for a live instructor, not the
Student Notes placed onto slides. Slides carry diagrams, short
statements, questions, and live code the instructor points to and talks
around - never paragraphs read aloud.

Design system, component library, and file structure follow the
convention established in Classes 01-04's generate_presentation.py (same
palette, fonts, canvas, and shape-drawing primitives), reusing that
diagram-builder toolkit directly wherever the shape fits (pipelines,
vertical flows, word grids, definitions, statements), and adding only
the few new diagram shapes Class 05 actually needs: a monospace "code
editor" card, an "output" / "error" console card, a combined
code-and-result view, and a two-panel editor/output orientation diagram.
Class 05 is the first class where students watch and write real code, so
these new shapes carry more of the deck than usual.

Structure of this file:
  1. Theme configuration (colors, fonts, spacing)
  2. Low-level utility functions (shapes, text, arrows)
  3. Reusable slide-layout components (title, question, diagram, ...)
  4. Content-aware diagram builders (pipeline, vertical flow, code, ...)
  5. Slide-specific builders (slide_01 .. slide_23)
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
# Same palette as Classes 01-04, for cross-class brand consistency.
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

# New for Class 05: an error/warning accent, used only by the error
# console card - the one genuinely new visual idea this class needs
# (a Python program that fails on purpose, read calmly).
ERROR_RED = RGBColor(0xB8, 0x3A, 0x3A)
ERROR_BG = RGBColor(0xFC, 0xEC, 0xEC)
ERROR_BORDER = RGBColor(0xEE, 0xB9, 0xB9)

# -- Fonts ------------------------------------------------------------------
FONT_DISPLAY = "Aptos Display"
FONT_BODY = "Aptos"
# New for Class 05: a monospace face for anything that is literal Python
# source code or program output, so code visually reads as code.
FONT_MONO = "Consolas"

# -- Canvas -----------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN

FOOTER_TEXT = "Bong Study Hub  ·  Foundation Batch 2026  ·  Class 05"


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


# -- New for Class 05: code / editor / output shapes -----------------------

def draw_code_block(lines, font_size=22):
    """A dark 'editor' card holding monospace Python source, one string per
    line. The small cyan dot in the corner reads as a window/tab marker -
    just enough chrome to signal 'this is an editor', nothing literal."""
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
    """A light 'console' card for program output - or, if is_error, an
    error-tinted card for a Python error message. A thin left bar and a
    small label (OUTPUT / ERROR) mirror the callout treatment used for
    quotes and definitions elsewhere in this design system."""
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
    """The core Class 05 shape: an editor card on top, its console result
    (or error) beneath it - literally the 'two areas' from Section 12 of
    the Master Guide, reused for every live-coding slide after it."""
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
    """Two side-by-side code+output (or code+error) panels - used for
    comparing two small programs at once (e.g. two different errors)."""
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


def draw_editor_output_orientation():
    """Setup slide: a labeled editor panel above a labeled output panel,
    with a small worked example already sitting in each - the 60-second
    orientation from Section 12 of the Master Guide, before any code is
    written live."""
    def _fn(slide, x, y, w, h):
        gap = Inches(0.4)
        top_h = h * 0.56
        bot_h = h - top_h - gap
        add_rect(slide, x, y, w, top_h, fill=NAVY, radius=0.06)
        add_oval(slide, x + Inches(0.35), y + Inches(0.3), Inches(0.15),
                  Inches(0.15), fill=CYAN, line=None)
        add_text(slide, x + Inches(0.65), y + Inches(0.24), w - Inches(1.0),
                  Inches(0.4), "EDITOR — you type here", size=17, color=CYAN,
                  bold=True, font=FONT_BODY)
        add_text(slide, x + Inches(0.65), y + Inches(0.85), w - Inches(1.0),
                  top_h - Inches(1.05), 'print("Hello, World!")',
                  size=24, color=WHITE, font=FONT_MONO)
        out_y = y + top_h + gap
        add_rect(slide, x, out_y, w, bot_h, fill=CARD_BG, line=CARD_BORDER,
                  line_w=Pt(1.25), radius=0.06)
        add_text(slide, x + Inches(0.35), out_y + Inches(0.2),
                  w - Inches(0.7), Inches(0.35), "OUTPUT — you see results here",
                  size=15, color=MUTED, bold=True)
        add_text(slide, x + Inches(0.35), out_y + Inches(0.75),
                  w - Inches(0.7), bot_h - Inches(0.95), "Hello, World!",
                  size=22, color=NAVY, font=FONT_MONO)
    return _fn


# ============================================================================
# 5. SLIDE-SPECIFIC BUILDERS
# ============================================================================

def slide_01_title(prs):
    slide = layout_title(
        prs, "Bong Study Hub · Foundation Batch 2026 · Class 05",
        ["Your First", "Python Program"],
        "From English Instructions → Python Code")
    set_notes(slide, timing="2 min",
              purpose="Set tone; do not read the slide aloud.",
              say="Open with the 'follow this instruction literally' bit "
                  "(Guide §8) before this slide is even shown, if possible.",
              transition="If a computer only does exactly what it's told, "
                          "how do we tell it something it can actually "
                          "follow?")
    return slide


def slide_02_big_question(prs):
    slide = layout_big_question(
        prs, "The Big Question",
        "If a computer only does exactly\nwhat it's told, how do we tell "
        "it\nsomething it can actually follow?",
        size=32)
    set_notes(slide, markers=["ASK", "PAUSE", "DO NOT ANSWER YET"],
              timing="(closes Guide §8)",
              purpose="Land the central question of the whole class right "
                      "after the opening 'stand up' demonstration.",
              board="None.",
              transition="Let's back up to something we drew in Class 01 "
                          "and never actually opened.")
    return slide


def slide_03_look_back(prs):
    slide = layout_diagram(
        prs, "Look Back — Class 01", "One Box We Never Opened",
        draw_vertical_flow(
            ["PROBLEM", "LOGIC", "ALGORITHM", "PROGRAM  (never opened)",
             "RESULT"], highlight_indices={3}, box_w=Inches(5.6),
            font_size=17),
        caption="Four classes. Never once did we write a real program.")
    set_notes(slide, markers=["ASK"], timing="5 min (Guide §9)",
              purpose="Re-open Class 01's chain and point directly at the "
                      "box that's never been written for real.",
              question="Have we ever written an actual program in this "
                        "course? What's the difference between an "
                        "algorithm and a program?",
              expected="No. An algorithm is steps a person can follow; a "
                        "program is those steps precise enough for a "
                        "computer to follow.",
              board="None.",
              transition="If a computer only does exactly what it's told, "
                          "what would a language built for it need to be "
                          "like?")
    return slide


def slide_04_programming_language(prs):
    slide = layout_diagram(
        prs, "Naming the Idea", "What Is a Programming Language?",
        draw_statement("A LANGUAGE WITH STRICT,\nPRECISE RULES —\nZERO "
                        "GUESSING ALLOWED.", size=34))
    set_notes(slide, timing="6 min (Guide §10)",
              purpose="Land the core idea before naming Python - "
                      "precision, not English, is the point.",
              say="It's still a real language humans read and write - "
                  "just far less forgiving about exactly how you write "
                  "it than English is.",
              board="None.",
              transition="Here's the same instruction, in English and in "
                          "Python.")
    return slide


def slide_05_english_vs_python(prs):
    slide = layout_two_column(
        prs, "Same Idea, Two Languages", "Precision, Side by Side",
        {"tag": "IN ENGLISH", "title": "“Go on, print Hello World "
         "for me.”", "title_size": 21,
         "sub": "A person fills in every gap automatically - which "
                "words, what tone, even whether you're serious."},
        {"tag": "IN PYTHON", "title": 'print("Hello, World!")',
         "title_size": 22, "title_font": FONT_MONO,
         "sub": "One exact form. Nothing left for the computer to "
                "guess."},
        connector_symbol="=")
    set_notes(slide, timing="(part of Guide §10)",
              purpose="A concrete, memorable contrast before Python is "
                      "formally named.",
              board="None.",
              transition="There are many programming languages. Today "
                          "we're using Python.")
    return slide


def slide_06_meet_python(prs):
    slide = layout_diagram(
        prs, "The Tool We're Using", "Meet Python",
        draw_definition("PYTHON", "A PROGRAMMING LANGUAGE,\nDESIGNED TO "
                          "BE READABLE\n\nONE OF MANY — NOT “THE” "
                          "PROGRAMMING LANGUAGE", term_size=68, def_size=22))
    set_notes(slide, timing="5 min (Guide §11)",
              purpose="Name the tool briefly and reassuringly - not a "
                      "history lecture.",
              say="Python isn't the only programming language - it's one "
                  "of many. We're starting here because it gets out of "
                  "the way and lets the underlying ideas show through.",
              board="None.",
              transition="Let's open it up and see where we'll actually "
                          "be typing.")
    return slide


def slide_07_setup(prs):
    slide = layout_diagram(
        prs, "Orientation", "Where Code Runs",
        draw_editor_output_orientation(),
        caption="Editor: where you type. Output: where you see what "
                "happened. That's the whole mental model for today.")
    set_notes(slide, timing="4 min (Guide §12)",
              purpose="A 60-second orientation, not an install session - "
                      "software should already be open from before class.",
              question="Which area is where you type? Which shows what "
                        "happened?",
              expected="Editor (top); output (bottom/console).",
              board="Live screen - point at the real editor and output "
                    "areas as you talk, not just this slide.",
              transition="Let's write the very first line of code any of "
                          "you will ever run.")
    return slide


def slide_08_first_line(prs):
    slide = layout_diagram(
        prs, "Type It Yourself", "Your First Line",
        draw_code_block(['print("Hello, World!")'], font_size=30),
        caption="Type this exact line yourself before we run it. What do "
                "you think will happen?")
    set_notes(slide, markers=["TYPE-ALONG", "ASK"], timing="8 min "
              "(Guide §13) — NON-NEGOTIABLE",
              purpose="Every student types this exact line themselves - "
                      "the single most important 60 seconds of the "
                      "class. Walk the room.",
              say="print tells Python 'display something.' The "
                  "parentheses hold what to display. The quotes mark it "
                  "as text - we'll come back to why in a few minutes.",
              question="Before I run this - what do you think will "
                        "happen?",
              expected="It will show 'Hello, World!'",
              board="Live screen - type it slowly, narrating every "
                    "character.",
              transition="Let's actually run it and see.")
    return slide


def slide_09_running_output(prs):
    slide = layout_diagram(
        prs, "Press Run", "Running the Program",
        draw_code_and_output(['print("Hello, World!")'], ["Hello, World!"],
                              code_font=26, output_font=22))
    set_notes(slide, markers=["LIVE"], timing="7 min (Guide §14) — "
              "NON-NEGOTIABLE",
              purpose="Output appears because of code the student "
                      "personally wrote and ran - land this explicitly.",
              say="Remember INPUT → PROCESS → OUTPUT from Class 01? You "
                  "just watched it happen for real. Now personalize it: "
                  "print(\"Hello, my name is ___!\") with your own name, "
                  "and run it again.",
              question="What just happened when you pressed run?",
              expected="The computer carried out the instruction and "
                        "displayed the text.",
              board="Live screen.",
              transition="Let's go back to those quotes - what happens "
                          "if we leave them out?")
    return slide


def slide_10_broken_quotes(prs):
    slide = layout_diagram(
        prs, "Break It On Purpose", "Strings Need Quotes",
        draw_code_and_output(["print(Hello, World!)"],
                              ["NameError: name 'Hello' is not defined"],
                              is_error=True, code_font=24, output_font=17))
    set_notes(slide, markers=["LIVE", "BREAK ON PURPOSE"], timing="6 min "
              "(Guide §15)",
              purpose="Show the quotes matter by removing them, live, and "
                      "watching it break.",
              say="Without quotes, Python doesn't know 'Hello, World!' is "
                  "just text - it tries to treat those words as more "
                  "instructions and gets confused. Single and double "
                  "quotes both work - just match what you open with what "
                  "you close with.",
              question="Why did removing the quotes cause a problem?",
              expected="Python no longer knows that text is literal text, "
                        "not code.",
              board="Live screen.",
              transition="One instruction is great. Real programs have "
                          "many. Let's add more lines.")
    return slide


def slide_11_multiple_lines(prs):
    slide = layout_diagram(
        prs, "Building Live", "Multiple Instructions, In Order",
        draw_code_and_output(
            ['print("Hello, my name is Priya.")',
             'print("I am learning Python.")',
             'print("This is my very first program!")'],
            ["Hello, my name is Priya.", "I am learning Python.",
             "This is my very first program!"],
            code_font=17, output_font=16))
    set_notes(slide, markers=["LIVE", "ASK"], timing="7 min (Guide §16) "
              "— NON-NEGOTIABLE",
              purpose="Build this live, one line at a time - predict the "
                      "order before running.",
              say="This is exactly what 'algorithm' meant in Class 01 - "
                  "a sequence of steps, followed in order. Python runs "
                  "top to bottom, exactly as written.",
              question="Before I run this - in what order do you think "
                        "these three lines will appear?",
              expected="Top to bottom, in the order they're written.",
              board="Live screen.",
              transition="What do you think would happen if I swapped "
                          "lines 1 and 3?")
    return slide


def slide_12_order_question(prs):
    slide = layout_big_question(
        prs, "Predict Before You Run",
        "What happens to the output\nif I swap lines 1 and 3?", size=34,
        note="Try it live if time allows - the output order swaps too.")
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(bridges Guide "
              "§16 → §17)",
              purpose="One more prediction rep before moving on to "
                      "comments.",
              expected="The output order swaps to match the new code "
                        "order.",
              board="None.",
              transition="Sometimes you want to leave yourself a note in "
                          "the code that Python should completely "
                          "ignore.")
    return slide


def slide_13_comments(prs):
    slide = layout_diagram(
        prs, "Notes for Humans", "Comments",
        draw_code_and_output(
            ["# This program introduces me",
             'print("Hello, my name is Priya.")   # prints my name',
             'print("I am learning Python.")'],
            ["Hello, my name is Priya.", "I am learning Python."],
            code_font=15, output_font=17,
            output_label="OUTPUT — unchanged by the comments"))
    set_notes(slide, markers=["LIVE"], timing="7 min (Guide §17) — "
              "NON-NEGOTIABLE",
              purpose="Prove comments produce nothing by running code "
                      "with and without them and comparing output.",
              say="Anything after a # on a line is a comment - Python "
                  "skips it completely. It's not an instruction. It's a "
                  "note for whoever reads the code next - a teammate, or "
                  "you, months from now.",
              question="Why might a programmer want notes the computer "
                        "completely ignores?",
              expected="To explain what the code does, for teammates or "
                        "future-you.",
              board="Live screen.",
              transition="Let's deliberately break something else - your "
                          "first error should happen on purpose, in a "
                          "safe moment.")
    return slide


def slide_14_errors_two_examples(prs):
    slide = layout_diagram(
        prs, "Read It Calmly", "When Syntax Breaks: Two Errors",
        draw_two_code_examples(
            {"code": ['print("Hello, World!)'],
             "output": ["SyntaxError: unterminated", "string literal"],
             "is_error": True, "label": "MISSING QUOTE"},
            {"code": ['Print("Hello, World!")'],
             "output": ["NameError: name 'Print'", "is not defined"],
             "is_error": True, "label": "WRONG CAPITALIZATION"},
        ))
    set_notes(slide, markers=["LIVE", "BREAK ON PURPOSE"], timing="8 min "
              "(Guide §18) — NON-NEGOTIABLE",
              purpose="Show two small, clear errors on purpose, before "
                      "any student hits one by accident.",
              say="Read each one out loud, slowly. It's not yelling at "
                  "you - it's telling you exactly what rule got broken. "
                  "Python is case-sensitive: print and Print are "
                  "completely different words to it.",
              question="Does an error mean you broke the computer? "
                        "What's the fastest way to start understanding "
                        "one?",
              expected="No, it's normal feedback. Read the last line "
                        "first - it usually names the actual problem.",
              board="Live screen.",
              transition="Every programmer has seen hundreds of these.")
    return slide


def slide_15_errors_are_normal(prs):
    slide = layout_diagram(
        prs, "Say It Plainly", "Errors Are Normal",
        draw_statement("AN ERROR IS NOT\nA JUDGMENT ON YOU.\nIT'S PYTHON "
                        "TELLING YOU\nEXACTLY WHERE IT GOT CONFUSED.",
                        size=28))
    set_notes(slide, timing="(closes Guide §18)",
              purpose="One clean, quotable statement to close the "
                      "errors discussion and defuse anxiety before the "
                      "hands-on activity.",
              board="None.",
              transition="Notice what you just did without even "
                          "thinking about it - that cycle has a name.")
    return slide


def slide_16_write_run_read_fix(prs):
    slide = layout_diagram(
        prs, "Name the Pattern", "The Write–Run–Read–Fix Loop",
        draw_pipeline(
            [("WRITE", None), ("RUN", None), ("READ", None), ("FIX", None)],
            height=Inches(1.5), font_size=22, gap=Inches(0.5)),
        caption="...then run again. Nobody writes a perfect program on "
                "the first try - this loop is the normal way it works.")
    set_notes(slide, timing="7 min (Guide §19)",
              purpose="Name a pattern students have already lived "
                      "through four or five times in the last 30 "
                      "minutes.",
              question="What are the steps of this loop, in your own "
                        "words? Is needing to fix something a sign you "
                        "did it wrong?",
              expected="Write, run, read the result, fix if needed, run "
                        "again. No - it's the normal, expected cycle.",
              board="None.",
              transition="Let's put the whole day on one chain - "
                          "starting all the way back at Class 01.")
    return slide


def slide_17_full_bridge(prs):
    items = ["PROBLEM", "LOGIC", "ALGORITHM", "PYTHON CODE", "RUN",
             "OUTPUT / RESULT"]
    slide = layout_full_screen_visual(
        prs, "The Hero Diagram", None,
        draw_vertical_flow(items, highlight_indices={3, 4, 5},
                            box_w=Inches(5.2), font_size=18),
        caption="Cyan = new today  ·  Card = already known from Class 01")
    set_notes(slide, markers=["LIVE"], timing="7 min (Guide §20) — "
              "NON-NEGOTIABLE, HERO MOMENT",
              purpose="Build this top to bottom, one line at a time - "
                      "never reveal it finished. The top three lines are "
                      "exactly Class 01's chain; today opened PROGRAM "
                      "into something real.",
              board="Whiteboard - the one non-screen drawing before the "
                    "activity.",
              transition="Time to try this yourselves.")
    return slide


def slide_18_activity_intro(prs):
    slide = layout_activity(
        prs, "Try It Yourself", "My First Program: About Me",
        ["At least three print() lines.", "At least one comment (#)."],
        sub="Write it, run it, then break it on purpose - remove a "
            "quote, or misspell print - and read the error together.")
    set_notes(slide, markers=["ACTIVITY"], timing="18 min (Guide §21) "
              "— NON-NEGOTIABLE, HERO ACTIVITY",
              purpose="Every student writes and runs an original, "
                      "multi-line program - no copying the class example "
                      "verbatim. Circulate constantly.",
              say="Stuck? What are three true things about you a "
                  "stranger couldn't guess?",
              board="Circulate and read screens rather than calling on "
                    "students verbally.",
              transition="Here's a template if you want a starting "
                          "point.")
    return slide


def slide_19_activity_template(prs):
    slide = layout_diagram(
        prs, "A Starting Point (Optional)", "About Me — Template",
        draw_code_block(
            ["# About Me",
             'print("Hello, my name is ___.")',
             'print("I am learning Python for the first time.")',
             'print("My favorite ___ is ___.")'],
            font_size=19))
    set_notes(slide, timing="(support for Guide §21)",
              purpose="A worked template for students who want a "
                      "starting point - not the only correct answer, and "
                      "not required.",
              board="None.",
              transition="Let a few students run their program for the "
                          "room.")
    return slide


def slide_20_activity_question(prs):
    slide = layout_big_question(
        prs, "Reflect",
        "Did the computer do anything\nyou didn't tell it to?", size=36)
    set_notes(slide, markers=["ASK", "PAUSE"], timing="(closes Guide "
              "§21)",
              purpose="Land the realization the activity was built for - "
                      "the computer only ever does exactly what's "
                      "written.",
              expected="No - only exactly what was written, nothing "
                        "more.",
              board="None.",
              transition="Let's check a couple of misconceptions before "
                          "we close.")
    return slide


def slide_21_recap(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Quick Recap", "Quick Recap")
    draw_word_grid(["PROGRAM", "PYTHON", "PRINT()", "STRING", "COMMENT",
                     "SYNTAX ERROR"], cols=6, font_size=13)(
        slide, MARGIN, y + Inches(0.1), CONTENT_W, Inches(1.1))
    draw_pipeline(
        [("PROBLEM", None), ("LOGIC", None), ("ALGORITHM", None),
         ("PYTHON\nCODE", None), ("RUN", None), ("OUTPUT/\nRESULT", None)],
        height=Inches(1.15), font_size=11, gap=Inches(0.28))(
        slide, MARGIN, y + Inches(1.7), CONTENT_W, Inches(1.4))
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="4 min (Guide §23) — "
              "NON-NEGOTIABLE",
              purpose="One visual summary of every keyword and the full "
                      "bridged chain.",
              question="Why can't we just type English at a computer? "
                        "What does print() do? Why do strings need "
                        "quotes? What order do instructions run in? What "
                        "does Python do with a comment? Is an error a "
                        "sign something's badly wrong?",
              board="None.",
              transition="One question to leave you with.")
    return slide


def slide_22_bridge_forward(prs):
    slide = layout_big_question(
        prs, "A Question for Next Time",
        "Right now, every piece of text\nin your programs is fixed. What "
        "if\na program needed to remember\nsomething that changes?",
        size=28)
    set_notes(slide, markers=["DO NOT ANSWER"], timing="(Guide §24)",
              purpose="Leave this open as a deliberate hook into Class "
                      "06 (Variables & Data Types).",
              board="None.",
              transition="Class ends on the final takeaway.")
    return slide


def slide_23_final_takeaway(prs):
    slide = layout_section_divider(
        prs, "Final Takeaway",
        "“You didn't just learn about\nprogramming today — you did it. "
        "Every\nprogram you will ever write is built\nfrom exactly this: "
        "precise instructions,\nrun in order, read carefully when\nthey "
        "go wrong.”",
        title_size=27)
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
    slide_04_programming_language, slide_05_english_vs_python,
    slide_06_meet_python, slide_07_setup, slide_08_first_line,
    slide_09_running_output, slide_10_broken_quotes,
    slide_11_multiple_lines, slide_12_order_question, slide_13_comments,
    slide_14_errors_two_examples, slide_15_errors_are_normal,
    slide_16_write_run_read_fix, slide_17_full_bridge,
    slide_18_activity_intro, slide_19_activity_template,
    slide_20_activity_question, slide_21_recap, slide_22_bridge_forward,
    slide_23_final_takeaway,
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
    out = os.path.join(here, "Class_05_Your_First_Python_Program.pptx")
    n = build_presentation(out)
    print(f"Generated {n} slides -> {out}")
