# Homework 2 — Grading Rubric

**Bong Study Hub — Foundation Batch 2026 · Class 02: How Machines Learn**

**Total: 20 points.** This is a first-year conceptual assignment. Grade
for understanding, not polish or vocabulary precision.

## What This Rubric Does NOT Grade

- ❌ Exact terminology — "it looks at examples" earns the same credit as
  "it uses data," as long as the idea is right.
- ❌ Handwriting quality or English fluency (beyond being
  understandable).
- ❌ Programming or mathematical knowledge — none is expected, and none
  should appear.
- ❌ Length — a short, correct, precise answer beats a long, padded one.

**Do not penalize imperfect technical vocabulary if the underlying
idea is correct.** This is the single most important grading principle
for this assignment.

---

## Scoring Table

| Q | Topic | Points |
|---|---|---|
| 1 | Rules | 2 |
| 2 | Why rules become difficult | 2 |
| 3 | The pivot | 1 |
| 4 | Core pipeline | 3 |
| 5 | Traditional programming vs. ML | 2 |
| 6 | Cats vs. dogs | 2 |
| 7 | Prediction ≠ certainty | 2 |
| 8 | Data quality | 2 |
| 9 | Misconception correction | 2 |
| 10 | Apply it to an everyday example | 2 |
| — | Optional reflection | 0 (ungraded) |
| | **Total** | **20** |

---

## Q1 — Rules (2 points)

**Full credit (2):** Two plausible spam rules given, each with a
concrete example of a case where it would fail (a false positive or
false negative).

