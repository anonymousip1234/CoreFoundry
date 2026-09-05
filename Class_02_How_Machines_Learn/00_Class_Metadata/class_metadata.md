# Class 02 — Metadata

**Bong Study Hub — Foundation Batch 2026**

This file is the single-source factual record for Class 02. Every later
artifact (Instructor Guide, Student Notes, Presentation, Pen-Tablet Plan,
Interaction Pack, Homework, Assessment, Cheat Sheet, Resources) must stay
consistent with what's defined here. If a future revision changes
anything below, update this file first, then propagate the change
downstream — never the other way around.

---

## Class Number

**02**

## Class Title

**How Machines Learn**

## Subtitle

**From Rules → Data → Intelligence**

## Target Audience

First-year college students, mixed backgrounds:

- Some students have never programmed.
- Some come from non-CS engineering branches.
- Some already know basic Python.
- Mathematical background cannot be assumed.

Class 02 must remain accessible to the same full spectrum of students
Class 01 was designed for — no student should feel newly excluded because
this class is "about AI."

## Prerequisites

**Class 01 — Welcome to Computer Science**, specifically the concepts it
established:

- What Computer Science is, and why it's broader than programming.
- What a program is; what programming means.
- What an algorithm is; Algorithm vs. Program.
- Input → Process → Output.
- Problem → Logic → Algorithm → Program → Result.
- Computational thinking.
- Why computers require precise instructions.
- The high-level learning staircase: Programming → Computer Science →
  Mathematics → Data → Machine Learning → Deep Learning → LLMs → Agents.

No additional prerequisite exists. Specifically: **no programming
experience, no mathematics beyond everyday arithmetic, and no prior
exposure to AI/ML concepts are required.**

## Estimated Duration

**Approximately 110–120 minutes** (matches Class 01's target-duration
philosophy; a compressed/expanded strategy should be defined in the
Master Instructor Guide the same way Class 01 defined 90/110/120-minute
versions).

## Short Description

Class 02 opens the AI arc of the program by answering one question
conceptually: when nobody can manually write a rule for every situation,
how can a machine still make a decision? Students discover, through
everyday examples and a hands-on cats-vs-dogs activity, that machines can
learn patterns from data instead of following hand-written rules — and
walk away with a simple, durable mental map of AI, Machine Learning, Deep
Learning, and Generative AI.

## Class Purpose

Class 01 gave students the mental model for *traditional* computing:
precise, human-written instructions that a computer executes exactly.
Class 02 exists to introduce the one idea that makes the rest of the
program's AI arc make sense: **some problems are too varied, too fuzzy,
or too large for a human to hand-write every rule — and machine learning
is the alternative that learns the "rule" from examples instead.**

