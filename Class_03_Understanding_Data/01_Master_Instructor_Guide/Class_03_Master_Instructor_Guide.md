# Class 03 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Understanding Data
**Subtitle:** From the Real World → Information → Data
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 02 — How Machines Learn

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01 and Class 02](#3-relationship-to-class-01-and-class-02)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening — What Is Data? (0–8)](#8-opening--what-is-data-0-8)
9. [Class 02 Callback (8–15)](#9-class-02-callback-8-15)
10. [Data Is Not Just Numbers (15–27)](#10-data-is-not-just-numbers-15-27)
11. [Real World → Observation → Data (27–39)](#11-real-world--observation--data-27-39)
12. [One Thing, Many Pieces of Data (39–50)](#12-one-thing-many-pieces-of-data-39-50)
13. [Examples, Records, and Datasets (50–61)](#13-examples-records-and-datasets-50-61)
14. [Reading a Data Table + Table Activity (61–74)](#14-reading-a-data-table--table-activity-61-74)
15. [Messy Data (74–82)](#15-messy-data-74-82)
16. [More Data ≠ Automatically Better Data (82–90)](#16-more-data--automatically-better-data-82-90)
17. [Labels and Features (90–99)](#17-labels-and-features-90-99)
18. [Useful Data Depends on the Problem (99–107)](#18-useful-data-depends-on-the-problem-99-107)
19. [Connect Back to ML + Data ≠ ML + Final Recap (107–110)](#19-connect-back-to-ml--data--ml--final-recap-107-110)
20. [Final Student Takeaway](#20-final-student-takeaway)
21. [Common Misconceptions](#21-common-misconceptions)
22. [Instructor Language / Teaching Guardrails](#22-instructor-language--teaching-guardrails)
23. [Interaction Philosophy](#23-interaction-philosophy)
24. [Visual / Board Plan](#24-visual--board-plan)
25. [Class 1 / Class 2 Continuity](#25-class-1--class-2-continuity)
26. [Assessment of Understanding](#26-assessment-of-understanding)
27. [Differentiation](#27-differentiation)
28. [Time Management / Timing Safety](#28-time-management--timing-safety)
29. [Extended Version](#29-extended-version)
30. [Advanced Question Parking Lot](#30-advanced-question-parking-lot)
31. [Teacher FAQ](#31-teacher-faq)
32. [Class Success Check](#32-class-success-check)
33. [Source-of-Truth / QA Checklist](#33-source-of-truth--qa-checklist)

---

## 1. Class Identity

| Field | Value |
|---|---|
| Class number | 03 |
| Title | Understanding Data |
| Subtitle | From the Real World → Information → Data |
| Audience | First-year college students, mixed backgrounds — some non-CS, some with basic programming, some with none. No coding prerequisite. No mathematics beyond everyday arithmetic/reasoning. |
| Prerequisites | Class 01 (Problem → Logic → Algorithm → Program → Result; Input → Process → Output) and Class 02 (Traditional Programming vs. Machine Learning; `DATA → LEARNING → MODEL → PREDICTION`). No new prerequisite beyond those two classes. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 02 opened with the word **DATA** and moved on quickly to *learning*, *model*, and *prediction*. Class 03 goes back and opens that first box. It answers the question Class 02 deliberately left unanswered: *what exactly is data, and where does it come from?* |
| Core question | **"How do we turn something happening in the real world into something a computer can work with?"** |
| Core concept | `REAL WORLD → OBSERVATION → DATA`, expanding into `DATA → EXAMPLES → FEATURES → LABELS → DATASET` |
| Class success metric | Without prompting, most students can: (1) define data as "recorded information about something," in their own words; (2) give a non-numeric example of data; (3) explain how an everyday observation becomes recorded data; (4) correctly read a simple table — identify what one row and one column mean; (5) distinguish a feature from a label using a simple example; (6) explain why more data is not automatically better data; (7) state that useful data depends on the question being asked; (8) reconnect today's ideas to Class 02's `DATA → LEARNING → MODEL → PREDICTION`. |

This class is entirely conceptual. **No code. No mathematics. No
statistics. No databases. No implementation.** This is not a Data
Science class — it is the class that makes a future Data Science class
make sense. If you ever feel tempted to explain *how* data is actually
stored, cleaned, or processed, that is the signal to simplify further,
not to go deeper.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one sentence in a student's head with another.
Before this class: *"Data is basically numbers in a spreadsheet."*
After this class: *"Data is recorded information about something in the
real world — and before a machine can learn from it, someone has to
decide what to observe and record in the first place."* That's it.
Every example, table, and activity below exists to land that one
replacement cleanly.

**Teaching philosophy, in one line:** identical in spirit to Class 01 and
Class 02 — intuition before terminology, example before definition, ask
before explaining, everyday examples over invented ones, questions
students can argue about rather than facts they must accept.

**What students should feel by the end:**

- A beginner should feel: *"I always thought 'data' meant numbers and
  spreadsheets. Now I get that a photo, a voice note, or a sentence is
  also data — anything recorded about something is data."*
- A stronger student should feel: *"I can already see why Machine
  Learning cares so much about data quality and variety — bad or narrow
  data was always going to be the actual bottleneck, not the algorithm."*
- Everyone should feel comfortable *looking at a simple table* and
  correctly saying what a row and a column mean — a small, concrete,
  durable skill.

**State this to yourself before you walk in:**

> This is **not** a Data Science class. Nobody in this room is cleaning
> a dataset today. This class exists so that the moment students later
> touch a spreadsheet, a CSV file, or a real dataset, they already have
> the right mental model waiting for it — the same way Class 01 gave
> them a mental model for code before they wrote any, and Class 02 gave
> them a mental model for AI before they built any.

If a question drifts toward "how is data actually stored/cleaned/
processed," pull it back to "what *is* this data, and what does it
represent" — that redirect is always available and is never a cop-out;
it is the actual scope of the class.

---

## 3. Relationship to Class 01 and Class 02

Class 01 built:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
INPUT → PROCESS → OUTPUT
```

Class 02 built:

```
TRADITIONAL PROGRAMMING:   INPUT  →  HUMAN-WRITTEN RULES  →  OUTPUT
MACHINE LEARNING:          DATA   →  LEARNING  →  MODEL   →  PREDICTION
```

...and left one box conspicuously unopened: **DATA**. Class 02's whole
argument — "let the machine learn a pattern from examples instead of
writing every rule by hand" — quietly assumed the class already knew
what "examples" and "data" meant. Class 03 is where that assumption gets
paid off.

**Say this explicitly, early (Section 9 is the natural spot):**

> "Last class, everything started with one word: Data. We moved past it
> fast, because the real excitement was Learning → Model → Prediction.
> Today we're rewinding to that very first box and asking the question
> we skipped: what actually *is* data, and where does it come from
> before a machine ever sees it?"

**The relationship is not new content bolted on — it is zooming in:**

```
Class 2 pipeline:     DATA  →  LEARNING  →  MODEL  →  PREDICTION
Class 3 opens this:   ▲▲▲▲
                       REAL WORLD → OBSERVATION → DATA
```

Frame it exactly like this, because it matters for how students file the
class away mentally:

> "We are not changing what we learned in Class 2. We're looking more
> closely at one part of it."

This prevents students from experiencing the course as a string of
unrelated topics, and reinforces the "staircase" framing Class 01 and
Class 02 both used — see Section 25 for the full continuity treatment.

---

## 4. Learning Objectives

Taken directly from the class brief. For each, the bar is **conceptual
understanding and curiosity** — the same bar Class 01 and Class 02 set.
Nothing here needs to survive an exam.

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | Data is recorded information about something | Can say "data is information that's been recorded" in their own words | A formal/technical definition |
| 2 | Data is not just numbers | Can name a non-numeric example (photo, text, voice, location) unprompted | Any notion of data types, encoding, or file formats |
| 3 | Observations become recorded data | Can describe, for a simple event, what could be observed and how it gets written down | Sensors, binary encoding, digitization detail |
| 4 | The same real-world thing → many possible pieces of data | Can list 3+ different pieces of information describing one person/object | Any formal notion of a "schema" |
| 5 | Identify one example/record in a simple dataset | Can point to a row and say "that's one example" | Database terminology (record vs. tuple, etc.) |
| 6 | Row = example, Column = piece of information | Can correctly state both, for a table they haven't seen before | Any notion of primary keys, relations |
| 7 | Dataset = collection of related examples | Can define it in one sentence and give an example | Any formal data-structure definition |
| 8 | Feature = a piece of information describing an example | Can point at a column and call it a feature, informally | Feature engineering, feature selection |
| 9 | Label = the known answer/category attached to an example | Can point at a "target" column and explain what it represents | "Supervised learning" as a formal term |
| 10 | Real-world data can be messy, incomplete, inconsistent, or wrong | Can point out 2+ problems in a deliberately messy table | Data-cleaning techniques, imputation |
| 11 | More data ≠ automatically better data | Can explain, informally, why quantity without quality/variety isn't enough | Statistical sampling theory |
| 12 | Useful data depends on the problem | Can propose plausible data for a stated problem and explain why it fits | Feature selection algorithms |
| 13 | Connect data to Class 02's pipeline | Can restate `DATA → LEARNING → MODEL → PREDICTION` and place today's ideas inside the DATA box | Any new ML mechanics |
| 14 | Data is a representation of reality, not reality itself | Can explain that a table about a person leaves things out | Epistemology / philosophy of measurement |

---

## 5. Key Terminology

Small and durable beats large and forgettable. These are the **only**
terms this class needs — and even these should be earned through
example first, not opened with.

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Data** | Recorded information about something — from the real world. | "Recorded information about something." | "Data means numbers." "Data means spreadsheets." | Yes — core term |
| **Observation** | Noticing or measuring something about the real world. | "What we notice or check." | Sensors, instrumentation detail | Loosely |
| **Example / Record** | One instance described by data — one student, one car, one email. | "One entry — one thing we're describing." | "Row" as if it's the only correct word (it's the visual form, not the concept) | Yes |
| **Dataset** | A collection of related examples. | "A pile of related examples, put together." | Database, table schema | Yes |
| **Feature / Attribute** | A piece of information describing an example. | "One piece of information about the example." | Feature engineering, feature vector, feature space | Loosely — name only |
| **Label** | The known answer or category attached to an example. | "The answer we already know for that example." | "Supervised learning," "target variable," "ground truth" | Loosely — name only |
| **Row** *(table term)* | The visual line in a table that represents one example. | "One row = one example." | — | Yes |
| **Column** *(table term)* | The visual line in a table that represents one piece of information across all examples. | "One column = one kind of information." | — | Yes |
| **Messy data** | Data that is missing, inconsistent, or wrong. | "Data with problems in it." | Null values, data cleaning, imputation | No — used conversationally |
| **Representation** | Data stands in for something real, but is not the thing itself. | "Data represents reality — it isn't reality." | — | Loosely |

---

## 6. Class at a Glance

Canonical **110-minute** flow. Section 28 gives the 90- and 120-minute
deltas. Timings match the reference arc supplied for this class, with
one adjustment noted below.

| Time | Dur. | Section | Objective | Teaching mode | Pen-tablet | Interaction | Expected student state |
|---|---|---|---|---|---|---|---|
| 0–8 | 8 | Opening — What is Data? | Surface the naive "data = numbers" assumption | Ask → debate → frame | None yet | High — cold-open debate | Curious, a little unsettled |
| 8–15 | 7 | Class 02 Callback | Re-open the DATA box Class 02 skipped | Recall → question | None | Medium | "Oh — we never actually answered that" |
| 15–27 | 12 | Data Is Not Just Numbers | Break the "data = numbers" assumption for good | Ask → challenge → define | Optional light list | High | Genuinely surprised, engaged |
| 27–39 | 12 | Real World → Observation → Data | Install the first core chain | Build live | **Drawing #1 (built live)** | High | Watching closely, anchoring the chain |
| 39–50 | 11 | One Thing, Many Pieces of Data | Data is a representation, not the thing itself | Ask → build together | Drawing #2 | High | "The student didn't change, the description did" |
| 50–61 | 11 | Examples, Records, and Datasets | Install example/record and dataset | Build live with car example | Light | Medium | Comfortable with the vocabulary |
| 61–74 | 13 | Reading a Data Table + Table Activity | Row = example, Column = feature | Build table → guided activity | **Drawing #3** | Very high | Confident reading a table cold |
| 74–82 | 8 | Messy Data | Real data has problems | Show → diagnose | Drawing #4 | High | A little amused, newly skeptical of "clean" data |
| 82–90 | 8 | More Data ≠ Automatically Better | Quality/variety > raw quantity | Ask → escalate → connect to Class 02 | Reuse Drawing #4 area | Medium-high | Reconsidering an assumption |
| 90–99 | 9 | Labels and Features | Distinguish describing-information from known-answer | Build spam-email table live | Drawing #5 | High | Can point at "the answer column" confidently |
| 99–107 | 8 | Useful Data Depends on the Problem | Data is a lens; usefulness is problem-relative | Scenario → canteen activity → debate | None new | Very high | Reasoning, disagreeing productively |
| 107–110 | 3 | Connect Back to ML + Data ≠ ML + Recap | Consolidate, verify, hand off | Ask → students answer | **Drawing #6 (hero, live)** | High | Leaving with 1–2 clear sentences they can repeat |

**Timing note (transparency, per the guide's own instructions):** The
original reference flow allocates 101–107 (6 min) to "useful data
depends on the problem" alone, without a separate slot for the "data is
a lens" idea or the canteen application activity described later in the
brief. Rather than add a 13th row and stretch the class past 110
minutes, this guide **merges** "useful data depends on the problem,"
"data is a lens," and the canteen scenario into one 8-minute block
(99–107, borrowing 2 minutes trimmed evenly from Sections 10, 11, and 14
above, each cut by a few minutes without losing their core moment). The
canteen activity is kept intentionally brief and open-ended inside that
block — see Section 18 for exact pacing. The overall ~110-minute
target and every non-negotiable moment are preserved.

**Non-negotiable blocks** (never compressed away — see Section 28): Data
Is Not Just Numbers, Real World → Observation → Data, Reading a Data
Table, Messy Data, Useful Data Depends on the Problem, Connect Back to
ML + Recap.

---

## 7. Section-by-Section Teaching Guide

Quick **A–G** index for every block; full teaching notes for each live in
Sections 8–19 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening | Surface "data = numbers" as an assumption worth questioning | Students disagree productively about what counts as data | No |
| 2 | Class 02 Callback | Create a felt reason for today's class | Students state that Class 02 never actually defined "data" | No |
| 3 | Not Just Numbers | Break the numbers-only assumption | Students name a non-numeric example of data unprompted | **Yes** |
| 4 | Real World → Observation → Data | Install the first core chain | Students can restate the three-step chain | **Yes** |
| 5 | One Thing, Many Pieces of Data | Data = representation, not the object itself | Students explain that the student described didn't change, only the description did | No |
| 6 | Examples, Records, Datasets | Install example/record and dataset vocabulary | Students point at "one example" and "a dataset" correctly | No |
| 7 | Reading a Data Table | Row/column fluency | Students correctly state what a row and column mean, unprompted, on a new table | **Yes** |
| 8 | Messy Data | Real data has problems | Students spot 2+ concrete problems in a messy table | **Yes** |
| 9 | More Data ≠ Better | Quality/variety over raw quantity | Students explain why 1M wrong examples aren't good data | No |
| 10 | Labels and Features | Distinguish describing-info from known-answer | Students correctly label the "answer" column vs. the "describing" columns | No |
| 11 | Useful Data Depends on the Problem | Data usefulness is problem-relative | Students propose plausible, reasoned data for a stated problem | **Yes** |
| 12 | Connect Back + Recap | Consolidate and hand off | Students restate `DATA → LEARNING → MODEL → PREDICTION` with today's ideas inside the DATA box | **Yes** |

---

## 8. Opening — What Is Data? (0–8)

Do **not** open with "Today we will learn about data." Open with a
concrete, low-stakes real-world question, exactly as Class 01 opened
with smartphone use and Class 02 opened with recommendation feeds.

**Exact opening approach:**

1. Ask, conversationally: *"Imagine I ask you: how crowded is your
   college canteen right now? How would you answer me?"*
2. Collect several different-shaped answers without correcting any of
   them. Expected: "very crowded," "around 50 people," "almost empty,"
   "80% full," "more crowded than yesterday."
3. Write (or just say back) 3–4 of the answers side by side.
4. Ask the pivot question and let it sit: **"Which one of these is
   data?"**
5. Let students debate. Some will say only the number counts. Some will
   say all of them count. Some will say none of them count until it's
   "in a computer."
6. **Do not resolve the debate yet.** Bank it: *"Hold that thought —
   we're about to spend the whole class figuring out exactly this."*
7. Land the framing question: **"How did something happening in the
   real world — people sitting in a canteen — turn into something you
   just told me, in words or numbers? That's today's question: how do we
   turn something happening in the real world into something a computer
   can work with?"**

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "How crowded is the canteen right now?" | "very crowded," "50 people," "almost empty," "80% full," "busier than yesterday" | Offer your own first: "I'd probably say 'packed' — what would you say?" |
| "Which one of these is data?" | Split opinions — some say only numbers, some say all of them | Narrow it: "Is 'almost empty' information about the real world, or not?" |

**How to handle silence:** Never let a question hang more than ~5–7
seconds unaddressed at this stage — these are genuinely low-stakes, so
gentle cold-calling by row/name is fine. The goal is disagreement, not a
correct answer yet.

**Transition:** Once the debate has produced real disagreement, say the
core question aloud slowly: *"How do we turn something happening in the
real world into something a computer can work with? Let's find out — but
first, a quick rewind to last class."*

---

## 9. Class 02 Callback (8–15)

Bring back the Class 02 pipeline exactly as it was left:

```
DATA → LEARNING → MODEL → PREDICTION
```

**What the instructor says:**

> "Last class, what did Machine Learning start with?"

Expected: **Data.** (If students say "examples" or "labeled examples,"
accept it — same idea, different word — and bridge: "Right, examples —
which are made of data. Which brings us to the actual question...")

> "But what exactly *is* data? Last class, we used the word constantly —
> labeled cat and dog photos, labeled emails — and moved straight on to
> Learning, Model, and Prediction. We never actually stopped and asked:
> what is data, and where does it come from before a machine ever touches
> it?"

**Do not answer this yet.** Let it stand as the reason the whole class
exists:

> "That's Class 3. Today we open that first box."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did ML start with, last class?" | "Data" / "examples" |
| "Did we ever define what data actually is?" | Most will realize: "not really" |
| "So where does data even come from?" | Mixed guesses — "the internet," "spreadsheets," "someone collects it" — all fine, don't resolve yet |

**Transition:** *"Let's start with a much more basic question than you'd
expect: when you hear the word 'data,' what do you picture?"*

---

## 10. Data Is Not Just Numbers (15–27) — NON-NEGOTIABLE

**This is the first major teaching moment. Do not rush it.**

**Ask first, before defining anything:**

> "When you hear the word 'data,' what do you imagine?"

Expected: numbers, Excel, spreadsheets, tables, graphs, statistics.

**Then challenge it, one example at a time, pausing for a real answer
after each:**

- "Is a photograph data?"
- "Is a voice recording data?"
- "Is a text message data?"
- "Is your phone's location data?"
- "Is 'the canteen felt almost empty' — a sentence, not a number —
  data?" (callback to the opening)

Let students argue both sides for each — some will insist a photo isn't
data until it's "turned into" something computer-readable. Don't correct
that instinct harshly; it contains a true idea (there's a step between
"a photo exists" and "a computer can use it"), but it is out of scope
for today — gently table it: *"You're onto something — how something
gets stored inside a computer is a whole topic on its own. Today we're
only asking whether it counts as information about the real world."*

**Land the working definition — write it up, keep it exactly this
simple:**

```
DATA = RECORDED INFORMATION ABOUT SOMETHING
```

> "Notice what's *not* in that definition — no mention of numbers,
> spreadsheets, or computers. A photo is recorded information about a
> moment. A voice note is recorded information about what someone said.
> Numbers are just one *form* data can take — not the definition of
> data."

**Resolve the opening debate explicitly now:**

> "Back to the canteen question — 'very crowded,' '50 people,' 'almost
> empty' — which one was data? All of them. Every single answer was
> recorded information about the real world. They're just different
> *forms* of the same thing."

**Common misconception to pre-empt here:** "A dataset is just an Excel
file." Plant the seed now that data existed long before spreadsheets —
spreadsheets are one convenient *container* for data, not what data
*means*. Return to this fully in Section 21.

**Transition:** *"Okay — so data isn't just numbers. But something still
had to happen for 'the canteen felt crowded' to become information we
can actually record and work with. What was that something?"*

---

## 11. Real World → Observation → Data (27–39) — NON-NEGOTIABLE, HERO MOMENT

**Use a simple, low-stakes real-world example:**

> "It is raining outside."

**Ask what could be observed about that one fact:**

> "If I wanted to record information about 'it is raining outside,'
> what could I actually observe or check?"

Expected: temperature, rain/no rain (yes or no), wind, how heavy the
rain is, what time it is, where you are.

**Build the chain live, one step at a time — do not reveal it
finished:**

1. Write **REAL WORLD** — *"Something is actually happening: it's
   raining."*
2. Arrow down, write **OBSERVE** — *"Someone notices or checks
   something about it — is it raining, how hard, what time."*
3. Arrow down, write **RECORD** — *"That observation gets written down,
   said aloud, saved, typed, photographed — put into some form that can
   be kept."*
4. Arrow down, write **DATA** — *"Now it's data — recorded information
   about something that happened in the real world."*

Finished board:

```
REAL WORLD
    ↓
OBSERVE
    ↓
RECORD
    ↓
DATA
```

**Important nuance — say this explicitly, it's the whole point of the
chain:**

> "An observation only becomes *useful* data once it's recorded in some
> form that can be stored or worked with later. If I notice it's raining
> but never tell anyone or write it down, that observation disappears —
> it never became data. The 'record' step is what makes it stick
> around."

Do **not** introduce sensors, binary encoding, or file formats — the
chain stays entirely at the conceptual level.

**Immediately re-run the chain with the opening's canteen example** to
cement it before moving on:

> "Real world: the canteen right now. Observe: someone looks around, or
> counts people, or checks a crowd-tracking app. Record: they say '80%
> full,' or type a number into a spreadsheet, or take a photo. Data:
> whatever got recorded — a number, a sentence, or a photo, it's all
> data."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What could we observe about 'it is raining'?" | Temperature, rain/no rain, wind, time, amount |
| "Does an observation nobody writes down count as data?" | After discussion: "not really — it has to be recorded somewhere" |
| "Where does data come from, in one sentence?" | "Someone observes something real and records it" |

**Transition:** *"So one real-world thing — a rainy day, a canteen, a
student — can be observed in a lot of different ways. Let's stick with
something even more familiar: you."*

---

## 12. One Thing, Many Pieces of Data (39–50)

Use a student as the example (with their consent, or a hypothetical
"Student X" if anyone's shy).

**Build a list live:**

```
STUDENT
  ↓
Name
Age
Height
Attendance
Marks
```

**Ask, and let the answer land:**

> "Did the student change while I was listing those five things?"

Expected: **No.**

> "Did the way we *describe* the student change?"

Expected: **Yes — we now have five different pieces of information about
the same one person.**

**Land the core statement:**

```
DATA IS A REPRESENTATION OF SOMETHING IN THE REAL WORLD.
```

> "The student is real. Name, Age, Height, Attendance, and Marks are
> data *about* the student — five different observations, all recorded
> about the same one real thing."

**Introduce the term lightly — do not turn this into a vocabulary
lecture:**

> "Each one of those — Name, Age, Height — is called a **feature** or
> **attribute**. All that means is: one piece of information describing
> an example. You'll hear this word again later in the course; today,
> just get comfortable with the idea, not the word."

**Ask for a second round to reinforce the pattern with a different
object:**

> "Now you try — pick something in this room. What are three different
> pieces of data we could record about it?"

Expected: a chair → color, material, height, how many legs; a phone →
brand, battery %, screen size.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Did the student change?" | No |
| "Did the description change?" | Yes |
| "So what is data, in relation to the real thing it describes?" | "A representation of it" / "information about it" |

**Transition:** *"So one real-world thing can turn into several pieces
of data. Now — what do we call it when we put those pieces together,
and what do we call it when we have many of these all lined up?"*

---

## 13. Examples, Records, and Datasets (50–61)

Use a car example — deliberately different domain from "student," to
show the pattern generalizes.

**Build live, one car first:**

```
CAR A
  Price
  Year
  Mileage
```

> "This one car, described by three pieces of data — Price, Year,
> Mileage — is what we'll call one **example**, or one **record**. One
> real thing, described by its data."

**Then expand to several cars:**

```
Car A
Car B
Car C
Car D
Car E
```

> "Now I have five examples, all described the same way. Put together,
> this collection is called a **dataset**."

**Land the definition — keep it visual and simple:**

```
DATASET = COLLECTION OF RELATED EXAMPLES / DATA
```

**Ask:**

> "If I bought a sixth car and wanted to add it to this collection, what
> would I be adding — a whole new dataset, or one more example inside the
> same dataset?"

Expected: one more example inside the same dataset.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What's one car, described by its data, called?" | An example / a record |
| "What's the whole collection called?" | A dataset |
| "If I add a sixth car, is that a new dataset?" | No — one more example in the same dataset |

**Transition:** *"We keep saying 'collection' and 'examples' out loud —
but there's a much more natural way to actually *see* a dataset. Let's
look at one."*

---

## 14. Reading a Data Table + Table Activity (61–74) — NON-NEGOTIABLE

### Part A — Building the table (61–68)

Use a simple table:

```
Student | Age | Attendance | Marks
```

Fill in 3–4 rows live, using the class's earlier "student" example plus
a couple of invented ones.

**Ask:**

> "What does one row represent?"

Expected: **one student / one example.**

> "What does one column represent?"

Expected: **one piece of information about all of the examples.**

**Land the structure — this is one of the most important visual ideas
of the whole class:**

```
ROW    → ONE EXAMPLE
COLUMN → ONE ATTRIBUTE / FEATURE
```

Say it out loud, slowly, and let students repeat it back in their own
words before moving on — this needs to be automatic by the end of the
class.

Do **not** introduce relational databases, primary keys, or SQL.

### Part B — Table activity: movies (68–74)

Show a new table students have not seen used yet, so they must apply
the row/column idea cold rather than recall the student example:

```
Movie          | Genre    | Duration | Rating
---------------|----------|----------|-------
Interstellar   | Sci-Fi   | 169 min  | 8.7
Chhichhore     | Drama    | 143 min  | 8.2
Andhadhun      | Thriller | 139 min  | 8.3
Dangal         | Sports   | 161 min  | 8.4
```

**Ask, in order, waiting for a real answer each time:**

1. "How many examples are in this table?" *(Four.)*
2. "What does one row represent?" *(One movie.)*
3. "What does the Rating column tell us, for every single movie in this
   table?" *(One piece of information — the rating — for each movie.)*
4. "If I add a fifth movie, do I add a row or a column?" *(A row — a new
   example, described by the same four pieces of information.)*
5. *(Stretch)* "If I decided I also wanted to record each movie's
   language, would that be a new row or a new column?" *(A new column —
   a new piece of information about every existing example.)*

**Purpose:** students should leave able to visually read *any* simple
structured table, not just the ones used in class.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How many examples here?" | 4 |
| "What does a row mean?" | One movie / one example |
| "What does the Rating column tell us?" | One piece of info per movie |
| "New movie → row or column?" | Row |
| "New kind of info about every movie → row or column?" | Column |

**Transition:** *"You can now read any simple data table. But real-world
data doesn't always look this clean. Let's look at what actually happens
in practice."*

---

## 15. Messy Data (74–82) — NON-NEGOTIABLE

**Introduce a deliberately problematic table:**

```
Student | Age       | Attendance
--------|-----------|------------
A       | 18        | 92%
B       | ?         | 78%
C       | 18        | 105%
D       | "eighteen"| 65%
```

**Ask, and let students actually look for the problems themselves before
you name any:**

> "Can a computer easily work with this table, as it is? What's wrong
> with it?"

Give real wait time (5–10 seconds) — let students hunt.

Expected findings:

- **Student B's age is missing** — "?" instead of a value.
- **Student C's attendance is 105%** — impossible; attendance can't
  exceed 100%.
- **Student D's age is written as the word "eighteen"** instead of the
  number 18 — same information, inconsistent form.

**Land the core statement:**

```
REAL-WORLD DATA IS OFTEN MESSY.
```

> "Missing values, impossible values, inconsistent formats — this is
> completely normal. Almost no dataset arrives perfectly clean. We are
> not going to learn how to fix this today — just how to *recognize*
> it, because recognizing it is the first step, and it's a habit worth
> having from day one."

**Explicitly do not teach data-cleaning techniques** — no imputation, no
normalization, no rules for "what to do" with each problem. If a
student asks "so what do we do about it," the honest answer is:

> "Good instinct — that's a real skill called data cleaning, and it's
> its own topic later in the course. Today, the goal is just to be able
> to *spot* messy data when you see it."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What's wrong with Student B's row?" | Age is missing |
| "What's wrong with Student C's row?" | Attendance over 100% — impossible |
| "What's wrong with Student D's row?" | Age written as a word, not a number — inconsistent |
| "Is messy data rare or common in the real world?" | Common |

**Transition:** *"So real data can be messy. Here's a related question
that trips people up: if messy data is a problem, does having a *huge
amount* of data automatically fix it?"*

---

## 16. More Data ≠ Automatically Better Data (82–90)

**Ask, and let the "obviously yes" instinct show itself first:**

> "If I have one million examples, is that automatically good data?"

Many will say yes at first. Push:

> "What if every single one of those million examples is wrong, or
> they're all nearly identical to each other?"

Expected: **No — that's not good, no matter how many there are.**

> "What if instead I have just 1,000 examples, but they're accurate and
> cover a good variety of real situations?"

Expected: **That's better — even though it's a much smaller number.**

**Land the core statement:**

```
MORE DATA ≠ AUTOMATICALLY BETTER DATA
```

> "Quantity is not the same thing as quality, and it's not the same
> thing as variety either. A dataset needs to be accurate, and it needs
> to cover the different situations you actually care about."

**Explicit callback to Class 02 — do this, it's one of the strongest
connective threads in the class:**

> "Remember the cats-vs-dogs example from last class? If the issue ever
> came up that the system was struggling, was the problem simply *not
> enough photos*? Or could it just as easily have been that the photos
> weren't varied enough — say, only small dogs and only big cats? The
> issue was never purely a quantity problem — it's the same idea we just
> landed on."

Do **not** introduce sampling, statistical significance, or any formal
terminology — keep this entirely intuitive.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Is 1 million examples automatically good data?" | No |
| "What if they're all wrong?" | Still not good |
| "What if 1,000 examples are accurate and varied?" | Better than 1 million bad ones |
| "What was the real issue in the Class 2 cats/dogs example?" | Lack of variety, not just lack of quantity |

**Transition:** *"So far we've talked about data describing examples in
general. Now let's look at a special, very useful kind of column that
shows up in a lot of datasets — one that holds the 'answer.'"*

---

## 17. Labels and Features (90–99)

### Part A — Labels (90–95)

**Build a table live:**

```
Email                    | Label
-------------------------|----------
"Win free money!"        | Spam
"Meeting at 3 PM"        | Not Spam
"Claim your prize"       | Spam
"Project update"         | Not Spam
```

**Ask:**

> "What does the second column tell us, for each email?"

Expected: **whether it's spam or not — the answer, already known, for
each example.**

**Land the definition:**

```
LABEL = THE KNOWN ANSWER OR CATEGORY ATTACHED TO AN EXAMPLE
```

> "Someone already looked at each of these emails and decided: spam, or
> not spam. That decision — already known, already attached to the
> example — is the label."

Do **not** introduce "supervised learning" as a formal term. If it
naturally comes up, it's fine to *say the words once* and move on:
"later, you'll hear this called supervised learning — for today, just
'label' is enough."

### Part B — Features vs. Label (95–99)

**Expand the table:**

```
Email Text          | Sender Type | Time    | Label
--------------------|-------------|---------|----------
"Win free money!"   | Unknown     | 2:14 AM | Spam
"Meeting at 3 PM"   | Colleague   | 9:02 AM | Not Spam
"Claim your prize"  | Unknown     | 3:47 AM | Spam
"Project update"    | Colleague   | 11:15 AM| Not Spam
```

**Ask:**

> "Which columns describe the example, and which column holds the
> answer we already know?"

Expected: Email Text, Sender Type, and Time **describe** the example —
those are **features**. Label holds the known answer.

**State explicitly, this prevents a real and common misconception:**

> "Not every dataset has a label column. Some datasets are just a
> collection of examples described by features, with no known answer
> attached at all. Today we're simply learning what the word *label*
> means, for the datasets that do have one."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does the Label column tell us?" | The known answer/category for that example |
| "Which columns are features, in the expanded table?" | Email Text, Sender Type, Time |
| "Does every dataset need a label?" | No |

**Transition:** *"Now that we know what data can look like — examples,
features, labels, whole datasets — here's the real question every data
person actually has to answer first: which data should we even bother
collecting?"*

---

## 18. Useful Data Depends on the Problem (99–107) — NON-NEGOTIABLE

This block deliberately combines three closely related ideas from the
class brief — data-depends-on-the-problem, data-as-a-lens, and the
canteen application activity — into one continuous 8-minute arc (see the
timing note in Section 6). Keep the pace brisk; this works because all
three ideas are really one idea told three ways.

### Part A — Data depends on the problem (99–102)

**Pose a problem:**

> "Suppose we want to predict: will a food order be late?"

**Ask:**

> "What data might actually matter here?"

Expected: distance to the restaurant, which restaurant, time of day,
the restaurant's past order history, weather, traffic.

**Then pivot hard:**

> "Would that same data — distance, restaurant, traffic — be useful for
> a completely different question: will a student enjoy a movie?"

Expected: **No — mostly unrelated.**

**Land the core statement:**

```
USEFUL DATA DEPENDS ON THE PROBLEM.
```

> "This is one of the most important ideas in this entire class. There's
> no such thing as 'good data' floating in the abstract — data is useful
> *relative to* the question you're trying to answer."

### Part B — Data is a lens (102–104)

**Return to the student example from Section 12:**

```
PERSON
 ↓
Age
Height
Attendance
Marks
```

**Ask:**

> "Does this list completely describe the person?"

Expected: **No — obviously not; it leaves out personality, interests,
health, everything else.**

**Land the statement, and keep it practical, not philosophical:**

```
DATA IS A REPRESENTATION OF REALITY.
EVERY REPRESENTATION LEAVES SOMETHING OUT.
```

> "That's not a flaw to fix — it's just true of any data, always.
> Which is exactly why the next point matters so much: **what we choose
> to record matters**, because whatever we don't record simply isn't
> there for anyone — or any machine — to use later."

### Part C — Canteen application activity (104–107)

**Return to the class's own opening example, now as a group activity:**

> "Suppose our college wants to know whether the canteen will be crowded
> at 1 PM tomorrow. What data could we collect?"

Collect freely for ~1 minute: number of classes ending around 1 PM,
today's menu, day of the week, weather, past crowd patterns, whether
it's exam season.

**Then ask the harder question:**

> "Of everything we just listed, which of these do you actually think
> would be useful — and which are probably useless?"

**Encourage real disagreement.** Two students can reasonably argue for
or against "weather" or "today's menu" — that's the point. **Do not
converge on one official correct list.** The goal is the *reasoning*,
not a settled answer:

> "There's no single perfect list here, and that's intentional. What
> matters is that you're now asking the right questions: what's the
> problem, what should we observe, what should we record, what
> information might actually matter."

This is explicitly framed as an early taste of **Data Science
thinking** — reasoning about what to collect, before any collecting,
cleaning, or modeling happens.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What data matters for 'will this order be late?'" | Distance, restaurant, time, traffic, past history |
| "Would that same data help predict movie enjoyment?" | No |
| "Does Age/Height/Attendance/Marks fully describe a person?" | No |
| "What data might predict canteen crowding at 1 PM?" | Class schedules, menu, day, weather, past patterns — open debate |

**Transition:** *"We've now gone all the way from 'what even is data' to
'how do we decide what data to collect for a real problem.' Let's put
the whole picture back together, and connect it to where we started —
Machine Learning."*

---

## 19. Connect Back to ML + Data ≠ ML + Final Recap (107–110) — NON-NEGOTIABLE

**Time is tight here by design (see Section 6's timing note) — this
block should feel like a fast, satisfying assembly of everything
already built, not new teaching.**

### Reconstruct the full chain (Drawing #6, HERO — build live)

> "Let's put the whole day on one board."

Build it top to bottom, one line at a time, pausing half a beat between
each — do **not** reveal it finished:

```
REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
    ↓
LEARNING
    ↓
MODEL
    ↓
PREDICTION
```

> "The bottom four lines are exactly what Class 2 taught you: Data →
> Learning → Model → Prediction. Today, we opened the very first box and
> found what's actually above it: Real World → Observation → Data.
> Nothing from last class changes — we just filled in where Data
> actually comes from."

**Quickly show the second expansion, already built across today's
class, as one more line beneath DATA:**

```
DATA
 ↓
EXAMPLES
 ↓
FEATURES
 ↓
LABELS
 ↓
DATASET
```

> "And inside that same DATA box: examples get described by features,
> some examples carry a label, and a collection of examples is a
> dataset. 'Data' was never one abstract magic ingredient — it's built
> out of pieces you now know by name."

### Data ≠ Machine Learning

**Ask directly:**

> "If I hand you a dataset right now, do you automatically have Machine
> Learning?"

Expected: **No.**

```
DATA ≠ MACHINE LEARNING
```

> "Data is an ingredient. Machine Learning is the *process* that uses
> data to learn patterns and build a model — that's Section 14 from last
> class, Learning → Model. Today's whole class lived entirely inside the
> first ingredient."

### Final recap — ask, don't tell

Ask students to answer in their own words, cold-calling or show-of-hands
as time allows (compress to 4–5 of these if genuinely short on time —
protect #1, #6, #7, and the final ML-connection question):

1. What is data?
2. Can data be something other than numbers?
3. What is a dataset?
4. What does a row represent? What does a column represent?
5. What is a feature? What is a label?
6. Why can real-world data be messy?
7. Why isn't more data automatically better?
8. Why does useful data depend on the problem?
9. **"How does today's class connect to Machine Learning?"** — expected:
   *"Machine Learning needs data, and data represents examples from the
   real world."*

### Close with the final statement, said slowly

> "Before we can teach a machine from data, we first have to understand
> what data we're giving it. That's the whole of today's class in one
> sentence."

---

## 20. Final Student Takeaway

Put this on the board or final slide, unchanged from the class brief:

```
DATA     = recorded information about something
DATASET  = collection of related examples
FEATURE  = information describing an example
LABEL    = known answer/category for an example

REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
    ↓
LEARNING
    ↓
MODEL
    ↓
PREDICTION
```

> "Before we can teach a machine from data, we first have to understand
> what data we're giving it."

---

## 21. Common Misconceptions

For each: **listen for** it, use a **short reframe**, never shame the
student who raised it, and **return to the mental model** rather than
arguing the point in the abstract.

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "Data means numbers." | "Isn't data just numbers/statistics?" | "Numbers are one *form* data takes — a photo or a sentence is also recorded information." | `DATA = RECORDED INFORMATION ABOUT SOMETHING` |
| 2 | "A photograph isn't data." | "That's not really data, it's just a picture." | "It's recorded information about a real moment — that's exactly what data means here." | Section 10 |
| 3 | "A dataset is just an Excel file." | "So a dataset is a spreadsheet, right?" | "A spreadsheet is one convenient *container* for a dataset — the dataset is the collection of examples, not the file format." | Section 13 |
| 4 | "Every row is a different feature." | Row/column reversed in their own words | "A row is one whole example. A column is one piece of information shared across all examples." | `ROW → EXAMPLE`, `COLUMN → FEATURE` |
| 5 | "Every dataset must have a label." | "So there's always an answer column?" | "Some datasets have labels, some don't — today we only learned what the word means when one is present." | Section 17, Part B |
| 6 | "More data always means better data." | "So we should just collect as much as possible?" | "Quantity without accuracy or variety isn't automatically useful — quality and coverage matter more." | Section 16 |
| 7 | "If data is recorded, it must be correct." | Treating a table as automatically trustworthy | "Recording something doesn't make it accurate — that's exactly what messy data looks like." | Section 15 |
| 8 | "Data completely describes reality." | "So this table tells us everything about the person?" | "Every representation leaves something out — that's normal, not a flaw." | Section 18, Part B |
| 9 | "Any data is useful for any problem." | Applying one problem's data to an unrelated one | "Useful data is relative to the question — traffic data won't help predict movie taste." | Section 18, Part A |
| 10 | "Data itself is Machine Learning." | "So if I have a dataset, I have an ML model?" | "Data is the ingredient. Learning is the process that turns it into a model." | `DATA ≠ MACHINE LEARNING` |

---

## 22. Instructor Language / Teaching Guardrails

The instructor must **NOT**, at any point in this class:

- start coding, or show any programming language
- teach SQL, spreadsheets-as-a-tool, or database software
- explain relational databases, keys, or schemas formally
- teach statistics, probability, or distributions
- teach data cleaning, preprocessing, normalization, or imputation
  techniques
- teach train/test split, model evaluation, or accuracy metrics
- teach formal ML algorithms, supervised/unsupervised learning as named
  topics, regression, or classification as formal ML concepts
- go into neural networks, deep learning, transformers, embeddings,
  RAG, or agents
- introduce mathematical notation of any kind

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that later. Today we're
> understanding what data actually is."

Then return to whichever anchor fits the moment:

```
REAL WORLD → OBSERVATION → DATA
```

or

```
DATA → LEARNING → MODEL → PREDICTION
```

See Section 30 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 23. Interaction Philosophy

Class 03 should be interactive throughout, but **not every section
needs to be a formal activity** — use questions strategically rather
than turning each block into a structured exercise.

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 5–10 seconds for major reasoning questions —
specifically: "Which of these is data?" (Section 8), "How many rules
would we need... / what could we give the computer instead" — wait,
that's Class 02; for Class 03 the equivalent major-reasoning moments
are: "Can a computer easily work with this table?" (Section 15), "Is
one million examples automatically good data?" (Section 16), and "Which
of these would actually be useful?" (Section 18, canteen activity).

**Do not immediately rescue students from silence.** A pause before an
answer emerges is doing real cognitive work — resist the urge to fill it.

**Built-in reasoning opportunities to protect, in priority order:**

1. What counts as data? (Section 8, 10)
2. Real world → observation → data (Section 11)
3. Reading a table cold (Section 14, Part B)
4. Identifying messy data (Section 15)
5. Quality vs. quantity (Section 16)
6. Features vs. labels (Section 17)
7. What data would be useful for a stated problem? (Section 18)

---

## 24. Visual / Board Plan

These are the key drawings later Pen-Tablet and Presentation artifacts
will build on. Do not create those artifacts now — this section only
specifies what they must contain.

**Drawing 1 — Real World → Observation → Data**
Built live in Section 11. Three arrows, four words. The first
foundational chain of the class.

**Drawing 2 — One Example, Many Pieces of Information**
Built live in Section 12. One box ("STUDENT") branching into 4–5
labeled pieces of information (Name, Age, Height, Attendance, Marks).

**Drawing 3 — Data Table Structure**
Built live in Section 14. A simple table with an arrow pointing across
one row labeled "EXAMPLE" and an arrow pointing down one column labeled
"FEATURE."

**Drawing 4 — Messy Data**
Built live in Section 15. The problem student table, with the three
issues (missing, impossible, inconsistent) circled or annotated as they
are discovered — annotate live, don't pre-mark it.

**Drawing 5 — Data → Examples → Features → Labels → Dataset**
Built live across Sections 13 and 17, assembled explicitly in Section
19 as part of the hero reconstruction.

**Drawing 6 — HERO — Real World → Observation → Data → Learning → Model
→ Prediction**
Reserved for Section 19. Mark this as a **live construction** — do not
show the completed six-line chain before students have reasoned their
way to each piece across the class. This is the single most important
drawing of Class 03, the same way the four-box pipeline was the hero
drawing of Class 02.

---

## 25. Class 1 / Class 2 Continuity

Explicitly narrate where Class 03 sits in the course staircase — this
prevents students from experiencing each class as an unrelated topic.

**Class 1:**

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**Class 2:**

```
DATA → LEARNING → MODEL → PREDICTION
```

**Class 3:**

Opens the **DATA** box from Class 2.

**Say this once, clearly (Section 9 or Section 19 are the natural
spots):**

> "We are not changing what we learned in Class 2. We're looking more
> closely at one part of it."

This is the single most important continuity statement in the guide —
it is what turns three separate classes into one staircase.

---

## 26. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks only, throughout the class, not at the end alone.

A student is demonstrating real understanding if they can:

- give a non-numeric example of data, unprompted
- explain how an everyday observation becomes recorded data
- correctly identify what a row and a column represent, on a table
  they haven't seen before
- distinguish a feature from a label, using a simple example
- spot at least one concrete problem in a messy data table
- explain, informally, why more data isn't automatically better data
- propose plausible, reasoned data for a stated problem (canteen,
  delivery lateness, etc.)
- connect today's material back to `DATA → LEARNING → MODEL →
  PREDICTION` without being told to

**Do not** judge understanding solely from students correctly repeating
the definitions in Section 5 — repeating "data is recorded information
about something" proves memorization, not understanding. The table
activity (Section 14, Part B) and the canteen activity (Section 18,
Part C) are the two strongest real-time understanding signals in the
class.

---

## 27. Differentiation

**For students with no programming/data background:** Anchor everything
in the student and canteen examples specifically — they require zero
prior exposure to anything technical. If row/column terminology is
confusing, physically point: "this whole line = one example; this whole
line, going down, = one kind of information."

**For students with prior spreadsheet/Excel exposure:** They will
recognize the table structure immediately — use them productively by
asking them to describe row/column in their own words first, then have
the rest of the class confirm or refine it. Watch for them jumping ahead
to spreadsheet *formulas* or *functions* — redirect gently: "hold onto
that, today's just about the structure, not the tool."

**For stronger/more curious students:** Let them propose their own
messy-data examples in Section 15, or their own second real-world
scenario in Section 18 (beyond the canteen) to reason through with
similar rigor — this deepens reasoning without adding new technical
scope, matching the Extended Version guidance in Section 29.

**For students who stay quiet:** The canteen activity (Section 18, Part
C) and the movie table activity (Section 14, Part B) are the easiest
re-entry points — both have low-stakes, multiple-reasonable-answers
questions where there is no risk of a starkly "wrong" answer.

---

## 28. Time Management / Timing Safety

**If the class is running long, protect these blocks, in priority
order** (matches the non-negotiable list in Section 7):

1. Real World → Observation → Data (Section 11)
2. Reading a Data Table (Section 14)
3. Messy Data (Section 15)
4. Features vs. Labels distinction (Section 17)
5. Useful Data Depends on the Problem (Section 18)
6. Connect Back to ML + Recap (Section 19)

**Compress, in this order, before touching the protected list:**

- Extended examples and second-round activities (e.g., the "pick
  something in the room" extension in Section 12)
- Number of student responses collected per question (settle for 2–3
  instead of open-ended)
- Discussion time around minor terminology (feature/attribute naming)
- The canteen activity's open debate (Section 18, Part C) — cap at one
  round of "useful vs. not" instead of extended back-and-forth

**Do not cut:** the Class 02 connection (Section 9 and Section 19), the
row/column structure (Section 14), or messy data (Section 15) — these
three are the load-bearing walls of the entire class.

### 90-minute version

Trim as follows: Opening to 5 min, Class 02 Callback to 5 min, Not Just
Numbers to 9 min, Real World→Observation→Data unchanged (12 min),
One-Thing-Many-Data to 7 min, Examples/Datasets to 8 min, Table +
Activity to 10 min, Messy Data unchanged (8 min), More-Data-Not-Better
to 5 min, Labels/Features to 7 min, Depends-on-Problem to 6 min,
Connect-Back+Recap unchanged (3 min). Cut the "pick something in the
room" extension and the second messy-data example entirely.

### 120-minute version

Add time back to: Not Just Numbers (+2 min, allow a 5th or 6th
data-or-not example), One-Thing-Many-Data (+2 min, run the "pick
something in the room" extension fully), Table Activity (+3 min, add a
second practice table students build column-by-column themselves),
Depends-on-Problem (+3 min, let students propose and debate a *second*
real-world scenario beyond the canteen, per Section 29).

---

## 29. Extended Version

If time allows, deepen reasoning — do **not** introduce any new
technical scope.

- Let students propose additional non-numeric data examples beyond the
  five given (Section 10).
- Compare different possible representations of the same real-world
  event (e.g., "the canteen is crowded" — sentence, percentage, count,
  photo) and discuss what each form makes easy or hard to do with it,
  without going into file formats.
- Examine a second, different messy-data table students help construct
  themselves (Section 15).
- Run a second round of "useful data depends on the problem" with a
  scenario students propose themselves — e.g., "will it rain during our
  college fest," "which club should a new student join."
- Ask students, in pairs, to invent their own tiny 3-column, 3-row
  dataset about anything they choose, and identify which column (if
  any) would be a label.

---

## 30. Advanced Question Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "How does a computer actually store a photo as data?" | "That's about file formats and encoding — a real topic, just not today's." | "Today we're only asking whether it counts as recorded information." |
| "How do you actually clean messy data?" | "That's a real skill called data cleaning — its own topic later." | Return to: "today's goal is just spotting it." |
| "Isn't a label the same as what supervised learning uses?" | "Yes — you'll hear 'supervised learning' formally later." | Return to: "for today, 'label' is enough." |
| "How much data does an ML model actually need?" | "That depends on the problem — no fixed number." | Return to: `MORE DATA ≠ AUTOMATICALLY BETTER DATA` |
| "What about privacy — should all this data even be collected?" | "That's a real and important question — data ethics is worth its own dedicated conversation." | Return to: "today we're only asking what data *is*, not whether every use of it is okay." |
| "Can a computer read text/audio directly like it reads numbers?" | "There are ways to convert it — that's a deeper topic ahead." | Return to: "today, both count as data either way." |

---

## 31. Teacher FAQ

**Q: A student insists a photo "isn't really data" because it's not in
a spreadsheet. How far do I push back?**
A: Use the reframe in Section 21, #2. Don't need to fully win the
argument in the moment — planting "recorded information, not just
numbers" is enough; it will get reinforced again in Section 19's recap.

**Q: What if the canteen activity (Section 18) converges too fast on
one "obviously correct" answer and nobody disagrees?**
A: Introduce a deliberately debatable item yourself — e.g., "what about
today's menu?" — and ask directly: "does anyone think this one
*wouldn't* actually help?" Manufactured disagreement is fine here; the
point is the reasoning process, not organic conflict.

**Q: A student already knows the terms "feature" and "label" from
outside class (YouTube, a friend, prior exposure). Do I let them use
them?**
A: Yes — welcome it, but keep the class's own pace for everyone else.
Use them as a checkpoint: "Right — can you explain what that word means
to the rest of the class, in your own words?"

**Q: What if I run out of time before the canteen activity?**
A: Per Section 28, compress it to a single quick round rather than
cutting it — it's the class's best "Data Science thinking" moment and
is explicitly non-negotiable.

---

## 32. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Define data as recorded information about something, in their own
   words.
2. Give at least one non-numeric example of data.
3. Explain how an everyday observation becomes recorded data.
4. Correctly read a simple, unfamiliar table — state what one row and
   one column mean.
5. Distinguish a feature from a label using a simple example.
6. Explain why more data is not automatically better data.
7. State that useful data depends on the question being asked.
8. Reconnect today's ideas to `DATA → LEARNING → MODEL → PREDICTION`.

A class where most students can do these in plain, imperfect language —
not exact textbook wording — has met the bar.

---

## 33. Source-of-Truth / QA Checklist

Verified against the class brief before finalizing this guide:

- [x] Class 03 clearly follows Class 01 and Class 02 (Sections 3, 25).
- [x] The core question is preserved: "How do we turn something
      happening in the real world into something a computer can work
      with?"
- [x] The central concept is "What is data?"
- [x] Data is introduced as recorded information about something
      (Section 10).
- [x] Data is not restricted to numbers (Section 10).
- [x] Real World → Observation → Data is clearly established (Section
      11).
- [x] Dataset is introduced simply (Section 13).
- [x] Row and column concepts are clear (Section 14).
- [x] Feature is introduced only conceptually (Section 12, 17).
- [x] Label is introduced only conceptually (Section 17).
- [x] It is explicit that not every dataset must have labels (Section
      17, Part B).
- [x] Messy data is demonstrated (Section 15).
- [x] More data ≠ automatically better data (Section 16).
- [x] Useful data depends on the problem (Section 18).
- [x] Data is framed as a representation of reality (Section 18, Part
      B).
- [x] DATA ≠ Machine Learning is established (Section 19).
- [x] Class 02 pipeline is preserved unchanged: `DATA → LEARNING →
      MODEL → PREDICTION`.
- [x] No advanced ML concepts were introduced (Section 22).
- [x] No coding, mathematics, statistics, or database/SQL content
      (Section 22).
- [x] No implementation details anywhere in the guide.
- [x] Activities encourage reasoning, not recall (Sections 14, 15, 18).
- [x] Students are not expected to memorize terminology exactly
      (Section 26).
- [x] The final recap checks conceptual understanding, not definitions
      (Section 19).
- [x] This Master Guide is the source of truth for all future Class 03
      artifacts (Student Notes, Presentation, Pen Tablet, Interaction
      Pack, Homework).
