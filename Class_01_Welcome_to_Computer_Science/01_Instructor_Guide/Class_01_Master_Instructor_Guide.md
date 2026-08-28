# Class 01 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Welcome to Computer Science
**Subtitle:** From Using Technology → Understanding Technology
**Target duration:** 90–120 minutes (recommended ≈110 minutes)
**Prerequisite:** None

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to read
aloud. Use your own voice.

---

## Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Emotional / Pedagogical Objective](#2-emotional--pedagogical-objective)
3. [The One Story This Class Tells](#3-the-one-story-this-class-tells)
4. [Class Flow & Timing](#4-class-flow--timing)
5. [Section-by-Section Teaching Notes](#5-section-by-section-teaching-notes)
6. [Pen-Tablet Drawing Guide](#6-pen-tablet-drawing-guide)
7. [Instructor Speaking Style](#7-instructor-speaking-style)
8. [Misconceptions to Pre-empt](#8-misconceptions-to-pre-empt)
9. [Differentiated Questions](#9-differentiated-questions)
10. [Class Success Criteria](#10-class-success-criteria)
11. [Recap (Final 5 Questions)](#11-recap-final-5-questions)
12. [Homework — Assignment 1: Think Like a Programmer](#12-homework--assignment-1-think-like-a-programmer)
13. [Instructor Reflection Checklist](#13-instructor-reflection-checklist)
14. [Pedagogical Guardrail](#14-pedagogical-guardrail)

---

## 1. Learning Objectives

By the end of Class 1, a beginner should be able to explain, **in their own
words, informally**:

1. What Computer Science is.
2. Why Computer Science is broader than programming.
3. What a computer program is.
4. What programming means.
5. What an algorithm is.
6. The difference between an algorithm and a program.
7. Input → Process → Output.
8. The chain: Problem → Logic → Algorithm → Program → Result.
9. The basic idea of computational thinking.
10. Why computers require precise instructions.
11. How programming and CS eventually connect to AI.

No formal mastery is expected. The bar is **conceptual understanding and
curiosity**, not correctness under exam conditions.

## 2. Emotional / Pedagogical Objective

- A **beginner** should leave thinking: *"I don't know everything yet, but I
  can understand this."*
- A **stronger student** should leave thinking: *"There is much more to
  Computer Science than just writing code."*

The class should lower fear of programming and raise curiosity. It should
never feel like a lecture hall reciting definitions — it should feel like a
conversation that happens to arrive at Computer Science.

## 3. The One Story This Class Tells

Everything taught today is one continuous chain. If you ever feel a section
drifting into an isolated definition, pull it back to this spine:

```
I use technology
      ↓
What is actually happening?
      ↓
Computer Science
      ↓
Computers execute instructions
      ↓
Programming gives instructions
      ↓
Problems need solutions
      ↓
Solutions require logic
      ↓
Logic can become algorithms
      ↓
Algorithms can become programs
      ↓
Programs produce results
      ↓
These foundations eventually lead toward AI
```

Every section below exists to advance this chain by one link. Say the
connecting sentence out loud when you move between sections — it's what
makes the class feel like one story instead of ten definitions.

## 4. Class Flow & Timing

Three schedules are provided. Use the **Recommended (110 min)** by default.
Switch to the 90-minute version only if the slot is genuinely shorter — don't
compress live unless you're already behind (see the "never cut" list below).

### 4.1 Recommended flow — 110 minutes

| # | Section | Ideal | Min | Max | Shortenable? |
|---|---|---|---|---|---|
| 1 | Opening + student interaction | 8 | 5 | 10 | Yes |
| 2 | What is Computer Science? | 13 | 10 | 15 | Yes |
| 3 | Computer → Program → Application | 12 | 10 | 15 | Yes |
| 4 | Input → Process → Output | 10 | 8 | 12 | Yes |
| 5 | Programming + Algorithm | 16 | 14 | 18 | **No** (core concept) |
| 6 | Computational Thinking | 12 | 8 | 14 | Yes |
| 7 | Interactive activity (Tea) | 15 | 13 | 18 | **No** (core activity) |
| 8 | Connecting CS → AI | 9 | 7 | 10 | Yes |
| 9 | Four-month roadmap | 7 | 5 | 8 | Yes |
| 10 | Recap + homework | 8 | 6 | 8 | **No** (core close) |
| | **Total** | **110** | 86 | 128 | |

### 4.2 Full flow — 120 minutes

Same as above, but let Sections 2, 3, and 6 run to their **Max** column
instead of **Ideal** (+2, +3, +2 minutes respectively — 7 minutes total).
Use the remaining ~3 minutes as a general buffer across the day (settling
time, slower transitions). Spend the extra time on more student answers and
a slower live drawing pace — not new content.

### 4.3 Compressed flow — 90 minutes

Drop straight to the **Min** column for every *shortenable* section above,
and cut the Optional ATM activity entirely (it's already optional). Do
**not** touch the Min values already assigned to Sections 5, 7, and 10 —
those are protected regardless of time pressure. This yields ≈86–90 minutes.

If you're still over time mid-class, cut in this order: (1) Optional ATM
activity, (2) roadmap detail (name the four months, skip the reasoning
walkthrough), (3) "What happens when we use technology" Like-button trace
inside Section 3, (4) number of student answers collected in Section 2.

**Never cut:** the algorithm concept (Section 5), the tea activity (Section
7), or the final recap (Section 11). These three are what the class is
actually assessed on.

## 5. Section-by-Section Teaching Notes

### 5.1 Opening (Section 1)

**Goal:** Break the ice, surface what students *think* CS is, and show that
answer is incomplete — without embarrassing anyone.

**Do not open with a definition.** Open with lived experience:

- "How many of you used a smartphone today?"
- "How many of you used a computer?"
- "How many of you actually know what happens inside that device when you
  press a button?" *(expect very few hands — that's the point)*
- "We're going to start understanding that today."

Then ask the anchor question of the whole opening:

> **"What is Computer Science?"**

Collect **3–5 answers** before saying anything formal. Typical answers:
coding, programming, computers, AI, software, "making apps," "hacking."
Write them somewhere visible (or just repeat them back) — you'll use them
in Section 5.2 to show that **Computer Science ≠ Coding**, and that
programming is one part of a bigger field.

**Interaction:**
- *Ask:* "What is Computer Science?"
- *Expected:* "Coding" / "Programming" / "Computers" / "AI"
- *Correct framing:* All of these are *part of* Computer Science, not the
  whole of it — that's exactly what we're about to map out.
- *Follow-up:* "If Computer Science was only coding, would things like the
  internet, databases, or AI even fit anywhere?"

### 5.2 What is Computer Science? (Section 2)

**Goal:** Give students a map of the field, not a definition to memorize.

Conceptual definition (say it once, don't drill it):

> "Computer Science is the study of computation, information, algorithms,
> and problem solving."

Immediately follow with the map — CS *includes* (not "is only"):
Programming, Algorithms, Data Structures, Operating Systems, Databases,
Computer Networks, Computer Architecture, Artificial Intelligence, Security,
and more.

Explicitly call back to the opening answers: "You said coding, AI,
software — all of you were *right*, you each named one room in a much
bigger building." This is where **pen-tablet drawing #1** happens (see
Section 6).

Do **not** teach any of these subfields today. Name them, place them on the
map, move on. Depth here is the opposite of the goal.

**Interaction:**
- *Ask:* "Looking at this map, which of these have you already touched
  without realizing it was Computer Science?" (e.g., using a database app,
  a Wi-Fi network, a video game)
- *Expected:* Silence at first, then scattered examples once one student
  answers.
- *Follow-up:* "So which of these is programming?" *(point to one box)* —
  reinforces CS ⊃ programming.

### 5.3 What happens when we use technology? (Section 3a)

**Goal:** Show that a "simple" action hides real computing concepts —
motivates *why* CS is worth studying.

Use the "Like button" example and trace it conceptually:

```
User → Device → Application → Network → Server → Database → Response → Device
```

State clearly: *"This is a simplified conceptual model, not the real
architecture — we are not doing networking today."* The goal is only to
produce the reaction "wait, all of that happens when I tap one button?"

Keep this brief — it's a hook for Section 3b, not a lecture on distributed
systems.

### 5.4 Computer → Program → Application (Section 3b)

**Goal:** Give students precise, reusable vocabulary.

- **Computer:** a machine capable of executing instructions.
- **Program:** a sequence of instructions a computer can execute.
- **Application:** software designed to perform a useful task for users.

Examples to ground each: Calculator, Browser, Game, Messaging app, AI
chatbot. For each, ask "is this a program or an application, or both?" —
most things students name are both; the point is that *application* is
about the user-facing purpose, *program* is about the instruction sequence
underneath it.

**Interaction:**
- *Ask:* "Is a calculator app a program?"
- *Expected:* "Yes" (usually correct but under-explained)
- *Correct explanation:* It's both — a program (instructions) built and
  packaged as an application (a useful tool for a user).
- *Follow-up:* "What's the smallest 'program' you can imagine — something
  with almost no useful purpose but still counts?" (primes them for later
  algorithm/program distinction)

### 5.5 Input → Process → Output (Section 4)

**Goal:** Install the simplest mental model of computation.

```
INPUT → PROCESS → OUTPUT
```

Worked example — calculator:

```
15 + 20 → Addition → 35
```

State explicitly: *"This is a simple mental model, useful for understanding
a huge range of systems — but real systems can be far more complex than
three boxes. We are not claiming every modern app is literally this
simple."* This caveat matters — don't let strong students silently reject
the model because it looks too simple for what they already know.

This is **pen-tablet drawing #2**.

**Interaction:**
- *Ask:* "What's the input and output when you unlock your phone with your
  face?"
- *Expected:* Input = face/camera image, Output = unlocked screen (Process
  = matching, often shrugged at — that's fine, that's *today's* mystery box,
  not something to resolve now).
- *Follow-up:* "What do you think is happening inside the 'Process' box?
  We'll spend the rest of the program answering that, one layer at a time."

### 5.6 Programming (Section 6, spec) + Algorithm (Section 7, spec)

This is the **conceptual core of the class** — protect its time above all
else except the tea activity.

**Programming**, defined plainly:

> Programming = giving a computer precise instructions to solve a problem.

Then establish the pipeline — **pen-tablet drawing #3**:

```
REAL-WORLD PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

Walk each arrow, don't just show the boxes:
- Problem → Logic: "First you have to *think* about how to solve it — no
  computer yet."
- Logic → Algorithm: "Then you write that thinking down as clear, ordered
  steps."
- Algorithm → Program: "Then you translate those steps into a language a
  computer can execute."
- Program → Result: "Then the computer runs it and produces an answer."

**Algorithm**, taught through a worked problem — *find the larger of two
numbers* — built **interactively**, not presented finished:

- Give A = 15, B = 21. Ask students to describe, out loud, how they'd find
  the larger one. Build the steps from their answers.
- Land on something like:
  1. Take two numbers.
  2. Compare them.
  3. If A > B, A is larger.
  4. Otherwise, B is larger.
- Definition (after the example, not before): *"An algorithm is a finite
  sequence of clear steps used to solve a problem."*

Then draw the sharp distinction, explicitly:

| | Algorithm | Program |
|---|---|---|
| What it is | A solution strategy | An implementation of that strategy in a programming language |
| Language-dependent? | No — same algorithm, any language | Yes — Python code ≠ C code, even for the same algorithm |
| Can a human follow it? | Yes | Only a computer executes it directly |

**Interaction:**
- *Ask:* "Could two different programming languages implement the exact
  same algorithm?"
- *Expected:* Uncertain / "maybe" / "no, they're different"
- *Correct explanation:* Yes — the same "larger of two numbers" algorithm
  could become five lines of Python or five lines of C. The *steps* don't
  change; the *language* does.
- *Follow-up:* "So is an algorithm closer to a recipe or closer to the dish
  itself?" (recipe)

### 5.7 Computational Thinking (Section 8)

**Goal:** Intuitive exposure to four thinking habits, not a memorized list.

1. **Decomposition** — breaking a big problem into smaller ones. *"Planning
   a birthday party" → invitations, food, venue, guest list.*
2. **Pattern recognition** — noticing similarities across problems.
   *"Finding the larger of two numbers" and "finding the tallest student in
   class" use the same comparing idea."*
3. **Abstraction** — ignoring irrelevant detail, keeping what matters.
   *"When you drive a car you don't think about the engine's combustion
   cycle — you think 'accelerator = go.'"*
4. **Algorithmic thinking** — expressing a solution as clear, ordered
   steps. *(Callback to Section 5.6 — they already did this.)*

Keep each example to one line. This is **pen-tablet drawing #4** — four
quadrants, one word + one icon/example each. Do not turn this into a
definitions quiz; ask "can you think of your own example?" for one or two
of the four, live.

### 5.8 Main Interactive Activity — "Teach a Computer How to Make Tea" (Section 9)

**This is the emotional and pedagogical centerpiece of the class. Protect
its time.**

Setup: *"Imagine I am a computer. I will do exactly — and only — what you
tell me, in the exact order you tell me. Nothing more, nothing assumed."*

Ask a student (or the group) to give instructions for making tea, one step
at a time. Play the literal-minded computer:

- If a student says "boil the water," ask: *"Where is the water? Where is
  the pan? How much water?"*
- If a student says "add tea leaves," ask: *"How many? Into what?"*
- Deliberately break at least one instruction: *"There's no gas available —
  what do I do now? You never told me."*

Let the class watch the instructions fail or stall in real time — that
failure **is** the lesson, don't rescue it too early.

Close with the key line, said plainly:

> "Programming requires us to turn human intentions into precise
> instructions."

**Interaction is the entire activity** — there's no separate Q&A block
needed here. Just keep steering with "where," "how much," "what if," until
the class feels the gap between what they *meant* and what they *said*.

#### Optional second activity — ATM withdrawal (if time allows)

Ask the class to build an algorithm for withdrawing cash from an ATM. Let
them discover, unprompted where possible:
- What if the PIN is wrong?
- What if the balance is insufficient?
- What if the machine is out of cash?

Do **not** introduce if/else syntax or the word "branching" formally — just
point out: *"Notice your algorithm just grew a decision — 'if this, do
that, otherwise do this other thing.' That idea has a name, and you'll meet
it properly when we start programming."* This is a seed, not a lesson.

### 5.9 Connecting to AI (Section 10)

**Goal:** A light conceptual bridge — not an ML lecture.

Three parallel pipelines, shown side by side (or one at a time) —
**pen-tablet drawing #5**:

```
Traditional Programming:   INPUT   → RULES     → OUTPUT
Machine Learning:          DATA    → LEARNING  → MODEL → PREDICTION
Generative AI:              PROMPT  → LLM       → GENERATED RESPONSE
```

Say plainly: *"In traditional programming, you write the rules. In machine
learning, the rules are learned from data instead of written by hand. In
generative AI, the model produces new content instead of a single
prediction."* No architecture, no training details, no LLM internals.

Then the staircase — **pen-tablet drawing #6**:

```
Programming → Computer Science → Mathematics → Data → Machine Learning →
Deep Learning → LLMs → Agents
```

Key line: *"We are not going to jump to the bottom. We are going to build
the staircase."*

### 5.10 Four-Month Roadmap (Section 11)

**Goal:** Show *why* the program is sequenced this way, not list every
topic.

- **Month 1 — Foundations:** learn how to think and program.
- **Month 2 — CS & Problem Solving:** understand computer science and
  problem solving properly (C, DSA, algorithms, SQL, discrete math).
- **Month 3 — Engineering + AI:** connect software engineering practice
  with AI (Linux, Git, APIs, ML, GenAI, agents, math for AI).
- **Month 4 — Consolidation:** revise, build projects, get assessed, demo
  what you built.

Explain the *reasoning*, not the topic list: you can't build reliable AI
systems on shaky programming fundamentals, and you can't reason about
algorithms without first being comfortable giving a computer instructions
at all. Today is the first step of that staircase.

### 5.11 Recap + Homework (close)

See [Section 11](#11-recap-final-5-questions) and
[Section 12](#12-homework--assignment-1-think-like-a-programmer) below —
use them directly to close class.

---

## 6. Pen-Tablet Drawing Guide

Six live drawings. Keep every one simple — this is explanation, not art.
Draw slowly enough that students can copy while you talk, not so slowly
that the room goes quiet.

### Drawing 1 — Computer Science Map

- **When:** During Section 5.2, right after collecting opening answers.
- **Why draw live (not pre-slide):** Watching the map *grow* from the
  words students themselves said ("coding," "AI," "software") makes the
  point that CS ⊃ programming land emotionally, not just logically.
- **On slide beforehand:** Just the title "Computer Science" in a circle —
  nothing else.
- **While drawing:** Add each subfield as a satellite bubble around the
  central circle, narrating: "You said coding — that's here. You said AI —
  that's here too, over on this side." Add 2–3 fields students didn't
  mention (e.g., Networks, Security) to show the map is bigger than their
  answers.
- **Students copy:** The central circle + all bubbles, roughly positioned.
- **Do NOT draw:** Sub-bubbles inside each field (e.g., don't expand
  "Algorithms" into sorting/searching/graphs) — that's a future class.

### Drawing 2 — Input → Process → Output

- **When:** Start of Section 5.5.
- **Why draw live:** The calculator numbers should visibly flow left to
  right as you talk, so the arrow direction *is* the causality, not just a
  label.
- **On slide beforehand:** Nothing, or just the section title.
- **While drawing:** Three boxes, arrows between them. Fill Input = "15 +
  20", Process = "Addition", Output = "35" as you narrate the example, then
  erase/replace with the face-unlock example from the follow-up question.
- **Students copy:** The three-box skeleton with the calculator example.
- **Do NOT draw:** Anything suggesting internal steps of "Process" — that
  box stays a black box today, on purpose.

### Drawing 3 — Problem → Logic → Algorithm → Program → Result

- **When:** Start of Section 5.6 (Programming).
- **Why draw live:** This is the single most important diagram in the
  class. Drawing it by hand, slowly, with a beat between each arrow, gives
  it the weight it needs — a pre-made slide would let students glance past
  it.
- **On slide beforehand:** Nothing.
- **While drawing:** Five boxes in a row. Narrate each arrow as you draw
  it, using the "larger of two numbers" example to fill Problem and
  Algorithm as you go (Result can be filled in later, after Section 5.6's
  worked example concludes).
- **Students copy:** The full five-box chain — tell them explicitly "this
  one goes in your notes, we'll refer back to it throughout the program."
- **Do NOT draw:** Actual program code inside the "Program" box — a
  language-agnostic label ("Python / C / etc.") is enough; real syntax
  isn't taught until later classes.

### Drawing 4 — Computational Thinking (four quadrants)

- **When:** Start of Section 5.7.
- **Why draw live:** Four short labels drawn as a 2×2 grid, filled one at a
  time as each idea is introduced, keeps the four ideas visually distinct
  instead of blurring into one paragraph.
- **On slide beforehand:** An empty 2×2 grid outline is acceptable here
  (structure only, no labels) since the content is the point, not the
  layout.
- **While drawing:** Write one word + one example per quadrant as you
  introduce it: Decomposition (birthday party), Pattern Recognition
  (comparing numbers vs. comparing heights), Abstraction (driving a car),
  Algorithmic Thinking (→ points back to Drawing 3).
- **Students copy:** All four quadrants with their one-line examples.
- **Do NOT draw:** Formal definitions — one word and one example per idea
  is the ceiling for today.

### Drawing 5 — Traditional Programming vs. ML vs. Generative AI

- **When:** Start of Section 5.9.
- **Why draw live:** Drawing the three pipelines stacked, one under the
  next, makes the *shift in what's on the left side of the arrow* (rules →
  data → prompt) visually obvious in a way a finished slide doesn't.
- **On slide beforehand:** Nothing.
- **While drawing:** Three rows, same arrow style as Drawing 2 for
  continuity: `INPUT → RULES → OUTPUT`, then `DATA → LEARNING → MODEL →
  PREDICTION`, then `PROMPT → LLM → GENERATED RESPONSE`. Point out that row
  1 is what they've been learning about all class.
- **Students copy:** All three rows.
- **Do NOT draw:** Neural network diagrams, model architecture, or
  training loops — none of that is in scope today.

### Drawing 6 — Programming → CS → Math → AI Staircase

- **When:** Immediately after Drawing 5, still in Section 5.9.
- **Why draw live:** Draw it literally as ascending stair steps — the
  physical metaphor ("we build the staircase, we don't jump to the top")
  lands better as a drawn staircase than as a bullet list.
- **On slide beforehand:** Nothing.
- **While drawing:** Steps going up, one label per step: Programming → CS →
  Mathematics → Data → Machine Learning → Deep Learning → LLMs → Agents.
  Circle "Programming" and "CS" — today's starting steps.
- **Students copy:** The staircase with all eight labels.
- **Do NOT draw:** Timelines, month numbers, or course names on this
  diagram — the roadmap (Section 5.10) is a separate, simpler visual (or
  just spoken) and shouldn't be merged into this one.

---

## 7. Instructor Speaking Style

**Sound:** confident, friendly, technically credible, approachable,
curious, encouraging.

**Avoid:** corporate jargon, buzzword-dropping, over-academic phrasing,
talking down to students, fake motivational speeches, and any promise that
AI/this program guarantees a job.

**Your actual advantage in the room:** you're an industry AI engineer who
can connect *academic concept → real-world engineering → future AI
application* in one breath. Use that — when a concept lands, add one real
sentence about where it shows up in industry, then move on. Don't turn it
into a story.

---

## 8. Misconceptions to Pre-empt

| Misconception | Why students think this | Correct explanation | Analogy |
|---|---|---|---|
| "Computer Science = coding." | Coding is the most visible, most marketed part of CS (YouTube, coding bootcamps, "learn to code" ads). | Coding is *how* you express solutions to a computer; CS also covers how computers store data, communicate, and reason — coding is one skill inside a much larger field. | Coding is to CS what *writing* is to *literature* — essential, but not the whole subject. |
| "Algorithm = code." | Both are associated with "the logic" and are often taught together, so they blur. | An algorithm is the language-independent strategy; code is one specific implementation of it in one specific language. | An algorithm is a recipe; code is the dish cooked in one particular kitchen. |
| "AI is completely separate from programming." | AI is marketed as its own magical category, disconnected from "normal coding." | AI systems are built, trained, and deployed using programming, data structures, and algorithms — it sits *on top of* CS foundations, not apart from them. | AI is a skyscraper; programming and CS are the foundation it's built on — remove the foundation and it can't stand. |
| "Python is AI." | Most visible AI tutorials use Python, so the language and the field get conflated. | Python is a programming language used to *build* AI systems, among many other things (websites, automation, data analysis). It's a tool, not the field itself. | Python is a hammer; AI is one of many things you can build with it. |
| "AI means the computer thinks exactly like a human." | Sci-fi, media portrayals, and anthropomorphic language ("the AI understands," "the AI thinks") reinforce this. | AI systems recognize patterns in data and generate outputs based on that — they don't reason, feel, or understand the way humans do, even when the output looks fluent. | A very advanced calculator can output "correct-looking" answers without understanding anything — impressive pattern-matching isn't the same as thought. |
| "Knowing ChatGPT means knowing AI engineering." | Using a chatbot is the most common hands-on contact people have with "AI." | Using an AI product is like using any app — it doesn't require (or teach) how the underlying model was built, trained, or deployed. AI engineering is the staircase we're building throughout the program. | Knowing how to drive a car doesn't mean you know how to build an engine. |

Address these opportunistically as they surface in student answers — don't
read this table aloud as a block.

---

## 9. Differentiated Questions

Never label a question "for weak students" or "for strong students" out
loud — offer them naturally as the discussion allows, and let students
self-select by who answers.

| Concept | Foundation | Builder | Challenge |
|---|---|---|---|
| Input/Process/Output | "What is an input?" | "Give your own input-process-output example, different from the calculator." | "Can a system have more than one input feeding the same process? Give an example." |
| Computer Science map | "Name one thing that's part of Computer Science besides coding." | "Which part of the map do you think you'd enjoy learning most, and why?" | "Could something belong to more than one area of the map at once? Give an example." |
| Algorithm | "What is an algorithm, in your own words?" | "Describe the algorithm for finding the largest of *three* numbers." | "How would your algorithm change if two or more of the values were equal?" |
| Algorithm vs. Program | "Which one is the 'recipe' and which is the 'dish'?" | "Could the same algorithm be written in two different programming languages? What would stay the same, what would change?" | "Could two *different* algorithms solve the same problem and both be correct? Can you think of one for 'find the larger of two numbers'?" |
| Computational thinking | "What does 'breaking a big problem into smaller ones' mean to you?" | "Pick a daily task and decompose it into 3–4 smaller steps." | "Find a pattern connecting two problems that look unrelated on the surface (e.g., finding a book on a shelf vs. finding a contact in your phone)." |
| Tea activity | "What's one instruction you gave that the 'computer' followed correctly?" | "What assumption did you make that turned out to be missing information?" | "Rewrite your tea algorithm to handle 'what if there's no gas' without skipping straight to a solution — what should the computer *do* instead?" |
| CS → AI bridge | "Which pipeline uses a prompt: programming, ML, or GenAI?" | "What's the key difference between traditional programming and machine learning?" | "Why might 'rules written by a human' fail for a problem like recognizing handwriting, where ML tends to work better?" |

---

## 10. Class Success Criteria

Class 1 is successful if **most students** can, by the end:

1. Explain Computer Science in simple words.
2. Explain input/process/output.
3. Explain what an algorithm is.
4. Distinguish an algorithm from a program.
5. Create a simple everyday algorithm.
6. Explain why computers require precise instructions.
7. Describe how today's foundation eventually connects to AI.

Success is measured by these seven outcomes — **not** by how many slides or
topics were covered. If you ran out of time and had to cut the roadmap
section but every student can do 1–6, the class succeeded.

---

## 11. Recap (Final 5 Questions)

Ask these aloud, cold-call or open-floor, in the last 6–8 minutes. These
test understanding, not memorized definitions — accept answers phrased in
the student's own words.

1. **"In your own words — what is Computer Science?"**
   - *Expected:* Something like "the study of how computers solve problems /
     handle information," possibly naming 1–2 subfields.
   - *Common wrong answer:* "It's coding" (without qualification) — gently
     redirect: "Coding is part of it — what else is part of it?"

2. **"What's the difference between an algorithm and a program?"**
   - *Expected:* Algorithm = the steps/strategy; program = the steps
     written in a programming language.
   - *Common wrong answer:* "They're the same thing" — redirect with the
     recipe/dish analogy.

3. **"Give me an input, a process, and an output for something you did
   this morning."**
   - *Expected:* Any coherent triple (e.g., alarm sound = input, waking up
     = process, getting out of bed = output).
   - *Common wrong answer:* Naming only two of the three, or an output with
     no clear input — probe with "what triggered that?"

4. **"Why does a computer need very precise instructions, more precise than
   a human usually needs?"**
   - *Expected:* Callback to the tea activity — computers don't fill in
     unstated assumptions the way humans do.
   - *Common wrong answer:* "Because computers are dumb" — accept the
     instinct, sharpen the language: "Not dumb — literal. It only does
     exactly what it's told."

5. **"Where does today's lesson eventually connect to AI?"**
   - *Expected:* Something like "AI is built on top of programming and CS —
     we're building the foundation first" / mentions the staircase.
   - *Common wrong answer:* "AI is unrelated to what we learned today" —
     this is the one misconception you must not let stand uncorrected
     before dismissing class.

---

## 12. Homework — Assignment 1: Think Like a Programmer

### Student instructions

Pick **one** everyday process from this list (or propose your own, with
instructor approval):

- Ordering food
- ATM withdrawal
- Online shopping
- Booking a train ticket
- Sending a message
- Making tea
- Booking a cab
- Going to college

For your chosen process:

1. Identify the **Input**, **Process**, and **Output**.
2. Write a simple **algorithm** with **at least 5 numbered steps**.
3. Write in plain language — no programming language, no code.

### Example solution — "Making Tea"

- **Input:** Water, milk, tea leaves/tea bag, sugar, stove/kettle, cup
- **Process:** Boiling, mixing, straining
- **Output:** A cup of ready tea

**Algorithm:**
1. Take a pan and add water.
2. Place the pan on the stove and turn on the heat.
3. Add tea leaves (and milk, if desired) to the water.
4. Let the mixture boil for 2–3 minutes.
5. Add sugar to taste and stir.
6. Turn off the heat and pour the tea through a strainer into a cup.

### Submission expectations

- One page (handwritten photo, doc, or text file — instructor's choice for
  the cohort).
- Must clearly label Input / Process / Output as three separate items.
- Must number the algorithm steps (minimum 5).
- No code, no pseudocode syntax required — plain sentences are fine.

### Beginner version

If 5 steps feels hard, it's fine to under-specify slightly — the goal is
attempting the Input/Process/Output split and *some* ordered list, even if
an instructor would later point out a missing assumption (just like the tea
activity in class).

### Challenge version

Add a **decision point** to your algorithm — a step where the outcome
depends on a condition (e.g., "if the ATM balance is insufficient, the
withdrawal fails and the card is returned"). You don't need to know
if/else syntax; just describe the branch in plain English, the way we did
with the optional ATM activity in class.

Do **not** mention GitHub, code submission, or any tooling — none of that
is required for this assignment.

---

## 13. Instructor Reflection Checklist

Fill this out immediately after class, while memory is fresh.

- [ ] What confused students?
- [ ] Which analogy worked best?
- [ ] Which question generated the most discussion?
- [ ] Where did students lose attention?
- [ ] Which students appeared to need additional support?
- [ ] Which students appeared significantly ahead?
- [ ] Was the pace appropriate — did any section run long or short against
      the timing table in Section 4?
- [ ] Did the pen tablet work effectively? Were students able to copy the
      six drawings in time?
- [ ] What should change before the next cohort runs Class 1?

---

## 14. Pedagogical Guardrail

Before adding *anything* to this class in a future revision, ask:

> "Does this help a complete beginner understand what Computer Science and
> programming actually are?"

If the honest answer is no, defer it to a later class. Depth on the seven
success criteria beats breadth of topics covered, every time.