**Partial credit (1):** Two rules given, but only one has a working
failure example, or both failure examples are vague/generic ("it might
not always work").

**Zero credit (0):** Rules are missing, are not actually rules ("it
uses AI to detect spam"), or no failure case is attempted at all.

**Common misconception:** Students sometimes give a rule and a failure
case that don't actually connect (the failure case doesn't test the
specific rule stated). Read the pairing, not just the two halves in
isolation.

---

## Q2 — Why Rules Become Difficult (2 points)

**Full credit (2):** Clearly explains that real-world cases vary or
keep changing, so a fixed rule list can't realistically keep up —
in the student's own words, without needing the phrase "rule
explosion."

**Partial credit (1):** Gestures at "there are a lot of rules needed"
without explaining *why* (variety, exceptions, changing behavior).

**Zero credit (0):** Answer is generic ("it's hard because computers
are hard") or unrelated to rules/exceptions at all.

**Common misconception:** "Rules become difficult because programming
is hard" — this misses the actual point (scale/variety of real-world
cases), not difficulty of coding itself.

---

## Q3 — The Pivot (1 point)

**Full credit (1):** Answer lands on giving the computer
examples/data/past cases instead of rules — any reasonable phrasing
accepted.

**Zero credit (0):** Answer doesn't identify examples/data as the
alternative (e.g., "give it more rules," "make it smarter," "use AI"
without explaining how).

**Common misconception:** "Just make the computer more powerful" — this
avoids the actual conceptual shift (rules → data) the question is
testing.

---

## Q4 — Core Pipeline (3 points)

**3 points:** Correct order (`DATA → LEARNING → MODEL → PREDICTION`) +
a meaningful, correct one-sentence explanation of all four stages.

**2 points:** Correct order + mostly correct explanations (one stage
explained weakly or slightly off).

**1 point:** Correct order but weak/incomplete explanations for most
stages, OR order is slightly wrong but explanations show real
understanding of what each stage does.

**0 points:** Pipeline order is fundamentally incorrect (e.g.,
Prediction placed before Data) and explanations don't recover the
correct relationship.

**Common misconception:** Students sometimes swap Model and Prediction,
or describe "Learning" as the system's final output rather than the
process that produces the Model. Also watch for "patterns" being
written in as a fifth stage — gently note in feedback that patterns
are what Learning finds, not a stage of their own (see Feedback
Comments, "Pipeline confusion").

---

## Q5 — Traditional Programming vs. ML (2 points)

**Full credit (2):** Blanks correctly filled (`HUMAN-WRITTEN RULES` for
the traditional chain; `DATA` and `PREDICTION` for the ML chain) **and**
the difference is explained correctly: traditional programming uses
human-written rules; Machine Learning uses examples/data and a
learning process to build a model that makes predictions.

**Partial credit (1):** Blanks mostly correct (e.g., "rules" without
"human-written," or one blank missing) OR the difference explanation
is correct but the blanks have an error.

**Zero credit (0):** Blanks are unrelated to the pipeline, or the
difference explanation shows the two approaches are not actually
distinguished (e.g., "they're basically the same").

**Accept equivalent wording** for the explanation — "a person writes
the rules" is exactly as good as "human-written rules."

---

## Q6 — Cats vs. Dogs (2 points)

**Full credit (2):** Explanation includes using what was learned from
examples, looking for patterns, and making a prediction/guess on the
new image — in the student's own words, no computer-vision
terminology required or expected.

**Partial credit (1):** Mentions using past examples or "comparing" the
new image, but doesn't complete the reasoning through to a
prediction/guess.

**Zero credit (0):** Answer describes a rule-based approach instead
(e.g., "if it has pointy ears, it's a cat") without any reference to
learning from examples, or is left blank/unrelated.

**Common misconception:** A student describing a hand-written rule
here (rather than pattern-based reasoning from examples) suggests the
Traditional-vs-ML distinction from Q5 hasn't fully landed — flag for
the "Pipeline confusion" feedback category.

---

## Q7 — Prediction ≠ Certainty (2 points)

**Full credit (2):** Correctly says "No" (the system can still be
using Machine Learning) **and** explains that a prediction is a best
guess based on learned patterns, not a guarantee.

**Partial credit (1):** Correct "No" but the "why" is vague or
incomplete (e.g., "sometimes it just makes mistakes" without
connecting to best-guess-not-guarantee).

**Zero credit (0):** Answers "Yes" (concludes the mistake means it
wasn't real Machine Learning), or leaves the "why" blank/unrelated.

**Common misconception:** "If it's Machine Learning, it should always
be right" — this is exactly the misconception Q7 is designed to
surface; see "Prediction vs certainty confusion" in Feedback Comments.

---

## Q8 — Data Quality (2 points)

**Full credit (2):** Explains that the system might misclassify or get
confused by the large white cat, **and** connects this to the limited/
narrow examples it learned from (only small-white-cat and
large-black-dog patterns).

**Partial credit (1):** Correctly predicts the system might struggle,
but doesn't clearly explain *why* (doesn't connect it back to the
limited training examples).

**Zero credit (0):** Answer doesn't engage with the data-quality angle
at all (e.g., "it would definitely get it wrong" with no reasoning, or
"it would always be correct").

**Common misconception:** Students sometimes reach for "bias" as a
buzzword without explaining the mechanism — that's fine to accept if
the explanation underneath is sound, but don't award full credit for
the word alone without the reasoning.

---

## Q9 — Misconception Correction (2 points)

**Full credit (2):** All three correctly identified as incorrect, with
reasonable rewrites for each (roughly: ML is an *additional* approach,
not a replacement for programming; a prediction is a best guess, not
guaranteed correct; the system finds patterns, it doesn't think/
understand like a human).

**Partial credit (1):** Two of three correctly identified and
rewritten; or all three identified correctly but rewrites are weak/
vague.

**Zero credit (0):** One or none correctly identified as incorrect, or
no rewrites attempted.

**Common misconception:** A student may correctly say a statement is
"incorrect" but then write a rewrite that keeps the same misconception
in different words — read the rewrite itself, not just the correct/
incorrect judgment.

---

## Q10 — Apply It to an Everyday Example (2 points)

**Full credit (2):** All four sub-questions (input/examples, patterns,
output/prediction, why it could be wrong) answered with reasonable,
conceptually sound guesses for the chosen system — no proprietary
knowledge expected or required.

**Partial credit (1):** Three of four sub-questions answered
reasonably, or all four attempted but one or two are generic/vague.

**Zero credit (0):** Answer describes rules instead of a learning-
based approach, attempts to describe real internal implementation
details instead of reasoning conceptually, or is left blank.

**Common misconception:** Watch for answers that revert to a rule-
based description ("it checks if the sender is on a list") for a
system the student themselves chose as an ML example — this is a
useful signal that Q5's distinction hasn't fully landed yet.

---

## Optional Reflection — Not Scored

Do not assign points. If a student writes something insightful here,
it's worth a brief, warm acknowledgment in your feedback comments (see
`Class_02_Homework_Feedback_Comments.md`), but it must never affect the
numeric score.

---

## Quick Reference — What a 20/20 Submission Looks Like

- Correctly reconstructs `DATA → LEARNING → MODEL → PREDICTION`, with
  each stage explained meaningfully.
- Clearly distinguishes traditional programming (human-written rules)
  from Machine Learning (learning from examples).
- Explains, in their own words, why rules can become impractical and
  why a prediction is a best guess rather than a guarantee.
- Applies the mental model to a new, unfamiliar example without
  reverting to rule-based thinking or claiming to know a real
  product's internals.
- Contains no code, no math, and no formal ML terminology the class
  never taught.

That's the whole bar. Nothing more is required for full marks.
