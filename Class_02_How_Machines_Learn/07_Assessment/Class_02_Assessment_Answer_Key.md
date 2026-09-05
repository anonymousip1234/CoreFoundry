# Class 02 Assessment — Answer Key

**Bong Study Hub — Foundation Batch 2026 · Class 02: How Machines Learn**
**Instructor-only. Do not distribute to students.**

**The single most important instruction in this document: grade the
underlying idea, not exact terminology.** Every question below has
more than one reasonable phrasing of a correct answer. Where a student
uses different words but demonstrates the same reasoning, that is a
full-credit answer.

---

## Question 1 — The Rule Problem (3 points)

**What a full-credit answer demonstrates:** The student explains that
as more real photo submissions arrive, they'll keep encountering new
variations (lighting, poses, accessories, camera angles, styles) that
no fixed rule list anticipated — and that the rule list would have to
keep growing, indefinitely, to keep up. The answer should connect
*variety* and *exceptions* (and ideally *change over time* — e.g.,
new phone cameras, new fashion trends) to the difficulty, not just
assert that "it would be hard."

**Acceptable alternative reasoning:** A student may focus on just one
or two of the three ideas (variety / exceptions / change) in real
depth rather than naming all three shallowly — that's fine. A student
who invents their own vivid example of an edge case (e.g., "someone
wearing prescription glasses that look a bit like sunglasses") and
reasons from it is demonstrating exactly the target skill.

**Common wrong reasoning:** "It would be hard because writing rules
takes a long time" (treats this as an effort/time problem rather than
a scale/variety problem) or "It would be hard because computers can't
understand photos" (reaches for a technical limitation never taught,
rather than the conceptual rule-explosion idea).

**Why it's conceptually wrong:** The Rule Problem isn't about how long
rule-writing takes or a technical capability gap — it's about the
combinatorial growth of cases and exceptions outpacing what any fixed,
hand-written list can realistically cover.

**Grading nuance:** Do not require the phrase "rule explosion" — it's
an informal class label, not a required term. A strong answer with
zero class vocabulary should still score full marks.

---

## Question 2 — The Pivot (2 points)

