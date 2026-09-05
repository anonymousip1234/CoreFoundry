# Class 02 Assessment — Rubric

**Bong Study Hub — Foundation Batch 2026 · Class 02: How Machines Learn**
**Instructor-only. Do not distribute to students.**

**Total: 20 points.** This is a first-year conceptual assessment,
noticeably more demanding than the Homework because the scenarios are
unfamiliar — not because it requires harder technical knowledge. Grade
for transferable understanding, not vocabulary sophistication.

---

## What This Rubric Does NOT Grade

- ❌ English fluency, as long as the answer is understandable.
- ❌ Handwriting quality.
- ❌ Exact terminology — "a person types in the logic" earns the same
  credit as "human-written rules."
- ❌ Concise answers — a short, precise, correct answer beats a long,
  padded one.
- ❌ Different but logically valid examples or predictions (e.g., in
  Question 6, guessing the motorbike gets classified as either
  category is fine — the reasoning is what's graded, not the guess).

**Do not penalize imperfect technical vocabulary if the underlying
idea is correct.** This carries over unchanged from the Homework
rubric's philosophy.

## What This Rubric DOES Penalize

- Misunderstanding the Rule Problem (treating it as a difficulty/time
  problem rather than a variety/scale problem).
- Confusing DATA, LEARNING, MODEL, and PREDICTION with each other
  (especially swapping Model and Prediction).
- Treating a prediction as guaranteed truth (the single highest-
  priority misconception to catch — see Question 5).
- Reverting to explicit hand-written rules when asked to reason about
  a Machine Learning approach.
- Claiming a system can only work with cases identical to its training
  examples (rather than reasoning about how it would handle something
  new, even imperfectly).
- Unsupported claims about how a real, proprietary product actually
  works internally.

---

## Scoring Table

| Q | Topic | Points |
|---|---|---|
| 1 | The Rule Problem | 3 |
| 2 | The Pivot | 2 |
| 3 | Pipeline Reasoning | 4 |
| 4 | Traditional Programming vs. ML | 3 |
| 5 | Prediction Is Not Certainty | 3 |
| 6 | Data Quality / Unseen Case | 3 |
| 7 | Unfamiliar Application | 2 |
| — | Optional reflection | 0 (ungraded) |
| | **Total** | **20** |

---

## Q1 — The Rule Problem (3 points)

**3 — Full conceptual understanding:** Explains that growing variety
and exceptions in real submissions make a fixed rule list impractical
to maintain, with at least one concrete supporting idea or example.

**2 — Partial understanding:** Identifies that "many rules would be
needed" but explains the *why* only thinly (doesn't clearly connect to
variety/exceptions/change).

**1 — Misconception present but salvageable:** Frames the difficulty
as an effort/time problem ("it would take too long to write") or a
vague "computers are limited" claim, without engaging the actual
scale/variety reasoning — but the response is otherwise coherent and
on-topic.

**0 — Unrelated or blank:** No attempt, or an answer unrelated to the
rule-scaling problem.

---

## Q2 — The Pivot (2 points)

**2 — Full conceptual understanding:** Correctly identifies giving the
computer examples/data instead of rules, and describes the system
building/using something (a model, in substance if not by name) from
those examples.

**1 — Partial understanding:** Names "examples" or "data" but doesn't
describe what the computer does with them, or vice versa.

**0 — Misconception or blank:** Answer doesn't identify examples/data
as the alternative (e.g., "just use better rules," "use AI" with no
explanation), or is blank/unrelated.

---

## Q3 — Pipeline Reasoning (4 points)

**4 — Full conceptual understanding:** All four stages (Data,
Learning, Model, Prediction) correctly mapped to the delivery-app
scenario, with the connections between stages shown, not just isolated
definitions.

**3 — Mostly correct:** All four stages correctly identified and
mapped to the scenario, but one stage's explanation is weak, generic,
or not clearly connected to the others.