This class is deliberately conceptual. It contains no code, no
mathematics, and no implementation detail. Its entire job is to install
one clear pipeline — `DATA → LEARNING → MODEL → PREDICTION` — as firmly
in students' minds as Class 01 installed `PROBLEM → LOGIC → ALGORITHM →
PROGRAM → RESULT`, and to show, through everyday examples, exactly where
that pipeline shows up in technology students already use.

## Learning Objectives

By the end of Class 02, a beginner should be able to explain, **in their
own words, informally**:

1. Why some problems can't realistically be solved by manually writing
   every rule.
2. The class's core question, and an answer to it in their own words.
3. The pipeline: Data → Learning → Model → Prediction.
4. The contrast between traditional programming (Input → Human-Written
   Rules → Output) and machine learning (Data → Learning → Model →
   Prediction).
5. At least two real-world examples of machine learning already present
   in daily life (e.g., spam detection, recommendations, maps/
   navigation, face unlock, generative AI).
6. How a system could learn to tell cats from dogs by seeing examples,
   rather than by following a hand-written rule list — using their own
   reasoning from the class's cats-vs-dogs activity.
7. A simple mental map relating Artificial Intelligence, Machine
   Learning, Deep Learning, and Generative AI to one another (broad to
   narrow), without memorizing formal definitions.
8. Why a prediction is not the same thing as a certainty.
9. Why poor data can lead to poor predictions.
10. Why "AI is not magic" — that AI systems have real, explainable
    limitations.
11. How this class connects to the learning staircase introduced in
    Class 01, and what's still ahead.

No formal mastery is expected. The bar is **conceptual understanding and
curiosity** — the same bar Class 01 set.

## Core Question

> **"How can a machine make a decision when nobody explicitly wrote the
> rule for every situation?"**

## Core Concept

```
DATA → LEARNING → MODEL → PREDICTION
```

## Key Concepts

- Traditional programming vs. machine learning as two different
  pipelines (`INPUT → RULES → OUTPUT` vs. `DATA → LEARNING → MODEL →
  PREDICTION`) — a direct extension of Class 01's Drawing 5.
- The provocation question: *"If we cannot manually write every rule for
  a problem, what alternative do we have?"* — leading naturally to
  machine learning.
- Everyday examples: spam detection, recommendation systems (movies,
  social media), maps/navigation, face unlock, generative AI (ChatGPT).
- The cats-vs-dogs activity: reasoning about patterns, data, and
  prediction through examples, without any code or math.
- A high-level mental map: Artificial Intelligence ⊃ Machine Learning ⊃
  Deep Learning, with Generative AI placed as a modern, prominent
  application area — introduced only as a map, not a taxonomy lecture.
- AI systems depend on data.
- Predictions are not the same thing as certainty.
- Poor data can lead to poor predictions.
- AI is not magic; AI systems have real limitations.

## Concepts Intentionally Deferred to Later Classes

Explicitly out of scope for Class 02 — these belong to Month 3
(Engineering + AI) or later, once programming and mathematical
foundations exist to support them:

- Python or any programming syntax.
- Neural network mathematics.
- Gradient descent / optimization.
- Transformers.
- Embeddings.
- Retrieval-Augmented Generation (RAG).
- AI agents.
- Prompt engineering, beyond a passing conceptual mention of what a
  "prompt" is (already touched in Class 01's AI bridge).
- Statistical/mathematical formalism of learning (loss functions,
  probability theory, evaluation metrics such as precision/recall).
- Model training implementation of any kind.
- Deep AI ethics (bias, fairness, safety, policy) — Class 02 only
  establishes the conceptual foundation ("poor data → poor predictions,"
  "AI is not magic") that a later, dedicated ethics discussion will
  build on.

## Teaching Philosophy

Identical in spirit to Class 01, applied to AI-specific material:

- Intuition before terminology.
- Example before formal definition.
- Ask before explaining.
- Use real-world, everyday examples students already have direct
  experience with.
- Never assume mathematics or programming knowledge.
- Never overwhelm students with AI terminology — a small, durable
  vocabulary beats a large, forgettable one.
- The goal is conceptual understanding, not implementation.

## Expected Student Outcome

- A **beginner** should leave thinking: *"I finally understand why
  Netflix recommendations and spam filters aren't just giant lists of
  rules someone wrote — they're learned from examples, the same way I'd
  learn to recognize a cat after seeing enough of them."*
- A **stronger student** should leave thinking: *"There's real depth
  underneath 'learning from data' — I can already see why the next
  classes need mathematics and more structured data to go further."*

The class should reduce the "AI is mysterious/magic" reaction and replace
it with grounded curiosity — the same emotional arc Class 01 built for
programming, now extended to AI.

## Relationship to Class 01

Class 02 is the direct continuation of Class 01's closing "staircase"
moment. Class 01 explicitly told students: *"We are not going to jump to
the bottom. We are going to build the staircase."* Class 02 is the first
real step onto that staircase's AI arc — but it stays strictly
conceptual, matching the same step-by-step philosophy: no code, no math,
just the next layer of intuition.

Every structural element of Class 01 is reused, not reinvented:
- The `PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT` chain is echoed by
  `DATA → LEARNING → MODEL → PREDICTION` as a parallel, not a
  replacement.
- The "ask before explaining" and "example before definition" teaching
  loop carries over unchanged.
- The AI/ML/GenAI comparison briefly introduced in Class 01 (Drawing 5,
  "Traditional Programming vs. ML vs. Generative AI") is the direct seed
  Class 02 grows from — Class 02 should feel like picking that thread
  back up, not starting a new one.

**Note for whoever writes the Master Instructor Guide:** Class 01's own
four-month roadmap slide placed AI/ML under "Month 3 — Engineering + AI."
Class 02 arrives immediately after Class 01, which means the program is
choosing to give students an early, deliberately non-technical conceptual
preview of the AI arc before returning to Month 1/2 foundations
(programming, C, DSA, SQL). The Instructor Guide should address this
explicitly and briefly — framing Class 02 as "a preview from the top of
the staircase, looking down" rather than silently contradicting the
roadmap students were just shown.

## Suggested Class Success Metric

Class 02 is successful if, without prompting, most students can:

1. Explain *why* a machine learning approach was necessary for at least
   one of the class's real-world examples (not just name the example).
2. Correctly state the Data → Learning → Model → Prediction chain, and
   distinguish it from Input → Rules → Output — in their own words,
   without needing exact terminology.
3. Give a plausible, reasoned answer for how a system could learn to
   tell cats from dogs apart from examples, referencing the in-class
   activity.
4. State at least one reason predictions aren't certainties, and one
   reason AI has limitations.

Success is measured by these four outcomes — not by how much AI
terminology students can recite. A class where every student can do
1–3 confidently, even if a formal definition of "Machine Learning" is
shaky, has succeeded.
