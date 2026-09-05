# Class 02 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** How Machines Learn
**Subtitle:** From Rules → Data → Intelligence
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisite:** Class 01 — Welcome to Computer Science

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01](#3-relationship-to-class-01)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening — 0 to 10 Minutes](#8-opening--0-to-10-minutes)
9. [What Is AI?](#9-what-is-ai)
10. [AI Around Us](#10-ai-around-us)
11. [Traditional Programming](#11-traditional-programming)
12. [The Rule Problem](#12-the-rule-problem)
13. [Introducing Machine Learning](#13-introducing-machine-learning)
14. [The Core Pipeline](#14-the-core-pipeline)
15. [Cats-vs-Dogs Activity](#15-cats-vs-dogs-activity)
16. [Prediction ≠ Certainty](#16-prediction--certainty)
17. [AI Is Not Magic](#17-ai-is-not-magic)
18. [AI / ML / Deep Learning / Generative AI](#18-ai--ml--deep-learning--generative-ai)
19. [Return to the Learning Staircase](#19-return-to-the-learning-staircase)
20. [Recap](#20-recap)
21. [Exit Check](#21-exit-check)
22. [Homework Bridge](#22-homework-bridge)
23. [Differentiation](#23-differentiation)
24. [Common Misconceptions](#24-common-misconceptions)
25. [Instructor Language Guardrails](#25-instructor-language-guardrails)
26. [Pen-Tablet Moments](#26-pen-tablet-moments)
27. [Slide Relationship](#27-slide-relationship)
28. [Time Management](#28-time-management)
29. [90-Minute Version](#29-90-minute-version)
30. [120-Minute Version](#30-120-minute-version)
31. [Classroom Management](#31-classroom-management)
32. [Advanced Question Parking Lot](#32-advanced-question-parking-lot)
33. [Teacher FAQ](#33-teacher-faq)
34. [Class Success Check](#34-class-success-check)
35. [Post-Class Reflection Prompts](#35-post-class-reflection-prompts)
36. [Source-of-Truth / QA Section](#36-source-of-truth--qa-section)

---

## 1. Class Identity

| Field | Value |
|---|---|
| Class number | 02 |
| Title | How Machines Learn |
| Subtitle | From Rules → Data → Intelligence |
| Audience | First-year college students, mixed backgrounds — some have never programmed, some are from non-CS branches, some already know basic Python. No mathematics background can be assumed. |
| Prerequisites | Class 01 — Welcome to Computer Science (Problem → Logic → Algorithm → Program → Result; Input → Process → Output; the learning staircase). No programming, no math beyond arithmetic, no prior AI/ML exposure required. |
| Duration | ~110–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 01 installed the mental model of *traditional* computing: precise, human-written instructions a computer executes exactly. Class 02 introduces the one idea that makes the rest of the program's AI arc make sense — some problems are too varied, fuzzy, or large for a human to hand-write every rule, and machine learning is the alternative that learns the "rule" from examples instead. |
| Core question | **"How can a machine make a decision when nobody explicitly wrote the rule for every situation?"** |
| Core concept | `DATA → LEARNING → MODEL → PREDICTION` |
| Class success metric | Without prompting, most students can: (1) explain *why* ML was necessary for at least one real-world example — not just name it; (2) correctly state Data → Learning → Model → Prediction and distinguish it from Input → Rules → Output, in their own words; (3) give a plausible, reasoned answer for how a system could learn cats from dogs, referencing the in-class activity; (4) state one reason predictions aren't certainties and one reason AI has limitations. |

This class is entirely conceptual. **No code. No mathematics. No
implementation.** If you ever feel tempted to explain *how* something
works at a technical level, that's the signal to simplify further, not to
go deeper.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one sentence in a student's head with another.
Before this class: *"Computers only do exactly what a programmer typed
in."* After this class: *"Computers can also learn a pattern from
examples, when no one could realistically type in a rule for every
case."* That's it. Everything else in this guide — the examples, the
activity, the taxonomy map — exists in service of landing that one
replacement cleanly.

**Teaching philosophy, in one line:** intuition before terminology,
example before definition, ask before explaining, everyday examples over
invented ones. Identical in spirit to Class 01, now aimed at AI-shaped
material instead of programming-shaped material.

**What students should feel by the end:**

- A beginner should feel: *"I finally understand why Netflix
  recommendations and spam filters aren't just giant lists of rules
  someone wrote — they're learned from examples, the same way I'd learn
  to recognize a cat after seeing enough of them."*
- A stronger student should feel: *"There's real depth underneath
  'learning from data' — I can already see why the next classes need
  mathematics and structured data to go further."*
- Everyone should feel a *reduction* in the "AI is mysterious/magic"
  reaction, replaced with grounded curiosity — not awe, not fear.

**State this to yourself before you walk in, and to students if it's ever
useful mid-class:**

> This is **not** a class about becoming an AI engineer. Nobody in this
> room is training a model today. This is the first conceptual doorway
> into AI — the same way Class 01 was the first conceptual doorway into
> programming. Doorways don't require tools; they require a shift in how
> you see something you already use every day.

If a section ever drifts toward "how would I actually build this," pull
it back to "how would I *reason about* this" — that redirect is always
available and is never a cop-out; it's the actual scope of the class.

---

## 3. Relationship to Class 01

Class 01 built one chain and one closing image:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

...and ended on the **learning staircase**: `Programming → Computer
Science → Mathematics → Data → Machine Learning → Deep Learning → LLMs →
Agents`, with the line *"we are not going to jump to the bottom, we are
going to build the staircase."* Class 02 is the first real step onto that
staircase's AI side — but it stays at the same conceptual altitude Class
01 taught at. No code, no math, just the next layer of intuition.

The two pipelines are **parallel, not competing**:

```
TRADITIONAL PROGRAMMING:   INPUT  →  HUMAN-WRITTEN RULES  →  OUTPUT
MACHINE LEARNING:          DATA   →  LEARNING  →  MODEL   →  PREDICTION
```

Traditional programming answers *"I know the rule, I just need to
express it precisely."* Machine learning answers a different question:
*"I don't have a rule I can write down — can the machine find one from
examples instead?"* The second pipeline doesn't replace the first — most
real software still runs on Input → Rules → Output. Class 02 is about the
narrower, important slice of problems where that approach breaks down.

**The roadmap issue — address this honestly, briefly, once:**

Class 01's own four-month roadmap slide placed AI/ML under *"Month 3 —
Engineering + AI,"* after Python, C, DSA, and SQL. Class 02 arrives as
the very next class instead. Don't let this sit as a silent contradiction
— name it, in one breath, early in the class (Section 8 or 19 are good
spots):

> "Quick honesty check — last class's roadmap put AI under Month 3, after
> programming and CS foundations. So why are we talking about AI in
> Class 2? Because this isn't Month 3's AI class. Think of today as
> standing at the *top* of the staircase for ten seconds and looking
> down, before we go back to building it step by step. You're not
> learning to build AI today — you're learning what question AI actually
> answers, so that every step between here and Month 3 has a destination
> you can already picture."

Say this like a reasonable design choice, because it is one — not an
apology, not a disclaimer that undercuts the class.

---

## 4. Learning Objectives

Taken directly from `class_metadata.md`. For each, the bar is
**conceptual understanding and curiosity** — the same bar Class 01 set.
Nothing here needs to survive an exam.

| # | Objective | What students need to understand | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|---|
| 1 | Why some problems can't realistically be solved by manually writing every rule | That variety, scale, and fuzziness can make rule-writing impractical, not impossible in principle | Can say, in their own words, "there'd be too many rules" or "language/cases change too much" for a given example | Any formal notion of complexity, combinatorics, or "rule explosion" as a technical term |
| 2 | The class's core question, and an answer in their own words | The question itself, and that the answer is "learn from data instead" | Can restate the question and give the one-line answer | Precise wording match to the metadata phrasing |
| 3 | The pipeline: Data → Learning → Model → Prediction | What each of the four words stands for, in plain terms | Can name all four in order and describe each in one sentence | Any notion of what happens mathematically inside "Learning" |
| 4 | Contrast: Input → Rules → Output vs. Data → Learning → Model → Prediction | These are two different strategies for getting a computer to produce an output | Can say which strategy fits which kind of problem, with a reason | Formal criteria for choosing one over the other |
| 5 | Two real-world ML examples from daily life | That spam filters, recommendations, maps, face unlock, and generative AI all rely on learned patterns, not hand-written rules | Can name two and gesture at "it learned from examples" for each | Any detail of what data or algorithm each system actually uses |
| 6 | Reasoning through cats-vs-dogs | A system can tell cats from dogs by noticing patterns across many labeled examples, not by following a rule list | Can explain, using their own words from the activity, how seeing many examples could produce a guess about a new one | Any notion of feature vectors, classifiers, or algorithms by name |
| 7 | Simple mental map: AI, ML, Deep Learning, Generative AI | Broad-to-narrow relationship, and where Generative AI sits as a modern application area | Can order the four broad-to-narrow and place GenAI without hesitation | Formal definitions of any of the four terms |
| 8 | Prediction ≠ certainty | A model's output is a best guess based on learned patterns, and best guesses can be wrong | Can give one example of a prediction that could plausibly be wrong | Probability, confidence scores, or accuracy as formal concepts |
| 9 | Poor data → poor predictions | The patterns a model learns can only be as good as the examples it saw | Can explain, informally, why bad or biased examples would produce bad guesses | Formal notions of bias, fairness, or dataset statistics |
| 10 | "AI is not magic" — real, explainable limitations | AI systems are built from data and learned patterns, not mysterious intelligence | Can state one concrete reason an AI system might fail | Deep AI safety, policy, or ethics discussion |
| 11 | Connection to the Class 01 learning staircase | Today was a preview from the top of the staircase; the steps underneath still need to be built | Can explain, in one sentence, why this class came before the programming/math steps that support it | Any specific content of the later staircase steps |

---

## 5. Key Terminology

Small and durable beats large and forgettable. These are the **only**
terms this class needs.

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Artificial Intelligence (AI)** | The broad field of building computer systems that do things which normally seem to need human-like intelligence — recognizing, deciding, predicting, generating. | "The umbrella field." | "Computers that think or feel like humans." | Name only, loosely |
| **Machine Learning (ML)** | An approach where a computer gets better at a task by finding patterns in examples, instead of following rules a human typed in. | "Learning from data instead of hand-written rules." | "The computer decides things on its own, like a person." | Yes — core term |
| **Data** | The examples we show the system — like a pile of labeled cat and dog photos. | "The examples." | Any mention of structured/unstructured data types. | Yes |
| **Learning** *(the process)* | The process of looking at many examples and picking out useful patterns that separate one kind of thing from another. | "Finding useful patterns in the data." | "Learning exactly like a human brain does," gradient descent, training loops. | Loosely |
| **Model** | What comes out of the learning process — something that has picked up patterns from the data and can now be used on new examples. | "What the system builds after looking at the examples." | "A mathematical function," "weights," "parameters." | Yes |
| **Prediction** | The model's best guess about a new example it hasn't seen before, based on the patterns it learned. | "Its best guess." | "The final truth," "guaranteed correct." | Yes |
| **Pattern** | Something that shows up repeatedly across examples and helps tell one category from another. | "Something the examples have in common." | "Feature vector," "feature engineering." | No — used conversationally |
| **Rule** *(contrast term)* | An explicit instruction a human writes, e.g. "if the email contains the word 'free', mark it spam." | "Something a person had to think of and type in themselves." | — | No |
| **Deep Learning** | A more powerful, layered style of machine learning, often used for very complex patterns like images, speech, and language. | "A stronger form of machine learning, good at very complex patterns." | Neural network math, layers, neurons, backpropagation. | Name/position only |
| **Generative AI** | AI systems — like ChatGPT — that don't just predict a category, but generate new content: text, images, and more. | "AI that creates new content instead of just picking a category." | Transformers, embeddings, tokens. | Name/position only |

---

## 6. Class at a Glance

Canonical **110-minute** flow. (Section 29 and 30 give the 90- and
120-minute deltas.) Timings are the reference arc supplied for this
class, refined slightly for realism — the overall arc and every
non-negotiable moment is preserved.

| Time | Dur. | Section | Objective | Teaching mode | Slides | Pen-tablet | Interaction | Expected student state |
|---|---|---|---|---|---|---|---|---|
| 0–8 | 8 | Opening + AI perception | Activate existing AI experience, raise curiosity | Ask → collect → frame | Minimal (1 title slide) | None yet | High — cold-open questions | Curious, a little unsure where this is going |
| 8–19 | 11 | What is AI? | Working, non-philosophical notion of AI | Ask → build together | Light | None | Medium | Oriented, not yet committed to a definition |
| 19–31 | 12 | AI around us | See ML already present in daily tools | Ask → example → explain | Medium (example images/icons) | Optional light sketch per example | High | "Oh — I already use this" |
| 31–43 | 12 | Traditional programming | Recall/extend Input→Rules→Output to a concrete case | Ask → build rules together | Light | Drawing #2 | High | Confident — this feels familiar from Class 01 |
| 43–59 | 16 | The rule problem | Feel the limitation of hand-written rules directly | Escalate → struggle → reflect | Minimal | Drawing #3 | Very high | Slightly stuck — productively so |
| 59–70 | 11 | Introducing Machine Learning | First naming of ML as the alternative | Ask → reveal → explain | Light | None yet | Medium-high | Relieved — "there's an answer" |
| 70–78 | 8 | **The Core Pipeline** *(hero)* | Install Data→Learning→Model→Prediction | Build live, one box at a time | Minimal | **Drawing #4 (built live)** | High | Watching closely, anchoring the term |
| 78–90 | 12 | **Cats-vs-Dogs Activity** *(hero)* | Reason through the pipeline concretely | Facilitated activity | Example images | Light — record student answers | Very high | Engaged, reasoning aloud, a little playful |
| 90–95 | 5 | Prediction ≠ certainty | Predictions are best guesses, not truths | Ask → explain | Minimal | None | Medium | Realistic, not disillusioned |
| 95–99 | 4 | AI is not magic | Data quality → prediction quality; real limitations | Explain → connect | Minimal | Reuse Drawing #4 | Medium | Grounded |
| 99–104 | 5 | AI/ML/DL/GenAI map | Orientation, not taxonomy | Build map live | Light | Drawing #5 | Medium | Oriented, not quizzed |
| 104–107 | 3 | Return to the learning staircase | Reconnect to Class 01's closing image | Explain + connect | Reuse staircase visual | Drawing #6 (reuse/extend) | Low-medium | "This all connects" |
| 107–110 | 3 | Recap + exit check + homework bridge | Consolidate, verify, hand off | Ask → students answer | Minimal | None | High | Leaving with 1–2 clear sentences they can repeat |

**Non-negotiable blocks** (never compressed away — see Section 28): The
Rule Problem, Introducing Machine Learning → Core Pipeline hand-off, the
Core Pipeline itself, Cats-vs-Dogs, Prediction ≠ Certainty, Recap.

---

## 7. Section-by-Section Teaching Guide

Full **A–O** breakdown for every block in Section 6. Sections 8–22 below
give **additional, deeper** material for the blocks the class design
calls out as hero moments or facilitator-guide-worthy — treat those as
extensions of the same block's entry here, not a repeat.

### 7.1 Opening + AI Perception (0–8)

- **A. Purpose:** Activate lived experience with AI before naming the field.
- **B. Learning objective:** Students recognize they already interact with AI daily, without yet defining it.
- **C. Instructor goal:** Curiosity, not a definition, by minute 8.
- **D. What the instructor says:** Open with a relatable, concrete moment — "You open Instagram/YouTube/Netflix and it already seems to know what you'll want to watch next. Ever wondered how?"
- **E. What the instructor asks:** "Where have you noticed something 'smart' like this in an app you use daily?" Then: "You use AI every day — but how does a computer actually know what to recommend, recognize, or predict?"
- **F. Expected student responses:** Netflix/YouTube/Instagram recommendations, Google Maps, ChatGPT, Face unlock, autocorrect.
- **G. Follow-up questions:** "How do you think it knows that, though — did someone write a rule for every single person?"
- **H. Common misconceptions:** "It's just programmed to do that" (true but circular — doesn't yet distinguish rules from learning).
- **I. How to respond:** Don't correct yet — bank the answer: "Hold that thought, we're going to open that box today."
- **J. Pen-tablet action:** None yet — keep hands free for full attention on the room.
- **K. Slide support:** One simple title slide only; do not put the core question on a slide yet — say it live.
- **L. Transition:** "To answer that, let's first get clear on what 'AI' even means — not the sci-fi version, the real one."
- **M. Time checkpoint:** Should be moving into Section 9 by minute 8.
- **N. Optional compression:** Drop to 2–3 examples collected instead of open-ended collection (see Section 29).
- **O. Optional expansion:** Let 1–2 more students describe an experience in more detail (see Section 30).

*(Full opening design in Section 8.)*

### 7.2 What Is AI? (8–19)

- **A. Purpose:** Land a usable, non-philosophical working notion of AI.
- **B. Learning objective:** Students can describe AI as "computers doing tasks that seem to need intelligence" without needing a textbook definition.
- **C. Instructor goal:** Avoid both over-simplification ("AI = robots") and over-formalization (any academic definition).
- **D. What the instructor says:** "AI is our word for computer systems built to do things that normally seem to require some kind of intelligence — recognizing a face, recommending a movie, answering a question."
- **E. What the instructor asks:** "Based on that, is a calculator AI? Is a thermostat? Is a chess app that always plays the same fixed moves?"
- **F. Expected student responses:** Mixed — some say yes to all, some say no to all; disagreement is useful here.
- **G. Follow-up questions:** "What's different between a calculator following one fixed formula, and Netflix guessing what *you specifically* might like?"
- **H. Common misconceptions:** "AI = robots / sci-fi machines"; "AI means the computer is conscious/thinking."
- **I. How to respond:** Redirect to task, not appearance: "Forget robots for a second — AI today mostly lives inside apps you already use, with no body at all."
- **J. Pen-tablet action:** None required; optional one-word board note ("AI = tasks that seem to need intelligence").
- **K. Slide support:** One slide with 3–4 icons (chatbot, camera/face, recommendation feed, map) — no formal definition text.
- **L. Transition:** "Let's actually go look at where this shows up in things you use every single day."
- **M. Time checkpoint:** Wrap by minute 19.
- **N. Optional compression:** Skip the calculator/thermostat debate; state the working notion directly (Section 29).
- **O. Optional expansion:** Let the calculator-vs-Netflix debate run longer; it previews the rules-vs-learning contrast nicely (Section 30).

*(Full teaching notes in Section 9.)*

### 7.3 AI Around Us (19–31)

- **A. Purpose:** Ground AI in concrete, everyday, approved examples.
- **B. Learning objective:** Name at least two real-world ML-powered systems and describe input/output for each.
- **C. Instructor goal:** Build a shared example bank the rest of the class (especially the rule problem) will draw from.
- **D. What the instructor says:** For each example, describe it before naming the mechanism: "Think about Google Maps picking a route — what is it looking at, and what does it hand back to you?"
- **E. What the instructor asks:** Per example — "What does the system receive? What does it produce? Why is that interesting/hard?"
- **F. Expected student responses:** Spam filters catch junk mail; Netflix/Spotify suggest content; Maps picks routes/predicts traffic; Face unlock recognizes owners; ChatGPT answers in natural language.
- **G. Follow-up questions:** "Do you think someone sat down and wrote a rule for every possible spam email? Every possible good movie recommendation for every person?"
- **H. Common misconceptions:** "Someone just programmed it to know that" (again circular — plant the seed, don't resolve yet).
- **I. How to respond:** "Hold onto that question — it's exactly where we're headed next."
- **J. Pen-tablet action:** Optional: list the 4–5 examples as a simple bullet column while discussing.
- **K. Slide support:** One slide per example with an icon/screenshot-style graphic; keep text minimal.
- **L. Transition:** "So all of these look like magic from the outside. Let's try to actually build one — starting with something simple: a spam filter."
- **M. Time checkpoint:** Wrap by minute 31.
- **N. Optional compression:** Use 3 examples (spam, recommendations, face unlock) instead of 5 (Section 29).
- **O. Optional expansion:** Add a 6th example students suggest themselves; ask each table/breakout to share one they use (Section 30).

*(Full example-by-example breakdown in Section 10.)*

### 7.4 Traditional Programming (31–43)

- **A. Purpose:** Re-anchor Input → Rules → Output from Class 01, applied to a concrete new case (spam).
- **B. Learning objective:** Students can propose explicit rules for a rule-based spam filter.
- **C. Instructor goal:** Let students feel ownership of "the rules" before the rules are shown to fail.
- **D. What the instructor says:** "Remember Class 1 — Input → Process → Output? In traditional programming, the 'Process' box is rules a human wrote. Let's write spam-filter rules together, right now."
- **E. What the instructor asks:** "If you were building a spam filter by hand, what's your first rule?"
- **F. Expected student responses:** "If email contains 'free' → spam"; "if sender is unknown → spam"; "if it has too many exclamation marks → spam"; "if it asks for money → spam."
- **G. Follow-up questions:** "Great — what if a legitimate email from your bank says 'your loan offer'? Would your rule wrongly flag it?"
- **H. Common misconceptions:** Believing a handful of keyword rules would work well in general.
- **I. How to respond:** Don't shoot the idea down yet — let it stand as a real, reasonable first attempt; the next section is where it strains.
- **J. Pen-tablet action:** Drawing #2 — Input → Rules → Output, filled with the spam example live.
- **K. Slide support:** None needed — this should be entirely built on the board from student answers.
- **L. Transition:** "This is a great start. Let's now throw more real-world emails at it and see how far these rules actually get us."
- **M. Time checkpoint:** Wrap by minute 43.
- **N. Optional compression:** Cap rule collection at 3 rules instead of open-ended (Section 29).
- **O. Optional expansion:** Ask students to also write one rule for a *different* domain (e.g., recommending movies by genre) to show the pattern generalizes (Section 30).

*(Full teaching notes in Section 11.)*

### 7.5 The Rule Problem (43–59) — NON-NEGOTIABLE

- **A. Purpose:** Make the limits of hand-written rules a felt experience, not an assertion.
- **B. Learning objective:** Explain, unprompted, why manual rules struggle at scale/variety.
- **C. Instructor goal:** Let the rules the class just wrote visibly break.
- **D. What the instructor says:** Introduce escalating counter-examples one at a time, pausing after each: "Here's a real spam email that doesn't contain 'free' or '$'. Does your rule catch it? Here's a legitimate email that *does* contain 'free' — does your rule wrongly block it?"
- **E. What the instructor asks:** "How many rules do you think you'd need to catch every kind of spam, in every language, written by people constantly changing their wording to dodge filters?" then, after letting the number climb: "If humans cannot realistically write every rule, what could we give the computer instead?"
- **F. Expected student responses:** "Hundreds"; "thousands"; "it's impossible to list them all"; eventually — after the prompt — some version of "show it examples" or "let it figure out the pattern itself."
- **G. Follow-up questions:** "What happens when spammers change their wording specifically to dodge your rules?" "Could you write one rule that works in every language your users write in?"
- **H. Common misconceptions:** "You'd just need more rules" (true but reveals the scale problem rather than solving it); "programmers just think of all the cases in advance" (real software still misses cases constantly).
- **I. How to respond:** Let the escalating count do the convincing — don't argue against "more rules," just keep supplying cases that need yet another rule, until the room feels the growth.
- **J. Pen-tablet action:** Drawing #3 — informally sketch "rule explosion" as a rapidly branching/crowded list, not a technical diagram.
- **K. Slide support:** None — this section should feel entirely live and unscripted.
- **L. Transition:** Once a student proposes "show it examples" or similar — "That instinct has a name. Let's build it properly."
- **M. Time checkpoint:** This is the longest single block (16 min) — protect it; do not let it run under 13.
- **N. Optional compression:** Use 3 escalating counter-examples instead of 5–6 (Section 29) — the felt struggle is what matters, not the count.
- **O. Optional expansion:** Let students try to patch their own rules live for 2–3 more rounds before revealing the alternative — the longer they struggle productively, the more Section 13 lands (Section 30).

*(Full teaching notes in Section 12 — this is a major teaching moment.)*

### 7.6 Introducing Machine Learning (59–70)

- **A. Purpose:** Name Machine Learning only now that its necessity has been felt.
- **B. Learning objective:** State, informally, "give examples instead of rules, let the machine find the pattern."
- **C. Instructor goal:** Careful wording — no anthropomorphizing.
- **D. What the instructor says:** "Instead of manually writing every rule, what if we gave the computer a large pile of examples — emails already labeled 'spam' or 'not spam' — and let a learning process figure out useful patterns on its own? That's Machine Learning."
- **E. What the instructor asks:** "What do you think 'learning a pattern' from examples actually means, compared to being told a rule directly?"
- **F. Expected student responses:** "It looks at a lot of examples and notices what spam emails have in common"; some will still say "it thinks like us" — flag for correction.
- **G. Follow-up questions:** "Does the machine need to *understand* spam the way you do, or just notice what tends to go together?"
- **H. Common misconceptions:** "The machine learns exactly like a human brain"; "it understands meaning."
- **I. How to respond:** Use the guardrail language from Section 25: "Think of learning here as finding useful patterns in data — not understanding the way you do."
- **J. Pen-tablet action:** None yet — save the drawing for the pipeline reveal next.
- **K. Slide support:** One slide, bare: "Machine Learning" — no bullet-point definition dump.
- **L. Transition:** "Let's actually build out what 'learning from examples' looks like, step by step."
- **M. Time checkpoint:** Wrap by minute 70 to protect the Core Pipeline block.
- **N. Optional compression:** Shorten to a single clean statement + one check-in question (Section 29).
- **O. Optional expansion:** Add a second worked mini-example (e.g., movie recommendations) before the pipeline reveal (Section 30).

*(Full teaching notes in Section 13.)*

### 7.7 The Core Pipeline (70–78) — NON-NEGOTIABLE, HERO MOMENT

See full live-build sequence in Section 14. Summary:

- **A. Purpose:** Install `DATA → LEARNING → MODEL → PREDICTION` as durably as Class 01 installed its five-box chain.
- **B. Learning objective:** Name all four stages, in order, and describe each in one sentence.
- **C. Instructor goal:** Build it live, box by box, with a question before each addition — never reveal it finished.
- **J. Pen-tablet action:** Drawing #4 — the single most important drawing of the class.
- **M. Time checkpoint:** Do not compress below 7 minutes even under time pressure.

### 7.8 Cats-vs-Dogs Activity (78–90) — NON-NEGOTIABLE, HERO ACTIVITY

Full facilitator guide in Section 15. Summary:

- **A. Purpose:** Let students *reason through* the pipeline concretely, without code or math.
- **B. Learning objective:** Explain how a system could learn to tell cats from dogs from examples.
- **M. Time checkpoint:** Protect at least 10 minutes even in the 90-minute version.

### 7.9 Prediction ≠ Certainty (90–95) — NON-NEGOTIABLE

- **A. Purpose:** Prevent the misconception that model output equals truth.
- **B. Learning objective:** State one reason a prediction can be wrong.
- **C. Instructor goal:** Land this before "AI is not magic," using the cats-vs-dogs ambiguous example as the anchor.
- **D. What the instructor says:** "A model gives its best guess based on patterns it has learned — not a guarantee. Remember the ambiguous cat/dog picture from the activity? That's exactly this."
- **E. What the instructor asks:** "Can you think of a time a recommendation app suggested something completely wrong for you? Why do you think that happened?"
- **F. Expected student responses:** "Yes, all the time — it recommended something totally unrelated"; "autocorrect changes a word to the wrong one."
- **G. Follow-up questions:** "So was the app 'broken,' or did it just make a reasonable guess that happened to be wrong?"
- **H. Common misconceptions:** "If it's wrong, it must be broken/badly built."
- **I. How to respond:** "A wrong guess isn't the same as a broken system — even people make reasonable guesses that turn out wrong."
- **J. Pen-tablet action:** None new — point back at Drawing #4's "Prediction" box.
- **K. Slide support:** None needed.
- **L. Transition:** "This connects to a bigger idea — AI isn't magic, and it has real limits. Let's name them."
- **M. Time checkpoint:** Wrap by minute 95.
- **N. Optional compression:** Fold directly into Section 7.10 as one continuous idea (Section 29).
- **O. Optional expansion:** Collect 2–3 student anecdotes instead of 1 (Section 30).

*(Full teaching notes in Section 16.)*

### 7.10 AI Is Not Magic (95–99)

- **A. Purpose:** Ground AI as dependent on data, not mysterious.
- **B. Learning objective:** State that poor data can lead to poor predictions.
- **C. Instructor goal:** Keep this short, concrete, and non-preachy — not an ethics lecture.
- **D. What the instructor says:** "Everything comes back to the pipeline. If the data going in is limited, one-sided, or wrong, the patterns learned — and the predictions — will be too. Garbage in, garbage out, just like any other system."
- **E. What the instructor asks:** "If a spam filter only ever saw English emails, what do you think would happen when it meets an email in Bengali?"
- **F. Expected student responses:** "It would probably fail / get confused / not know what to do."
- **G. Follow-up questions:** "So is that the AI being 'dumb,' or is that the *data* being incomplete?"
- **H. Common misconceptions:** "AI should just automatically know everything."
- **I. How to respond:** "AI systems only know what their examples showed them — nothing more, nothing magic."
- **J. Pen-tablet action:** Reuse Drawing #4; annotate "Data" box with "→ if this is limited, everything downstream is too."
- **K. Slide support:** None needed.
- **L. Transition:** "Now that you understand what AI actually is and isn't, let's zoom out and see how all the AI terms you've heard fit together."
- **M. Time checkpoint:** Wrap by minute 99.
- **N. Optional compression:** State it as a single connected idea with Section 7.9 (Section 29).
- **O. Optional expansion:** Add a second example beyond language (e.g., a face-unlock system only trained on limited examples) (Section 30).

*(Full teaching notes in Section 17.)*

### 7.11 AI/ML/DL/GenAI Map (99–104)

Full notes in Section 18. Build the nested map live (Drawing #5); explicitly frame it as orientation, not taxonomy to memorize.

### 7.12 Return to the Learning Staircase (104–107)

Full notes in Section 19. Reuse/extend the Class 01 staircase image; deliver the "preview from the top, looking down" framing from Section 3.

### 7.13 Recap + Exit Check + Homework Bridge (107–110) — NON-NEGOTIABLE

Full notes in Sections 20–22.

---

## 8. Opening — 0 to 10 Minutes

Do **not** open with "Today we will learn Artificial Intelligence." Open
with lived experience, exactly as Class 01 opened with smartphone use
rather than a CS definition.

**Exact opening approach:**

1. Start conversational, not slide-first: *"Quick show of hands — who
   used Instagram, YouTube, Netflix, or Google Maps in the last 24
   hours?"* (expect nearly every hand)
2. *"Now — how many of you have actually thought about how it knows what
   to show you, or which route to pick?"* (expect very few hands — that's
   the point, mirroring Class 01's "how many actually know what happens
   inside" beat)
3. Land the framing question: **"You use AI every day. But how does a
   computer actually know what to recommend, recognize, or predict?"**
4. Collect 2–4 quick answers without correcting any of them yet.
5. Bridge: *"By the end of today, you'll be able to answer that yourself
   — and you'll have actually reasoned through a working example."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "What app on your phone feels like it 'just knows' what you want?" | Instagram/YouTube/TikTok feed, Netflix, Spotify, Google Maps | Name one yourself first: "I'll go first — Spotify's Discover Weekly always creeps me out a little. Anyone else?" |
| "How do you *think* it knows that?" | "It's programmed to"; "it tracks what I watch"; silence | Reframe smaller: "Did someone sit and write a rule just for *you*, specifically? Or something else?" |

**How to handle silence:** Never let a question hang more than ~5–7
seconds unaddressed — rephrase narrower, or answer it yourself briefly
and toss it back ("I'll start us off... now can someone else add one?").
Cold-calling gently by row/name is acceptable here since the questions
are low-stakes (no wrong answers yet).

**Transition into the class question:** Once 2–3 answers land, say the
core question aloud, slowly, and let it sit for a second before moving
on: *"How can a machine make a decision when nobody explicitly wrote the
rule for every situation? That's exactly what we're going to figure out
today."*

---

## 9. What Is AI?

Do not begin with a textbook definition. Build toward: **machines
performing tasks that appear to require some form of intelligence.**

**Usable instructor explanation (say close to this):**

> "For today, let's use a simple working idea: Artificial Intelligence is
> our name for computer systems built to do things that normally seem to
> require some kind of intelligence — recognizing a face, recommending a
> movie, understanding a sentence, predicting traffic. It's not about
> robots, and it's not about whether the computer is 'really' thinking —
> we're not going to get into that debate today. It's about the *kind of
> task* being done."

Explicitly avoid philosophical debates about consciousness or whether
machines are "truly" intelligent — if a student raises it, acknowledge
and park it (see Section 32), don't engage it in depth.

**Light interactive check:** "Is a basic calculator AI? A thermostat that
turns on at a fixed temperature? A chess app that always plays the exact
same fixed moves?" Most students will say no to all three once they think
about it — use that to sharpen the working idea: fixed, unchanging
behavior for every input isn't what people mean by AI; systems that
adapt their output based on patterns in what they've seen are closer to
it. This sets up Section 12 perfectly without naming ML yet.

---

## 10. AI Around Us

Use only the approved examples. For each: what students observe → what
the system receives → what it produces → why it's interesting. Ask the
question before explaining.

| Example | Ask first | What students observe | What the system receives | What it produces | Why it's interesting |
|---|---|---|---|---|---|
| **Spam detection** | "How does your inbox already know what's junk before you open it?" | Junk mail auto-sorted away | The email's content, sender, patterns across millions of past emails | A spam / not-spam decision | No one wrote a rule for every scam phrasing ever invented |
| **Recommendation systems** (movies, social media) | "Why does everyone's Netflix homepage look different?" | Personalized suggestions | What you (and similar users) watched, liked, skipped | A ranked list of suggestions | It's personalized *per user*, at a scale no team could hand-write |
| **Maps / navigation** | "How does Maps know which route is fastest *right now*?" | A suggested route + ETA | Current and historical traffic, road data, other users' live locations | A route and time estimate | It updates constantly — no fixed rule table could cover every road at every moment |
| **Face unlock** | "How does your phone recognize your face specifically, in different lighting, with glasses on or off?" | Instant unlock | Many prior images of your face, then a new camera image | A match/no-match decision | It generalizes across huge variation (angle, lighting) no rulebook could enumerate |
| **Generative AI (ChatGPT)** | "How does it answer questions it was never explicitly programmed to answer?" | A fluent, relevant reply | Enormous amounts of text it learned patterns from, plus your question | A generated response | It produces genuinely new text, not a lookup from a fixed list of answers |

Keep each example to ~2 minutes. Resist the urge to explain *how* any of
these actually work internally — the point at this stage is only "these
depend on learning from examples," which gets earned properly in Sections
12–14, not here.

---

## 11. Traditional Programming

Connect directly to Class 01's `INPUT → PROCESS → OUTPUT` and the
Problem → Logic → Algorithm → Program → Result chain.

> "In Class 1, the 'Process' box was always something a human worked out
> and wrote precise instructions for. Let's do exactly that for a real
> problem: a spam filter. If you were writing the rules yourself, what
> would you check for?"

Let students propose rules conversationally, and write them up as
plain, conceptual statements — never as code or pseudocode syntax:

```
IF email contains "you have won" → spam
IF sender is unknown and asks for money → spam
IF subject is ALL CAPS with lots of "!!!" → spam
IF email contains "urgent" and a suspicious link → spam
```

Keep it conceptual: `INPUT → RULES → OUTPUT`, where "Rules" is explicitly
labeled *"rules a human sat down and thought of."* Do not let this turn
into programming syntax discussion (no `if/else`, no variables) — the
point is entirely that a person had to think of and write each one.

---

## 12. The Rule Problem

**This is a major teaching moment — do not rush it.**

Escalate deliberately. After the class's rule list from Section 11 is on
the board, start supplying real-shaped counter-examples one at a time,
pausing for reaction after each:

1. A real spam email that contains none of the flagged words (e.g., a
   scam that just says "Please review the attached document").
2. A legitimate email that *does* trip a rule (e.g., a genuine airline
   email saying "Your booking is urgent — confirm now!").
3. A spam email in a different language, or using intentional misspellings
   ("fr33", "\u{0430}mazon") to dodge keyword rules.
4. A spammer who changes their wording every week specifically to evade
   filters.

After each, ask: *"Does your rule catch this? Does it wrongly block
this?"* Let the room notice, on their own, that the rule list needs to
keep growing.

Then ask the scaling question directly: **"If we wanted this filter to
work well for millions of people, in multiple languages, against
spammers who keep changing tactics — roughly how many rules do you think
we'd need?"** Let guesses climb ("hundreds," "thousands," "it never
ends"). Name the feeling informally as **"rule explosion"** — not a
formal term to memorize, just a label for what they just experienced:
*"That feeling of the rule list growing forever and still missing
cases — that's what we call rule explosion. It's not that it's
impossible, it's that it stops being realistic."*

Then ask the pivot question, and let it sit:

> **"If humans cannot realistically write every rule, what could we give
> the computer instead?"**

Give real wait time here — 10–15 seconds of silence is fine and
productive. Do **not** answer it yourself. If nothing comes, prompt
narrower: *"Instead of telling it the rule directly, what if we showed
it a lot of already-labeled examples — 'this one's spam, this one
isn't' — a thousand times over? What might it be able to do with that?"*
Almost always, someone will land near "notice a pattern" or "figure it
out itself" — that's the exact door into Section 13.

---

## 13. Introducing Machine Learning

Only now, after the problem is felt, name Machine Learning.

> "Instead of manually writing every rule, we give the computer a large
> set of examples — emails already labeled spam or not-spam — and let a
> learning process find useful patterns in them. That's Machine
> Learning: learning from data instead of being told the rule directly."

**Wording care (see Section 25 for the full guardrail list):** never say
the machine "understands" spam or "thinks" about it. Say it "notices
patterns" or "picks up on what tends to go together." Use the level of
abstraction a beginner needs — not a human-learning analogy taken
literally, and not an algorithmic/statistical description either.

Then reveal the chain — this is the direct setup for Section 14's live
build, so don't fully draw it here, just say it once out loud to prime
the room:

> "So instead of Input → Rules → Output, we now have a different chain:
> Data → Learning → Model → Prediction. Let's build that one together,
> piece by piece."

---

## 14. The Core Pipeline

**This is the HERO MOMENT of the class.** Build it live on the pen
tablet — never reveal it as a finished diagram.

**Recommended live-build sequence:**

1. Write **DATA** alone on the board. Ask: *"What do we need to give the
   machine, if we're not giving it rules?"* → land on "labeled examples"
   (e.g., emails already marked spam / not-spam).
2. Draw the arrow, write **LEARNING**. Ask: *"What happens to those
   examples next?"* → land on "a process that looks across all of them
   and finds what separates spam from not-spam."
3. Draw the arrow, write **MODEL**. Ask: *"What do we get after that
   learning process finishes?"* → land on "something that has picked up
   the patterns — call it the model."
4. Draw the arrow, write **PREDICTION**. Ask: *"Now a brand new email
   arrives, one the model has never seen. What happens?"* → land on
   "the model uses what it learned to make its best guess."

Finished board:

```
DATA  →  LEARNING  →  MODEL  →  PREDICTION
```

**Explicitly contrast it, side by side, with Section 11's chain** (this
is the intellectual backbone of the whole class — say it plainly):

```
TRADITIONAL PROGRAMMING:   INPUT  →  RULES        →  OUTPUT
MACHINE LEARNING:          DATA   →  LEARNING → MODEL →  PREDICTION
```

> "Same basic shape — something goes in, something happens, something
> comes out. The difference is *who* decides the 'something happens' in
> the middle: a human, or a learning process working from examples."

Immediately connect the pipeline back to the spam example, tracing all
four boxes with the actual spam scenario before moving to cats-vs-dogs:
*Data = past labeled emails → Learning = finding patterns across them →
Model = the trained spam filter → Prediction = spam/not-spam for a new
email.*

**Do not compress this block below 7 minutes**, even under time
pressure — see Section 28.

---

## 15. Cats-vs-Dogs Activity

**This is the HERO ACTIVITY.** No code. No equations. No pretending
students are actually training anything — this is a reasoning activity.

### Facilitator instructions (timed, ~12 minutes at canonical pace)

1. **(2 min) Show/describe several cat examples.** Use slide images or
   verbal description: several cats, varied — different colors, breeds,
   poses, indoor/outdoor.
2. **(2 min) Show/describe several dog examples,** similarly varied.
3. **(2 min) Ask:** *"What patterns do you notice that seem to separate
   cats from dogs across these examples?"* Collect answers freely —
   ear shape, size, face shape, tail, typical posture, sounds (if
   mentioned).
4. **(1 min) Ask:** *"If a computer looked at hundreds of labeled cat and
   dog photos instead of just these few, what do you think it might end
   up 'noticing,' the same way you just did?"* → land on: it could pick
   up on similar patterns, without anyone telling it those patterns
   directly.
5. **(2 min) Introduce a new, deliberately ambiguous example** — e.g., a
   photo of an unusual-looking dog breed that looks a bit cat-like, or a
   verbal description ("a small, fluffy animal with pointy ears and a
   flat face — what is it?").
6. **(2 min) Ask students to predict:** "Cat or dog? Why?" Collect a few
   different reasoned guesses — some will disagree, which is the point.
7. **(1 min) Ask:** *"Is your prediction guaranteed to be correct?"* →
   land on: no — it's a reasoned best guess based on patterns, and best
   guesses can be wrong.
8. **Connect back explicitly:** "This is exactly the pipeline. The
   labeled cat/dog photos are the Data. Noticing ears, size, and face
   shape is the Learning. What you've now built in your head — a sense
   of 'what usually makes something a cat vs. a dog' — is your Model.
   Your guess on the new photo is the Prediction."

### Questions and expected responses

| Question | Expected response |
|---|---|
| "What patterns separate cats from dogs?" | Ear shape, size, face shape, tail, fur texture, posture |
| "Could a computer notice these same patterns from enough examples?" | "Yes, if it saw enough labeled examples" |
| "Is the guess on the ambiguous example guaranteed correct?" | "No — it's a best guess" |
| "What would happen if the computer only ever saw big dogs and small cats?" | "It might get confused by a small dog" (seeds Section 17) |

### Misconceptions during the activity

| Misconception | Response |
|---|---|
| "The computer *sees* the picture the way we do." | "It processes the image data — let's not worry about exactly how; what matters is it can pick up on patterns the same way you just did by eye." |
| "There must be one definite correct rule that separates all cats from all dogs." | "That's exactly why rules struggle here — real cats and dogs vary too much for one clean rule. Patterns learned from many examples handle that variation better." |
| "If enough examples are shown, the prediction will always be right." | "More good examples help, but 'best guess' never becomes 'guaranteed' — that's Section 16, coming right up." |

### Timing, extension, and support

- **Canonical timing:** ~12 minutes total, per the breakdown above.
- **Stronger-student extension:** Ask them to propose a *harder* ambiguous
  example themselves (e.g., a fox, a hairless cat, a wolf-like dog breed)
  and reason through it the same way — reinforces the idea without adding
  new scope.
- **Weaker-student support:** If a student is stuck naming a pattern,
  narrow the question: "Just look at the ears in these two photos — what's
  different?" One concrete visual comparison is usually enough to unlock
  participation.
- **Transition back to the main lesson:** "You just did, by reasoning,
  exactly what a machine learning system does mechanically: looked at
  labeled examples, found patterns, and used them to make a guess on
  something new. Let's talk about that last part — the guess — a little
  more."

---

## 16. Prediction ≠ Certainty

Introduce the distinction plainly, anchored in the ambiguous cats-vs-dogs
example just completed.

> "A model produces a prediction based on patterns it has learned from
> data. That prediction is a best guess — not a guarantee. Just like your
> guess on that ambiguous photo, a real system's guess can be wrong."

Do **not** introduce probability scores, confidence percentages, or
formal accuracy metrics — none of that is in scope. Keep it entirely at
the level of "best guess, not certainty."

Connect to real examples already established: a recommendation app
suggesting something you'd never actually like; autocorrect changing a
word to the wrong one; a spam filter letting through one scam email or
blocking one real one. Ask: *"Does one wrong guess mean the whole system
is broken?"* Land on: no — reasonable systems make reasonable guesses
that are sometimes wrong, the same way people do.

---

## 17. AI Is Not Magic

Build the idea as a direct extension of the pipeline, not a new diagram:

```
DATA
  ↓
PATTERNS
  ↓
MODEL
  ↓
PREDICTION
```

Establish, briefly and concretely — this is **not** an ethics lecture:

- **Data matters.** The model only knows what its examples showed it.
- **Examples matter.** Limited or one-sided examples produce limited or
  one-sided patterns.
- **Limitations exist.** No system generalizes perfectly to situations
  unlike anything it has seen.
- **Poor data → poor predictions.** A spam filter trained only on
  English emails will struggle with other languages; a face-unlock
  system trained on limited examples may struggle with different
  lighting or appearances.

Keep this to 3–4 minutes with one worked example (Section 7.10 above)
before moving on. If a student pushes toward bias/fairness/safety in
depth, use the parking-lot response pattern from Section 32 — validate,
give the safe conceptual layer already covered here, and park the rest
for a dedicated later class.

---

## 18. AI / ML / Deep Learning / Generative AI

Give students a simple orientation map, **not** a taxonomy exam.

Build it live (Drawing #5), as nested circles, from the outside in:

```
┌─────────────────────────────────────────┐
│      ARTIFICIAL INTELLIGENCE            │
│   ┌───────────────────────────────┐     │
│   │      MACHINE LEARNING          │     │
│   │   ┌─────────────────────┐      │     │
│   │   │   DEEP LEARNING       │     │     │
│   │   └─────────────────────┘      │     │
│   └───────────────────────────────┘      │
│                                            │
│         ✦ GENERATIVE AI                   │
│    (a major modern application area)      │
└─────────────────────────────────────────┘
```

Say explicitly: *"AI is the broad field. Machine Learning is one major
approach inside it — the one we spent today on. Deep Learning is a more
powerful style of machine learning, used for very complex patterns like
images and language. Generative AI — ChatGPT and similar tools — is one
of the biggest modern application areas built using deep learning, but
don't worry about drawing a perfect boundary around it. This is a map to
help you get oriented, not a diagram to memorize."*

Explicitly state: **students do not need to memorize formal
definitions.** The goal is orientation — broad to narrow, and knowing
roughly where each term sits relative to the others.

---

## 19. Return to the Learning Staircase

Reuse Class 01's staircase image (`Programming → Computer Science →
Mathematics → Data → Machine Learning → Deep Learning → LLMs → Agents`).

> "We gave you a preview of where this staircase leads. We are not
> skipping the steps underneath it. Today you stood at the top step for
> a few minutes and looked down — Machine Learning, Deep Learning, and
> Generative AI. The next several months build the steps that actually
> get you there: programming, computer science fundamentals, and
> mathematics. Once those exist, everything you reasoned through today —
> Data → Learning → Model → Prediction — becomes something you can
> actually build, not just explain."

This is also the natural place to close the loop on Section 3's roadmap
honesty point if it wasn't said in the opening.

---

## 20. Recap

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last several minutes:

1. **"Why can rules become difficult to write by hand?"**
   *Expected:* Too many cases, language/behavior changes, patterns are
   hard to state explicitly. *If stuck:* point back at the spam rule
   list from Section 12.
2. **"What does machine learning change?"**
   *Expected:* Instead of a human writing the rule, the machine finds a
   pattern from labeled examples.
3. **"What's the core pipeline?"**
   *Expected:* Data → Learning → Model → Prediction, in order, roughly
   in their own words.
4. **"Give one real-world example."**
   *Expected:* Any of spam filters, recommendations, maps, face unlock,
   generative AI — with a reason, not just the name.
5. **"Why isn't a prediction the same as certainty?"**
   *Expected:* It's a best guess from learned patterns, and best guesses
   can be wrong — callback to the ambiguous cats-vs-dogs example.
6. **"Why does data matter so much?"**
   *Expected:* The model only knows what its examples showed it; poor or
   limited data produces poor or limited predictions.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 21. Exit Check

A short, ungraded, formative check aligned to the class success metric
(Section 1 / Section 34) — **explanation questions, not terminology
recall.** Use as a quick round of cold-call or show-of-hands-then-explain
in the closing minutes, or as a 2-minute written exit slip if the format
allows.

1. "In your own words, why couldn't a spam filter just be a big list of
   hand-written rules?"
2. "Put Data, Learning, Model, and Prediction in the right order, and
   explain what happens at each step."
3. "If a computer saw a hundred labeled cat and dog photos, how might it
   guess on a new, unlabeled one?"
4. "Give one reason a model's prediction might be wrong."
5. "Give one reason bad data leads to a bad AI system."

A class where most students can answer these in plain language — even
imperfectly — has met the success metric, regardless of exact wording.

---

## 22. Homework Bridge

The homework itself is created later, in `06_Homework/`, derived from
this guide — do not create it here. This section specifies only what it
must reinforce.

- **Purpose:** Extend the Data → Learning → Model → Prediction pipeline
  reasoning to a new, self-chosen everyday example — the same way Class
  01's homework extended Input → Process → Output/algorithm-writing to a
  self-chosen everyday process.
- **Expected student thinking:** Given a real-world AI-powered system
  (chosen by the student, e.g., a music app, a photo app's auto-tagging,
  a food-delivery app's ETA estimate), the student should reason through:
  what data the system might use, what pattern it might be learning,
  what its model's prediction looks like, and one reason that prediction
  could be wrong.
- **What the homework should assess:** Whether the student can apply the
  pipeline to a *new* example independently — not whether they can
  recite the pipeline's definition. It should require zero code, zero
  math, and zero research into how the chosen system actually works
  internally (informed, reasoned guessing is the entire point, mirroring
  the cats-vs-dogs activity).

---

## 23. Differentiation

| Group | Strategy |
|---|---|
| **A. Zero programming experience** | Everything today is already code-free by design — no adjustment needed. If Section 11's "rules" discussion drifts toward syntax, redirect to plain sentences immediately. |
| **B. Basic Python knowledge** | These students may try to describe rules as `if/else` code. Welcome the instinct, then redirect: "Right idea — but today we're staying at the concept level, not the code. What's the plain-English version?" |
| **C. Stronger students who already know AI** | Give them the extension role in the cats-vs-dogs activity (propose a harder ambiguous example) and let them field one Section 32 parking-lot question first, with your safe-answer backup ready. Don't let them dominate the main Q&A — redirect a second advanced comment with "hold that thought for the parking lot at the end." |
| **D. Quiet/reluctant students** | Use paired "turn to your neighbor for 20 seconds" before open questions in the Rule Problem and Cats-vs-Dogs sections, then ask for pair answers rather than individual ones — lowers the stakes of being wrong in public. |
| **E. Students who dominate discussion** | Use "let's hear from someone who hasn't answered yet" explicitly but kindly; assign them the "scribe" role (repeating the board list back) to keep them engaged without holding the mic. |

The class should stay engaging for A and B without feeling like review,
and stay accessible for C and D without feeling like a repeat of things
they already know — the rule-problem struggle and the hero activity are
the equalizers: nobody has "already reasoned through this specific
class's examples" before.

---

## 24. Common Misconceptions

| Misconception | Why students think this | Instructor response | Correct beginner mental model |
|---|---|---|---|
| "AI is just programming." | Both involve computers "doing smart things"; the distinction is invisible from the outside. | "Programming is telling a computer exactly what to do, step by step. Machine learning is a way of building software where the computer finds the rule itself, from examples, instead of being told it directly." | AI/ML is *built using* programming, but the ML approach solves a different kind of problem than hand-written rules do. |
| "Machine learning means the computer thinks like a human." | Media, marketing, and words like "learning" and "intelligence" invite the comparison. | "Think of learning here as finding useful patterns in data — not understanding the way you do." | The system notices statistical patterns across examples; it doesn't understand meaning the way a person does. |
| "More data always means better AI." | "More examples = smarter" seems intuitively true, and is often repeated as a slogan. | "More *good, relevant* data usually helps. But more messy, biased, or irrelevant data can just teach the system the wrong patterns faster." | Data quality and relevance matter as much as, or more than, raw quantity. |
| "A prediction must be correct." | The word "prediction" sounds authoritative, like a calculation with one right answer. | "A prediction is a best guess based on patterns — like your guess on the ambiguous cat/dog photo. Best guesses can be wrong." | Predictions are probabilistic best guesses, not guaranteed facts. |
| "AI understands things exactly like humans." | Fluent chatbot responses feel like genuine understanding. | "It can produce very fluent, useful output by learning patterns in enormous amounts of text — that's different from understanding meaning the way you do." | Fluent output is a sign of strong pattern-learning, not proof of human-like understanding. |
| "Generative AI is completely separate from AI." | GenAI is marketed as its own trend/category (ChatGPT, image generators). | "Generative AI is a major modern application area built on top of AI and machine learning — it's a branch of the same tree, not a different tree." | Use the nested map (Section 18) — GenAI sits within/alongside ML and Deep Learning, not apart from them. |
| "Machine learning replaces programming." | If the machine "learns the rule itself," it can sound like programmers become unnecessary. | "Someone still has to build, prepare data for, and deploy these systems — that's still programming, just aimed at a different kind of problem." | ML is an addition to the programmer's toolkit, not a replacement for programming. |
| "If an AI makes a mistake, it must be broken." | People expect computers to be either perfectly right or malfunctioning — no middle ground. | "A reasonable guess that turns out wrong isn't the same as a malfunction — the same way a person's reasonable guess can be wrong without them being 'broken.'" | Wrong predictions are an expected, normal part of a system built on best guesses, not evidence of failure. |

Address these opportunistically as they surface in student answers —
don't read the table aloud as a block.

---

## 25. Instructor Language Guardrails

**Phrases to use:**

- "The model learns patterns from examples."
- "The system uses learned patterns to make predictions."
- "At this level, think of learning as finding useful patterns in data."
- "That's its best guess, based on what it's seen before."
- "Someone had to think of and write that rule" (for the traditional-
  programming side of the contrast).

**Phrases to avoid:**

- "The computer understands exactly like a human."
- "The AI thinks exactly like us."
- "The machine knows what a cat is."
- "The AI decided to..." (implies intent/agency)
- Any confident claim about *how* a specific real product (ChatGPT,
  Netflix, etc.) works internally — you don't know its actual
  implementation, and it's out of scope anyway. Stick to the general
  pipeline.

If you slip and anthropomorphize mid-sentence, it's fine to self-correct
out loud — that's actually a useful, visible modeling moment: *"—
notices, I mean, not 'understands.' Small but important difference."*

---

## 26. Pen-Tablet Moments

Six live drawings. Draw slowly enough that students can copy while you
talk, not so slowly the room goes quiet.

### Drawing 1 — AI Around Us

- **When:** During Section 10, optionally, as a running list.
- **Draw first:** A simple header, "AI Around Us."
- **Add second:** One line per example as it's discussed (spam, recs,
  maps, face unlock, GenAI).
- **Questions while drawing:** "What does it receive? What does it
  produce?" jotted as two short sub-notes per example if time allows.
- **Students should notice:** These are all *different* systems doing a
  *similar* underlying thing.
- **Do NOT pre-draw:** The list — build it from student-named examples,
  not a pre-filled slide.
- **Estimated time:** 3–4 minutes, spread across the section.

### Drawing 2 — Traditional Programming

- **When:** Start of Section 11.
- **Draw first:** `INPUT → RULES → OUTPUT`, three boxes and two arrows.
- **Add second:** Fill "Input" with "a new email," and fill "Rules" live
  as students propose spam rules.
- **Questions while drawing:** "What's your first rule?" after each box
  is added.
- **Students should notice:** "Rules" is a box a *human* has to fill in
  by hand, one rule at a time.
- **Do NOT pre-draw:** Any rules — the box starts empty.
- **Estimated time:** 2–3 minutes.

### Drawing 3 — The Rule Problem

- **When:** Start of Section 12.
- **Draw first:** Keep the same "Rules" box from Drawing 2 visible.
- **Add second:** As each counter-example breaks a rule, add another
  rule beside it, packed increasingly close together — let it visually
  crowd and sprawl.
- **Questions while drawing:** "Does this new rule catch it? What about
  this one?"
- **Students should notice:** The box is visually overflowing/crowded —
  the "explosion" should be felt just by looking at it.
- **Do NOT pre-draw:** A "finished" crowded box — it must grow live,
  rule by rule, in front of them.
- **Estimated time:** 4–5 minutes, spread across the section.

### Drawing 4 — Data → Learning → Model → Prediction *(THE CORE PIPELINE — MUST be constructed live)*

- **When:** Start of Section 14, immediately after naming Machine
  Learning.
- **Draw first:** Just the word **DATA**, alone.
- **Add second:** Arrow + **LEARNING**, after asking "what happens to
  those examples?"
- **Then:** Arrow + **MODEL**, after asking "what do we get after
  learning?"
- **Then:** Arrow + **PREDICTION**, after asking "what happens with a
  new example?"
- **Finally:** Below it, draw Drawing 2's chain again for direct
  side-by-side contrast.
- **Questions while drawing:** One question before each box (see Section
  14's exact sequence).
- **Students should notice:** The same left-to-right shape as Drawing 2,
  but a learning process — not a human — fills the middle.
- **Do NOT pre-draw:** Any part of this before the live build — this is
  the single diagram in the whole class that must never appear
  pre-finished.
- **Estimated time:** 5–6 minutes.

### Drawing 5 — AI / ML / Deep Learning / GenAI Map

- **When:** Start of Section 18.
- **Draw first:** One large circle, labeled "Artificial Intelligence."
- **Add second:** A smaller circle inside it, "Machine Learning," then a
  smaller one inside that, "Deep Learning."
- **Then:** Place a star/marker near the ML/Deep Learning boundary
  labeled "Generative AI," explicitly drawn touching both rather than
  strictly inside one.
- **Questions while drawing:** "Where do you think ChatGPT belongs on
  this map?" before placing the Generative AI marker.
- **Students should notice:** Broad-to-narrow nesting; Generative AI is
  a modern application area, not a fourth strictly-nested layer.
- **Do NOT pre-draw:** The full nested map in advance — build it ring by
  ring, naming each as you go.
- **Estimated time:** 3–4 minutes.

### Drawing 6 — Traditional Programming vs. Machine Learning (final contrast)

- **When:** Optionally re-drawn or pointed back to during Section 19
  (Return to the Learning Staircase), or Section 20 (Recap).
- **Draw first:** Reuse Drawing 4's two stacked chains if still visible;
  otherwise redraw both quickly.
- **Add second:** Point along Class 01's staircase image, connecting
  "Machine Learning" and "Deep Learning" on the staircase to the chains
  just drawn.
- **Questions while drawing:** "Which chain have we been building all
  class?"
- **Students should notice:** Today's whole lesson is one link on that
  staircase, not a separate, disconnected topic.
- **Do NOT pre-draw:** Month numbers or course names — that's the
  four-month roadmap from Class 01, a separate visual not to be
  re-merged here.
- **Estimated time:** 2 minutes.

---

## 27. Slide Relationship

**Slides are support, not lecture notes.** They should never carry more
information than what's being said live — if a slide could be read
standalone and teach the class, it's doing too much.

| Section | What's shown on slide | What's said live | What's drawn instead | Where interaction takes over |
|---|---|---|---|---|
| Opening | One title slide, nothing else | The framing question, live | — | Immediately — this is discussion from second one |
| What is AI? | 3–4 icons (chatbot, camera, feed, map) | The working definition | — | The calculator/thermostat check |
| AI Around Us | One slide per example, image/icon only | Input/output/why-interesting per example | Optional running list (Drawing 1) | Ask-before-explain per example |
| Traditional Programming | Empty or none | The rules students propose | Drawing 2, built entirely live | Rule proposals from students |
| The Rule Problem | None | Counter-examples, spoken | Drawing 3, grown live | The entire section — near-continuous |
| Introducing ML | One bare "Machine Learning" title slide | The careful definition | — | The pivot question and wait time |
| Core Pipeline | None | The four build-questions | Drawing 4 — never pre-shown | Every box addition is a question first |
| Cats-vs-Dogs | Cat/dog example images only | Facilitator questions | Optional light notes of student answers | The entire activity |
| Prediction ≠ Certainty | None | The distinction, anchored in the activity | — | Student anecdotes |
| AI Is Not Magic | None | The data-quality point | Reuse Drawing 4 | The language-example question |
| AI/ML/DL/GenAI Map | Light — reuse the same nested-circle visual once drawn, if repeating for absentees | The orientation framing | Drawing 5, built ring by ring | "Where does X belong?" |
| Return to Staircase | Reuse Class 01's staircase visual | The honest roadmap framing | Drawing 6 (pointer/extension) | Minimal — mostly delivered |
| Recap | None | The six recap questions | — | Entirely — students answer, instructor doesn't lecture |

---

## 28. Time Management

**Ideal pace check:** by minute 43 you should be finishing Traditional
Programming and entering the Rule Problem; by minute 78 the Core Pipeline
should be freshly drawn and complete; by minute 95 Prediction ≠ Certainty
should be wrapping.

**Signs you're going too slowly:** you're still collecting AI-Around-Us
examples past minute 33; the Rule Problem hasn't reached the pivot
question by minute 57; you haven't started drawing the Core Pipeline by
minute 80.

**Signs you're going too quickly:** the Rule Problem wrapped in under 10
minutes (students haven't felt the struggle); the Cats-vs-Dogs activity
finished in under 8 minutes (reasoning was rushed, not earned); you have
more than 10 minutes unexpectedly left before the Recap.

**What to compress (in this order) if behind:** (1) AI Around Us — drop
to 3 examples; (2) What Is AI? — skip the calculator/thermostat debate;
(3) Introducing Machine Learning — shorten to the one-line definition;
(4) AI/ML/DL/GenAI Map — trim to naming the four terms without the full
live-drawn map, using a simpler spoken version instead.

**What must never be skipped (non-negotiable moments):**

- The Rule Problem
- The Machine Learning discovery moment (the pivot question and its
  answer)
- The Core Pipeline
- The Cats-vs-Dogs reasoning activity
- Prediction ≠ Certainty
- The Recap

**What can be expanded if students are engaged:** the Rule Problem
(more counter-examples), the Cats-vs-Dogs activity (a stronger-student
extension round), the AI/ML/DL/GenAI map (more "where does X belong?"
questions).

---

## 29. 90-Minute Version

Compressed timeline (deltas from the canonical 110-minute table in
Section 6). Every non-negotiable section is preserved; nothing is cut at
random.

| Time | Dur. | Section | Change from canonical |
|---|---|---|---|
| 0–6 | 6 | Opening + AI perception | −2: collect 2–3 examples instead of open-ended |
| 6–14 | 8 | What is AI? | −3: skip the calculator/thermostat debate; state the working idea directly |
| 14–23 | 9 | AI around us | −3: use 3 examples (spam, recommendations, face unlock) instead of 5 |
| 23–33 | 10 | Traditional programming | −2: cap rule collection at 3 rules |
| 33–46 | 13 | The rule problem | −3: use 3 escalating counter-examples instead of 5–6; core struggle preserved |
| 46–54 | 8 | Introducing Machine Learning | −3: one clean statement + one check-in question, no second mini-example |
| 54–61 | 7 | **Core Pipeline** *(hero)* | −1: same live-build sequence, slightly brisker pacing |
| 61–71 | 10 | **Cats-vs-Dogs Activity** *(hero)* | −2: drop the stronger-student extension round; keep the full core sequence |
| 71–75 | 4 | Prediction ≠ certainty | −1: one anecdote instead of open collection |
| 75–78 | 3 | AI is not magic | −1: one example only (language, not a second) |
| 78–84 | 6 | AI/ML/DL/GenAI map | unchanged |
| 84–87 | 3 | Return to staircase | unchanged |
| 87–90 | 3 | Recap + exit check + homework bridge | unchanged — never compressed |

**Preserved hero moments:** Core Pipeline (built live, full sequence),
Cats-vs-Dogs (full 8-step sequence, just without the extension), Recap
(full six questions). If still running over at minute 46 (end of Rule
Problem), cut the AI/ML/DL/GenAI map to a 2-minute spoken version instead
of a live-drawn one — that is the one acceptable further cut, not the
Recap.

---

## 30. 120-Minute Version

Expanded timeline — every added minute goes to **interaction and deeper
reasoning**, never new technical content.

| Time | Dur. | Section | Expansion from canonical |
|---|---|---|---|
| 0–9 | 9 | Opening + AI perception | +1: one more student describes their example in more detail |
| 9–20 | 11 | What is AI? | unchanged |
| 20–34 | 14 | AI around us | +2: add a 6th example students suggest themselves |
| 34–46 | 12 | Traditional programming | unchanged |
| 46–64 | 18 | The rule problem | +2: let students try to patch their own rules for 2–3 more rounds before the reveal |
| 64–75 | 11 | Introducing Machine Learning | unchanged |
| 75–83 | 8 | **Core Pipeline** *(hero)* | unchanged pace, but slower live drawing with more pauses |
| 83–98 | 15 | **Cats-vs-Dogs Activity** *(hero)* | +3: add the stronger-student extension round (a harder ambiguous example, proposed and reasoned by students) |
| 98–103 | 5 | Prediction ≠ certainty | unchanged |
| 103–107 | 4 | AI is not magic | unchanged |
| 107–113 | 6 | AI/ML/DL/GenAI map | +1: more "where does X belong?" questions (e.g., self-driving cars, voice assistants) |
| 113–116 | 3 | Return to staircase | unchanged |
| 116–120 | 4 | Recap + exit check + homework bridge | +1: slightly more time per recap question, still no new content |

No advanced technical material is added anywhere in this version — the
extra 10 minutes buys more student reasoning time on material already in
scope, not new scope.

---

## 31. Classroom Management

This is an **online live class** — plan interaction accordingly.

| Situation | Guidance |
|---|---|
| **Silence after a question** | Wait 7–10 seconds (longer than feels comfortable) before rephrasing narrower. Online, explicitly invite chat answers as a lower-stakes alternative to unmuting: "Type one word in chat if speaking feels like too much right now." |
| **Wrong answers** | Never say "no" flatly. Acknowledge the reasoning, then redirect: "I can see why you'd think that — here's the piece that changes it..." |
| **Advanced questions mid-flow** | Validate briefly, park explicitly (Section 32), and name *when* it'll be answered ("great question — that's Month 3 material, let's park it and I'll give you the short version at the end"). |
| **"I already know AI"** | Welcome it publicly, then give them a specific job: "Perfect — you're on point for the harder cats-vs-dogs example later," or let them field one parking-lot question first. Redirect further volunteering to "let's hear it in the extension round." |
| **Going off-topic** | Acknowledge in one sentence, then bridge back explicitly: "Interesting — a bit outside today's scope, but it connects to [X] we'll hit later. Back to..." |
| **Technical problems (audio/video/connection)** | Keep talking through brief drops — don't stall the room for one student's issue; follow up 1:1 in chat/DM after class if needed. |
| **Online interaction generally** | Use chat polls or literal "type A/B in chat" for quick checks (e.g., "type YES or NO — does this rule catch this email?") to keep engagement measurable without needing everyone to unmute. |
| **Chat participation** | Periodically read 1–2 chat answers aloud by name — this rewards typing as a valid form of participation and keeps chat-only students engaged. |
| **Poll/hand-raise style participation** | Use the raise-hand/reaction feature for the low-stakes opening questions (Section 8) instead of open mic, to get a fast visible read of the room. |

---

## 32. Advanced Question Parking Lot

For each: validate → give only the safe conceptual answer already in
scope → explicitly park the rest for later.

| Student question | Response |
|---|---|
| "How does neural network training actually work?" | "Great question — under the hood, it's a more complex version of the 'Learning' box we drew today, but the actual mechanics involve math we haven't covered yet. That's Month 3 territory, once we've built up mathematics and programming. For today: it's still fundamentally learning patterns from examples." |
| "What algorithm does Netflix use?" | "I don't want to guess at their exact internals, and it's not public in detail anyway — but it fits the same pipeline we drew: data about what you and similar users watched, a learning process, a model, and a prediction of what you'd like next." |
| "How does ChatGPT understand language?" | "It doesn't 'understand' the way you do — it's learned extremely rich patterns in language from enormous amounts of text. *How* it represents those patterns internally is genuinely advanced material — we'll get there once you have the programming and math foundations to make sense of it." |
| "What is a transformer?" | "That's the name of a specific, powerful design used inside many modern AI systems, including ChatGPT. It's out of scope for today — file it away, you'll meet it properly later in the program." |
| "What are embeddings?" | "Good instinct to ask — that's a technical idea about how AI systems represent information internally. It needs some math background first, so it's parked for a later class." |
| "How are models trained?" | "In spirit, exactly like today's pipeline: lots of examples go in, a learning process finds patterns, out comes a model. The actual mechanics of *how* that learning process works mathematically is Month 3+ material." |

Never teach the deferred topic itself, even briefly, beyond the one
safe sentence already provided above — repeating it verbatim is fine and
intentional.

---

## 33. Teacher FAQ

**Q: A student asks if I can show them actual code or a real model. Should I?**
A: No — this class is explicitly code-free and implementation-free. Redirect: "That's exactly what later classes are for, once we've built the programming foundation."

**Q: What if a student already took an online AI course and finds this too basic?**
A: Use Section 23.C's differentiation — give them the extension roles rather than more content. The class's actual value for them is the shared vocabulary and shared examples the rest of the cohort will reference for the rest of the program.

**Q: What if the rule-problem escalation doesn't land — students just keep proposing more rules confidently?**
A: That's fine and even useful — let the rule count visibly climb past 10–15 before asking the scaling question. The larger the visible list, the more obvious "this doesn't scale" becomes on its own.

**Q: Is it okay to use a different everyday example instead of spam for the Traditional Programming / Rule Problem sections?**
A: Stick with spam — it's the approved example the rest of the class (recap, exit check, later artifacts) is built around. Introducing a different core example here would break consistency with derived materials built from this guide.

**Q: What if I run out of ambiguous cat/dog examples students find genuinely ambiguous?**
A: A verbal description works as well as an image — "a small fluffy animal with pointy ears, a flat face, and a short tail" is deliberately usable without any image at all.

**Q: A student asks whether AI will take their job. How do I handle that?**
A: Acknowledge it's a fair and common concern, then redirect to scope: "That's a real conversation, but it's more of a career/policy discussion than a Class 2 concept question — let's stay focused on how these systems actually work today, which is the more useful foundation for reasoning about that question yourself later."

**Q: The class is running short (finished early). What do I do with spare time?**
A: Use Section 30's expansion menu (more AI-around-us examples, the cats-vs-dogs extension round, more map questions) — never introduce new deferred content to fill time.

---

## 34. Class Success Check

Final instructor checklist, based exactly on the metadata's success
metric. Answer honestly after class — this is self-assessment, not a
student grade.

- [ ] Can students explain, unprompted, *why* manual rules become
      difficult — using their own reasoning, not a recited definition?
- [ ] Can students state the Data → Learning → Model → Prediction chain
      and distinguish it from Input → Rules → Output, in their own
      words?
- [ ] Can students give a plausible, reasoned answer for how a system
      could learn to tell cats from dogs, referencing the in-class
      activity?
- [ ] Can students state at least one reason predictions aren't
      certainties?
- [ ] Can students state at least one reason AI has real limitations
      (poor data → poor predictions)?

If most students can do all five, the class succeeded — regardless of
how much AI terminology they can recite, and regardless of whether every
planned section ran at full length.

---

## 35. Post-Class Reflection Prompts

For `10_Reflection/`, filled in **after** the class is actually taught —
not created in advance. Prompts to answer immediately afterward, while
memory is fresh:

- Where did students become confused, and at which exact question or
  transition?
- Which everyday examples (spam, recommendations, maps, face unlock,
  GenAI) generated the most genuine recognition/engagement, and which
  fell flat?
- Which questions generated real discussion vs. which were answered
  with a single word and silence?
- Was the Data → Learning → Model → Prediction pipeline actually
  understood — could students restate it unprompted in the recap, or
  did it need re-explaining?
- Did the Cats-vs-Dogs activity work as intended — did students propose
  their own patterns, or did they need heavy prompting?
- How was pacing against the Section 6 timing table — which sections ran
  long, which ran short, and why?
- Was the AI/ML/Deep Learning/Generative AI map section too much, too
  little, or about right — did students seem to need it, or did it feel
  like filler?
- What should change before the next cohort runs Class 02?

---

## 36. Source-of-Truth / QA Section

Verified against `00_Class_Metadata/class_metadata.md` and `README.md`.

| Check | Result |
|---|---|
| Class number, title, subtitle | Match exactly: 02, "How Machines Learn," "From Rules → Data → Intelligence." |
| Audience | Matches: first-year, mixed backgrounds, no programming/math/AI prerequisite assumed beyond Class 01. |
| Prerequisites | Matches: Class 01 concepts listed and referenced throughout (Section 3, 4, 19). |
| Learning objectives | All 11 metadata objectives reproduced and expanded in Section 4, in the same order and substance. |
| Duration | 110–120 minutes, canonical 110, with 90/120 versions provided (Sections 29–30), matching metadata's request for a Class-01-style compressed/expanded strategy. |
| Core question | Reproduced verbatim in Section 1 and used verbatim at the Section 8 opening and Section 12 pivot. |
| Core concept | `DATA → LEARNING → MODEL → PREDICTION` used verbatim and consistently throughout — no wording drift across sections. |
| Deferred topics | No programming syntax, neural-network math, gradient descent, transformers, embeddings, RAG, agents, deep prompt engineering, statistical/mathematical formalism, training implementation, or deep AI ethics/policy appear anywhere as *taught content*. Each surfaces only in Section 32 as a validated-and-parked question. |
| Teaching philosophy | Ask-before-explain, example-before-definition, everyday examples only — applied in every section (8–20). |
| Relationship to Class 01 | Section 3 explicitly parallels the two pipelines and resolves the Month-3-roadmap tension honestly, per the metadata's explicit instruction not to make it sound like a mistake. |
| Success metric | Section 34's checklist reproduces the four metadata outcomes exactly, in the same order and wording. |

**Explicit scope re-verification:** every deferred topic in the
metadata's list was searched for across this document — none appear as
instructional content; each mention is confined to Section 32 (validated
and parked) or Section 33 (an FAQ answer that explicitly redirects away
from it). No mathematics, no code, no implementation detail appears
anywhere in this guide.

---

*End of Class 02 Master Instructor Guide. Per the program's
source-of-truth workflow (see `README.md`), no other Class 02 artifact
should be created until this guide is reviewed and confirmed — Student
Notes, Presentation, Pen-Tablet Plan, Interaction Pack, Homework,
Assessment, Cheat Sheet, and Resources all derive from this document,
never independently.*
