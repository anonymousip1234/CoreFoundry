# Class 02 — Pen-Tablet Board Plan

**Bong Study Hub — Foundation Batch 2026**
**How Machines Learn** — *From Rules → Data → Intelligence*
**Delivery format:** live online class, drawn on a digital pen tablet /
whiteboard surface (tool-agnostic — OneNote, Xournal++, Jamboard, Miro,
or equivalent all work; nothing below assumes a specific product)

This document is **Step 3** of Class 02's artifact chain:

```
class_metadata.md → Master Instructor Guide → Student Notes → THIS DOCUMENT
```

It does not invent teaching content. Every drawing, question, example,
and phrase below is derived from `01_Instructor_Guide/
Class_02_Master_Instructor_Guide.md` (primarily Section 26, "Pen-Tablet
Moments," cross-checked against Sections 10–19) and
`02_Student_Notes/Class_02_Student_Notes.md`. Where the Instructor Guide
gives the spoken teaching language, this document gives the **drawing
choreography** — what's on the board, in what order, and how it survives
across an online session.

**Non-negotiable terminology, used exactly as follows everywhere below:**

```
TRADITIONAL PROGRAMMING:   INPUT  →  HUMAN-WRITTEN RULES  →  OUTPUT
MACHINE LEARNING:          DATA   →  LEARNING  →  MODEL  →  PREDICTION
```

See Section 12, "Flagged Ambiguities," for one wording inconsistency
found in the source documents and how this Board Plan resolves it.

---

## 0. How to Use This Document

- The **Master Instructor Guide** remains the source of truth for
  spoken teaching language. This document tells you what to draw and
  when — it does not re-script what to say beyond short, board-specific
  prompts (`QUESTION` / `DRAW` / `SAY` / `CONNECT`).
- Six numbered drawings exist. **No seventh major drawing is
  introduced.** The Cats-vs-Dogs activity (Instructor Guide Section 15)
  is a reasoning activity, not a drawing — see Section 7 below for how
  the board supports it without becoming a seventh drawing.
- Drawing #4 (the Core Pipeline) is reused twice later in class
  (Prediction ≠ Certainty, AI Is Not Magic) instead of being redrawn —
  this is the single most important board-management decision in the
  whole class. Plan your canvas layout around keeping it retrievable.

---

## 1. Board & Tooling Setup

### 1.1 Canvas / Page Strategy

Use a **multi-page canvas** (most digital whiteboard tools support
pages, frames, or infinite-canvas zones). Recommended layout:

| Page / zone | Holds |
|---|---|
| **Page 1** | Drawing #1 — AI Around Us |
| **Page 2** | Drawing #2 — Traditional Programming, which grows into Drawing #3 — The Rule Problem on the *same* page (Drawing #3 is a direct escalation of Drawing #2's board, not a fresh page) |
| **Page 3 — "the anchor page"** | Drawing #4 — The Core Pipeline. **Do not reuse this page for anything else.** Keep it reachable with a single click/swipe from minute ~76 through minute ~107. |
| **Page 4** | Drawing #5 — AI / ML / Deep Learning / Generative AI map |
| **Page 5** | Drawing #6 — Return to the Learning Staircase |

If your tool doesn't support multiple pages, use distinct, well-spaced
regions of one large canvas and rely on zoom/pan instead — the
principle that matters is that **Drawing #4 must never be erased or
overwritten**, whatever the mechanism.

### 1.2 Color / Inking Guidance

Three functional colors, used for role, not decoration. The source
documents don't prescribe specific colors, so pick any three
high-contrast, readable-on-recording colors and hold these roles fixed
for the whole class:

| Role | Used for |
|---|---|
| **Primary** | All main structure — box outlines, arrows, core labels (DATA, LEARNING, MODEL, PREDICTION; INPUT, HUMAN-WRITTEN RULES, OUTPUT). |
| **Emphasis** | Anything a student said that's being written up live (a proposed rule, a named pattern, an answer to a question) — this visually separates "what the class produced" from "what the instructor pre-structured." |
| **Arrows / flow** | Directional arrows and the growth marks in Drawing #3 (the crowding rule list). Keeping arrows in one consistent color makes flow direction readable at a glance even in a small recording thumbnail. |

Do not add a fourth color "for variety" — a first-year, non-technical
class benefits from fewer visual decisions to parse, not more.

### 1.3 General Online Presentation Rules

- **Text size:** large enough to read in a 720p recording at normal
  laptop size — err on the side of too big rather than too small; you
  can always zoom out.
- **Zoom discipline:** zoom *in* while building a box-by-box drawing so
  handwriting stays legible; zoom *out* once a drawing is finished so
  students see the whole shape at once.
- **Crowding prevention:** once a page starts feeling full, that's the
  signal to move to the next page — never shrink text to fit more in;
  Drawing #3 is the one deliberate exception, where visual crowding
  is the *point* (see Section 5).
- **Pointing back to earlier pages:** say the page's name out loud
  before switching to it ("let's go back to the pipeline we built
  earlier") so students following the recording later aren't
  disoriented by a sudden jump.
- **Retention vs. clearing:** as a default, nothing gets erased mid
  class — pages accumulate. The only page that *must* survive
  untouched is Drawing #4's anchor page.

---

## 2. The Six Drawings — Overview

| # | Drawing | Class window (110-min canonical) | Duration | Live-build? | Retained until |
|---|---|---|---|---|---|
| 1 | AI Around Us | 19–31 min | 3–4 min (spread) | Yes | End of class (reference only) |
| 2 | Traditional Programming | 31–43 min | 2–3 min | Yes | Minute ~59 (feeds Drawing 3, then superseded by Drawing 4) |
| 3 | The Rule Problem / Rule Explosion | 43–59 min | 4–5 min (spread) | Yes | Through the Machine Learning pivot (~minute 62) |
| 4 | **The Core Pipeline** (HERO) | 70–78 min | 5–6 min | Yes | **Minute 107** (reused at Prediction ≠ Certainty and AI Is Not Magic) |
| 5 | AI / ML / Deep Learning / Generative AI Map | 99–104 min | 3–4 min | Yes | End of class (reference only) |
| 6 | Return to the Learning Staircase | 104–107 min | 2 min | Partial (callback) | End of class |

No dedicated drawing exists for Cats-vs-Dogs (78–90 min) — see Section 7.

---

## 3. Drawing #1 — AI Around Us

**Concept anchored:** AI already exists inside ordinary technology
students use daily — before any pipeline or mechanism is discussed.

**Class window:** 19–31 min (Instructor Guide Section 10 / 7.3).
**Source examples (use only these five, in this order):** spam
detection, recommendation systems, maps/navigation, face unlock,
generative AI (ChatGPT).

1. **What is already on the board:** Nothing — this is the first
   drawing of the class. Page 1 is blank except perhaps a light header
   already visible from a title slide.
2. **Question asked:** "Where have you noticed something 'smart' like
   this in an app you use daily?" (already asked once in the Opening —
   here it's re-anchored per example, one at a time: "Think about
   Google Maps picking a route — what is it looking at, and what does
   it hand back to you?")
3. **Expected student responses:** Netflix/YouTube/Spotify
   recommendations, Google Maps, ChatGPT, face unlock, spam folder
   sorting itself.
4. **What the instructor draws next:** A short header, "AI Around Us,"
   then **one line per example, added only as it comes up in
   discussion** — never all five pre-listed.
5. **What the instructor says while drawing:** For each example, jot
   at most two or three words per line — the example name plus,
   *if time allows*, a two-word "receives / produces" pair (e.g., "Spam
   filter — email → spam/not-spam"). Do not write full sentences.
6. **What should NOT be drawn yet:** No mechanism, no pipeline, no
   arrows connecting the five examples to each other — this drawing is
   a flat list, not a diagram. Do not draw logos or app icons that
   could look like an endorsement or a claim about proprietary
   internals.
7. **Final board state:** A five-line list, each line student-named,
   each with at most a short "receives → produces" tag.
8. **Approximate drawing time:** 3–4 minutes, spread across the ~12
   minute section (one line added per example as it's discussed, not
   all at once at the end).
9. **Concept anchored:** AI is already present in ordinary technology —
   sets up the "how does it actually do that?" curiosity the rest of
   the class answers.
10. **Reuse later in class:** Referenced verbally in Section 12 (Rule
    Problem) and Section 18 (Map) — "remember the five examples we
    listed" — but the page itself is not redrawn or added to again.

**Board layout suggestion:** left-aligned vertical list, generous line
spacing (this keeps it legible even if a student joins late and only
sees a thumbnail). Keep the whole list within one screen — no
scrolling required to see all five at once.

**Online notes:** small canvas footprint (roughly a quarter of the
page) — leave the rest of Page 1 blank in case a student's suggested
sixth example comes up in the 120-minute expanded version (Section
10.3). No zoom needed; this is a resting, easy-to-read page. Keep
visible for the rest of class as a scroll-back reference, but do not
actively point back to it except in passing.

**Drawing language:**
- **QUESTION:** "Where have you noticed something 'smart' like this in
  an app you use daily?"
- **DRAW:** One line per named example, student-driven order.
- **SAY:** "Receives [X], produces [Y]" — two or three words each side.
- **CONNECT:** "All five of these — none of them work by someone
  hand-writing a rule for every case. Let's see why that's hard,
  starting with one of these: spam."

---

## 4. Drawing #2 — Traditional Programming

**Concept anchored:** `INPUT → HUMAN-WRITTEN RULES → OUTPUT` — a human
thinks of the rule, the computer just follows it. Direct continuation
of Class 01's Input → Process → Output.

**Class window:** 31–43 min (Instructor Guide Section 11 / 7.4).
**Source example:** the spam filter, carried over from Drawing #1's
list.

1. **What is already on the board:** Page 2 starts blank.
2. **Question asked:** "If you were building a spam filter by hand,
   what's your first rule?"
3. **Expected student responses:** "If email contains 'free' → spam,"
   "if sender is unknown → spam," "if it has lots of exclamation marks
   → spam," "if it asks for money → spam."
4. **What the instructor draws next:** Three boxes and two arrows —
   `INPUT → HUMAN-WRITTEN RULES → OUTPUT` — drawn **empty** first, then
   filled: "Input" gets "a new email"; "Human-Written Rules" starts
   empty and fills live, one rule per student answer.
5. **What the instructor says while drawing:** As each rule is written
   into the middle box (in the emphasis color, since it's student-
   authored): "Someone had to think of and type in this exact rule."
6. **What should NOT be drawn yet:** No `if/else` syntax, no code
   formatting, no programming-language framing — every rule is written
   as a plain sentence (e.g., "contains 'you have won' → spam"), never
   as pseudocode. Do not fill in "Output" yet beyond the label
   "spam / not spam" — no worked numeric example is needed here.
7. **Final board state:** Three labeled boxes with 3–4 student-authored
   rules sitting inside the middle box, written as short plain-English
   lines, stacked.
8. **Approximate drawing time:** 2–3 minutes for the skeleton plus
   rule-collection woven through the rest of the ~12-minute section.
9. **Concept anchored:** In traditional programming, a **human**
   supplies the rule; the computer only follows it.
10. **Reuse later in class:** This exact box becomes the stress-test
    surface for Drawing #3 (below) — do not start a new page for the
    Rule Problem.

**Board layout suggestion:** left-to-right, generous horizontal
spacing between the three boxes — the middle "Human-Written Rules" box
should be visibly the largest of the three, since it's the one about to
fill up and then overflow in Drawing #3.

**Online notes:** center this on Page 2 with room below and to the
sides of the middle box — that empty space is deliberately reserved for
Drawing #3's crowding effect. Do not zoom in tightly yet; keep the
whole three-box skeleton in frame from the start so students see the
shape before it fills.

**Drawing language:**
- **QUESTION:** "What's your first rule?"
- **DRAW:** `INPUT → HUMAN-WRITTEN RULES → OUTPUT`, then each proposed
  rule as a line inside the middle box.
- **SAY:** "A human had to think of and write this rule."
- **CONNECT:** "Great start. Now let's throw some real emails at these
  rules and see how far they get us."

---

## 5. Drawing #3 — The Rule Problem / Rule Explosion

**Concept anchored:** hand-written rules become impractical — not
impossible, but unrealistic — once real-world variety and change are
introduced. "Rule explosion" is used only as the class's own informal
label for this feeling, exactly as framed in the Instructor Guide — not
a technical term.

**Class window:** 43–59 min (Instructor Guide Section 12 / 7.5) —
**non-negotiable, longest single teaching block in the class.**

1. **What is already on the board:** Drawing #2's three-box skeleton,
   with 3–4 rules already sitting in the middle box.
2. **Question asked, per counter-example:** "Does this new rule catch
   it?" / "Does it wrongly block this?" — then, once the list has
   visibly grown, the scaling question: "Roughly how many rules do you
   think we'd need for this to work well for millions of people, in
   multiple languages, against spammers who keep changing tactics?"
3. **Expected student responses:** Growing uncertainty as counter-
   examples land — "hundreds," "thousands," "it never really ends."
4. **What the instructor draws next:** One additional rule line per
   counter-example, **packed increasingly close together** inside and
   around the original "Human-Written Rules" box — let the list
   visibly crowd and spill toward the edges of the reserved space from
   Drawing #2. Use exactly the four counter-examples already
   established:
   - A real spam email that contains none of the flagged words (e.g.,
     "please review the attached document").
   - A genuine airline email that trips a rule ("Your booking is
     urgent — confirm now!").
   - A spam email using deliberate misspellings ("fr33", "amaz0n") or a
     different language.
   - A spammer who keeps changing their wording every week.
5. **What the instructor says while drawing:** After each new rule is
   crammed in: "And another one." Let the visual density do the
   persuading — avoid over-narrating the point before the board has
   made it visible.
6. **What should NOT be drawn yet:** No formal counting, no numbers or
   combinatorics on the board, no attempt to actually estimate a real
   number of rules — the crowding is felt, not calculated. Do not yet
   draw or hint at the Data → Learning → Model → Prediction pipeline;
   that reveal belongs entirely to Drawing #4.
7. **Final board state:** The original three-box skeleton, now with a
   visibly overcrowded, sprawling middle box — rules packed edge to
   edge, some at odd angles if space runs out, deliberately messy.
8. **Approximate drawing time:** 4–5 minutes, spread across the full
   16-minute section as counter-examples land one at a time.
9. **Concept anchored:** Real-world variety makes hand-written rules
   impractical at scale — the felt experience that motivates Machine
   Learning.
10. **Reuse later in class:** None directly — this page's job ends once
    the pivot question is asked and answered; the class moves to a
    fresh page (Drawing #4) rather than building on top of the
    crowded box.

**Board layout suggestion:** keep growing inside/around the same
footprint used in Drawing #2 rather than expanding onto a new area of
the page — the visual "running out of room" effect is part of the
teaching point.

**Online notes:** this is the one drawing where crowding is
intentional — do not fight it by shrinking text below readability. If
the box genuinely runs out of drawable space before all four
counter-examples land, that is itself a usable moment ("look — we've
already run out of room, and we're not even done") rather than a
problem to solve by zooming out. After the pivot question is asked, sit
with silence — do not draw anything for the 10–15 second wait time this
section calls for.

**Drawing language:**
- **QUESTION:** "Does this new rule catch it? Does it wrongly block
  this one?" → then: "Roughly how many rules would we need?"
- **DRAW:** One more crammed-in rule per counter-example.
- **SAY:** "And another one."
- **CONNECT (the pivot, said, not drawn):** "If humans cannot
  realistically write every rule, what could we give the computer
  instead?" — wait for an answer before touching the pen again.

---

## 6. Drawing #4 — The Core Pipeline (HERO DRAWING)

**Concept anchored:** `DATA → LEARNING → MODEL → PREDICTION` — the
single most important diagram in Class 02. This is the strongest visual
anchor of the whole class and the page that must survive, untouched,
the longest.

**Class window:** 70–78 min (Instructor Guide Section 14 / 7.7) —
**non-negotiable hero moment; never compress below 7 minutes.**

1. **What is already on the board:** A fresh page (Page 3, "the anchor
   page"). Nothing pre-drawn — this diagram must never appear finished
   before the live build.
2. **Question asked, one before each box:**
   - "What do we need to give the machine, if we're not giving it
     rules?"
   - "What happens to those examples next?"
   - "What do we get after that learning process finishes?"
   - "Now a brand-new email arrives, one the model has never seen —
     what happens?"
3. **Expected student responses, matching each question:** "Examples" /
   labeled emails → "it looks for patterns" / "it figures out what's
   common" → "something that learned the patterns" / "a model" →
   "it guesses" / "it predicts spam or not."
4. **What the instructor draws next, box by box, in order:**
   1. Write **DATA** alone.
   2. Draw the arrow, write **LEARNING**.
   3. Draw the arrow, write **MODEL**.
   4. Draw the arrow, write **PREDICTION**.
   Then, immediately below, redraw (or reveal) Drawing #2's chain —
   `INPUT → HUMAN-WRITTEN RULES → OUTPUT` — directly beneath it for a
   stacked side-by-side contrast.
5. **What the instructor says while drawing:** After each box lands,
   ground it in the running spam example before moving to the next
   question — Data = past labeled emails; Learning = finding patterns
   across them; Model = the trained spam filter; Prediction = spam /
   not-spam for a brand-new email. Once both chains are stacked: "Same
   basic shape — something goes in, something happens, something comes
   out. The difference is *who* decides the middle part: a human, or a
   learning process working from examples."
6. **What should NOT be drawn yet:** No training algorithms, no neural
   networks, no weights or parameters, no probability, confidence
   scores, accuracy, loss functions, or gradient descent — the diagram
   stays four labeled boxes and four arrows, nothing more.
7. **Final board state:** Two stacked four-part (and three-part) chains:
   ```
   TRADITIONAL PROGRAMMING:   INPUT  →  HUMAN-WRITTEN RULES  →  OUTPUT
   MACHINE LEARNING:          DATA   →  LEARNING  →  MODEL  →  PREDICTION
   ```
   with the spam-filter grounding words small and light beneath each
   Machine Learning box (Data → "past labeled emails," Learning →
   "finds patterns," Model → "trained filter," Prediction → "spam? /
   not spam?").
8. **Approximate drawing time:** 5–6 minutes for the build itself,
   within an 8-minute section.
9. **Concept anchored:** The core pipeline, and its direct contrast
   with traditional programming — the intellectual backbone of the
   entire class.
10. **Reuse later in class — this is the critical instruction for this
    drawing:**
    - **Prediction ≠ Certainty (90–95 min):** do not create a new
      drawing. Return to this page, point at the **PREDICTION** box,
      and say the distinction there — "that's exactly this box: a best
      guess, not a guarantee." No new marks are required; at most,
      circle the word PREDICTION for emphasis.
    - **AI Is Not Magic (95–99 min):** return to the same page again.
      Point at the **DATA** box and annotate lightly (small arrow or
      note near the box, not a redraw): "if this is limited, everything
      downstream is too." This is the only new ink this page receives
      after its initial build.

**Board layout suggestion:** stack the two chains vertically, left-
aligned, with identical box widths where possible so the visual
parallel (input-like box under input-like box) is immediate. Leave a
small margin below the Machine Learning chain for the two light
annotations added later (Prediction circle, Data note) — don't crowd
this page the way Drawing #3 was allowed to crowd.

**Online notes:** this page needs the most generous canvas real estate
in the whole class and must be reachable in one click/swipe for the
next ~30 minutes of teaching. Zoom in for the box-by-box build (so
handwriting is legible), then zoom out to show the full two-chain
contrast once both are complete — that zoomed-out view is the shot
worth holding on screen the longest. Do **not** clear or reuse this
page for anything else before minute 107.

**Drawing language:**
- **QUESTION (×4, one per box):** "What do we need to give the
  machine?" → "What happens to those examples next?" → "What do we get
  after learning?" → "What happens with a brand-new email?"
- **DRAW:** DATA → LEARNING → MODEL → PREDICTION, one box at a time;
  then the Input/Rules/Output chain stacked beneath it.
- **SAY:** Ground every box in the spam example before moving on.
- **CONNECT:** "Same shape as before — the difference is who fills in
  the middle."

---

## 7. Note on Cats-vs-Dogs (78–90 min) — No Dedicated Drawing

Per the Instructor Guide (Section 15) and this task's own instruction,
Cats-vs-Dogs is a **facilitated reasoning activity**, not a drawing
moment, and must not be replaced or diluted by one. The board's role
here is minimal and optional:

- If useful, jot the **patterns students name** (ear shape, size, face
  shape, tail, posture) as a short word list on a scratch area of Page
  3 or a small new area — this is optional, light-touch, and not one of
  the six numbered drawings.
- **Do not** draw a new pipeline for cats-vs-dogs — instead, verbally
  point back to Drawing #4's anchor page and trace the same four boxes
  with the cat/dog framing (Data = labeled photos, Learning = noticing
  patterns, Model = "what you now have in your head," Prediction =
  the guess on the new photo). No new ink is required for this trace.
- Keep this activity's board footprint small enough that it doesn't
  compete with or crowd Drawing #4's page.

---

## 8. Drawing #5 — AI / ML / Deep Learning / Generative AI Map

**Concept anchored:** a simple broad-to-narrow orientation map — **not**
a technical taxonomy. Students do not need to memorize formal
definitions of any of the four terms.

**Class window:** 99–104 min (Instructor Guide Section 18 / 7.11).

1. **What is already on the board:** Page 4 starts blank.
2. **Question asked:** Before placing the Generative AI marker: "Where
   do you think ChatGPT belongs on this map?"
3. **Expected student responses:** Mixed guesses — "inside AI,"
   "inside Machine Learning," "its own separate thing" (the last one is
   a useful misconception to gently correct in the moment).
4. **What the instructor draws next, ring by ring:**
   1. One large circle, labeled **Artificial Intelligence**.
   2. A smaller circle inside it, **Machine Learning**.
   3. A smaller circle inside that, **Deep Learning**.
   4. A star or marker placed near the Machine Learning / Deep Learning
      boundary, labeled **Generative AI**, drawn explicitly touching
      both rather than strictly nested inside either.
5. **What the instructor says while drawing:** Name each ring as it's
   drawn: "AI is the broad field. Machine Learning — what we spent
   today on — is one major approach inside it. Deep Learning is a more
   powerful style of machine learning, for very complex patterns like
   images and language." Once the Generative AI marker is placed: "This
   is a map to help you get oriented, not a diagram to memorize."
6. **What should NOT be drawn yet:** No neural-network architecture, no
   transformers, no LLM internals, no embeddings or tokens — Generative
   AI gets a label and a position, nothing about its mechanism.
7. **Final board state:** Three concentric rings (AI ⊃ ML ⊃ Deep
   Learning) with a Generative AI marker sitting at the ML/Deep
   Learning boundary.
8. **Approximate drawing time:** 3–4 minutes, within a 5-minute
   section.
9. **Concept anchored:** Orientation among AI, Machine Learning, Deep
   Learning, and Generative AI — broad to narrow, not a taxonomy to
   memorize.
10. **Reuse later in class:** None — this page stands alone as a
    reference; it is not redrawn in Section 9 (Staircase).

**Board layout suggestion:** center the nested circles; leave the
Generative AI star clearly outside the innermost ring's crowding but
visibly touching the middle two rings' boundary, so its "not strictly
nested" positioning is legible at a glance.

**Online notes:** build ring by ring with a brief pause and question
between each — do not zoom in tight during this drawing, since the
nesting relationship only reads clearly at a zoomed-out view. Keep it
on screen for the full explanation; no need to retain it actively
afterward beyond normal scroll-back.

**Drawing language:**
- **QUESTION:** "Where do you think ChatGPT belongs on this map?"
- **DRAW:** Three nested circles, then a boundary-straddling star for
  Generative AI.
- **SAY:** "This is a map to help you get oriented, not a diagram to
  memorize."
- **CONNECT:** "Now that you've got the map, let's zoom out to where
  today's whole lesson fits in the bigger program."

---

## 9. Drawing #6 — Return to the Learning Staircase

**Concept anchored:** Class 02 is a conceptual preview from the top of
Class 01's staircase, looking down — not a new curriculum diagram, and
not a signal that any step is being skipped.

**Class window:** 104–107 min (Instructor Guide Section 19 / 7.12).

1. **What is already on the board:** Page 5 starts blank. Drawing #4's
   page (Page 3) remains reachable but is not currently displayed.
2. **Question asked:** None required — this section is a callback and
   a connective statement more than a live-reasoning moment; if useful,
   a light rhetorical check works: "Which chain have we been building
   all class?"
3. **Expected student responses:** "Data → Learning → Model →
   Prediction."
4. **What the instructor draws next:** A quick staircase — eight
   ascending steps, one label per step, drawn as a **fast callback**,
   not a slow live-build (Class 01 already did the slow version):
   `Programming → Computer Science → Mathematics → Data → Machine
   Learning → Deep Learning → LLMs → Agents`.
5. **What the instructor says while drawing:** "We gave you a preview of
   where this staircase leads. We are not skipping the steps
   underneath it." Once drawn: "We are not skipping the steps. We are
   learning where the staircase leads."
6. **What should NOT be drawn yet:** No month numbers, no course names —
   that roadmap detail belongs to Class 01, not here. Do not turn this
   into a new, slower teaching moment; it should feel visibly quicker
   than Class 01's original construction of the same staircase.
7. **Final board state:** The eight-label staircase, drawn quickly, no
   embellishment.
8. **Approximate drawing time:** 2 minutes.
9. **Concept anchored:** Continuity with Class 01; today was a preview,
   not a shortcut.
10. **Reuse later in class:** None — this closes directly into the
    Recap.

**On the optional Traditional-vs-ML comparison callback:** the source
material allows including a final side-by-side reminder of the two
pipelines here, "only if it can be done without overcrowding the
board." Given the 2-minute window available in the canonical 110-minute
plan, **this Board Plan's recommendation is: do not redraw it.**
Instead, verbally point back to Drawing #4's still-live anchor page
(Page 3) for that final reminder — "and remember, that's this chain
right here" (swipe to Page 3, point, swipe back). This satisfies the
comparison without a second drawing, without overcrowding Page 5, and
without spending time re-inking something already on screen elsewhere.
Only redraw it from scratch if Drawing #4's page is, for some reason,
no longer reachable.

**Board layout suggestion:** a simple ascending staircase, left to
right and bottom to top, one label per step — no need for the
photorealistic staircase shape Class 01 may have used; simple ascending
blocks or a diagonal line with labels are sufficient here since this is
a callback, not a first introduction.

**Online notes:** small canvas footprint, quick to draw, no zoom
choreography needed beyond making sure all eight labels are legible at
once. If time allows (see Section 10.3, 120-minute version), you may
briefly swipe to Drawing #4's page as described above; otherwise this
page and the verbal callback are sufficient.

**Drawing language:**
- **QUESTION (optional):** "Which chain have we been building all
  class?"
- **DRAW:** Eight-step staircase, quickly, no new detail beyond Class
  01's original.
- **SAY:** "We are not skipping the steps. We are learning where the
  staircase leads."
- **CONNECT:** Straight into the Recap — no further drawing.

---

## 10. Timing Guidance

### 10.1 Canonical 110-Minute Plan (primary reference)

| Drawing | Window | Duration |
|---|---|---|
| #1 AI Around Us | 19–31 min | 3–4 min |
| #2 Traditional Programming | 31–43 min | 2–3 min |
| #3 The Rule Problem | 43–59 min | 4–5 min |
| *(Cats-vs-Dogs — no drawing)* | 78–90 min | — |
| #4 Core Pipeline *(hero)* | 70–78 min | 5–6 min |
| *(Prediction ≠ Certainty — reuse #4)* | 90–95 min | pointer only |
| *(AI Is Not Magic — reuse #4)* | 95–99 min | pointer + 1 light annotation |
| #5 AI/ML/DL/GenAI Map | 99–104 min | 3–4 min |
| #6 Staircase | 104–107 min | 2 min |

### 10.2 90-Minute Compressed Guidance

Per the Instructor Guide's 90-minute version (Section 29), timing
windows shift earlier and tighten, but **every drawing still happens** —
compression comes from spoken content and counter-example count, not
from cutting a diagram:

- **Drawing #1:** shift to roughly 14–23 min; use 3 examples instead of
  5 (spam, recommendations, face unlock) — draw only those three lines.
- **Drawing #2:** roughly 23–33 min; cap rule collection at 3 rules
  instead of an open-ended count — the three-box skeleton is unchanged.
- **Drawing #3:** roughly 33–46 min; use 3 escalating counter-examples
  instead of 4 — the crowding effect still needs to visibly land, just
  with slightly less packed-in text. **Do not compress this below a
  genuinely crowded-looking box** — the felt struggle is non-negotiable.
- **Drawing #4:** roughly 54–61 min; **build sequence and final state
  are unchanged** — this is the one drawing this Board Plan will not
  let you trim further; if you are behind schedule anywhere else,
  protect this drawing's full 5–6 minutes.
- **Cats-vs-Dogs:** roughly 61–71 min, no drawing, full core sequence
  preserved, extension round dropped.
- **Drawing #5:** roughly 78–84 min, unchanged build sequence.
- **Drawing #6:** roughly 84–87 min, unchanged (quick callback either
  way).

If you are still over time after Drawing #3, the Instructor Guide's
permitted further cut is to deliver Drawing #5 as a **spoken** map
instead of a live-drawn one — not to touch Drawing #4 or the Recap.

### 10.3 120-Minute Expanded Guidance

Per the Instructor Guide's 120-minute version (Section 30), the extra
10 minutes go entirely to **interaction and reasoning time around the
existing drawings** — no new drawings, no new technical content:

- **Drawing #1:** allow one extra student-suggested example if the
  class proposes a sixth one naturally (roughly 20–34 min window) — add
  it as a sixth line, same format as the other five.
- **Drawing #3:** allow slightly more time between counter-examples so
  the crowding builds more slowly and more visibly (roughly 46–64 min
  window) — same four counter-examples, just paced out further.
- **Drawing #4:** same build sequence, but draw slightly more slowly,
  with a longer pause after each question — do not add a fifth box or
  any technical detail.
- **Drawing #5:** allow 1–2 extra "where does X belong?" questions
  (e.g., self-driving cars, voice assistants) before finalizing the
  Generative AI marker — same three-ring structure, no new rings.
- **Drawing #6:** if time genuinely allows, this is the one place where
  redrawing the Traditional-vs-ML comparison next to the staircase
  (rather than pointing back to Page 3) becomes reasonable — but only
  if it demonstrably doesn't crowd Page 5.

---

## 11. Board State Management Summary

| Drawing | Start state | Build | Final state | Retention | Clear / transition |
|---|---|---|---|---|---|
| #1 | Blank page | One line per named example | 5-line flat list | Kept for scroll-back all class | Never actively cleared |
| #2 | Blank page | 3-box skeleton, rules filled live | 3 boxes, 3–4 rules inside middle box | Kept until Drawing #3 absorbs it | Superseded (not erased) once Drawing #4 opens |
| #3 | Drawing #2's board | Rules crammed in per counter-example | Visibly overcrowded middle box | Kept through the ML pivot (~min 62) | New page opened for Drawing #4; this page not reused |
| #4 | Blank page (dedicated) | Box-by-box, then stacked contrast with Drawing #2's chain | Two stacked chains + spam-example annotations | **Kept live from minute 70 to minute 107** | Only after the Staircase section closes |
| #5 | Blank page | Ring by ring, then GenAI marker | 3 nested circles + boundary star | Kept for scroll-back all class | Never actively cleared |
| #6 | Blank page | Quick 8-step staircase | Full staircase, no embellishment | Kept through Recap | Class ends |

---

## 12. Quality Assurance

### Source Alignment
- [x] `00_Class_Metadata/class_metadata.md` read (this and prior
      sessions in this conversation).
- [x] `README.md` read.
- [x] `01_Instructor_Guide/Class_02_Master_Instructor_Guide.md` read in
      full, including Section 26 (Pen-Tablet Moments) and the
      section-by-section teaching guide (Sections 7–22) that each
      drawing above is drawn from.
- [x] `02_Student_Notes/Class_02_Student_Notes.md` read in full and
      cross-checked for terminology and example consistency.

### Sequence Alignment
Confirmed: all six drawings occur in the instructional order set by the
Instructor Guide's Class-at-a-Glance table — AI Around Us → Traditional
Programming → The Rule Problem → (Introducing ML, spoken only) → Core
Pipeline → (Cats-vs-Dogs, no drawing) → (Prediction ≠ Certainty / AI Is
Not Magic, both reuse Drawing #4) → AI/ML/DL/GenAI Map → Return to the
Staircase. No drawing appears out of order and no drawing is introduced
that the Instructor Guide doesn't already name.

### Terminology Alignment
Confirmed exact, consistent use throughout this document of:
- `INPUT → HUMAN-WRITTEN RULES → OUTPUT`
- `DATA → LEARNING → MODEL → PREDICTION`
- Artificial Intelligence, Machine Learning, Deep Learning, Generative
  AI (used only as broad-to-narrow orientation terms, never given
  formal technical definitions)
- "Learning Staircase" (used exactly as named in the Instructor Guide
  and Student Notes)

### Scope Alignment
Confirmed this Board Plan does **not** direct the instructor to teach or
draw: Python or programming syntax, neural-network mathematics,
gradient descent, optimization, transformers, embeddings, RAG, agents
(named only as a future staircase-step label, never explained),
formal probability, accuracy/precision/recall, model-training
implementation, or deep AI ethics. Every "do not draw" list above was
checked against the Instructor Guide's own deferred-topics list and
matches it.

### Visual Alignment
- [x] All six drawings are live-build oriented (Drawing #6 is
      explicitly framed as a *fast* callback rather than a slow build,
      per the Instructor Guide's own instruction that it should "feel
      like a callback to Class 01, not a new curriculum diagram").
- [x] No drawing duplicates content already carried by a slide — Section
      27 of the Instructor Guide keeps slides to icons/images only, and
      nothing here asks the instructor to reproduce slide text on the
      board.
- [x] All drawings specify large text, minimal words, and online-legible
      layout.
- [x] The Core Pipeline (Drawing #4) is treated as the strongest visual
      anchor — it receives the most protected screen time, the only
      guaranteed non-erasure across the whole class, and both later
      reuse moments.
- [x] No unnecessary seventh major drawing was introduced — Cats-vs-Dogs
      is explicitly handled as a non-drawing activity (Section 7).

### Instructor Usability
A different qualified instructor could run this class's live drawings
from this document alone, without needing to invent layout, timing, or
sequencing decisions themselves — every drawing specifies its starting
state, build order, final state, retention window, and the exact
question/say/connect language to pair with it. Spoken teaching detail
beyond that remains the Master Instructor Guide's job, as intended.

### Flagged Ambiguities / Resolutions

**One genuine wording inconsistency exists in the source documents**
and is flagged here rather than silently resolved:

- The Instructor Guide itself uses **both** `INPUT → RULES → OUTPUT`
  (Sections 13, 14's ASCII contrast, and its own Drawing 2 spec in
  Section 26) **and** `INPUT → HUMAN-WRITTEN RULES → OUTPUT` (Section 3
  and its Section 14 prose). The Student Notes use the long form as the
  primary displayed pipeline (Sections 5, 9) and the short form only
  once, in the single-line "Everyday Mental Model" summary.
- **This Board Plan's resolution:** since this task's instructions state
  the traditional pipeline "MUST remain `INPUT → HUMAN-WRITTEN RULES →
  OUTPUT`," every drawing above (Drawing #2, and Drawing #4's stacked
  contrast) uses the **long form** consistently, on the board, at all
  times. The short form is not used anywhere in this document. This is
  a labeling choice only — the taught concept (a human supplies the
  rule) is identical either way — but it's worth the Instructor Guide
  author reconciling the short/long form split there in a future
  revision, since a student comparing their notes to the live board
  should never see two different labels for the same box.
- No other missing, ambiguous, or inconsistent content was found across
  the four source documents for this drawing set.
