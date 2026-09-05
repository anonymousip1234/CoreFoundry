# Class 02 — How Machines Learn

**Program:** Bong Study Hub — Foundation Batch 2026
**Subtitle:** From Rules → Data → Intelligence
**Core question:** "How can a machine make a decision when nobody
explicitly wrote the rule for every situation?"
**Core concept:** `DATA → LEARNING → MODEL → PREDICTION`
**Duration:** ~110–120 minutes
**Prerequisite:** Class 01 — Welcome to Computer Science

## What This Class Is

Class 02 is the first class of the program's AI arc. It is entirely
conceptual: no code, no mathematics, no implementation. Its one job is to
replace the mental model "a computer only does what a human explicitly
told it to do" — which Class 01 spent an entire class installing — with
its natural next layer: **a machine can learn a pattern from data when no
human could hand-write a rule for every case.**

Students leave with one durable pipeline (`Data → Learning → Model →
Prediction`), a small set of everyday examples they can point to
(spam filters, recommendations, maps, face unlock, generative AI), a
hands-on reasoning activity (teaching a computer to tell cats from dogs),
and a simple, non-taxonomic mental map of AI / Machine Learning / Deep
Learning / Generative AI. It does **not** teach Python, neural network
math, gradient descent, transformers, embeddings, RAG, agents, deep
prompt engineering, or AI ethics in depth — those are later classes'
jobs, once the programming and mathematical foundations exist to support
them (see `00_Class_Metadata/class_metadata.md` for the full deferred
list and reasoning).

## Where This Fits in the Curriculum

Class 02 continues directly from Class 01's closing moment — the
"learning staircase" (`Programming → Computer Science → Mathematics →
Data → Machine Learning → Deep Learning → LLMs → Agents`) and the line
*"we are not going to jump to the bottom, we are going to build the
staircase."* Class 02 is the first step onto that staircase's AI side,
taken deliberately at a conceptual, non-technical altitude.

**A note worth resolving explicitly when the Master Instructor Guide is
written:** Class 01's own four-month roadmap slide placed AI/ML under
"Month 3 — Engineering + AI," after Python, C, DSA, and SQL. Class 02
arrives as the very next class instead. This isn't a contradiction as
long as the Instructor Guide frames it honestly to students — as an
early, non-technical preview of where the staircase leads, before the
program returns to build the steps underneath it (Month 1/2 programming
and CS foundations). Silently ignoring this tension would undercut the
trust Class 01 built with the "we don't skip steps" message.

## Source-of-Truth Philosophy

Every class in this program follows one rule, proven across Class 01's
full artifact set: **one document governs the class, and every other
artifact is generated from it, never independently.**

- `00_Class_Metadata/class_metadata.md` (this stage) is the factual
  seed — class number, title, audience, objectives, scope, and what's
  explicitly deferred. It answers "what is this class," not "how do we
  teach it."
- The **Master Instructor Guide** (`01_Instructor_Guide/`) is the single
  source of truth for *how the class is taught* — narrative, timing,
  section-by-section teaching notes, and the exact scope boundary. It is
  built from the metadata file and must never contradict it.
- Every artifact after that — Student Notes, Presentation, Pen-Tablet
  Board Plan, Interaction Pack, Homework, Assessment, Teacher Cheat
  Sheet, Resources — is a **derived view** of the Master Instructor
  Guide, built for a different audience or medium (a student reading at
  home, a slide a student looks at live, a tablet drawing, a grading
  rubric), never a place where new scope, terminology, or sequencing
  decisions get introduced for the first time.

If a later artifact needs a concept, example, or wording the Instructor
Guide doesn't have, the fix is to update the Instructor Guide first, then
regenerate whatever derived artifact needed it — the same discipline
Class 01 used throughout.

## Artifact-Generation Workflow

This is the order Class 01 was actually built in, and the order Class 02
should follow:

1. **`00_Class_Metadata/`** — factual foundation (this step). ✅ Done.
2. **`01_Instructor_Guide/`** — the Master Instructor Guide. **This is
   the next artifact to create.** Nothing else should be started before
   it exists.
3. **`02_Student_Notes/`** — condensed take-home handout, derived from
   the Instructor Guide.
4. **`04_Pen_Tablet/`** — the live-drawing board plan, derived from the
   Instructor Guide's pen-tablet section.
