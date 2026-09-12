# -*- coding: utf-8 -*-
"""
generate_student_notes_pdf.py

Generates Class_04_Student_Notes.pdf directly from Class_04_Student_Notes.md.

Parses the actual Markdown file (headings, paragraphs, tables, code/
diagram blocks, bullet/numbered lists, blockquote callouts, and the
`<!-- PAGE BREAK -->` directive) into ReportLab flowables, rather than
re-typing the notes a second time anywhere. The Markdown file remains
the single source of truth; this script only renders it.

Reuses the same font-registration approach, color palette, and general
parsing strategy as Class 03's
`02_Student_Notes/generate_student_notes_pdf.py` (and its Homework
generator before that), so the whole program's PDFs read as one visual
identity.

Usage:
    python generate_student_notes_pdf.py

Re-run whenever Class_04_Student_Notes.md changes.
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
    HRFlowable, KeepTogether, PageBreak,
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

# ============================================================================
# Palette - matches the Class 03 Presentation and Homework, so the whole
# class's artifacts read as one visual identity.
# ============================================================================

NAVY = colors.HexColor("#1E3A72")
BLUE = colors.HexColor("#2A5CB8")
CYAN = colors.HexColor("#22C7E0")
INK = colors.HexColor("#1F2733")
MUTED = colors.HexColor("#647085")
CARD_BG = colors.HexColor("#EEF3FB")
CARD_BORDER = colors.HexColor("#C7D6EC")
CYAN_BG = colors.HexColor("#E4F9FB")
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
    "Note", fontName="Body-Italic", fontSize=10.5, leading=14,
    textColor=MUTED, spaceBefore=1, spaceAfter=10)
STYLE_H2 = ParagraphStyle(
    "H2", fontName="Body-Bold", fontSize=14.5, leading=18,
    textColor=NAVY, spaceBefore=16, spaceAfter=6)
STYLE_H3 = ParagraphStyle(
    "H3", fontName="Body-Bold", fontSize=11.8, leading=15,
    textColor=BLUE, spaceBefore=10, spaceAfter=5)
STYLE_BODY = ParagraphStyle(
    "Body", fontName="Body", fontSize=10.4, leading=15.5,
    textColor=INK, spaceAfter=7)
STYLE_BULLET = ParagraphStyle(
    "Bullet", parent=STYLE_BODY, leftIndent=14, firstLineIndent=-14,
    spaceAfter=4)
STYLE_NUMBERED = ParagraphStyle(
    "Numbered", parent=STYLE_BODY, leftIndent=18, firstLineIndent=-18,
    spaceAfter=5)
STYLE_QUOTE = ParagraphStyle(
    "Quote", fontName="Body", fontSize=10.6, leading=15.5, textColor=NAVY,
    spaceAfter=0)
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
    text = re.sub(r"`(.+?)`", r'<font face="Mono" color="#1E3A72">\1</font>', text)
    text = re.sub(r"~~(.+?)~~", r"<strike>\1</strike>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<i>\1</i>", text)
    return text


# ============================================================================
# Small flowable builders
# ============================================================================

def code_box(text):
    p = Paragraph(escape_xml(text).replace("\n", "<br/>"),
                   ParagraphStyle("Mono", fontName="Mono", fontSize=10.5,
                                   leading=16, textColor=NAVY,
                                   alignment=1))
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 0.75, CARD_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]


def quote_box(text):
    """A callout box for blockquotes (definitions, 'Think about it',
    'Remember') - light card fill with a cyan accent bar on the left,
    matching the presentation's callout treatment."""
    p = Paragraph(inline_md(text), STYLE_QUOTE)
    t = Table([[p]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 3.5, CYAN),
        ("BOX", (0, 0), (-1, -1), 0.75, CARD_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
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
    return [Spacer(1, 4), t, Spacer(1, 8)]


# ============================================================================
# Markdown -> flowables
# ============================================================================

def build_flowables(md_text):
    lines = md_text.split("\n")
    flowables = []
    para_buffer = []

    def flush_paragraph():
        if para_buffer:
            text = " ".join(para_buffer).strip()
            para_buffer.clear()
            if text:
                flowables.append(Paragraph(inline_md(text), STYLE_BODY))

    def gather_continuation(idx):
        """Soft-wrapped continuation lines belonging to the list item that
        starts at `idx - 1`."""
        texts = []
        while idx < n:
            nxt = lines[idx].strip()
            if nxt == "" or nxt.startswith(("#", "```", "|", "<!--", "- ", ">")) \
                    or re.match(r"^\d+\.\s", nxt):
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
            if "PAGE BREAK" in stripped:
                flowables.append(PageBreak())
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
            flowables.extend(code_box("\n".join(code_lines)))
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table_lines = []
            while i < n and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            flowables.extend(data_table(table_lines))
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote_lines = []
            while i < n and lines[i].strip().startswith(">"):
                q = lines[i].strip()[1:].strip()
                quote_lines.append(q)
                i += 1
            flowables.extend(quote_box(" ".join(quote_lines)))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            flowables.append(Paragraph(inline_md(stripped[2:]), STYLE_TITLE))
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            flowables.append(Paragraph(inline_md(stripped[4:]), STYLE_H3))
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            flowables.append(Paragraph(inline_md(stripped[3:]), STYLE_H2))
            flowables.append(HRFlowable(width="100%", thickness=1.4,
                                          color=CYAN, spaceBefore=0,
                                          spaceAfter=8))
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            first = stripped[2:].strip()
            cont, i = gather_continuation(i + 1)
            text = " ".join([first] + cont)
            flowables.append(Paragraph("•&nbsp;&nbsp;" + inline_md(text),
                                         STYLE_BULLET))
            continue

        if re.match(r"^\d+\.\s", stripped):
            flush_paragraph()
            cont, i = gather_continuation(i + 1)
            text = " ".join([stripped] + cont)
            flowables.append(Paragraph(inline_md(text), STYLE_NUMBERED))
            continue

        if re.match(r"^\*\*(.+)\*\*$", stripped):
            flush_paragraph()
            inner = re.match(r"^\*\*(.+)\*\*$", stripped).group(1)
            flowables.append(Paragraph(inline_md(inner), STYLE_STRONG_LINE))
            i += 1
            continue

        if re.match(r"^\*(.+)\*$", stripped):
            flush_paragraph()
            inner = re.match(r"^\*(.+)\*$", stripped).group(1)
            flowables.append(Paragraph(inline_md(inner), STYLE_NOTE))
            i += 1
            continue

        para_buffer.append(stripped)
        i += 1

    flush_paragraph()
    return flowables


# ============================================================================
# Main
# ============================================================================

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(here, "Class_04_Student_Notes.md")
    out_path = os.path.join(here, "Class_04_Student_Notes.pdf")

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    flowables = build_flowables(md_text)

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
        title="Class 04 Student Notes — How Computers Represent Information",
        author="Bong Study Hub",
        subject="Foundation Batch 2026 — Class 04 Student Notes",
    )
    count = len(flowables)
    doc.build(flowables)
    print(f"Generated student notes PDF ({count} flowables) -> {out_path}")


if __name__ == "__main__":
    main()
