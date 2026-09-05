# Class 02 — Interaction & Activity Pack

**Bong Study Hub — Foundation Batch 2026**
**How Machines Learn** — *From Rules → Data → Intelligence*

This is **Step 5** of Class 02's artifact chain:

```
Metadata → Master Instructor Guide → Student Notes → Pen Tablet →
Presentation → THIS INTERACTION PACK
```

This is **not** a second Instructor Guide. The Master Instructor Guide
remains the source of truth for pedagogy, sequencing, and spoken
teaching language. This document exists to answer one practical
question for every activity below: **how do I actually run this
moment, live, with a room (or a Zoom call) full of first-year
students?** — what to ask, how long to wait, what students will
probably say, how to respond, and what to watch for.

**The discovery journey this whole pack protects:**

```
COMPUTERS CAN FOLLOW RULES
        ↓
BUT RULES CAN BECOME HARD TO WRITE
        ↓
WHAT IF WE GIVE EXAMPLES?
        ↓
DATA → LEARNING → MODEL → PREDICTION
```

Every activity below exists to make one link of that chain *felt*,
not just stated. Students should never be told "Machine Learning
learns from data" as a bare fact — they should arrive at it themselves,
one activity at a time.

---

## Table of Contents

1. [How to Use This Document](#1-how-to-use-this-document)
2. [Activity 1 — AI Quick Reaction](#activity-1--ai-quick-reaction)
3. [Activity 2 — Build a Rule](#activity-2--build-a-rule)
4. [Activity 3 — Break the Rule](#activity-3--break-the-rule)
5. [Activity 4 — Rule Explosion](#activity-4--rule-explosion)
6. [Activity 5 — The Pivot Question](#activity-5--the-pivot-question)
7. [Activity 6 — Predict the Pipeline](#activity-6--predict-the-pipeline)
8. [Activity 7 — Cats vs. Dogs (Hero Activity)](#activity-7--cats-vs-dogs-hero-activity)
9. [Activity 8 — Prediction or Certainty?](#activity-8--prediction-or-certainty)
10. [Activity 9 — Data Quality Thought Experiment](#activity-9--data-quality-thought-experiment)
11. [Activity 10 — AI / ML / Deep Learning / GenAI Check](#activity-10--ai--ml--deep-learning--genai-check)
12. [Activity 11 — Exit Check](#activity-11--exit-check)
13. [Participation Methods](#13-participation-methods)
14. [Wait-Time Rule](#14-wait-time-rule)
15. [Wrong-Answer Handling](#15-wrong-answer-handling)
16. [Quiet Class Protocol](#16-quiet-class-protocol)
17. [Overly Active / Advanced Student Protocol](#17-overly-active--advanced-student-protocol)
18. [Common Misconceptions to Surface](#18-common-misconceptions-to-surface)
19. [Activity Timing Summary](#19-activity-timing-summary)
20. [90-Minute Version](#20-90-minute-version)
21. [120-Minute Version](#21-120-minute-version)
22. [Online Delivery Notes](#22-online-delivery-notes)
23. [Pen Tablet Integration](#23-pen-tablet-integration)
24. [Presentation Integration](#24-presentation-integration)
25. [Success Criteria](#25-success-criteria)
26. [Quality Assurance](#26-quality-assurance)

---

## 1. How to Use This Document

- Each activity below follows the same nine-field format: **Purpose,
  Time, Setup, Ask, Wait, Likely responses, Instructor move, Watch
  for, Transition.** This is a facilitation reference, not a script —
  say things in your own words.
- Timings are **embedded inside** the canonical 110-minute class flow
  from the Master Instructor Guide, not additional time on top of it.
  Section 19 makes this explicit.
- Every activity names which Pen Tablet drawing (if any) it pairs with
  and which slide(s) frame it — see Sections 23–24 for the full maps.
- Nothing here introduces a concept, example, or term that isn't
  already in the Master Instructor Guide, Student Notes, Pen Tablet
  Board Plan, or Presentation.

---

## Activity 1 — AI Quick Reaction

**Purpose:** Activate students' existing experience with AI before any
definition is given — activation, not terminology testing.

**Time:** ~5 minutes.

**Setup:** Slides 5–6 (AI Around Us cards) on screen, or simply named
verbally. No drawing needed yet.

**Ask:** "Which of these have you used or noticed — spam detection,
recommendation systems, maps/navigation, face unlock, generative AI
like ChatGPT?" Then: "What makes you call something 'smart'?"

**Wait:** 3–5 seconds after each question.

**Likely responses:** "It knows what I want." / "It recognizes me." /
"It predicts traffic." / "It recommends things." / "It answers
questions."

**Instructor move:** Acknowledge every answer as useful — do **not**
correct the language yet (e.g., don't yet push back on "it knows" or
"it understands"). Collect 3–4 answers, then bridge: "We are going to
understand what is happening underneath some of these systems."

**Watch for:** Nothing to correct here — misconceptions about
"understanding" or "knowing" are addressed later (Activity 6 onward),
not now. Introducing neural networks, algorithms, or probability at
this stage is out of scope.

**Transition:** Into Activity 2 — "Let's actually try to build one of
these ourselves, by hand: a spam filter."

---

## Activity 2 — Build a Rule

**Purpose:** Let students experience traditional rule-based thinking
first-hand, and feel ownership of the rules before they're stress-
tested.

**Time:** ~6 minutes.

**Setup:** Scenario: "You are designing a simple spam filter." Pen
Tablet Drawing 2 skeleton (`INPUT → HUMAN-WRITTEN RULES → OUTPUT`)
open and empty.

**Ask:** "What rule could we write to identify spam?"

**Wait:** 3–5 seconds.

**Likely responses:** Suspicious words, unknown sender, asking for
money, too many exclamation marks, prize/winner language.

**Instructor move:** Write 3–4 proposed rules directly into the
"Human-Written Rules" box as students say them. Then ask the important
move: **"Who decided that this was a rule?"** — guide toward "A
human." Explicitly connect: "That's exactly `INPUT → HUMAN-WRITTEN
RULES → OUTPUT` — a human supplies the rule, the computer just follows
it."

**Watch for:** Students slipping into code/`if-else` syntax — redirect
gently: "Right idea — say it in plain English instead." Do **not** yet
introduce the Machine Learning pipeline; this activity ends with rules
still standing, unbroken.

**Transition:** "This is a completely reasonable first attempt. Let's
throw some real emails at it."

---

## Activity 3 — Break the Rule

**Purpose:** Create the felt need for a different approach — not to
prove rules are useless, but to show where they strain.

**Time:** ~8 minutes.

**Setup:** Present two cases (matching Presentation Slide 9): a
genuine email — *"Your booking is urgent — confirm now!"* — and a real
spam email — *"fr33 amaz0n..."*. Pen Tablet Drawing 3 begins here,
building directly on top of Drawing 2's rule box.

**Ask:** "Would our rules handle these correctly?" Then, for whichever
rule a student defends, challenge it directly:
- If "urgent means spam" → "What about a real flight or hotel
  booking?"
- If "unknown sender means spam" → "What if your friend emails from a
  new address?"
- If "lots of !!! means spam" → "What if a real promotional email uses
  them?"

**Wait:** 3–5 seconds per challenge.

**Likely responses:** Growing hesitation — "Well, maybe not always,"
or a patch attempt ("okay, but only if it *also* asks for money").

**Instructor move:** Let each patch attempt stand, then supply the
next counter-case. The goal is not "you're wrong" — it's "let's
stress-test that a little more." Add each new rule/exception directly
onto the crowding Drawing 3 board.

**Watch for:** The temptation to declare rules useless — correct
gently: "Rules work well when humans can clearly describe the logic.
The problem is the number of situations and exceptions growing, not
that rules are a bad idea."

**Transition:** Straight into Activity 4 — "And there's always another
case waiting."

---

## Activity 4 — Rule Explosion

**Purpose:** Make the growing-rule problem visually and verbally
memorable before naming it.

**Time:** ~5 minutes.

**Setup:** Continue Drawing 3. Presentation Slide 10 (`ONE RULE → NEW
EXCEPTION → ANOTHER RULE → ANOTHER EXCEPTION → …`) can frame this
verbally while the real crowding happens on the pen tablet, not the
slide.

**Ask:** "If we keep doing this, what happens?"

**Wait:** 3–5 seconds.

**Likely responses:** Too many rules, difficult to maintain,
confusing, rules conflict, impossible to cover everything.

**Instructor move:** Name the feeling informally: **"rule explosion"**
— and immediately qualify it: "That's this class's own label for the
feeling, not a formal technical term." Do not introduce any formal
software-engineering vocabulary here.

**Watch for:** A student reaching for "complexity" or "Big O" or any
formal CS term — acknowledge briefly ("there's real depth under that
intuition") and keep the language informal.

**Transition:** "So if writing every rule by hand becomes impractical,
what else could we give the computer?" — straight into Activity 5.

---

## Activity 5 — The Pivot Question

**Purpose:** The single most important interaction moment before the
Machine Learning reveal — let students arrive at "examples" or "data"
themselves.

**Time:** ~4 minutes.

**Setup:** Presentation Slide 11, or simply the crowded Drawing 3 left
on screen. No new drawing yet.

**Ask:** "If humans cannot realistically write every rule, what could
we give the computer instead?" **STOP. Do not answer it yourself.**

**Wait:** 5–10 seconds of genuine silence — longer than feels
comfortable.

**Likely responses:** Silence at first, then "examples," "past
emails," "data," "previous cases," or a vaguer "show it what spam
looks like."

**Instructor move:** If someone says "data," reinforce it directly. If
nobody says "data" but someone says "examples," bridge explicitly:
"Exactly. Examples are data." Only *after* students have contributed
should you say: "Instead of manually writing every rule, we can give
the system examples."

**Watch for:** Rescuing the silence too early — the wait time here is
non-negotiable (see Section 14). If truly nothing comes after 10
seconds, narrow the question per Section 16's quiet-class protocol
rather than answering it outright.

**Transition:** "Let's see what happens next if we do that" — into
Activity 6, and Pen Tablet Drawing 4.

---

## Activity 6 — Predict the Pipeline

**Purpose:** Let students construct the conceptual pipeline themselves,
box by box, rather than receive it finished.

**Time:** ~8 minutes.

**Setup:** Fresh page — Pen Tablet Drawing 4, the hero drawing.
Presentation Slide 14 is deliberately minimal ("The Core Idea") and
must be on screen (or the slide hidden entirely) **before** any box is
drawn — never show the finished pipeline first.

**Ask, in order, one box at a time:**
1. "What are we giving it?"
2. "What does it do with those examples?"
3. "What does it build from what it learned?"
4. "What happens when we give it something new?"

**Wait:** 3–5 seconds after each question.

**Likely responses, matching each question:** "Examples" / labeled
emails → "it looks for patterns" / "it figures out what's common" →
"something that learned the patterns" / "a model" → "it guesses" / "it
predicts spam or not."

**Instructor move:** Write each box only after its question is
answered: **DATA → LEARNING → MODEL → PREDICTION**, one at a time,
grounding each in the spam example as it lands. **Use this exact
terminology — never substitute "patterns" for "Learning" as a pipeline
stage; patterns are what the learning process finds inside the data,
not a box of their own.** Only after all four boxes exist should
Presentation Slide 15 be shown, as reinforcement.

**Watch for:** A student saying "it thinks about it" or "it
understands" — gently redirect: "Think of it as *noticing patterns*,
not understanding the way you do." Do not let this become a debate;
one sentence and move on.

**Transition:** "Let's reason through this with something concrete:
cats and dogs" — into Activity 7.

---

## Activity 7 — Cats vs. Dogs (HERO ACTIVITY)

**Purpose:** Let students reason through the Machine Learning idea
using a visual classification example, entirely without code or
mathematics. This is the emotional and pedagogical centerpiece of the
class — protect its full time.

**Time:** ~12 minutes.

**Setup:** Show many labeled cat examples and many labeled dog
examples (images or verbal description), deliberately varied — cats:
different breeds, colors, poses, backgrounds; dogs: different breeds,
sizes, colors, poses, backgrounds. Presentation Slide 17 frames this;
no new pen-tablet drawing is created (see Section 23).

**Ask (question ladder — work through in order):**

| Level | Question |
|---|---|
| 1 — Observation | "What do you notice?" |
| 2 — Comparison | "What seems similar across the cat examples? Across the dog examples?" |
| 3 — Generalization | "If the next cat looks very different from these examples, could the system still recognize it?" |
| 4 — Ambiguity | "What if the new image is difficult to classify?" |
| 5 — Limitation | "Could the system make a mistake?" |

**Wait:** 5–10 seconds per question — this activity earns the longer
wait time.

**Likely responses:** Level 1–2: ears, face shape, body shape, fur,
nose, proportions, other visual patterns. Level 3: mixed — some say
yes confidently, some are unsure. Level 4–5: "maybe," building toward
"yes, it could still get it wrong."

**Instructor move:** Do **not** tell students which observations are
"correct features" — the point is to let them reason, not to grade
their pattern-spotting. After Level 2, introduce: "Now imagine we show
the system a brand-new image. What do you think it would do?" — guide
toward "compare it to patterns from examples," "use what it learned,"
"make a prediction." Then ask the critical follow-up directly: "Could
it still get it wrong?" — land on "Yes."

**Watch for:** Any drift toward computer-vision technicalities
("edges," "pixels," "features" as a formal term) — redirect to plain
language ("just call it a pattern you noticed"). This is explicitly
**not** a technical computer-vision discussion.

**Transition:** This is the direct bridge into **Prediction ≠
Certainty** — Activity 8.

---

## Activity 8 — Prediction or Certainty?

**Purpose:** Correct the misconception that AI outputs are
automatically correct.

**Time:** ~5 minutes.

**Setup:** No new drawing — point back at Pen Tablet Drawing 4's
PREDICTION box. Presentation Slide 18.

**Ask:** Present three situations — (1) a recommendation you dislike,
(2) a spam filter that makes a mistake, (3) the ambiguous cat/dog
image from Activity 7 — then ask: "Was the system making a prediction,
or guaranteeing the answer?"

**Wait:** 3–5 seconds.

**Likely responses:** "Prediction" (often after a beat of thought,
sometimes needing the three examples to click first).

**Instructor move:** Confirm and state plainly: "A prediction is a best
guess based on learned patterns. It is not a guarantee." Point at the
PREDICTION box on Drawing 4 while saying this.

**Watch for:** A student asking about accuracy percentages or
confidence scores — do not introduce them; redirect: "We're not
putting a number on it today — just 'best guess, not guaranteed.'"

**Transition:** "So does the data behind that guess matter?" — into
Activity 9.

---

## Activity 9 — Data Quality Thought Experiment

**Purpose:** Make "poor data → poor predictions" intuitive, without
statistical or fairness vocabulary.

**Time:** ~4 minutes.

**Setup:** No new drawing — light annotation near Drawing 4's DATA box
is optional. Presentation Slide 19.

**Ask:** "Suppose we teach our cat/dog system using only photographs
of small white cats and large black dogs. What might happen when it
sees a large white cat?"

**Wait:** 3–5 seconds.

**Likely responses:** "It might get confused," "it may learn the wrong
pattern," "it may make a poor prediction."

**Instructor move:** Let students reason it through, then ask
directly: "So does the data matter?" — land on "Yes." State plainly:
"Poor or limited data can lead to poor predictions."

**Watch for:** A student reaching for "bias" or "fairness" as a formal
term — acknowledge briefly and keep it at the intuitive level: "That's
a real and important idea, and it's exactly this — limited examples,
limited results. We'll go deeper into it in a later class."

**Transition:** "Now let's zoom out and see how all the AI terms
you've heard fit together" — into Activity 10.

---

## Activity 10 — AI / ML / Deep Learning / GenAI Check

**Purpose:** Check basic orientation among the four terms without
turning the map into a taxonomy lesson.

**Time:** ~4 minutes.

**Setup:** Pen Tablet Drawing 5 (nested AI/ML/Deep Learning circles +
Generative AI marker), built live ring by ring. Presentation Slide 20
reinforces afterward.

**Ask, in order:** "Which is the broader idea: AI or Machine
Learning?" → "Where does Deep Learning sit in our simple learning
map?" → "Where would you place Generative AI in the map we saw
today?"

**Wait:** 3–5 seconds per question.

**Likely responses:** "AI is broader," "Deep Learning is inside
Machine Learning," and a mix of guesses for Generative AI (some say
"inside ML," some say "its own thing" — both are useful to discuss
briefly).

**Instructor move:** Confirm the broad-to-narrow relationship, place
the Generative AI marker at the Machine Learning / Deep Learning
boundary as discussed. Explicitly remind: "This is a learning map, not
a complete technical taxonomy."

**Watch for:** Requests for formal definitions of any of the four
terms, or questions about neural networks/transformers — do not
answer in technical depth; this is an orientation exercise only (see
Section 17 for the parking response).

**Transition:** Into the Staircase callback and Recap (no numbered
activity — see Section 24), then Activity 11.

---

## Activity 11 — Exit Check

**Purpose:** Formative, ungraded check aligned to the class success
metric — explanation questions, not terminology recall.

**Time:** ~5 minutes.

**Setup:** Presentation Slide 24. Pen Tablet Drawing 4 (Core Pipeline)
and Drawing 6 (Staircase) stay visible for reference.

**Ask:**
1. "Why can hand-written rules become difficult to manage?"
2. "What is the difference between traditional programming and
   Machine Learning?"
3. "What does `DATA → LEARNING → MODEL → PREDICTION` mean?"
4. "Why isn't a prediction guaranteed to be correct?"

**Wait:** 3–5 seconds per question; accept written/chat answers
without forcing every student to speak aloud.

**Likely responses:** Informal but recognizable versions of the class's
own language — see the Student Notes' Answer Key for the target
substance of each answer.

**Instructor move:** Accept answers in the student's own words. Do not
grade correctness on exact terminology.

**Watch for:** A student reciting a memorized definition without
being able to explain it in their own words — gently probe with "can
you say that in your own way?"

**Transition:** Class closes — hand off to the homework bridge
(created separately, in `06_Homework/`).

---

## 13. Participation Methods

Because this is an online class, mix participation formats so no
single one carries the whole session:

| Method | Use it like |
|---|---|
| **Verbal** | "Tell me what you think." — default for most Ask prompts above. |
| **Chat** | "Type your answer in one sentence." — best for the Pivot Question and Exit Check, where typing lowers the stakes of being wrong publicly. |
| **Hand raise** | "Who thinks the rule would fail here?" — fast temperature-check during Activity 3 (Break the Rule). |
| **Poll** | Use only where the question is genuinely binary or small-option (e.g., "Prediction or Certainty?" in Activity 8 could be a two-option poll). |
| **Think → Pair → Share** | Only if the platform supports breakout rooms, and only selectively — this class favors quick whole-group reasoning; do not overuse breakout rooms. |

Design every activity so it still works if only a few students
participate verbally and most cameras are off — chat and hand-raise
are not fallbacks, they're equally valid primary channels here.

---

## 14. Wait-Time Rule

Deliberately wait after every conceptual question instead of filling
the silence.

- **Default:** 3–5 seconds minimum before answering your own question.
- **Pivot Question (Activity 5) and Cats-vs-Dogs (Activity 7):** 5–10
  seconds is acceptable and expected.
- Do not rescue students too quickly — silence is part of the learning
  process, not dead air to be filled.

---

## 15. Wrong-Answer Handling

Never respond "No, that's wrong." Use instead:

- "Interesting. Let's test that."
- "That could work here. What happens in this example?"
- "Let's stress-test that rule."

Treat every student answer as material for reasoning, not something to
grade in the moment. A wrong answer is genuinely useful when it helps
reveal a limitation — Activity 3 (Break the Rule) is built entirely on
this principle.

---

## 16. Quiet Class Protocol

If nobody answers, work down this list before moving on:

1. Repeat the question more simply.
2. Give two possible choices (e.g., instead of "What pattern should
   the system learn?" ask "Do you think the system should look at the
   words, the sender, or both?").
3. Ask for a chat response instead of a verbal one.
4. Give a concrete example to react to.
5. Then continue — do not let silence consume the entire lesson.

---

## 17. Overly Active / Advanced Student Protocol

If a student introduces neural networks, deep-learning mathematics,
probability, model architectures, transformers, embeddings, gradient
descent, or training algorithms — acknowledge the direction, then park
it:

> "Yes, that's where the technical story eventually becomes much
> deeper. Today we're building the mental model underneath it first."

Then return directly to `DATA → LEARNING → MODEL → PREDICTION`. Do not
let one advanced student pull the whole class into a later topic —
redirect once, warmly, and move on.

---

## 18. Common Misconceptions to Surface

| Misconception | Response |
|---|---|
| "Machine Learning means the computer thinks like a human." | "No. In this class, learning means finding useful patterns in data." |
| "Machine Learning replaces programming." | "No. It is another approach for problems where writing every rule directly can become impractical." |
| "If a model predicts something, it must be correct." | "No. A prediction is a best guess based on learned patterns." |
| "AI is magic." | "AI systems depend on data, patterns, and the systems built from them." |
| "More data automatically means a better system." | "More data is not automatically better; the examples and data quality matter." |

Keep every response at this same conceptual level — none of these
need a technical elaboration to land.

---

## 19. Activity Timing Summary

| Activity | Time |
|---|---|
| AI Quick Reaction | 5 min |
| Build a Rule | 6 min |
| Break the Rule | 8 min |
| Rule Explosion | 5 min |
| Pivot Question | 4 min |
| Predict the Pipeline | 8 min |
| Cats vs Dogs | 12 min |
| Prediction or Certainty | 5 min |
| Data Quality Thought Experiment | 4 min |
| AI/ML/DL/GenAI Check | 4 min |
| Exit Check | 5 min |
| **Total** | **66 min** |

**These interaction blocks are embedded inside the broader 110-minute
class** (see Instructor Guide Section 6, Class at a Glance) — they are
**not** 66 additional minutes added on top of it. The remaining ~44
minutes of the canonical flow are the opening, the What-Is-AI
discussion, instructor explanation between activities, the Staircase
callback, and the recap/homework bridge — all of which already exist
in the Master Instructor Guide.

---

## 20. 90-Minute Version

If compressed to 90 minutes, **protect** these six:

1. Rule Problem (Activities 3–4)
2. Pivot Question (Activity 5)
3. Core Pipeline (Activity 6)
4. Cats vs Dogs (Activity 7)
5. Prediction ≠ Certainty (Activity 8)
6. Exit Check (Activity 11)

**Compress** these:

- AI Quick Reaction (Activity 1) — collect fewer examples.
- The AI-Around-Us discussion generally.
- The AI/ML/DL/GenAI orientation discussion (Activity 10) — shorter,
  fewer "where does X belong" rounds.
- Data Quality Thought Experiment (Activity 9) — one exchange instead
  of a fuller back-and-forth.

**Do not remove the Cats-vs-Dogs activity** under any time pressure.

---

## 21. 120-Minute Version

Do not add technical topics. Use the extra time for:

- More student-generated rules in Activity 2.
- More stress-testing rounds in Activity 3.
- Extended Cats-vs-Dogs discussion (an extra ambiguous example,
  student-proposed) in Activity 7.
- More examples of prediction mistakes in Activity 8.
- More student questions generally, parked or answered as appropriate.

The goal is deeper reasoning on existing material, never broader
syllabus coverage.

---

## 22. Online Delivery Notes

Assumed environment: Zoom / Google Meet / Teams style, slides shared,
pen tablet available, students may have cameras off, chat available,
some students hesitant to speak.

- Every activity above is designed to work even if only a few students
  participate verbally.
- Avoid any activity that requires everyone to have a camera on —
  none of the eleven activities do.
- Chat is a first-class participation channel here, not a fallback —
  lean on it especially for the Pivot Question and Exit Check.

---

## 23. Pen Tablet Integration

| Drawing | Used during |
|---|---|
| **Drawing 1** — AI Around Us | Activity 1 (AI Quick Reaction) |
| **Drawing 2** — Traditional Programming | Activity 2 (Build a Rule) |
| **Drawing 3** — The Rule Problem | Activities 3–4 (Break the Rule + Rule Explosion) |
| **Drawing 4** — `DATA → LEARNING → MODEL → PREDICTION` | Activity 5 (Pivot Question) through Activity 6 (Predict the Pipeline); reused (pointed back to, not redrawn) in Activities 7, 8, and 9 |
| **Drawing 5** — AI / ML / Deep Learning / Generative AI | Activity 10 (AI/ML/DL/GenAI Check) |
| **Drawing 6** — Learning Staircase / Class 01 callback | The Staircase callback that follows Activity 10 (no numbered activity — a direct instructor-led moment per the Instructor Guide) |

No additional mandatory drawings are introduced by this pack. Cats vs.
Dogs (Activity 7) deliberately has **no dedicated drawing** — see the
Pen Tablet Board Plan, Section 7: it is a reasoning activity that
points back to Drawing 4 rather than generating a seventh drawing.

---

## 24. Presentation Integration

| Activity | Slide flow |
|---|---|
| 1 — AI Quick Reaction | Slides 5–6 (AI Around Us cards) → verbal discussion → Slide 7 |
| 2 — Build a Rule | Slide 7 (rules skeleton) → student rule generation → **switch to pen tablet, Drawing 2** → Slide 8 (worked rule examples) |
| 3 — Break the Rule | Slide 9 (stress-test cases) → **switch to pen tablet, Drawing 3** |
| 4 — Rule Explosion | Slide 10 (framing only) → pen tablet Drawing 3 continues → Slide 11 |
| 5 — Pivot Question | Slide 11 → student responses (chat encouraged) → Slide 12 |
| 6 — Predict the Pipeline | Slides 12–13 (ML named) → Slide 14 (minimal hero anchor) → **switch to pen tablet, Drawing 4, built live** → **return to Slide 15** (reinforcement) → Slide 16 (full comparison) |
| 7 — Cats vs Dogs | Slide 17 → verbal reasoning activity (no new drawing; point back to Drawing 4 if useful) → Slide 18 |
| 8 — Prediction or Certainty? | Slide 18 → point back to Drawing 4's PREDICTION box |
| 9 — Data Quality Thought Experiment | Slide 19 → optional light annotation on Drawing 4's DATA box |
| 10 — AI/ML/DL/GenAI Check | **switch to pen tablet, Drawing 5, built ring by ring** → **return to Slide 20** (reinforcement) |
| *(Staircase callback, no numbered activity)* | Slide 21 (everyday mental model) → Slide 22 (staircase, pen tablet Drawing 6) |
| 11 — Exit Check | Slide 23 (recap) → Slide 24 (exit check questions) → Slide 25 (closing) |

Example flow, as a quick visual (matching Activity 6):

```
Slide 12–13
    ↓
Slide 14 (minimal — no pipeline shown yet)
    ↓
switch to pen tablet
    ↓
Drawing 4 (built live, box by box)
    ↓
return to Slide 15 (pipeline reinforced)
```

---

## 25. Success Criteria

By the end of the interaction sequence, most students should be able
to:

1. Explain why writing every rule can become impractical.
2. Explain why examples/data can be useful.
3. Reconstruct `DATA → LEARNING → MODEL → PREDICTION`.
4. Explain the difference between traditional programming and Machine
   Learning.
5. Reason through the Cats-vs-Dogs example.
6. Explain why a prediction is not guaranteed to be correct.
7. State that poor or limited data can lead to poor predictions.

---

## 26. Quality Assurance

**Source alignment:** Every activity above traces directly to a named
section of the Master Instructor Guide (Sections 8–21) and reuses
only examples, terminology, and sequencing already established there,
in the Student Notes, the Pen Tablet Board Plan, and the Presentation
— cross-checked against the actual slide deck (25 slides, verified via
its text/notes extraction) rather than assumed from memory.

**Sequencing:** Confirmed — the Rule Problem (Activities 3–4) occurs
before the Pivot Question (Activity 5), which occurs before Machine
Learning is named (Activity 6). No activity reveals `DATA → LEARNING →
MODEL → PREDICTION` before Activity 6, and Activity 6 itself withholds
the finished pipeline until all four boxes are built live.

**Discovery:** Every activity's `Ask` field poses a question before
any instructor explanation — students think first in all eleven
activities, with no activity opening on a stated definition.

**Scope:** No advanced ML implementation topic (neural networks,
probability, confidence scores, gradient descent, transformers,
embeddings, training algorithms) appears as taught content anywhere in
this pack. Every occurrence of such a term is confined to Section 17
(the parking-lot response) or a "watch for" warning telling the
instructor not to introduce it.

**Terminology:** `DATA → LEARNING → MODEL → PREDICTION` is used
identically everywhere in this document — "patterns" is never
substituted as a pipeline stage; it is only ever described as what the
Learning step *finds*, exactly as Activity 6 specifies. `INPUT →
HUMAN-WRITTEN RULES → OUTPUT` is used identically wherever the
traditional pipeline appears (Activity 2, Section 23–24).

**Class 01 continuity:** The interaction sequence reconnects to
`PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT` implicitly through
Activity 2 ("a human supplies the rule," the same Input→Process→Output
lineage) and explicitly through the Staircase callback referenced in
Sections 23–24, matching the Instructor Guide and Presentation exactly.

**Online usability:** Every activity's Setup/Ask fields work with
chat, verbal response, or hand-raising; Section 13 confirms no
activity requires cameras on, and breakout rooms are flagged as
optional/selective rather than required anywhere.

**Instructor usability:** Each activity is self-contained in nine
short fields — an instructor can open this document mid-class and
know immediately what to ask, how long to wait, and what to do next,
without cross-referencing the Master Instructor Guide first.

**No over-scripting:** No activity reproduces full teaching prose from
the Instructor Guide — every `Ask` and `Instructor move` field is a
short prompt or one-line reasoning move, not a paragraph of narration.