5. **`05_Interaction/`** — question bank, activities (including the
   cats-vs-dogs activity's full facilitator guide), differentiated
   questions, classroom interaction flow, exit questions — all derived
   from the Instructor Guide.
6. **`03_Presentation/`** — the student-facing slide deck. Built after
   Student Notes, the Board Plan, and the Interaction Pack exist,
   because the deck's design depends on knowing what's drawn live
   (Pen-Tablet Plan) and what's asked live (Interaction Pack), so slides
   don't duplicate either.
7. **`06_Homework/`** — homework assignment and grading materials,
   derived from the Instructor Guide and Student Notes.
8. **`07_Assessment/`** — a separate, more formal check of understanding
   (quiz/recap assessment), distinct from homework — kept as its own
   folder this time so a graded assessment and a formative homework
   assignment don't get conflated.
9. **`08_Teacher_Cheat_Sheet/`** — a condensed, at-a-glance instructor
   reference distilled from everything above (comparable in spirit to
   Class 01's Board Quick Reference, but covering the whole class, not
   only the live drawings).
10. **`09_Resources/`** — curated supplementary material (further
    reading, optional videos, glossary extensions) — created last among
    the "before class" artifacts, once the core content is stable enough
    that supplementary links are actually the right ones.
11. **`10_Reflection/`** — filled in **after** the class is actually
    taught, not generated in advance — mirrors Class 01's Instructor
    Reflection Checklist, but as its own folder so post-class notes
    accumulate across cohorts without cluttering the Instructor Guide.

Do not skip ahead in this order and do not generate multiple artifacts in
one pass — each step's quality depends on the step before it being
finished and correct.

## Folder Purposes

| Folder | Purpose |
|---|---|
| `00_Class_Metadata/` | Factual seed: title, audience, objectives, scope, deferred topics. The only file every other artifact may be checked against for "is this in scope." |
| `01_Instructor_Guide/` | The Master Instructor Guide — single source of truth for teaching sequence, timing, and content. |
| `02_Student_Notes/` | Condensed, beginner-friendly take-home handout (Markdown + PDF). |
| `03_Presentation/` | The student-facing slide deck and its generator script. |
| `04_Pen_Tablet/` | The live digital-whiteboard board plan and instructor quick reference. |
| `05_Interaction/` | Question bank, activities (incl. cats-vs-dogs facilitator guide), differentiated questions, interaction flow, exit questions. |
| `06_Homework/` | The homework assignment, worked example, rubric, feedback comments, and grading workflow. |
| `07_Assessment/` | A separate formal assessment (quiz/recap check) distinct from homework. |
| `08_Teacher_Cheat_Sheet/` | One condensed, printable instructor reference distilled from the full artifact set. |
| `09_Resources/` | Curated optional supplementary material for students and instructors. |
| `10_Reflection/` | Post-class instructor reflection notes, filled in after each cohort actually runs the class. |

## Which Artifact Should Be Created First

**`01_Instructor_Guide/Class_02_Master_Instructor_Guide.md`** — the
Master Instructor Guide. Everything else in this README's workflow list
depends on it existing and being correct first.

## How Later Artifacts Must Derive From the Master Instructor Guide

When any future artifact in this class is generated, the following rules
apply — they are what "source of truth" means in practice, not just in
principle:

1. **Read the Master Instructor Guide (and `class_metadata.md`)
   completely before generating anything.** Do not generate from
   memory, assumption, or general AI-education knowledge.
2. **Do not introduce new terminology, examples, or sequencing** that
   isn't already in the Instructor Guide. If a derived artifact needs
   something new, that need is a signal to revise the Instructor Guide
   first — never to patch the gap locally in the derived artifact.
3. **Do not silently redesign the lesson.** An artifact that finds the
   Instructor Guide's approach lacking should say so explicitly (as an
   assumption or open question in its own report) rather than quietly
   diverging.
4. **Respect the deferred-topics list** in `class_metadata.md` in every
   artifact, not only the Instructor Guide — a slide, a homework
   question, or a resource link introducing gradient descent or
   transformers is a scope violation regardless of which folder it's in.
5. **Preserve terminology exactly** across artifacts. If the Instructor
   Guide says "Data → Learning → Model → Prediction," every other
   artifact uses that exact chain, in that exact order and wording —
   the same discipline that kept Class 01's six documents visually and
   verbally consistent.
6. **Every artifact's own QA pass must include a check against the
   Instructor Guide and the metadata file** — verifying sequence match,
   terminology match, and scope match — before it's considered done.

---

*This file and `00_Class_Metadata/class_metadata.md` are the only
artifacts created at this stage, by design. No slides, student notes,
homework, activities, or code exist yet for Class 02 — do not generate
them until the Master Instructor Guide exists and is explicitly
requested.*
