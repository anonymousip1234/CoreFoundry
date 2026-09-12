# -*- coding: utf-8 -*-
"""
generate_homework_pdf.py

Generates Class_04_Homework.pdf directly from Class_04_Homework.md.

This is the ONLY tool that produces the student-facing PDF - it parses
the actual Markdown file (headings, paragraphs, tables, code/diagram
blocks, bullet and lettered lists, checkbox lists, and the custom
`<!-- BLANK:N -->` writing-space directive) into ReportLab flowables,
rather than re-typing the homework content a second time anywhere.

Everything from the `<!-- ANSWER KEY BELOW THIS LINE ... -->` marker
onward is the instructor-only answer key and is deliberately EXCLUDED
from the PDF - only the student-facing content above that marker is
rendered.

Usage:
    python generate_homework_pdf.py

Re-run whenever Class_04_Homework.md changes.
"""

import os
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether,
)

# ============================================================================
# Fonts (registered from local TrueType files so Unicode arrows/≠/quotes
# render correctly - the base-14 PDF fonts only reliably cover WinAnsi).
# ============================================================================

FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Body", os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Body-Italic", os.path.join(FONT_DIR, "ariali.ttf")))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", os.path.join(FONT_DIR, "arialbi.ttf")))
pdfmetrics.registerFontFamily(
    "Body", normal="Body", bold="Body-Bold", italic="Body-Italic",
    boldItalic="Body-BoldItalic")
pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONT_DIR, "consola.ttf")))
pdfmetrics.registerFont(TTFont("Mono-Bold", os.path.join(FONT_DIR, "consolab.ttf")))

# ============================================================================
# Palette - matches the Class 04 Presentation's design system, so the
# whole class's artifacts read as one visual identity.
# ============================================================================

NAVY = colors.HexColor("#1E3A72")
BLUE = colors.HexColor("#2A5CB8")
CYAN = colors.HexColor("#22C7E0")
INK = colors.HexColor("#1F2733")
MUTED = colors.HexColor("#647085")
CARD_BG = colors.HexColor("#EEF3FB")
CARD_BORDER = colors.HexColor("#C7D6EC")
RULE = colors.HexColor("#DCE3ED")
WHITE = colors.white

PAGE_W, PAGE_H = A4
MARGIN = 0.85 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

# ============================================================================
# Paragraph styles
# ============================================================================

STYLE_TITLE = ParagraphStyle(
    "Title", fontName="Body-Bold", fontSize=21, leading=25,
    textColor=NAVY, spaceAfter=4)
STYLE_STRONG_LINE = ParagraphStyle(
    "StrongLine", fontName="Body-Bold", fontSize=11, leading=14,
    textColor=INK, spaceAfter=2)
STYLE_NOTE = ParagraphStyle(
    "Note", fontName="Body-Italic", fontSize=9.7, leading=13,
    textColor=MUTED, spaceBefore=1, spaceAfter=7)
STYLE_META = ParagraphStyle(
    "Meta", fontName="Body", fontSize=10, leading=14,
    textColor=INK, spaceAfter=2)
STYLE_H2 = ParagraphStyle(
    "H2", fontName="Body-Bold", fontSize=14.5, leading=18,
    textColor=NAVY, spaceBefore=16, spaceAfter=6)
STYLE_H3 = ParagraphStyle(
    "H3", fontName="Body-Bold", fontSize=12, leading=16,
    textColor=NAVY, spaceBefore=4, spaceAfter=6)
STYLE_BODY = ParagraphStyle(
    "Body", fontName="Body", fontSize=10.4, leading=15,
    textColor=INK, spaceAfter=6)
STYLE_BULLET = ParagraphStyle(
    "Bullet", parent=STYLE_BODY, leftIndent=14, firstLineIndent=-14,
    spaceAfter=4)
STYLE_LETTERED = ParagraphStyle(
    "Lettered", parent=STYLE_BODY, leftIndent=16, firstLineIndent=-16,
    spaceAfter=5)
