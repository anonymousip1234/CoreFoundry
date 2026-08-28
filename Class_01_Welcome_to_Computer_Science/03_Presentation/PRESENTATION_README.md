# Class 01 Presentation — README

**Bong Study Hub — Foundation Batch 2026 · Welcome to Computer Science**

This deck is the **visual spine** of Class 1, not the lecture. Many slides
are deliberately near-blank — the instructor builds the actual concept
live on a pen tablet, and the slide either sets up the question or shows
a clean reference *after* the live drawing. See "How Live-Board Moments
Work" below before presenting this deck for the first time.

---

## 1. How to Regenerate

```
cd Class_01_Welcome_to_Computer_Science/03_Presentation
pip install python-pptx
python generate_presentation.py
```

This overwrites `Class_01_Welcome_to_Computer_Science.pptx` in place.
There is no build cache or intermediate step — the script is the single
source of truth for the deck's content and design.

## 2. Dependencies

- Python 3.8+
- `python-pptx` (`pip install python-pptx`) — the only third-party
  dependency.
- No internet access, fonts, or external assets are required at
  generation time.

**Fonts:** the deck specifies **Aptos Display** (large titles/statements)
and **Aptos** (everything else) — both ship with current Windows/
Microsoft 365 installs. If Aptos isn't
installed on the machine that *opens* the deck, PowerPoint substitutes a
default font automatically — nothing breaks, text just renders in
whatever the system's default sans-serif is. **Arial** is the documented
fallback if you want to force a specific substitute. All text remains
fully editable either way; nothing is rasterized.

## 3. Design System

Defined once, at the top of `generate_presentation.py`, and used
everywhere else — never hard-coded per slide.

| Token | Value | Use |
|---|---|---|
| `NAVY` | `#1E3A72` | Primary — section-divider/title backgrounds, headings |
| `BLUE` | `#2A5CB8` | Secondary — kickers, arrows, links between ideas |
| `CYAN` | `#22C7E0` | Accent — used sparingly: progress dots, one highlight per diagram, homework badges |
| `INK` / `MUTED` | `#1F2733` / `#647085` | Body text / secondary text |
| `LIGHT_BG` / `CARD_BG` / `CYAN_BG` | near-white / light navy tint / light cyan tint | Slide and card backgrounds |
| `AMBER` | `#C2790F` | Reserved, unused in this deck (kept for consistency with the Board Plan's 3-color system if a future slide needs a warning beat) |

This is the **same palette used in the Class 01 Student Notes PDF**
(`02_Student_Notes/`), so the whole program's materials read as one
visual identity, not four separately-designed documents.

**Fonts:** `FONT_DISPLAY = "Aptos Display"` for large titles/statements,
`FONT_BODY = "Aptos"` for everything else. Change these two constants to
re-theme the whole deck's typography.

**Canvas:** 16:9 widescreen, `13.333in × 7.5in`, `MARGIN = 0.7in` on all
sides.

**To change the theme:** edit the constants block at the top of the file
(§1 "Theme Configuration") — every component reads from these constants,
so a palette or font change there propagates everywhere automatically.

## 4. Slide-Layout Component Library

Eleven reusable layout functions (§3 in the script), each usable on any
slide that needs that shape of content:

1. `layout_title` — the opening title slide.
2. `layout_section_divider` — full-bleed navy statement slide (used for
   the Tea Activity intro).
3. `layout_big_question` — large centered question, no answer.
4. `layout_concept_explanation` — short title + statement or a few
   bullets.
5. `layout_two_column` — comparison cards with a connecting arrow
   (Coding vs. CS, Algorithm vs. Program).
6. `layout_diagram` — title + a content-aware diagram + optional caption.
7. `layout_full_screen_visual` — minimal chrome, diagram dominates (the
   button-press flow).
8. `layout_activity` — tagged "ACTIVITY" prompt card.
9. `layout_roadmap` — N horizontal cards (the 4-month journey).
10. `layout_recap` — numbered or bulleted short-statement list.
11. `layout_homework` — closing navy slide with two columns.

Below that sit **content-aware diagram builders** (§4) — `draw_pipeline`,
`draw_cs_map`, `draw_quadrants`, `draw_staircase`,
`draw_stacked_pipelines`, `draw_vertical_flow`, `draw_three_words_cards`,
`draw_mcq`, `draw_single_word` — each returns a function
`(slide, x, y, w, h) -> None` that `layout_diagram` / `layout_full_screen_visual`
call, so the same diagram shape can be reused at any size.

## 5. Slide Structure (29 slides)

| # | Slide | Layout used | Mode |
|---|---|---|---|
| 1 | Title | `layout_title` | — |
| 2 | Opening Question | `layout_big_question` | Ask |
| 3 | What is Computer Science? | `layout_big_question` | Discuss |
| 4 | CS ≠ Coding | `layout_two_column` | Explain |
| 5 | The Computer Science Map | `layout_diagram` | **Live-board reference** |
| 6 | Quick Question | `layout_big_question` | Ask |
| 7 | What Happens When You Press a Button? | `layout_full_screen_visual` | Hook (optional, cut first under time pressure) |
| 8 | Three Words | `layout_diagram` | Reference |
| 9 | Quick Check (MCQ) | `layout_diagram` | Ask |
| 10 | Input → Process → Output | `layout_diagram` | **Live-board reference** |
| 11 | Your Turn | `layout_activity` | Pair activity |
| 12 | The Big Question | `layout_big_question` | Ask |
| 13 | The Core Pipeline (PROBLEM anchor) | `layout_diagram` | **Live-board anchor** |
| 14 | The Core Pipeline (clean reference) | `layout_diagram` | **Live-board reference** |
| 15 | Build an Algorithm | `layout_activity` | Ask |
| 16 | The Algorithm | `layout_recap` | Reference |
| 17 | Algorithm ≠ Program | `layout_two_column` | Explain |
| 18 | Computational Thinking | `layout_diagram` | **Live-board reference** |
| 19 | Live Thinking Prompt | `layout_big_question` | Ask |
| 20 | Teach a Computer How to Make Tea | `layout_section_divider` | **Activity — not spoiled** |
| 21 | The Lesson from Tea | custom (navy statement) | Key statement |
| 22 | Three Ways to Compute | `layout_diagram` | **Live-board reference** |
| 23 | Quick Question ("What changed?") | `layout_big_question` | Ask |
| 24 | The Learning Staircase | `layout_diagram` | **Live-board reference** |
| 25 | Why Not Start With Agents? | custom (Q + reveal) | Reflect |
| 26 | Your 4-Month Journey | `layout_roadmap` | Reference |
| 27 | What You Should Know Today | `layout_recap` | Reference |
| 28 | Exit Check | `layout_recap` | Ask |
| 29 | Homework | `layout_homework` | Close |

Six extra slides beyond the ~22–28 target come from treating the Core
Pipeline as an anchor slide (13) *plus* a post-drawing clean reference
(14) — see §6 below on why this isn't a duplicate.

## 6. How Live-Board Moments Work

Six concepts are drawn live on the pen tablet, per
`04_Pen_Tablet/Class_01_Pen_Tablet_Board_Plan.md`. For each one, this
deck follows one of two patterns:

- **Anchor pattern** (Slide 13, "PROBLEM"): the slide shows only the
  starting word before the instructor builds the rest live — matches the
  Board Plan's "slide state before drawing: Nothing" instruction almost
  exactly, while still giving the instructor a visual anchor to open on.
- **Reference pattern** (Slides 5, 10, 14, 18, 22, 24): the slide shows
  the finished, clean version of a diagram — but it is meant to be
  displayed **after** the live drawing is complete, as a callback/
  recap aid, never as a replacement for building it live. Speaker notes
  on every one of these slides say explicitly:

  > `[LIVE BOARD] — instructor draws this concept.`

**Practical rule for presenting:** don't advance to a reference slide
until the live drawing on the tablet is finished. Advancing early shows
students the answer before they've built it, which defeats the entire
point of the Board Plan's progressive-reveal design.

## 7. Which Slides Are Interactive

Every slide with a `[ASK]`, `[DISCUSS]`, `[ACTIVITY]`, or
`[CHECK UNDERSTANDING]` marker in its speaker notes expects a pause for
student response before advancing. That's 17 of the 29 slides — roughly
matching the "avoid a 110-minute monologue" instruction. The remaining
slides are calm reference/explanation beats (vocabulary, the roadmap,
homework) by design — see `05_Interaction/05_Classroom_Interaction_Flow.md`
for the exact minute-by-minute interaction map this deck was built to
match.

**Interaction markers live only in speaker notes — never on the visible
slide.** To see them: View → Notes Page in PowerPoint, or the Notes pane
in Normal view.

## 8. Speaker Notes Format

Every slide's notes follow the same structure (only populated fields
appear):

