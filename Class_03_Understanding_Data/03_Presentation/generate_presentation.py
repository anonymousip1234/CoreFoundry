# -*- coding: utf-8 -*-
"""
generate_presentation.py

Generates Class_03_Understanding_Data.pptx for
Bong Study Hub - Foundation Batch 2026.

Source of truth (do not redesign the lesson when editing this script):
  01_Master_Instructor_Guide/Class_03_Master_Instructor_Guide.md
  02_Student_Notes/Class_03_Student_Notes.md

This deck is a VISUAL TEACHING AID for a live instructor, not the
Student Notes placed onto slides. Slides carry diagrams, tables, and
short statements the instructor points to and talks around - never
paragraphs read aloud.

Design system, component library, and file structure follow the
convention established in
Class_01_Welcome_to_Computer_Science/03_Presentation/generate_presentation.py
(same palette, fonts, canvas, and shape-drawing primitives), adapted for
Class 03's own diagram shapes (tables, word grids, fan diagrams, a
lens-flow, stacked pipelines).

Structure of this file:
  1. Theme configuration (colors, fonts, spacing)
  2. Low-level utility functions (shapes, text, arrows)
  3. Reusable slide-layout components (title, question, diagram, ...)
  4. Content-aware diagram builders (pipeline, table, word grid, ...)
  5. Slide-specific builders (slide_01 .. slide_26)
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

# -- Colors -------------------------------------------------------------
# Same palette as the Class 01 deck / Student Notes PDFs, for cross-class
# brand consistency across the whole program.
NAVY = RGBColor(0x1E, 0x3A, 0x72)          # primary - dark blue
BLUE = RGBColor(0x2A, 0x5C, 0xB8)          # secondary - blue
CYAN = RGBColor(0x22, 0xC7, 0xE0)          # accent - electric blue / cyan
INK = RGBColor(0x1F, 0x27, 0x33)           # body text
MUTED = RGBColor(0x64, 0x70, 0x85)         # secondary text
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BG = RGBColor(0xF7, 0xF9, 0xFC)      # page background (light slides)
CARD_BG = RGBColor(0xEE, 0xF3, 0xFB)       # light navy-tinted card fill
CARD_BORDER = RGBColor(0xC7, 0xD6, 0xEC)
CYAN_BG = RGBColor(0xE4, 0xF9, 0xFB)
CYAN_BORDER = RGBColor(0x9F, 0xE6, 0xEE)
AMBER = RGBColor(0xC2, 0x79, 0x0F)         # used for "something's wrong
AMBER_BG = RGBColor(0xFB, 0xEE, 0xDC)      # here" — the messy-data slide.

# -- Fonts ----------------------------------------------------------------
FONT_DISPLAY = "Aptos Display"   # large titles / statements
FONT_BODY = "Aptos"              # everything else
FONT_FALLBACK = "Arial"          # Aptos ships with current Windows/Office
                                  # and degrades gracefully if unavailable.

# -- Canvas -----------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN

FOOTER_TEXT = "Bong Study Hub  ·  Foundation Batch 2026  ·  Class 03"


# ============================================================================
# 2. LOW-LEVEL UTILITIES
# ============================================================================

def new_slide(prs, bg=LIGHT_BG):
    """Add a blank slide with a solid background fill."""
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = bg
    return slide


def _i(v):
    """Coerce any coordinate to an exact integer EMU (python-pptx writes
    raw floats straight into the XML otherwise, which is invalid)."""
    return int(round(v))


def _no_shadow(shape):
    try:
        shape.shadow.inherit = False
    except Exception:
        pass


def add_rect(slide, x, y, w, h, fill=WHITE, line=None, line_w=Pt(1),
             radius=0.06, shadow=False):
    """Rounded rectangle. radius=None gives a sharp-cornered rectangle."""
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
    """A textbox with one or more paragraphs (split on \\n)."""
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
    """Small filled triangle used as an arrowhead. rotation: 90=right,
    180=down, 270=left, 0=up."""
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
    """Horizontal arrow from x1 to x2 at height y (pointing right)."""
    tip_gap = Emu(90000)
    add_line(slide, x1, y, x2 - tip_gap, y, color=color, width=width)
    add_triangle(slide, x2 - Emu(45000), y, Emu(160000), color, rotation=90)


def add_arrow_v(slide, x, y1, y2, color=BLUE, width=Pt(1.5)):
    """Vertical arrow from y1 to y2 at horizontal position x (pointing down)."""
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
    """Speaker notes are reminders, not scripts. Markers appear only here,
    never on the visible slide."""
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
    """Layout 1 - TITLE. Full navy background, minimal, premium."""
    slide = new_slide(prs, bg=NAVY)
    add_rect(slide, MARGIN, Inches(2.15), Inches(1.2), Inches(0.06), fill=CYAN)
    add_kicker(slide, MARGIN, Inches(1.75), Inches(10), kicker, color=CYAN)
    y = Inches(2.4)
    for line in title_lines:
        add_text(slide, MARGIN, y, Inches(11.5), Inches(1.1), line, size=54,
                  color=WHITE, bold=True, font=FONT_DISPLAY)
        y += Inches(1.05)
    add_text(slide, MARGIN, y + Inches(0.15), Inches(10.5), Inches(0.6),
              subtitle, size=20, color=RGBColor(0xB9, 0xCC, 0xEE),
              italic=True, font=FONT_BODY)
    add_text(slide, MARGIN, SLIDE_H - Inches(0.9), Inches(6), Inches(0.5),
              "Bong Study Hub\nFoundation Batch 2026", size=13,
              color=RGBColor(0x8F, 0xA6, 0xD1), font=FONT_BODY,
              line_spacing=1.15)
    return slide


def layout_section_divider(prs, kicker, title, subtitle=None, title_size=44):
    """Layout 2 - SECTION DIVIDER. Full navy background, one bold
    statement - used for the closing takeaway."""
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
    return title_y + Inches(1.15)  # y where content area starts


def layout_big_question(prs, kicker, question, note=None, size=40):
    """Layout 3 - BIG QUESTION. Minimal, large centered text, no answer."""
    slide = new_slide(prs, bg=LIGHT_BG)
    if kicker:
        add_kicker(slide, MARGIN, Inches(1.5), CONTENT_W, kicker, color=BLUE)
    add_text(slide, Inches(1.0), Inches(2.4), Inches(11.3), Inches(2.8),
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
    """Layout 5 - TWO-COLUMN COMPARISON.
    left/right = {"title": str, "sub": str, "tag": str}
    connector_symbol, when given (e.g. "VS", "≠"), replaces the arrow
    with a big centered symbol - used for contrasts rather than flows.
    """
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
    """Layout 6 - DIAGRAM. Title + a content-aware diagram drawn by
    diagram_fn(slide, x, y, w, h)."""
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
    """Layout 7 - FULL-SCREEN VISUAL. Minimal chrome, diagram dominates."""
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


def layout_recap(prs, kicker, title, items, numbered=False):
    """Layout 10 - RECAP. Short list of statements or questions."""
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
                  size=22, color=INK, anchor=MSO_ANCHOR.MIDDLE,
                  line_spacing=1.1)
        yy += row_h
    add_footer(slide)
    return slide


# ============================================================================
# 4. CONTENT-AWARE DIAGRAM BUILDERS
# ============================================================================

def draw_pipeline(items, height=Inches(1.3), font_size=15,
                   highlight_indices=None, gap=Inches(0.55)):
    """Horizontal chain of rounded boxes connected by arrows.
    items: list of (label, sub)."""
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
    """Vertical chain of rounded boxes connected by down-arrows."""
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


def draw_two_row_pipelines(rows_spec):
    """rows_spec: list of (row_label, [label, ...], highlight_indices_set)."""
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


def draw_table(headers, rows, highlight_cols=None, problem_cells=None,
               font_size=17):
    """A simple, readable data table. rows: list of lists of strings.
    problem_cells: set of (row_idx, col_idx) flagged amber - used for the
    messy-data slide. highlight_cols: set of column indices tinted cyan -
    used to mark a label column."""
    highlight_cols = highlight_cols or set()
    problem_cells = problem_cells or set()

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
                is_problem = (r, c) in problem_cells
                is_hl_col = c in highlight_cols
                if is_problem:
                    fill, border = AMBER_BG, AMBER
                elif is_hl_col:
                    fill, border = CYAN_BG, CYAN_BORDER
                else:
                    fill = WHITE if r % 2 == 0 else CARD_BG
                    border = CARD_BORDER
                add_rect(slide, cx + Inches(0.03), ry + Inches(0.03),
                          col_w - Inches(0.06), row_h - Inches(0.06),
                          fill=fill, line=border,
                          line_w=Pt(1.5 if is_problem else 1), radius=0.06)
                add_text(slide, cx, ry, col_w, row_h, str(val),
                          size=font_size, color=(AMBER if is_problem else INK),
                          bold=is_problem, align=PP_ALIGN.CENTER,
                          anchor=MSO_ANCHOR.MIDDLE)
    return _fn


def draw_table_annotated(headers, rows, row_idx=0, col_idx=2):
    """Same table as draw_table, plus a callout arrow pointing at one row
    ("ROW -> ONE EXAMPLE") and one column ("COLUMN -> ONE KIND OF
    INFORMATION")."""
    def _fn(slide, x, y, w, h):
        top_pad = Inches(0.65)
        left_pad = Inches(2.5)
        tx = x + left_pad
        ty = y + top_pad
        tw = w - left_pad
        th = h - top_pad
        ncols, nrows = len(headers), len(rows)
        row_h = min(Inches(0.85), th / (nrows + 1))
        total_h = row_h * (nrows + 1)
        table_top = ty + max(Inches(0), (th - total_h) / 2)
        col_w = tw / ncols
        for c, htext in enumerate(headers):
            cx = tx + c * col_w
            add_rect(slide, cx + Inches(0.03), table_top + Inches(0.03),
                      col_w - Inches(0.06), row_h - Inches(0.06), fill=NAVY,
                      radius=0.08)
            add_text(slide, cx, table_top, col_w, row_h, htext, size=18,
                      color=WHITE, bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
        for r, row in enumerate(rows):
            ry = table_top + (r + 1) * row_h
            is_target_row = (r == row_idx)
            for c, val in enumerate(row):
                cx = tx + c * col_w
                is_target_col = (c == col_idx)
                hl = is_target_row or is_target_col
                fill = CYAN_BG if hl else (WHITE if r % 2 == 0 else CARD_BG)
                border = CYAN if hl else CARD_BORDER
                add_rect(slide, cx + Inches(0.03), ry + Inches(0.03),
                          col_w - Inches(0.06), row_h - Inches(0.06),
                          fill=fill, line=border,
                          line_w=Pt(1.5 if hl else 1), radius=0.06)
                add_text(slide, cx, ry, col_w, row_h, str(val), size=18,
                          color=INK, align=PP_ALIGN.CENTER,
                          anchor=MSO_ANCHOR.MIDDLE)
        target_row_y = table_top + (row_idx + 1) * row_h
        add_text(slide, x, target_row_y, left_pad - Inches(0.3), row_h,
                  "ROW →\nONE EXAMPLE", size=15, color=NAVY, bold=True,
                  align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE,
                  line_spacing=1.05)
        add_arrow_h(slide, x + left_pad - Inches(0.28), target_row_y + row_h / 2,
                    tx - Inches(0.05), color=CYAN, width=Pt(2))
        target_col_x = tx + col_idx * col_w
        add_text(slide, target_col_x - Inches(0.6), y, col_w + Inches(1.2),
                  top_pad - Inches(0.1), "COLUMN → ONE KIND\nOF INFORMATION",
                  size=14, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                  line_spacing=1.0)
        add_arrow_v(slide, target_col_x + col_w / 2, y + top_pad - Inches(0.05),
                    table_top - Inches(0.03), color=CYAN, width=Pt(2))
    return _fn


def draw_word_grid(words, cols=4, highlight_indices=None, font_size=20):
    """A wrapping grid of word/phrase chips - used to show that data
    comes in many forms, or to list candidate pieces of information."""
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


def draw_fan(center_label, leaves):
    """One box at top branching down into several leaf boxes - shows one
    real-world thing producing several pieces of data."""
    def _fn(slide, x, y, w, h):
        center_w, center_h = Inches(2.8), Inches(0.85)
        cx0 = x + w / 2 - center_w / 2
        cy0 = y
        n = len(leaves)
        leaf_w, leaf_h = Inches(1.95), Inches(0.85)
        gap = (w - n * leaf_w) / (n - 1) if n > 1 else Inches(0)
        gap = max(Inches(0.12), min(gap, Inches(0.4)))
        total_w = n * leaf_w + (n - 1) * gap
        lx0 = x + (w - total_w) / 2
        leaf_y = y + h - leaf_h
        trunk_y = cy0 + center_h + (leaf_y - (cy0 + center_h)) / 2
        center_x = cx0 + center_w / 2
        add_rect(slide, cx0, cy0, center_w, center_h, fill=NAVY, radius=0.14)
        add_text(slide, cx0, cy0, center_w, center_h, center_label, size=22,
                  color=WHITE, bold=True, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE, font=FONT_DISPLAY)
        add_line(slide, center_x, cy0 + center_h, center_x, trunk_y,
                  color=BLUE, width=Pt(1.5))
        leaf_centers = [lx0 + i * (leaf_w + gap) + leaf_w / 2 for i in range(n)]
        add_line(slide, leaf_centers[0], trunk_y, leaf_centers[-1], trunk_y,
                  color=BLUE, width=Pt(1.5))
        for i, lc in enumerate(leaf_centers):
            add_arrow_v(slide, lc, trunk_y, leaf_y - Inches(0.02), color=BLUE,
                        width=Pt(1.5))
        for i in range(n):
            lx = lx0 + i * (leaf_w + gap)
            add_rect(slide, lx, leaf_y, leaf_w, leaf_h, fill=CARD_BG,
                      line=CARD_BORDER, line_w=Pt(1.1), radius=0.14)
            add_text(slide, lx, leaf_y, leaf_w, leaf_h, leaves[i], size=15,
                      color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                      anchor=MSO_ANCHOR.MIDDLE)
    return _fn


def draw_labeled_steps(pairs):
    """Vertical steps of (label, value) - e.g. REAL WORLD: Crowded
    canteen, OBSERVATION: What we notice, ..."""
    def _fn(slide, x, y, w, h):
        n = len(pairs)
        box_h = min(Inches(1.05), h / (n * 1.28))
        gap = (h - n * box_h) / (n - 1) if n > 1 else Inches(0)
        gap = max(Inches(0.1), min(gap, Inches(0.32)))
        total_h = n * box_h + (n - 1) * gap
        cy = y + max(Inches(0), (h - total_h) / 2)
        box_w = min(Inches(8.2), w)
        bx = x + w / 2 - box_w / 2
        for i, (label, value) in enumerate(pairs):
            add_rect(slide, bx, cy, box_w, box_h, fill=CARD_BG,
                      line=CARD_BORDER, line_w=Pt(1.1), radius=0.1)
            add_text(slide, bx + Inches(0.35), cy + Inches(0.12),
                      box_w - Inches(0.7), Inches(0.3), label, size=13,
                      color=BLUE, bold=True)
            add_text(slide, bx + Inches(0.35), cy + Inches(0.42),
                      box_w - Inches(0.7), box_h - Inches(0.5), value,
                      size=23, color=NAVY, bold=True, font=FONT_DISPLAY)
            if i < n - 1:
                add_arrow_v(slide, x + w / 2, cy + box_h + gap * 0.12,
                            cy + box_h + gap * 0.88, color=BLUE, width=Pt(1.6))
            cy += box_h + gap
    return _fn


def draw_definition(term, definition, term_size=72, def_size=28):
    """TERM, a thin rule, then a bold multi-line definition - both
    centered. The recurring shape for every "X = Y" slide."""
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
    """One big centered statement - for slides whose whole point is a
    single claim."""
    def _fn(slide, x, y, w, h):
        add_text(slide, x, y, w, h, text, size=size, color=color, bold=True,
                  font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.15)
    return _fn


def draw_lens_flow():
    """REAL WORLD -> (a lens) -> RECORDED INFORMATION."""
    def _fn(slide, x, y, w, h):
        box_w, box_h = Inches(3.1), Inches(1.05)
        mid_w, mid_h = Inches(1.6), Inches(1.6)
        cy = y + h / 2
        total = box_w + Inches(0.55) + mid_w + Inches(0.55) + box_w
        start_x = x + (w - total) / 2
        add_rect(slide, start_x, cy - box_h / 2, box_w, box_h, fill=CARD_BG,
                  line=CARD_BORDER, line_w=Pt(1.1), radius=0.1)
        add_text(slide, start_x, cy - box_h / 2, box_w, box_h, "REAL WORLD",
                  size=18, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE)
        lx2 = start_x + box_w
        add_arrow_h(slide, lx2 + Inches(0.06), cy, lx2 + Inches(0.55) - Inches(0.06),
                    color=BLUE, width=Pt(1.75))
        mx = lx2 + Inches(0.55)
        add_oval(slide, mx, cy - mid_h / 2, mid_w, mid_h, fill=CYAN_BG,
                  line=CYAN, line_w=Pt(1.75))
        add_text(slide, mx, cy - mid_h / 2, mid_w, mid_h, "DATA\nLENS",
                  size=17, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
        mx2 = mx + mid_w
        add_arrow_h(slide, mx2 + Inches(0.06), cy, mx2 + Inches(0.55) - Inches(0.06),
                    color=BLUE, width=Pt(1.75))
        rx = mx2 + Inches(0.55)
        add_rect(slide, rx, cy - box_h / 2, box_w, box_h, fill=CARD_BG,
                  line=CARD_BORDER, line_w=Pt(1.1), radius=0.1)
        add_text(slide, rx, cy - box_h / 2, box_w, box_h,
                  "RECORDED\nINFORMATION", size=17, color=NAVY, bold=True,
                  align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                  line_spacing=1.05)
    return _fn


def draw_badges(items):
    """items: list of (label, flagged). flagged=True renders an amber
    "flag" pill (e.g. Spam); False renders a neutral cyan pill."""
    def _fn(slide, x, y, w, h):
        n = len(items)
        gap = Inches(0.4)
        badge_w, badge_h = Inches(2.8), Inches(0.9)
        total_w = n * badge_w + (n - 1) * gap
        bx0 = x + (w - total_w) / 2
        by = y + h / 2 - badge_h / 2
        for i, (label, flagged) in enumerate(items):
            bx = bx0 + i * (badge_w + gap)
            fill = AMBER_BG if flagged else CYAN_BG
            border = AMBER if flagged else CYAN
            add_rect(slide, bx, by, badge_w, badge_h, fill=fill, line=border,
                      line_w=Pt(1.5), radius=0.5)
            add_text(slide, bx, by, badge_w, badge_h, label, size=20,
                      color=(AMBER if flagged else NAVY), bold=True,
                      align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return _fn


def draw_three_words_cards(cards):
    """cards: list of dicts {title, sub} - short word + one-line meaning."""
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
            add_text(slide, cx + Inches(0.3), top + Inches(0.4),
                      card_w - Inches(0.6), Inches(0.7), card["title"],
                      size=24, color=NAVY, bold=True, font=FONT_DISPLAY)
            add_text(slide, cx + Inches(0.3), top + Inches(1.15),
                      card_w - Inches(0.6), card_h - Inches(1.4), card["sub"],
                      size=15, color=INK, line_spacing=1.25)
    return _fn


# ============================================================================
# 5. SLIDE-SPECIFIC BUILDERS
# ============================================================================

def slide_01_title(prs):
    slide = layout_title(
        prs, "Bong Study Hub · Foundation Batch 2026 · Class 03",
        ["Understanding", "Data"],
        "From the Real World → Information → Data")
    set_notes(slide, timing="2 min",
              purpose="Set tone; do not read the slide aloud.",
              say="Briefly connect back to Class 02 in one sentence before "
                  "starting.",
              board="None.",
              transition="How would you answer: how crowded is your "
                          "college canteen right now?")
    return slide


def slide_02_big_question(prs):
    slide = layout_big_question(
        prs, "The Big Question",
        "How do we turn something happening\nin the real world into "
        "something\na computer can work with?", size=34)
    set_notes(slide, markers=["ASK", "PAUSE"], timing="3 min "
              "(Guide §8)",
              purpose="Open with the canteen debate before naming this "
                      "question.",
              question="How crowded is your college canteen right now? "
                        "Which of your answers just now counts as data?",
              expected="Split opinions - some say only the number counts, "
                        "some say all of them count.",
              board="None.",
              transition="Hold that thought - quick rewind to last class "
                          "first.")
    return slide


def slide_03_class02_callback(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Callback — Class 02",
                          "Data → Learning → Model → Prediction",
                          title_size=30)
    diagram_y = y + Inches(0.15)
    draw_pipeline([("DATA", None), ("LEARNING", None), ("MODEL", None),
                   ("PREDICTION", None)], highlight_indices={0},
                  height=Inches(1.3), font_size=18)(slide, MARGIN, diagram_y,
                                                      CONTENT_W, Inches(1.5))
    add_text(slide, MARGIN, diagram_y + Inches(1.85), CONTENT_W, Inches(1.0),
              "What exactly is DATA?", size=34, color=NAVY, bold=True,
              font=FONT_DISPLAY, align=PP_ALIGN.CENTER,
              anchor=MSO_ANCHOR.MIDDLE)
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="7 min (Guide §9)",
              purpose="Re-open the DATA box Class 02 skipped.",
              question="What did Machine Learning start with, last class? "
                        "Did we ever actually define what data is?",
              expected="\"Data\" / \"examples\" - then most will realize "
                        "\"not really\" to the second question.",
              board="None.",
              transition="Let's start with a much more basic question: "
                          "when you hear the word data, what do you "
                          "picture?")
    return slide


def slide_04_what_is_data(prs):
    slide = layout_diagram(
        prs, "Definition", "What Is Data?",
        draw_definition("DATA", "RECORDED INFORMATION\nABOUT SOMETHING",
                          term_size=78, def_size=30))
    set_notes(slide, timing="4 min (Guide §10)",
              purpose="Land the class's one working definition - no "
                      "mention of numbers, spreadsheets, or computers.",
              say="Numbers are just one form data can take - not the "
                  "definition of data.",
              board="None.",
              transition="So data isn't just numbers - let's actually "
                          "prove that.")
    return slide


def slide_05_not_just_numbers(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Breaking an Assumption",
                          "Data Is Not Just Numbers")
    words = ["NUMBER", "TEXT", "PHOTO", "AUDIO", "LOCATION", "MEASUREMENT",
             "RECORD"]
    draw_word_grid(words, cols=4)(slide, MARGIN, y + Inches(0.1), CONTENT_W,
                                    Inches(3.5))
    add_text(slide, MARGIN, SLIDE_H - Inches(1.15), CONTENT_W, Inches(0.5),
              "DATA ≠ ONLY NUMBERS", size=26, color=NAVY, bold=True,
              font=FONT_DISPLAY, align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK", "CHALLENGE"], timing="12 min "
              "(Guide §10) — NON-NEGOTIABLE",
              purpose="Challenge the numbers-only assumption one example "
                      "at a time: is a photo data? A voice recording? A "
                      "sentence? A location?",
              expected="Some will insist a photo isn't data until it's "
                        "'in' a computer - acknowledge the instinct, then "
                        "park it (Guide §10).",
              board="None.",
              transition="But something still had to happen for a fact to "
                          "become recorded data. What was that something?")
    return slide


def slide_06_real_world_chain(prs):
    slide = layout_diagram(
        prs, "The First Chain", "Real World → Observation → Data",
        draw_vertical_flow(["REAL WORLD", "OBSERVATION", "DATA"],
                            box_w=Inches(5.6), font_size=22),
        caption='e.g., "It is raining outside" → someone checks → '
                'it gets recorded.')
    set_notes(slide, markers=["LIVE"], timing="12 min (Guide §11) "
              "— NON-NEGOTIABLE, HERO MOMENT",
              purpose="Build this chain live, one box at a time, using "
                      "the rain example, then immediately re-run it with "
                      "the canteen example (next slide).",
              say="An observation only becomes useful data once it's "
                  "recorded in some form that can be stored or worked "
                  "with later.",
              board="Build REAL WORLD → OBSERVE → RECORD → "
                    "DATA live before showing this clean version.",
              transition="Let's re-run this exact chain with the canteen "
                          "example from the start of class.")
    return slide


def slide_07_canteen_example(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Applying the Chain", "The Canteen Example")
    pairs = [("REAL WORLD", "Crowded canteen"),
             ("OBSERVATION", "What we notice"),
             ("RECORDED", "“80% full”"),
             ("DATA", "“80% full”")]
    draw_labeled_steps(pairs)(slide, MARGIN, y, CONTENT_W, Inches(4.15))
    add_text(slide, MARGIN, SLIDE_H - Inches(1.1), CONTENT_W, Inches(0.5),
              "DATA IS A REPRESENTATION OF REALITY.", size=20, color=NAVY,
              bold=True, font=FONT_DISPLAY, align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, timing="(part of Guide §11)",
              purpose="Cement the chain with the class's own opening "
                      "example before moving on.",
              board="None.",
              transition="So one real-world thing can turn into several "
                          "pieces of data. Let's stick with something "
                          "even more familiar: you.")
    return slide


def slide_08_one_thing_many_data(prs):
    slide = layout_diagram(
        prs, "One Real Thing, Many Data Points",
        "One Thing → Many Pieces of Data",
        draw_fan("STUDENT", ["Name", "Year", "Attendance", "Department",
                              "Marks"]))
    set_notes(slide, markers=["ASK"], timing="11 min (Guide §12)",
              purpose="Show one real-world thing can be described by "
                      "several different pieces of data at once.",
              question="Did the student change while we listed all of "
                        "that? Did the way we describe the student "
                        "change?",
              expected="No, the student didn't change. Yes, the "
                        "description did.",
              board="None.",
              transition="Now - what do we call it when we put many of "
                          "these together?")
    return slide


def slide_09_examples_to_dataset(prs):
    headers = ["Student", "Year", "Attendance", "Marks"]
    rows = [["A", "1", "82%", "76"], ["B", "1", "91%", "84"],
            ["C", "1", "68%", "61"]]
    slide = layout_diagram(
        prs, "Putting Examples Together", "From Examples to a Dataset",
        draw_table(headers, rows, font_size=20))
    set_notes(slide, timing="11 min (Guide §13)",
              purpose="Introduce example/record and dataset using a "
                      "table students can see at once.",
              say="One student, described by its data, is one example. "
                  "The whole table is a dataset.",
              board="None.",
              transition="Now let's learn exactly how to read this "
                          "table.")
    return slide


def slide_10_reading_the_table(prs):
    headers = ["Student", "Year", "Attendance", "Marks"]
    rows = [["A", "1", "82%", "76"], ["B", "1", "91%", "84"],
            ["C", "1", "68%", "61"]]
    slide = layout_diagram(
        prs, "Reading the Structure", "How to Read the Table",
        draw_table_annotated(headers, rows, row_idx=0, col_idx=2))
    set_notes(slide, markers=["ASK", "REPEAT ALOUD"],
              timing="13 min (Guide §14, Part A) — NON-NEGOTIABLE",
              purpose="Land ROW → ONE EXAMPLE and COLUMN → ONE "
                      "KIND OF INFORMATION - say it slowly, have students "
                      "repeat it in their own words.",
              board="None.",
              transition="Try it cold on a table you haven't seen yet - "
                          "the movie table activity (see Student Notes).")
    return slide


def slide_11_what_is_a_dataset(prs):
    slide = layout_diagram(
        prs, "Definition", "What Is a Dataset?",
        draw_definition("DATASET", "COLLECTION OF\nRELATED EXAMPLES",
                          term_size=62, def_size=28))
    set_notes(slide, timing="(closes Guide §13/§14)",
              purpose="Land the dataset definition, connected visually "
                      "back to the table just shown.",
              board="None.",
              transition="But real-world data doesn't always look this "
                          "clean.")
    return slide


def slide_12_messy_data(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "A Necessary Reality Check",
                          "Real-World Data Can Be Messy")
    headers = ["Student", "Age", "City"]
    rows = [["A", "18", "Kolkata"], ["B", "“eighteen”", "kolkata"],
            ["C", "— missing —", "Calcutta"]]
    problem_cells = {(1, 1), (2, 1), (1, 2), (2, 2)}
    draw_table(headers, rows, problem_cells=problem_cells, font_size=19)(
        slide, MARGIN + Inches(1.4), y + Inches(0.05), CONTENT_W - Inches(2.8),
        Inches(2.7))
    add_text(slide, MARGIN, y + Inches(2.95), CONTENT_W, Inches(0.6),
              "What looks wrong here?", size=26, color=NAVY, bold=True,
              font=FONT_DISPLAY, align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK", "LET STUDENTS HUNT"],
              timing="8 min (Guide §15) — NON-NEGOTIABLE",
              purpose="Let students find the problems themselves before "
                      "naming any.",
              expected="Missing age (B), impossible/inconsistent age "
                        "format, inconsistent city spelling.",
              board="None.",
              transition="If messy data is a problem, does having a huge "
                          "amount of data automatically fix it?")
    return slide


def slide_13_more_data_not_better(prs):
    slide = layout_two_column(
        prs, "Quantity vs. Quality", "More Data ≠ Automatically Better Data",
        {"tag": "QUANTITY ALONE", "title": "1,000,000 examples",
         "sub": "Wrong, repetitive, or nearly all the same."},
        {"tag": "QUALITY + VARIETY", "title": "1,000 examples",
         "sub": "Accurate, and covering real variety."},
        connector_symbol="VS")
    set_notes(slide, markers=["ASK"], timing="8 min (Guide §16)",
              purpose="Quantity is not the same thing as quality or "
                      "variety.",
              question="Is one million examples automatically good data? "
                        "What if 1,000 are accurate and varied instead?",
              expected="No to the first; yes, the smaller set is better.",
              say="Remember Class 02's cats-vs-dogs example - the issue "
                  "was rarely 'not enough photos' alone, it was variety.",
              board="None.",
              transition="So far we've described examples in general. "
                          "Now let's look at a special kind of column.")
    return slide


def slide_14_what_makes_data_useful(prs):
    cards = [
        {"title": "Relevant", "sub": "Fits the question being asked."},
        {"title": "Useful", "sub": "Actually helps answer it."},
        {"title": "Representative", "sub": "Covers the variety that "
                                             "matters."},
    ]
    slide = layout_diagram(
        prs, "Three Words Worth Remembering", "What Makes Data Useful?",
        draw_three_words_cards(cards))
    set_notes(slide, timing="(folds into Guide §16/§18)",
              purpose="Keep this intuitive - not a formal data-quality "
                      "framework.",
              board="None.",
              transition="Now, the special column that holds a known "
                          "answer.")
    return slide


def slide_15_features(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Describing an Example", "Features")
    draw_definition("FEATURE", "INFORMATION DESCRIBING\nAN EXAMPLE",
                      term_size=62, def_size=26)(slide, MARGIN, y + Inches(0.1),
                                                   CONTENT_W, Inches(2.7))
    add_text(slide, MARGIN, SLIDE_H - Inches(1.15), CONTENT_W, Inches(0.6),
              'e.g., "Congratulations! You won a prize." → words used, '
              'sender, and phrases are all features.',
              size=15, color=MUTED, italic=True, align=PP_ALIGN.CENTER,
              line_spacing=1.15)
    add_footer(slide)
    set_notes(slide, timing="5 min (Guide §17, Part A/B)",
              purpose="A feature describes an example - keep it "
                      "conceptual, no feature engineering.",
              board="None.",
              transition="Now the other kind of column - the one that "
                          "holds a known answer.")
    return slide


def slide_16_labels(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "The Known Answer", "Labels")
    draw_definition("LABEL", "KNOWN ANSWER / CATEGORY,\nWHEN ONE EXISTS",
                      term_size=52, def_size=24)(slide, MARGIN, y + Inches(0.05),
                                                   CONTENT_W, Inches(2.0))
    draw_badges([("Spam", True), ("Not Spam", False)])(
        slide, MARGIN, y + Inches(2.15), CONTENT_W, Inches(1.1))
    add_footer(slide)
    set_notes(slide, timing="5 min (Guide §17, Part A)",
              purpose="A label is the known answer already attached to "
                      "an example. Not a formal 'supervised learning' "
                      "introduction.",
              board="None.",
              transition="Let's put features and a label in the same "
                          "table.")
    return slide


def slide_17_features_vs_label(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Two Different Jobs", "Features vs. Label")
    headers = ["Email", "Sender", "Time", "Label"]
    rows = [["“Win free money!”", "Unknown", "2:14 AM", "Spam"],
            ["“Meeting at 3 PM”", "Colleague", "9:02 AM", "Not Spam"]]
    draw_table(headers, rows, highlight_cols={3}, font_size=18)(
        slide, MARGIN, y + Inches(0.15), CONTENT_W, Inches(2.3))
    add_text(slide, MARGIN, y + Inches(2.65), CONTENT_W, Inches(0.5),
              "Not every dataset has a label.", size=18, color=MUTED,
              italic=True, align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="4 min (Guide §17, "
              "Part B)",
              purpose="Distinguish describing-columns (features) from "
                      "the answer-column (label), highlighted in cyan.",
              question="Which columns describe the example, and which "
                        "holds the answer we already know?",
              expected="Email/Sender/Time are features; Label holds the "
                        "answer.",
              board="None.",
              transition="Now - which data should we even bother "
                          "collecting?")
    return slide


def slide_18_canteen_question(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    add_kicker(slide, MARGIN, Inches(0.5), CONTENT_W, "A Question First",
                color=BLUE)
    add_text(slide, MARGIN, Inches(0.86), CONTENT_W, Inches(1.0),
              "Can We Predict Canteen Crowding?", size=30, color=NAVY,
              bold=True, font=FONT_DISPLAY)
    add_rect(slide, MARGIN, Inches(1.75), Inches(0.85), Inches(0.045),
              fill=CYAN)
    words = ["TIME", "DAY", "STUDENTS ON CAMPUS", "CLASS BREAK", "WEATHER"]
    draw_word_grid(words, cols=3, font_size=18)(slide, MARGIN, Inches(2.15),
                                                  CONTENT_W, Inches(3.0))
    add_text(slide, MARGIN, SLIDE_H - Inches(1.05), CONTENT_W, Inches(0.4),
              "Not the only correct list — the point is asking the "
              "right questions.", size=14, color=MUTED, italic=True,
              align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK", "ENCOURAGE DISAGREEMENT"],
              timing="8 min (Guide §18) — NON-NEGOTIABLE",
              purpose="Reasoning about what to collect, before any "
                      "collecting happens - an early taste of Data "
                      "Science thinking.",
              question="What data could we collect? Which of it do you "
                        "actually think would be useful?",
              expected="Open debate - do not converge on one official "
                        "list.",
              board="None.",
              transition="Would that same data help with a completely "
                          "different question?")
    return slide


def slide_19_different_question(prs):
    slide = layout_two_column(
        prs, "The Question Decides",
        "Different Question → Different Data",
        {"tag": "CANTEEN CROWDING?", "title": "Time · Day · Weather",
         "sub": "Class breaks, footfall patterns."},
        {"tag": "WILL A STUDENT LIKE THIS MOVIE?",
         "title": "Genre · Mood · Reviews",
         "sub": "Past ratings, favorite actors."},
        connector_symbol="VS")
    add_text(slide, MARGIN, Inches(5.25), CONTENT_W, Inches(0.7),
              "THE QUESTION DETERMINES WHAT DATA IS USEFUL.", size=21,
              color=NAVY, bold=True, font=FONT_DISPLAY,
              align=PP_ALIGN.CENTER)
    set_notes(slide, timing="(closes Guide §18, Part A)",
              purpose="There's no such thing as 'good data' floating in "
                      "the abstract.",
              board="None.",
              transition="One more idea before we reconnect to Machine "
                          "Learning.")
    return slide


def slide_20_representation(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "A Lens, Not a Mirror",
                          "Data Is a Representation")
    add_text(slide, MARGIN, y + Inches(0.05), CONTENT_W, Inches(0.7),
              "REAL WORLD ≠ DATA", size=32, color=NAVY, bold=True,
              font=FONT_DISPLAY, align=PP_ALIGN.CENTER)
    draw_lens_flow()(slide, MARGIN, y + Inches(0.95), CONTENT_W, Inches(2.0))
    add_text(slide, MARGIN, y + Inches(3.2), CONTENT_W, Inches(0.6),
              "EVERY REPRESENTATION LEAVES SOMETHING OUT.", size=21,
              color=NAVY, bold=True, font=FONT_DISPLAY,
              align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, markers=["ASK"], timing="(Guide §18, Part B)",
              purpose="Data is a lens we choose to look through - keep "
                      "this practical, not philosophical.",
              question="Does a list like Age/Height/Attendance/Marks "
                        "completely describe a person?",
              expected="No, obviously not.",
              board="None.",
              transition="Let's put the whole day on one board.")
    return slide


def slide_21_hero_pipeline(prs):
    items = ["REAL WORLD", "OBSERVATION", "DATA", "LEARNING", "MODEL",
             "PREDICTION"]
    slide = layout_full_screen_visual(
        prs, "The Hero Diagram", None,
        draw_vertical_flow(items, highlight_indices={0, 1}, box_w=Inches(5.2),
                            font_size=18),
        caption="Cyan = new today  ·  Card = already known from "
                "Class 02")
    set_notes(slide, markers=["LIVE"], timing="(Guide §19) — "
              "NON-NEGOTIABLE, HERO MOMENT",
              purpose="Build this top to bottom, one line at a time - "
                      "never reveal it finished. The bottom four lines "
                      "are exactly Class 02's pipeline; today filled in "
                      "what comes before DATA.",
              board="Build live, pausing between each line.",
              transition="And inside that same DATA box, today also "
                          "built a second chain.")
    return slide


def slide_22_what_we_added(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Class 02 + Class 03", "What We Added Today")
    rows_spec = [
        ("CLASS 02", ["DATA", "LEARNING", "MODEL", "PREDICTION"], set()),
        ("TODAY", ["REAL WORLD", "OBSERVATION", "DATA"], {0, 1}),
    ]
    draw_two_row_pipelines(rows_spec)(slide, MARGIN, y + Inches(0.3),
                                        CONTENT_W, Inches(2.6))
    add_text(slide, MARGIN, y + Inches(3.15), CONTENT_W, Inches(0.5),
              "Together, they form one continuous chain.", size=16,
              color=MUTED, italic=True, align=PP_ALIGN.CENTER)
    add_footer(slide)
    set_notes(slide, timing="(Guide §19)",
              purpose="Nothing from Class 02 changes - we filled in "
                      "where Data actually comes from.",
              board="None.",
              transition="One last, important distinction before we "
                          "close.")
    return slide


def slide_23_data_not_ml(prs):
    slide = layout_two_column(
        prs, "An Important Distinction", "Data ≠ Machine Learning",
        {"tag": "THE INGREDIENT", "title": "Data",
         "sub": "Recorded information about something."},
        {"tag": "THE PROCESS", "title": "Machine Learning",
         "sub": "Learns patterns from data to build a model."},
        connector_symbol="≠")
    set_notes(slide, markers=["ASK"], timing="(Guide §19)",
              purpose="Data is an ingredient; Machine Learning is the "
                      "process that uses it.",
              question="If I hand you a dataset right now, do you "
                        "automatically have Machine Learning?",
              expected="No.",
              board="None.",
              transition="Let's put it all together.")
    return slide


def slide_24_quick_recap(prs):
    slide = new_slide(prs, bg=LIGHT_BG)
    y = _content_header(slide, "Quick Recap", "Quick Recap")
    draw_word_grid(["DATA", "DATASET", "EXAMPLE", "FEATURE", "LABEL"],
                    cols=5, font_size=17)(slide, MARGIN, y + Inches(0.1),
                                            CONTENT_W, Inches(1.15))
    draw_pipeline(
        [("REAL WORLD", None), ("OBSERVATION", None), ("DATA", None),
         ("LEARNING", None), ("MODEL", None), ("PREDICTION", None)],
        height=Inches(1.05), font_size=12, gap=Inches(0.3))(
        slide, MARGIN, y + Inches(1.75), CONTENT_W, Inches(1.4))
    add_footer(slide)
    set_notes(slide, timing="(Guide §19, recap)",
              purpose="One visual summary of every keyword and the full "
                      "chain.",
              board="None.",
              transition="A few questions to sit with before we go.")
    return slide


def slide_25_think_about_it(prs):
    items = [
        "Can a photograph be data? Why?",
        "What does one row represent?",
        "What's the difference between a feature and a label?",
        "Why isn't more data automatically better?",
    ]
    slide = layout_recap(prs, "Think About It", "Think About It", items,
                           numbered=True)
    set_notes(slide, markers=["ASK", "LET STUDENTS ANSWER"],
              timing="(Guide §19, final recap)",
              purpose="Test understanding, not memorization - accept "
                      "answers in the student's own words.",
              board="None.",
              transition="One final line to close on.")
    return slide


def slide_26_final_takeaway(prs):
    slide = layout_section_divider(
        prs, "Final Takeaway",
        "“Before we can teach a machine from data,\nwe first have to "
        "understand what data\nwe’re giving it.”",
        title_size=38)
    set_notes(slide, timing="1 min",
              purpose="Close the class on this exact line, said slowly.",
              say="That's the whole of today's class in one sentence.",
              board="None.",
              transition="Class ends.")
    return slide


# ============================================================================
# 6. MAIN GENERATION FUNCTION
# ============================================================================

SLIDE_BUILDERS = [
    slide_01_title, slide_02_big_question, slide_03_class02_callback,
    slide_04_what_is_data, slide_05_not_just_numbers,
    slide_06_real_world_chain, slide_07_canteen_example,
    slide_08_one_thing_many_data, slide_09_examples_to_dataset,
    slide_10_reading_the_table, slide_11_what_is_a_dataset,
    slide_12_messy_data, slide_13_more_data_not_better,
    slide_14_what_makes_data_useful, slide_15_features, slide_16_labels,
    slide_17_features_vs_label, slide_18_canteen_question,
    slide_19_different_question, slide_20_representation,
    slide_21_hero_pipeline, slide_22_what_we_added, slide_23_data_not_ml,
    slide_24_quick_recap, slide_25_think_about_it, slide_26_final_takeaway,
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
    out = os.path.join(here, "Class_03_Understanding_Data.pptx")
    n = build_presentation(out)
    print(f"Generated {n} slides -> {out}")