**What a full-credit answer demonstrates:** The student says the
college could give the computer **examples** (labeled acceptable/
unacceptable photos, or equivalent phrasing — "data," "past cases,"
"sample photos") instead of more rules, and that the computer would
build/use a **model** from those examples (accept "something it
learns," "a system that recognizes patterns," etc.).

**Acceptable alternative reasoning:** The word "model" doesn't need to
appear explicitly if the student clearly describes "something built
from looking at the examples that can then judge new photos" — that is
the same idea in different words.

**Common wrong reasoning:** "Give it more powerful rules" or "use AI"
without explaining what changes about the approach.

**Why it's conceptually wrong:** This misses the actual pivot — from a
human supplying explicit logic to a system learning its own patterns
from examples. Naming "AI" without explaining the examples-to-model
shift doesn't demonstrate understanding of the pivot itself.

**Grading nuance:** A student who describes the model only vaguely
("something that knows what a good photo looks like") but clearly
grounds it in "from the examples it saw" should still receive full or
near-full credit — the mechanism understanding matters more than
precise vocabulary.

---

## Question 3 — Pipeline Reasoning (4 points)

**What a full-credit answer demonstrates:** All four stages correctly
mapped to the scenario, **and** the connections between them shown:

- **Data** = the past orders, already labeled "on time" or "late."
- **Learning** = the process of looking across those labeled orders
  and finding what tends to separate on-time from late (e.g.,
  patterns involving distance, time of day, restaurant, etc. — the
  student does not need to guess the actual pattern, just describe
  that a pattern is being found).
- **Model** = what the system builds after that learning process —
  something that has picked up on those patterns.
- **Prediction** = the model's best guess about the new order — will
  it likely be on time or late.

Full credit requires showing the four stages **flow into each other**
(data feeds learning, learning produces the model, the model produces
the prediction) — not four isolated definitions copied from memory.

**Acceptable alternative reasoning:** Any accurate description of what
kind of pattern the system might notice is fine (or the student may
reasonably say "we don't know exactly what pattern, just that it finds
one") — this question is not testing whether they can guess the actual
predictive factor.

**Common wrong reasoning:** Writing four correct-sounding one-line
definitions with no reference to the delivery scenario at all (a sign
of recall rather than reasoning); or swapping Model and Prediction
(describing the Model as "the guess" and Prediction as "what it
built").

**Why it's conceptually wrong:** The point of this question is to
test *transfer* — can the student re-derive the pipeline's meaning in
a new setting, not just recite it. Four generic definitions divorced
from the scenario, even if individually correct, do not demonstrate
that transfer. The Model/Prediction swap is a common and important
misconception: the model is the thing built from learning; the
prediction is what that model produces for something new.

**Grading nuance:** This is the highest-value question on the
assessment (4 points) — spend real attention here. A student who gets
the order right, ties each stage to the scenario, but explains one
stage weakly should land at 3/4, not 4/4 or 2/4. Do not award full
credit for merely writing the four words correctly in order without
scenario-specific explanation.

---

## Question 4 — Traditional Programming vs. Machine Learning (3 points)

**What a full-credit answer demonstrates:**
- **(a)** Approach A = traditional programming.
- **(b)** Approach B = Machine Learning.
- **(c)** The key difference stated in the student's own words: a
  human explicitly writes the deciding logic in Approach A, versus the
  system learning the deciding logic from labeled examples in Approach
  B.

**Acceptable alternative reasoning:** Any phrasing that correctly
captures "who/what decides the rule" (a person vs. a learning process
using examples) is acceptable — exact wording is not required.

**Common wrong reasoning:** Reversing (a) and (b); or, for (c), a
vague answer like "one uses AI and one doesn't" without explaining
what that actually means in this scenario.

**Why it's conceptually wrong:** Reversing (a)/(b) suggests the
student hasn't internalized which approach corresponds to which
label — a meaningful gap, not a minor slip. A vague "one uses AI"
answer for (c) doesn't demonstrate the actual conceptual distinction
the whole class is built around.

**Grading nuance:** If (a) and (b) are both correct but (c) is weak,
this typically lands at 2/3, not 1/3 — the two identifications are
worth real credit on their own.

---

## Question 5 — Prediction Is Not Certainty (3 points)

**What a full-credit answer demonstrates:** A clear "No" — the mistake
does not mean the app wasn't using Machine Learning — **plus** an
explanation that a prediction is a best guess based on learned
patterns, not a guarantee, so a wrong guess is expected behavior, not
proof the system is "broken" or non-ML.

**Acceptable alternative reasoning:** A student may reasonably note
that the recommendation could have been a "reasonable guess for most
students, just not this one" — this is a sophisticated and fully
correct way of expressing best-guess-not-guarantee.

**Common wrong reasoning:** "Yes, this means it wasn't really using
Machine Learning" or "Yes, because if it was really learning, it
would always get it right."

**Why it's conceptually wrong:** This is the single most important
misconception Class 02 addresses. It conflates "uses learned patterns"
with "produces guaranteed-correct output" — the entire point of
Prediction ≠ Certainty is that these are different things.

**Grading nuance:** This question, along with Question 3, is a
priority signal for the class-level misconception check in the
Grading Workflow. A "Yes" answer here should be flagged regardless of
how well-written the rest of the submission is.

---

## Question 6 — Data Quality / An Unseen Case (3 points)

**What a full-credit answer demonstrates:** The student explains the
system might struggle, hesitate, or misclassify the motorbike (e.g.,
guess "delivery vehicle" because it's motorized, or guess "student's
ride" because it's smaller than a van, or simply state it's "unclear"
to the system) — **and** explicitly connects this to the fact that the
system only ever saw two narrow, very different categories of examples
during learning, with nothing resembling a motorbike in between.

**Acceptable alternative reasoning:** Either predicted outcome
(misclassifies as one category, or "the system would be confused/
unsure") is acceptable, as long as the *reasoning* ties back to the
limited/narrow training examples. There is no single "correct" guess
about which way it would misclassify — that's not what's being
graded.

**Common wrong reasoning:** "It would definitely get it right because
it's AI" or "it would definitely get it wrong" stated with no
reasoning at all; or an answer that doesn't reference what the system
did or didn't see during learning.

**Why it's conceptually wrong:** Confidence in either direction
without reasoning misses the point — the question is testing whether
the student can connect an unfamiliar case's outcome to the narrowness
of what the system learned from, not whether they can predict the
exact outcome.

**Grading nuance:** Do not require the word "bias" — it was
deliberately not taught this class and should not be expected or
rewarded above a plain-language explanation of the same idea.

---

## Question 7 — An Unfamiliar Application (2 points)

**What a full-credit answer demonstrates:** Reasonable, internally
consistent answers to all three sub-questions: plausible examples/data
(e.g., past patterns of how full each floor was at different times/
days), a plausible pattern (e.g., time of day, day of week, exam
season), and a plausible prediction/output (e.g., "Floor 3 is likely
to have free seats in the next half hour").

**Acceptable alternative reasoning:** Since this is an invented
scenario, there is no real system to be "right" or "wrong" about —
credit any internally consistent, conceptually sound chain of
reasoning across the three sub-questions.

**Common wrong reasoning:** Describing a rule-based approach instead
(e.g., "if it's before 9am, floor 3 is free") without any reference to
learning from past examples; or attempting to describe how a real
sensor/camera system would technically work.

**Why it's conceptually wrong:** A rule-based answer here suggests the
Traditional-vs-ML distinction (Question 4) hasn't fully transferred to
a new context — this is exactly the kind of "reverts to rule-based
thinking" pattern the Grading Workflow asks you to watch for across
the whole submission.

**Grading nuance:** Do not penalize a student for not knowing (and not
guessing at) how such a system would actually be built — the question
explicitly says this is a made-up example, and proprietary/technical
speculation is out of scope either way.

---

## Optional Reflection

Not scored. If a response reveals a specific, addressable point of
confusion, it's worth folding into your cohort-level notes (see
`Class_02_Assessment_Grading_Workflow.md`, Step 9) — but it must never
affect the numeric score.