```
[MARKERS]
TIME: n min
Purpose: why this slide exists
Say: what the instructor should say (a reminder, not a script)
Ask: the question to pose
Expected: what students typically answer
Board: what happens on the pen tablet, if anything
Transition: the bridging line into the next slide
```

## 9. Known Rendering Note

This environment has no working PowerPoint COM automation or LibreOffice
available for visual QA rendering, so all visual QA for this deck was
performed with a purpose-built, geometry-accurate Pillow renderer that
reads the actual shapes, positions, colors, and text runs out of the
saved `.pptx` file (not a reinterpretation of the design). It substitutes
Calibri for Aptos (not installed on the QA machine) — sizes, weights,
colors, and positions are exact. The file itself specifies Aptos/Aptos
Display throughout and will render in those fonts on any machine that has
them.

## 10. Editing This Deck

- **Content changes:** edit the relevant `slide_NN_*` function in §5 of
  the script. Each one is short and self-contained.
- **New diagram type:** add a `draw_*` function in §4 that matches the
  `(slide, x, y, w, h) -> None` signature, then pass it to
  `layout_diagram` or `layout_full_screen_visual`.
- **Reordering slides:** edit the `SLIDE_BUILDERS` list at the bottom of
  the file — it's the single ordered list the whole deck is built from.
- **After any edit:** re-run `python generate_presentation.py`, then
  spot-check the changed slide(s) — a lightweight way to do this without
  PowerPoint installed is to adapt the QA renderer approach described in
  §9 (read shapes via `python-pptx`, rasterize with Pillow).

Do not redesign the lesson itself when editing this file — content must
stay consistent with the Instructor Guide, Student Notes, Board Plan, and
Interaction Pack in the sibling folders of this class.