**2 — Partial understanding:** Two stages are confused with each other
(most commonly Model and Prediction), or explanations are present but
disconnected from the specific scenario (read like memorized
definitions).

**1 — Minimal understanding:** Only one or two stages are meaningfully
addressed; the rest are missing, wrong, or unrelated to the scenario.

**0 — Fundamentally incorrect or blank:** Pipeline order/roles are
fundamentally scrambled with no recoverable logic, or left blank.

---

## Q4 — Traditional Programming vs. Machine Learning (3 points)

**3 — Full conceptual understanding:** (a) and (b) both correct, and
(c) clearly explains the human-writes-the-logic vs.
learns-from-examples distinction in the student's own words.

**2 — Mostly correct:** (a) and (b) both correct, but (c) is vague or
incomplete.

**1 — Partial understanding:** One of (a)/(b) is incorrect, but (c)
shows real understanding of the underlying distinction; OR both (a)
and (b) are correct but (c) is missing entirely.

**0 — Fundamentally incorrect or blank:** Both (a) and (b) reversed
and (c) shows no grasp of the distinction, or left blank.

---

## Q5 — Prediction Is Not Certainty (3 points)

**3 — Full conceptual understanding:** Clear "No," with a correct
explanation that a prediction is a best guess based on learned
patterns, not a guarantee.

**2 — Mostly correct:** Correct "No," but the explanation is thin or
only partially connects to best-guess-not-guarantee.

**1 — Misconception present:** Answers "No" but for the wrong reason
(e.g., "No, because the app probably has a bug" — avoids the actual
prediction-vs-certainty idea entirely), or hedges without committing to
an answer.

**0 — Core misconception or blank:** Answers "Yes" (concludes the
mistake means the system wasn't really using Machine Learning), or is
blank/unrelated. **This is the highest-priority misconception on the
assessment — flag regardless of the rest of the submission's
quality (see Grading Workflow).**

---

## Q6 — Data Quality / Unseen Case (3 points)

**3 — Full conceptual understanding:** Predicts a plausible outcome
(misclassification or uncertainty) **and** explicitly connects it to
the narrow, non-overlapping training examples the system saw.

**2 — Partial understanding:** Predicts a plausible outcome, but the
connection to the limited training examples is thin or implicit rather
than explained.

**1 — Misconception present:** States the system would definitely be
correct or definitely be wrong with no reasoning tied to what it
learned from, but the response is otherwise on-topic.

**0 — Unrelated or blank:** No engagement with the data-quality angle,
or blank.

---

## Q7 — Unfamiliar Application (2 points)

**2 — Full conceptual understanding:** All three sub-questions
answered with reasonable, internally consistent, learning-based
reasoning (not rule-based).

**1 — Partial understanding:** Two of three sub-questions answered
reasonably, or a rule-based ("if X then Y") answer is given instead of
a learning-based one for one part.

**0 — Misconception or blank:** Answer is fully rule-based throughout,
attempts real technical/proprietary speculation instead of conceptual
reasoning, or is blank.

---

## Optional Reflection — Not Scored

Never assign points here. A thoughtful response is worth a brief,
warm note in your feedback and a mental note for cohort-level
patterns (see Grading Workflow, Step 9) — it must never change the
numeric score.

---

## Quick Reference — What a 20/20 Submission Looks Like

- Explains why hand-written rules strain under real-world variety,
  using its own example or reasoning, not a memorized line.
- Correctly names the pivot to examples/data and what gets built from
  them.
- Re-derives `DATA → LEARNING → MODEL → PREDICTION` inside a brand-new
  scenario, with the four stages genuinely connected to each other.
- Cleanly distinguishes traditional programming from Machine Learning
  in a new comparison, not the one seen in class or homework.
- States plainly that a wrong prediction doesn't mean a system wasn't
  using Machine Learning.
- Connects an unfamiliar case's likely difficulty back to what a
  system did or didn't see while learning.
- Applies the mental model to a genuinely new, invented scenario
  without reverting to rule-based thinking.

That's the whole bar. Nothing more is required for full marks.