STYLE_CHECK_TEXT = ParagraphStyle(
    "CheckText", parent=STYLE_BODY, spaceAfter=0)
STYLE_TABLE_CELL = ParagraphStyle(
    "TableCell", fontName="Body", fontSize=9.6, leading=13, textColor=INK)
STYLE_TABLE_HEAD = ParagraphStyle(
    "TableHead", fontName="Body-Bold", fontSize=9.8, leading=13,
    textColor=WHITE)

# ============================================================================
# Inline markdown -> a small subset of ReportLab's paragraph markup
# ============================================================================

def escape_xml(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))


def inline_md(text):
    text = escape_xml(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<i>\1</i>", text)
    return text


# ============================================================================
# Small flowable builders
# ============================================================================

def blank_lines(n):
    """N ruled writing lines, rendered as a borderless table with only a
    bottom border per row - the PDF's "write your answer here" space."""
    data = [[""] for _ in range(n)]
    t = Table(data, colWidths=[CONTENT_W], rowHeights=[0.34 * inch] * n)
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 0.75, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 8)]


def code_box(text):
    p = Paragraph(escape_xml(text).replace("\n", "<br/>"),
                   ParagraphStyle("Mono", fontName="Mono", fontSize=10,
                                   leading=15, textColor=INK))
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 0.75, CARD_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]


def is_separator_row(cells):
    return all(re.match(r"^:?-+:?$", c) for c in cells if c != "") and \
        any(c != "" for c in cells)


def parse_table_rows(table_lines):
    rows = []
    for tl in table_lines:
        inner = tl.strip()
        if inner.startswith("|"):
            inner = inner[1:]
        if inner.endswith("|"):
            inner = inner[:-1]
        rows.append([c.strip() for c in inner.split("|")])
    header = None
    body = rows
    if len(rows) >= 2 and is_separator_row(rows[1]):
        header, body = rows[0], rows[2:]
    return header, body


def data_table(table_lines):
    header, body = parse_table_rows(table_lines)
    ncols = len(header) if header else (len(body[0]) if body else 1)
    col_w = CONTENT_W / ncols
    data = []
    if header:
        data.append([Paragraph(inline_md(c), STYLE_TABLE_HEAD) for c in header])
    for row in body:
        data.append([Paragraph(inline_md(c), STYLE_TABLE_CELL) for c in row])
    t = Table(data, colWidths=[col_w] * ncols)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.75, CARD_BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        row_start = 1
    else:
        row_start = 0
    for i in range(row_start, len(data)):
        if (i - row_start) % 2 == 1:
            style.append(("BACKGROUND", (0, i), (-1, i), CARD_BG))
        else:
            style.append(("BACKGROUND", (0, i), (-1, i), WHITE))
    t.setStyle(TableStyle(style))
    # KeepTogether so the table always moves to the next page as a whole
    # rather than splitting rows across a page break.
    return [Spacer(1, 4), KeepTogether([t]), Spacer(1, 8)]


def checkbox_row(text):
    box = Table([[""]], colWidths=[12], rowHeights=[12])
    box.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, MUTED),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    label = Paragraph(text, STYLE_CHECK_TEXT)
    row = Table([[box, label]], colWidths=[18, CONTENT_W - 18])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return row


# ============================================================================
# Markdown -> flowables
# ============================================================================

def build_flowables(md_text):
    lines = md_text.split("\n")

    cut_idx = None
    for i, l in enumerate(lines):
        if "ANSWER KEY BELOW THIS LINE" in l:
            cut_idx = i
            break
    if cut_idx is not None:
        lines = lines[:cut_idx]

    flowables = []
    current_group = None
    para_buffer = []

    def emit(flowable_or_list):
        target = current_group if current_group is not None else flowables
        if isinstance(flowable_or_list, list):
            target.extend(flowable_or_list)
        else:
            target.append(flowable_or_list)

    def flush_paragraph():
        if para_buffer:
            text = " ".join(para_buffer).strip()
            para_buffer.clear()
            if text:
                emit(Paragraph(inline_md(text), STYLE_BODY))

    def end_group():
        nonlocal current_group
        if current_group:
            flowables.append(KeepTogether(current_group))
        current_group = None

    def gather_continuation(idx):
        """Soft-wrapped continuation lines belonging to the list item that
        starts at `idx - 1` - i.e. everything up to the next blank line or
        the start of a new block (heading, list item, table, code fence,
        rule, or comment)."""
        texts = []
        while idx < n:
            nxt = lines[idx].strip()
            if nxt == "" or nxt.startswith(("#", "```", "|", "<!--", "- ", "---")) \
                    or re.match(r"^[a-d]\.\s", nxt):
                break
            texts.append(nxt)
            idx += 1
        return texts, idx

    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        stripped = raw.strip()

        if stripped == "":
            flush_paragraph()
            i += 1
            continue

        if stripped.startswith("<!--"):
            flush_paragraph()
            m = re.match(r"<!--\s*BLANK:(\d+)\s*-->", stripped)
            if m:
                emit(blank_lines(int(m.group(1))))
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            emit(code_box("\n".join(code_lines)))
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table_lines = []
            while i < n and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            emit(data_table(table_lines))
            continue

        if stripped == "---":
            flush_paragraph()
            emit(Spacer(1, 4))
            emit(HRFlowable(width="100%", thickness=0.75, color=RULE,
                              spaceBefore=0, spaceAfter=10))
            i += 1
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            emit(Paragraph(inline_md(stripped[2:]), STYLE_TITLE))
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            end_group()
            flowables.append(Paragraph(inline_md(stripped[3:]), STYLE_H2))
            flowables.append(HRFlowable(width="100%", thickness=1.4,
                                          color=CYAN, spaceBefore=0,
                                          spaceAfter=8))
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            end_group()
            current_group = []
            current_group.append(Paragraph(inline_md(stripped[4:]), STYLE_H3))
            i += 1
            continue

        if stripped.startswith("- [ ]"):
            flush_paragraph()
            first = stripped[5:].strip()
            cont, i = gather_continuation(i + 1)
            text = " ".join([first] + cont)
            emit(checkbox_row(inline_md(text)))
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            first = stripped[2:].strip()
            cont, i = gather_continuation(i + 1)
            text = " ".join([first] + cont)
            emit(Paragraph("•&nbsp;&nbsp;" + inline_md(text), STYLE_BULLET))
            continue

        if re.match(r"^[a-d]\.\s", stripped):
            flush_paragraph()
            cont, i = gather_continuation(i + 1)
            text = " ".join([stripped] + cont)
            emit(Paragraph(inline_md(text), STYLE_LETTERED))
            continue

        if re.match(r"^\*\*(.+)\*\*$", stripped):
            flush_paragraph()
            inner = re.match(r"^\*\*(.+)\*\*$", stripped).group(1)
            emit(Paragraph(inline_md(inner), STYLE_STRONG_LINE))
            i += 1
            continue

        if re.match(r"^\*(.+)\*$", stripped):
            flush_paragraph()
            inner = re.match(r"^\*(.+)\*$", stripped).group(1)
            emit(Paragraph(inline_md(inner), STYLE_NOTE))
            i += 1
            continue

        para_buffer.append(stripped)
        i += 1

    flush_paragraph()
    end_group()
    return flowables


# ============================================================================
# Main
# ============================================================================

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(here, "Class_04_Homework.md")
    out_path = os.path.join(here, "Class_04_Homework.pdf")

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    flowables = build_flowables(md_text)

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
        title="Class 04 Homework — How Computers Represent Information",
        author="Bong Study Hub",
        subject="Foundation Batch 2026 — Class 04 Homework",
    )
    count = len(flowables)
    doc.build(flowables)
    print(f"Generated student homework PDF ({count} flowables) -> {out_path}")


if __name__ == "__main__":
    main()
