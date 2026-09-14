# Class 06 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Variables & Data Types
**Subtitle:** Giving Values a Label That Can Change
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 02 — How
Machines Learn, Class 03 — Understanding Data, Class 04 — How Computers
Represent Information, Class 05 — Your First Python Program

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

**This class assumes Class 05's environment is already working** for
every student (see Class 05's Pre-Class Setup box) — nothing new needs
installing. Everything in Sections 8–25 is written assuming students can
type and run code exactly as they did last class.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01–05](#3-relationship-to-class-01-05)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening Mystery (0–5)](#8-opening-mystery-0-5)
9. [Callback — Something That Can Change (5–10)](#9-callback--something-that-can-change-5-10)
10. [What Is a Variable? (10–17)](#10-what-is-a-variable-10-17)
11. [Assignment: The = Sign (17–24)](#11-assignment-the--sign-17-24)
12. [Variables in print() (24–31)](#12-variables-in-print-24-31)
13. [Reassignment (31–38)](#13-reassignment-31-38)
14. [Naming Variables (38–43)](#14-naming-variables-38-43)
15. [Meet the Data Types (43–51)](#15-meet-the-data-types-43-51)
16. [Numbers: int vs float (51–57)](#16-numbers-int-vs-float-51-57)
17. [Strings, Revisited (57–62)](#17-strings-revisited-57-62)
18. [Booleans (62–68)](#18-booleans-62-68)
19. [Combining Text and Variables in print() (68–75)](#19-combining-text-and-variables-in-print-68-75)
20. [The Class 04 Callback — A Variable Is a Labeled Representation (75–82)](#20-the-class-04-callback--a-variable-is-a-labeled-representation-75-82)
21. [Full Class 01 → Class 06 Bridge (82–89)](#21-full-class-01--class-06-bridge-82-89)
22. [Interactive Activity — Variable Profile Card (89–103)](#22-interactive-activity--variable-profile-card-89-103)
23. [Misconceptions — In-Class Handling (103–107)](#23-misconceptions--in-class-handling-103-107)
24. [Recap (107–109)](#24-recap-107-109)
25. [Final Takeaway (109–110)](#25-final-takeaway-109-110)
26. [Common Misconceptions — Full Reference](#26-common-misconceptions--full-reference)
27. [Instructor Language / Teaching Guardrails](#27-instructor-language--teaching-guardrails)
28. [Interaction Philosophy](#28-interaction-philosophy)
29. [Visual / Board Plan](#29-visual--board-plan)
30. [Class 01–06 Continuity](#30-class-01-06-continuity)
31. [Assessment of Understanding](#31-assessment-of-understanding)
32. [Differentiation](#32-differentiation)
33. [Time Management / Timing Safety](#33-time-management--timing-safety)
34. [Extended Version](#34-extended-version)
35. [Advanced Topics Parking Lot](#35-advanced-topics-parking-lot)
36. [Teacher FAQ](#36-teacher-faq)
37. [Class Success Check](#37-class-success-check)
38. [Source-of-Truth / QA Checklist](#38-source-of-truth--qa-checklist)

---

## 1. Class Identity

| Field | Value |
|---|---|
| Class number | 06 |
| Title | Variables & Data Types |
| Subtitle | Giving Values a Label That Can Change |
| Audience | First-year college students, mixed backgrounds. Every student wrote and ran a `print()` program last class — this class assumes that comfort level, not more. |
| Prerequisites | Class 01 (`PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT`), Class 04 (`REPRESENTATION → BITS`), Class 05 (`print()`, quotes/strings, comments, running code). No prior use of variables assumed or required. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 05 ended on a deliberate, unresolved question: every piece of text in a Class 05 program is fixed, typed once. Class 06 answers it — a **variable** is a named, changeable place to keep a value, and it is the single idea that turns "a program that always does the same thing" into "a program that can hold, use, and update information." |
| Core question | **"If a program needs to remember something that changes — a score, an age, an answer — how does it hold onto it?"** |
| Core concept | `VALUE → VARIABLE (a label that can change) → DATA TYPE (what kind of value it is)`, landing inside Class 01's chain as a new box between `PYTHON CODE` and `RUN`. |
| Class success metric | Without prompting, most students can: (1) explain why fixed, typed-once text isn't enough for many programs; (2) create a variable with `=` and explain that `=` means "store," not mathematical equality; (3) correctly distinguish `print(name)` from `print("name")`; (4) reassign a variable and explain the old value is gone; (5) follow basic variable naming rules; (6) name and give an example of each of the four data types covered today (`int`, `float`, `str`, `bool`); (7) combine literal text and variables in one `print()` using commas; (8) connect a variable back to Class 04 — a human-readable label for something stored as bits. |

This class is entirely about variables, assignment, and four data types.
**No arithmetic operators (`+`, `-`, `*`, `/`) beyond what's needed to
notice numbers exist. No comparison operators (`==`, `<`, `>`). No
`input()`. No `if`/`elif`/`else`. No loops. No functions students
define. No lists, dictionaries, or any other data structure. No type
conversion functions (`int()`, `str()`, etc.) beyond a passing mention
in the parking lot.** If you feel tempted to show `if age >= 18:` to
"make an example more realistic," that is the signal to simplify
further, not to go deeper — Classes 07 and 08 own that.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one very specific limitation students personally
felt last class with a solution. In Class 05, every student wrote
`print("Hello, my name is Priya.")` — and if "Priya" needed to change,
the only option was to edit the code and run it again. Today that
limitation gets a name and a fix: **a variable**. Every example, every
"watch what happens when I change just one line" moment exists to make
that fix feel obvious and necessary, not arbitrary.

**Teaching philosophy, in one line:** identical in spirit to Classes
01–05 — intuition before syntax, example before rule, ask before
explaining, and (continuing Class 05's addition) **let students type it
themselves.**

**What students should feel by the end:**

- A beginner should feel: *"Now I get why you'd want a variable — I hit
  this exact wall last class without knowing it had a name."*
- A stronger student should feel: *"I can already see how a real program
  — a game score, a running total — needs dozens of these, all
  changing."*
- Everyone should feel the small, specific "aha" of watching
  `print(name)` and `print("name")` produce two completely different
  outputs side by side (Section 12) — this is the single most important
  visual moment in the class.

**State this to yourself before you walk in:**

> This is **not** a class about data structures or complex programs. By
> the end, nobody needs to have built anything beyond a handful of
> labeled values and some `print()` statements. This class exists so
> that "variable" stops being a vague word borrowed from math class and
> becomes something a student has personally created, changed, and
> watched change — the same way Class 05 turned "programming" from an
> abstract idea into something typed and run.

If a question drifts toward "how do I make the program decide something"
or "how do I let the user type in their own age," that is Class 08's and
Class 10's job respectively — redirect warmly using the parking-lot
response in Section 35.

---

## 3. Relationship to Class 01–05

Class 01 built:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

Class 04 built:

```
DATA → REPRESENTATION → BITS
```

Class 05 opened the `PROGRAM` box for real:

```
ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT
```

...and closed on a deliberate, unresolved hook:

> "Right now, every piece of text in your programs is fixed — typed once
> and never changing. What if a program needed to remember something
> that changes?"

Class 06 is the direct answer to that hook.

**Say this explicitly, early (Section 9 is the natural spot):**

> "Last class ended with a question we didn't answer: what if a program
> needs to hold onto something that changes? Today, that's the entire
> class."

**The relationship is not new content bolted on — it is Class 05's
`PYTHON CODE` box, opened one level further:**

```
Class 5 chain:   ... → PYTHON CODE → RUN → OUTPUT/RESULT
Class 6 opens:              ▲▲▲▲▲
                    FIXED TEXT (Class 05) vs. VARIABLES (today)
```

**It also reopens Class 04, on purpose:**

> "Remember Class 04? Information gets represented inside a computer as
> bits — you never see those bits directly. A variable is the
> human-readable label Python gives you for a piece of that stored,
> changeable representation. You write `age`. Python quietly manages the
> bits underneath."

This is the same staircase framing every prior class used — see Section
30 for the full continuity treatment.

---

## 4. Learning Objectives

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | A program needs a way to store values that can change while it runs | Can explain, in their own words, why Class 05's fixed text wasn't enough for something like a changing score | Any formal notion of program "state" |
| 2 | Create a variable using assignment (`=`) | Can write `name = "..."` (or a number/boolean) and explain what happened | Multiple assignment, chained assignment |
| 3 | `=` means "store," not mathematical equality | Can explain that `age = 18` stores 18 in `age` — it isn't a permanent equation | Formal computer-science treatment of assignment vs. equality |
| 4 | Use a variable inside `print()`, vs. literal text | Can correctly predict that `print(name)` shows the stored value and `print("name")` shows the literal word "name" | — |
| 5 | Reassign a variable | Can reassign a variable and explain that the previous value is completely replaced, not remembered | Multiple variables referencing the same value, memory/reference concepts |
| 6 | Follow basic variable naming rules | Can name a variable that starts with a letter/underscore, uses no spaces, and is reasonably descriptive | Full reserved-keyword list, PEP 8 in depth |
| 7 | Identify the four basic data types | Can name `int`, `float`, `str`, `bool` and give one example value of each | `type()`'s exact output formatting, type conversion |
| 8 | Combine literal text and variables in one `print()` | Can write `print("text", variable, "more text")` and predict the output, including the automatic spacing | String formatting methods (f-strings, `.format()`) |
| 9 | Connect variables back to Class 04's bits | Can restate, in their own words, that a variable is a label for something stored as bits | Any new representation/encoding content |

---

## 5. Key Terminology

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Variable** | A named container that stores a value — and can be given a new value later. | "A label you can put on a value, and move to a new value later." | "A box that holds many things at once" (it holds one value at a time) | Yes — core term |
| **Assignment (`=`)** | The act of storing a value in a variable. | "Store this value under this name." | "Equals," as in math | Yes — core term |
| **Value** | The actual piece of data itself — the thing being stored. | "What's actually inside." | — | Loosely |
| **Data type** | The kind of value a variable holds — a number, text, or a yes/no fact. | "What kind of value this is." | — | Loosely — name only |
| **Integer (`int`)** | A whole number, positive or negative, with no decimal point. | "A whole number." | — | Yes |
| **Float** | A number with a decimal point. | "A number with a decimal point." | — | Yes |
| **String (`str`)** | Text, written between matching quotes. | "Text, in quotes." | — | Loosely — already known from Class 05 |
| **Boolean (`bool`)** | One of exactly two values: `True` or `False`. | "A yes/no fact — capital T, capital F, no quotes." | "true/false" lowercase, or "yes/no" as the literal values | Yes |
| **Reassignment** | Giving a variable a new value, completely replacing the old one. | "Swapping out what's stored, under the same label." | "The variable remembers its old value too" | Yes |
| **`type()`** | A built-in tool that reports a value's data type. | "Ask Python what kind of value this is." | Formal type-system language | Loosely — a peek, not owned today |
| **Naming convention (`snake_case`)** | The common Python style of lowercase words joined by underscores. | "How Python variable names are usually written." | "The only way it can be written" (it's a convention, not a rule) | Loosely |

---

## 6. Class at a Glance

Canonical **110-minute** flow.

| Time | Dur. | Section | Objective | Teaching mode | Board/Screen | Interaction |
|---|---|---|---|---|---|---|
| 0–5 | 5 | Opening Mystery | Feel the limitation of fixed text | Ask → demonstrate → hold | Live screen | High |
| 5–10 | 5 | Callback | Re-open Class 05's hook and Class 04's bits | Recall → question | None | Medium |
| 10–17 | 7 | What Is a Variable? | Name the fix: a labeled, changeable value | Reveal → define | Live screen | High |
| 17–24 | 7 | Assignment: The = Sign | `=` means store, not equals | Ask → demonstrate | Live screen | High |
| 24–31 | 7 | Variables in print() | `print(name)` vs. `print("name")` | Type-along → contrast | Live screen | Very high |
| 31–38 | 7 | Reassignment | The old value is gone, not remembered | Build live | Live screen | High |
| 38–43 | 5 | Naming Variables | Rules and descriptive naming | Ask → demonstrate | Live screen | Medium |
| 43–51 | 8 | Meet the Data Types | Four kinds of value, at a glance | Reveal → survey | Live screen | Medium |
| 51–57 | 6 | Numbers: int vs float | Whole numbers vs. decimals | Ask → contrast | Live screen | Medium |
| 57–62 | 5 | Strings, Revisited | Quotes for literal text, not variable names | Ask → confirm | Live screen | Medium |
| 62–68 | 6 | Booleans | True/False, capitalized, no quotes | Ask → demonstrate | Live screen | Medium |
| 68–75 | 7 | Combining Text and Variables | Commas inside `print()` | Type-along | Live screen | High |
| 75–82 | 7 | The Class 04 Callback | A variable is a labeled representation | Explain → connect | None | Medium |
| 82–89 | 7 | Full Class 01 → 06 Bridge | Install the hero chain | Build live | **Hero diagram** | High |
| 89–103 | 14 | Interactive Activity — Variable Profile Card | Students build a multi-variable program | Facilitated hands-on | Circulate | Very high |
| 103–107 | 4 | Misconceptions | Directly address 2–3 common misreadings | Ask → reframe | None | Medium |
| 107–109 | 2 | Recap | Consolidate, verify | Ask → students answer | Reuse hero diagram | High |
| 109–110 | 1 | Final Takeaway | Close on one memorable line | State → bridge forward | None | Low |

**Non-negotiable blocks** (never compressed away — see Section 33):
Assignment: The = Sign, Variables in print(), Reassignment, Meet the Data
Types, Combining Text and Variables, the Class 01 → Class 06 bridge, and
the Variable Profile Card activity.

---

## 7. Section-by-Section Teaching Guide

Quick **A–D** index for every block; full teaching notes for each live in
Sections 8–25 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening Mystery | Feel the limitation of fixed text before naming the fix | Students recognize that rewriting code isn't a real solution | No |
| 2 | Callback | Re-open Class 05's hook and Class 04's bits | Students state the connection to both prior classes | No |
| 3 | What Is a Variable? | Name the fix | Students define a variable as a label that can change | No |
| 4 | Assignment: The = Sign | `=` means store | Students explain `=` is not mathematical equality | **Yes** |
| 5 | Variables in print() | Distinguish value from literal text | Students correctly predict `print(name)` vs. `print("name")` | **Yes** |
| 6 | Reassignment | The old value is replaced | Students explain the previous value is gone after reassignment | **Yes** |
| 7 | Naming Variables | Rules and good naming | Students name a variable correctly and descriptively | No |
| 8 | Meet the Data Types | Survey the four types | Students name all four types unprompted | **Yes** |
| 9 | Numbers: int vs float | Whole vs. decimal | Students correctly classify a number as `int` or `float` | No |
| 10 | Strings, Revisited | Quotes mark literal text only | Students explain why a variable name has no quotes | No |
| 11 | Booleans | True/False as a distinct type | Students write a boolean variable correctly | No |
| 12 | Combining Text and Variables | Build a readable sentence from parts | Students write a `print()` mixing text and variables | **Yes** |
| 13 | The Class 04 Callback | Reconnect to bits/representation | Students restate a variable as a labeled representation | No |
| 14 | Full Class 01 → 06 Bridge | Consolidate the whole continuity chain | Students restate the bridged chain | **Yes** |
| 15 | Interactive Activity | Build an original multi-variable program | Every student produces a working profile-card program | **Yes** |
| 16 | Misconceptions | Directly defuse common wrong models | Students can correct at least one misconception aloud | No |
| 17 | Recap | Verify understanding | Students answer recap questions in their own words | **Yes** |
| 18 | Final Takeaway | Close memorably, bridge forward | Students can repeat the final line's idea, not its wording | No |

---

## 8. Opening Mystery (0–5)

Do **not** open with "Today we will learn about variables." Open with a
live, felt limitation.

**Exact opening approach:**

1. Type and run, live: `print("Score: 0")`.
2. Say: *"Let's say this is a scoreboard for a quick class quiz. The
   score just changed to 10. How do I update it?"*
3. Let a student answer — they'll say "change the 0 to a 10 and run it
   again." **Do exactly that**, live: edit to `print("Score: 10")`,
   re-run.
4. Say: *"Fine for one change. Now imagine the score changes twenty
   times during one quiz — or a hundred times during one game. Are we
   editing and re-running the code every single time?"*
5. **Do not resolve it yet.** Let the impracticality sit for a moment.
6. Bridge: *"There has to be a better way to hold onto something that
   changes. There is — and it's the entire idea behind today's class."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "Are we really going to edit and re-run the code every time the score changes?" | "No," "that's ridiculous," "there must be a better way" | Narrow it: "What if this were a video game keeping score a hundred times a second — would editing code even be possible while it's running?" |

**Transition:** *"Let's go back to exactly where Class 05 left off — it
asked this same question and didn't answer it."*

---

## 9. Callback — Something That Can Change (5–10)

Bring back Class 05's closing hook exactly as it was left:

> "Right now, every piece of text in your programs is fixed — typed once
> and never changing. What if a program needed to remember something
> that changes?"

**What the instructor says:**

> "That's not a rhetorical question — it's today's entire class. And
> it also reopens something from further back. Remember Class 04?
> Information gets represented inside a computer as bits. You never see
> those bits directly. Today, you get a human-readable label for a piece
> of that stored, changeable information — and that label is called a
> **variable**."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did Class 05 leave unanswered?" | How to hold onto something that changes |
| "What did Class 04 teach about how a computer holds information?" | It represents information as bits |

**Transition:** *"Let's name the fix."*

---

## 10. What Is a Variable? (10–17)

**Use the physical-label analogy before any code:**

> "Imagine a small labeled box. The label says `SCORE`. Right now, it
> holds `0`. I can look inside and read `0`. Later, I can take out the
> `0` and put `10` in its place — same label, new contents. That's
> exactly what a variable is."

**Type this live:**

```
score = 0
print(score)
```

Run it — `0` appears.

**Land the core statement:**

> "A **variable** is a named place to store a value — and unlike Class
> 05's fixed text, its value can change later. `score` is the label.
> `0` is what's currently inside."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "In the labeled-box idea, what's the label? What's inside?" | The variable name is the label; the value is what's inside |
| "What's different about a variable compared to Class 05's fixed text?" | It can change; fixed text couldn't |

**Transition:** *"Let's look closely at the line that actually created
it — that `=` sign is doing something very specific."*

---

## 11. Assignment: The = Sign (17–24) — NON-NEGOTIABLE

**Ask directly:**

> "In math class, what does `=` mean?"

Expected: **equals — both sides are the same.**

> "In Python, `=` means something different: **store.** `score = 0`
> means 'store the value `0` under the name `score`' — not 'score
> equals zero forever, as an equation.'"

**Prove it live — this is the whole point of the section:**

```
score = 0
print(score)
score = 10
print(score)
```

Run line by line. > "If `=` meant mathematical equality, this would be a
contradiction — `score` can't equal both 0 and 10 at once. But it's not
an equation. It's an instruction: *store this value, right now, under
this name.* Each `=` just overwrites what was there."

**Say explicitly, an important guardrail:**

> "Read `score = 0` out loud as 'score **gets** 0,' not 'score equals
> 0.' That small habit avoids a lot of confusion later."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does `=` mean in Python?" | Store this value under this name — not mathematical equality |
| "How should you read `age = 18` out loud?" | "age gets 18," not "age equals 18" |

**Transition:** *"Now let's use this variable inside `print()` — and see
something that trips up almost every beginner at least once."*

---

## 12. Variables in print() (24–31) — NON-NEGOTIABLE

**Type this live, side by side, and run both:**

```
name = "Priya"
print(name)
print("name")
```

**Ask before running:**

> "These two `print()` lines look almost identical. Before I run them —
> will they show the same thing?"

Let guesses happen — many will guess yes.

**Run both. Let the contrast land:**

```
Priya
name
```

> "`print(name)` — no quotes — means 'show me whatever value is stored
> in the variable `name`.' `print("name")` — with quotes — means 'show
> me the literal four letters, n-a-m-e.' Quotes are the entire
> difference. This is the single easiest mistake to make in the next
> several classes — so let's make it on purpose, right now, so it's
> familiar."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does `print(name)` show?" | Whatever value is currently stored in the variable `name` |
| "What does `print(\"name\")` show?" | The literal text "name" |
| "What's the one difference between the two lines?" | Quotes |

**Transition:** *"Let's change what's stored in a variable and watch
what happens."*

---

## 13. Reassignment (31–38) — NON-NEGOTIABLE

**Build this live, one line at a time:**

```
score = 0
print(score)
score = 10
print(score)
score = 25
print(score)
```

**Ask before the second run:**

> "After I run `score = 10`, if I ask Python for `score` again, what
> happened to the `0`?"

Expected: uncertain guesses are fine — that's what this section resolves.

**Run it all. Land the core statement:**

> "The `0` is completely gone. Not hidden, not remembered somewhere —
> **overwritten.** A variable holds exactly one value at a time. Each
> reassignment replaces whatever was there before."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "After reassigning `score`, does Python remember the old value anywhere?" | No — it's completely replaced |
| "How many values can one variable hold at the same time?" | Exactly one |

**Transition:** *"Before we go further, let's talk about what you're
actually allowed to name a variable."*

---

## 14. Naming Variables (38–43)

**State the hard rules first, briefly:**

> "A variable name: must start with a letter or an underscore, not a
> digit. Can contain letters, digits, and underscores — but no spaces.
> Is case-sensitive — `age` and `Age` are two completely different
> variables. And it can't be one of Python's own reserved words, like
> `print`."

**Show valid and invalid examples live:**

```
age = 18            # valid
student_name = "Rio" # valid
_temp = 5            # valid

2nd_place = "Sam"     # invalid — starts with a digit
student name = "Rio"  # invalid — contains a space
```

**Land the convention, separate from the hard rules:**

> "Beyond what's actually required, good Python style uses
> **`snake_case`** — lowercase words joined by underscores — and
> **descriptive names.** `student_age` beats `x`. Nobody's forcing you,
> but future-you, reading this code in a month, will thank present-you."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Can a variable name start with a digit?" | No |
| "Are `age` and `Age` the same variable?" | No — Python is case-sensitive |
| "Why prefer a descriptive name over a single letter?" | It's easier for a human to read and understand later |

**Transition:** *"So far every variable held text or a number. Let's
name the different *kinds* of values a variable can hold."*

---

## 15. Meet the Data Types (43–51) — NON-NEGOTIABLE

**Type this live, one line at a time:**

```
age = 18
price = 19.99
name = "Priya"
is_student = True
```

> "Four lines, four different *kinds* of value. Python calls this kind
> of thing a **data type.** `age` holds a whole number — an `int`.
> `price` holds a number with a decimal point — a `float`. `name` holds
> text — a `str`, short for string, exactly like Class 05. `is_student`
> holds a yes/no fact — a `bool`, short for boolean, either `True` or
> `False`."

**Offer a peek at `type()` — light, not a deep dive:**

```
print(type(age))
```

→ `<class 'int'>`

> "You can literally ask Python what type something is. We won't use
> this constantly, but it's a good tool to know exists."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What are the four data types we just met?" | int, float, str, bool |
| "What does `type()` do?" | Reports the data type of a value |

**Transition:** *"Let's slow down on the first one — numbers actually
come in two flavors."*

---

## 16. Numbers: int vs float (51–57)

**Ask directly:**

> "What's different about `18` and `19.99`?"

Expected: **one is a whole number, one has a decimal point.**

**Land the core statement:**

```
apples = 3           # int — a whole number
temperature = 36.6   # float — has a decimal point
```

> "**`int`** is short for integer — a whole number, positive or
> negative, no decimal point. **`float`** is any number with a decimal
> point, even something like `5.0`. The decimal point is the entire
> test."

**Explicitly avoid teaching arithmetic here:**

> "We're not adding, subtracting, or doing any math with these numbers
> yet — that's next class's entire job. Today, we're just noticing that
> numbers come in two flavors."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Is `7` an int or a float?" | int |
| "Is `7.0` an int or a float?" | float — it has a decimal point |

**Transition:** *"Strings we already know from Class 05 — but let's
revisit exactly where quotes do and don't belong."*

---

## 17. Strings, Revisited (57–62)

**Ask directly:**

> "In Class 05, why did text need quotes?"

Expected: **so Python knows it's literal text, not more code.**

**Connect to today's new twist — Section 12's lesson, restated:**

```
city = "Kolkata"
print(city)        # Kolkata — city is a variable, no quotes needed
print("city")       # city — the literal word, because of the quotes
```

> "The rule from Class 05 hasn't changed: literal text still needs
> quotes. What's new today is that a **variable name is never in
> quotes** — quotes would turn it into literal text instead of a
> reference to the stored value."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Does a variable name ever go in quotes?" | No |
| "Does literal text still need quotes?" | Yes, exactly as in Class 05 |

**Transition:** *"One more data type — one that isn't a number or
text at all."*

---

## 18. Booleans (62–68)

**Type this live:**

```
is_raining = True
is_weekend = False
print(is_raining)
```

> "A **boolean** holds exactly one of two values: `True` or `False` —
> capital letters, no quotes. It represents a yes/no, on/off kind of
> fact."

**Say explicitly, an important guardrail:**

> "`True` and `False` are not text — no quotes — and not lowercase.
> `"true"` in quotes would just be a four-letter string, not a boolean."

Do **not** introduce comparison operators (`==`, `<`, `>`) here — that's
Class 07/08 territory. If asked how booleans get produced by comparisons,
park it (Section 35).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What are the only two possible boolean values?" | True and False |
| "Do booleans need quotes?" | No |

**Transition:** *"Let's put a variable inside a full sentence, not just
print it alone."*

---

## 19. Combining Text and Variables in print() (68–75) — NON-NEGOTIABLE

**Build this live:**

```
name = "Priya"
age = 18
print("My name is", name, "and I am", age, "years old.")
```

**Ask before running:**

> "Before I run this — what do you think the output will look like?"

Run it:

```
My name is Priya and I am 18 years old.
```

**Land the core statement:**

> "A comma inside `print()` lets you mix literal text and variables in
> one line. Python automatically puts a single space between each piece
> — that's a small, useful detail to notice, not something to
> memorize hard."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How do you mix literal text and a variable in one `print()`?" | Separate them with commas |
| "What does Python automatically add between each comma-separated piece?" | A single space |

**Transition:** *"Let's reconnect this whole idea to something from
several classes ago."*

---

## 20. The Class 04 Callback — A Variable Is a Labeled Representation (75–82)

**Land the core reframe of the whole class:**

> "Remember Class 04? A computer represents information as bits — 0s
> and 1s, combined. You never actually see those bits when you write
> Python. A variable is the human-readable label Python gives you for a
> piece of that stored representation. You write `age`. Underneath,
> Python and the computer are managing bits — you just never have to
> think about them directly."

**Draw the connecting idea:**

```
INFORMATION
    ↓
REPRESENTATION (Class 04)
    ↓
BITS (Class 04)
    ↓
VARIABLE — a human-readable label for it (today)
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did Class 04 say information gets represented as?" | Bits |
| "What does a variable give you that raw bits don't?" | A readable, meaningful name for the stored value |

**Transition:** *"Let's put the entire day's reasoning on one board —
starting all the way back at Class 01."*

---

## 21. Full Class 01 → Class 06 Bridge (82–89) — NON-NEGOTIABLE, HERO MOMENT

**This is the HERO MOMENT of the class.** Build it live, top to bottom,
one line at a time — never reveal it finished.

1. Write **PROBLEM** — *"Something we're trying to solve."* (Class 01)
2. Arrow down, write **LOGIC** — *"Reasoning about how to solve it."*
   (Class 01)
3. Arrow down, write **ALGORITHM** — *"The plan, as steps a person could
   follow."* (Class 01)
4. Arrow down, write **PYTHON CODE** — *"That plan, written precisely
   enough for a computer to follow."* (Class 05)
5. Arrow down, write **VARIABLES** — *"Labeled, changeable values the
   code can hold, use, and update."* (today)
6. Arrow down, write **RUN** — *"Telling the computer to actually carry
   it out."* (Class 05)
7. Arrow down, write **OUTPUT / RESULT** — *"What the program
   produces."* (Class 05)

Finished board:

```
PROBLEM
    ↓
LOGIC
    ↓
ALGORITHM
    ↓
PYTHON CODE
    ↓
VARIABLES
    ↓
RUN
    ↓
OUTPUT / RESULT
```

**Say explicitly, this is the whole point of the diagram:**

> "The top four lines and the last two are exactly Class 05's chain.
> Today we inserted one new box in the middle — `VARIABLES` — because
> now the code running on its way to an output can hold, use, and change
> values along the way, instead of only ever printing fixed text."

**Do not compress this block below 5 minutes**, even under time
pressure — see Section 33.

---

## 22. Interactive Activity — Variable Profile Card (89–103) — NON-NEGOTIABLE

**This is the HERO ACTIVITY.** Every student extends Class 05's "About
Me" idea using real variables and data types — no copying the class
example verbatim.

### Facilitator instructions (timed, ~14 minutes at canonical pace)

1. **(2 min) Set up:** "Build a 'Variable Profile Card.' You need **at
   least four variables**: one string, one integer, one float, and one
   boolean — about yourself, or a character you invent. Then use
   `print()` with commas to display each one in a full sentence."
2. **(8 min) Let students write and run independently (or in pairs).**
   Circulate constantly. Prompt stuck students with: "What's one true
   number about you? One true yes/no fact?"
3. **(2 min) Deliberately encourage one on-purpose mistake:** ask
   students to try printing one of their variable names in quotes (e.g.
   `print("name")` instead of `print(name)`) and confirm they can
   explain, out loud, why the output changed.
4. **(2 min) Invite 2–3 students to run their program for the room.**
   Celebrate variety in the data chosen, not just correctness.

### Questions and expected responses

| Question | Expected response |
|---|---|
| "Which of your variables is a string? An int? A float? A boolean?" | Any coherent, correctly typed answer |
| "What happened when you put your variable name in quotes?" | It printed the literal word instead of the stored value |
| "If you reassigned one of your variables right now, what would happen to the old value?" | It would be completely replaced |

**Do not introduce new syntax during this activity** (no `input()`, no
arithmetic, no conditionals) — if a student asks for one, use the
parking-lot response (Section 35) and let their program stay simple.

### Timing, extension, and support

- **Canonical timing:** ~14 minutes, per the breakdown above.
- **Stronger-student extension:** Ask them to add a fifth variable and
  reassign one existing variable partway through the program, with a
  `print()` before and after showing the change.
- **Weaker-student support:** Provide a fill-in-the-blank template (see
  Section 22's example in the Student Notes) — `name = "___"`,
  `age = ___`, `height = ___`, `is_student = ___` — and let them fill in
  the blanks rather than writing from a blank editor.
- **Transition back to the main lesson:** "You just created, used, and
  printed four different kinds of labeled, changeable values — entirely
  on your own. That's the whole idea of today's class."

---

## 23. Misconceptions — In-Class Handling (103–107)

Pick 2–3 of the misconceptions most likely to have surfaced already today
(see Section 26 for the full reference table) and address them directly
and briefly.

Suggested priority order for in-class handling:

1. "`=` means the two sides are permanently equal" (very likely surfaced
   in Section 11).
2. "`print(name)` and `print(\"name\")` should show the same thing"
   (likely surfaced in Section 12).
3. "A reassigned variable somehow remembers its old value too" (worth
   pre-empting if it came up during the activity).

Keep this to 4 minutes — this is a quick defusal pass, not a new lecture.

---

## 24. Recap (107–109) — NON-NEGOTIABLE

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last couple of minutes:

1. **"Why wasn't Class 05's fixed text enough for something like a
   score?"** *Expected:* it can't change without editing and re-running
   the code.
2. **"What does `=` actually do in Python?"** *Expected:* stores a
   value under a name — it isn't mathematical equality.
3. **"What's the difference between `print(name)` and
   `print(\"name\")`?"** *Expected:* one shows the stored value, one
   shows the literal word.
4. **"After you reassign a variable, what happens to the old value?"**
   *Expected:* it's completely replaced.
5. **"Name the four data types from today."** *Expected:* int, float,
   str, bool.
6. **"How does a variable connect back to Class 04?"** *Expected:* it's
   a human-readable label for information stored as bits.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 25. Final Takeaway (109–110)

**Close with the final statement, said slowly:**

> "Last class, your programs could only ever say the exact same thing,
> every single time you ran them. Today, they can hold something,
> change it, and tell you about it. That one idea — a labeled value that
> can change — is what makes a program feel alive instead of frozen."

**Then leave the bridge-forward question open, explicitly not answered
today:**

> "Right now, we can only print numbers — we haven't actually done any
> math with them. What if a program needed to add a score, calculate a
> total, or compare two values? That's exactly where we pick up next
> class."

Do not resolve this — it is intentionally a hook into Class 07
(Operators & Expressions).

---

## 26. Common Misconceptions — Full Reference

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "`=` means the two sides are permanently, mathematically equal." | Confusion when a variable is reassigned to a different value | "In Python, `=` means 'store this value here' — read it as 'gets,' not 'equals.' It's an instruction, not an equation." | Section 11 |
| 2 | "`print(name)` and `print(\"name\")` should show the same thing." | Using quotes around a variable name inside `print()` | "Quotes turn anything into literal text. `name` without quotes means 'the value stored in this variable'; `\"name\"` means the literal word." | Section 12 |
| 3 | "A reassigned variable somehow remembers its old value too." | Expecting a variable to hold more than one value at once | "A variable holds exactly one value at a time. Reassignment completely replaces what was there — nothing is kept." | Section 13 |
| 4 | "Any word can be a variable name, including Python's own keywords." | Trying to name a variable `print`, `if`, or similar | "A handful of words are reserved for Python itself — using them as variable names causes confusing problems, even if Python briefly allows it." | Section 14 |
| 5 | "`True`/`False` are just text, so they need quotes like any other word." | Writing `is_raining = "True"` | "Without quotes, `True` is a boolean — one of exactly two special values. With quotes, `\"True\"` is just a four-letter string, a completely different data type." | Section 18 |

---

## 27. Instructor Language / Teaching Guardrails

**Prefer:**

- "A variable is a label for a value that can change" — **over** "a
  variable is a box" alone (the label framing carries the *naming*
  idea; "box" alone underweights it).
- "Read `=` as 'gets,' not 'equals'" — **over** letting students default
  to the math-class reading.

**Avoid:**

- "Variables are basically like algebra" — this actively reinforces
  Misconception 1; if a student says this, use Section 26's reframe
  immediately.
- Introducing type conversion (`int()`, `str()`, etc.) "just to show
  it's possible" — it isn't today's scope, even briefly.

**The instructor must NOT**, at any point in this class:

- introduce arithmetic operators (`+`, `-`, `*`, `/`) as something to
  actually compute with (numbers existing is fine; doing math with them
  is Class 07's job)
- introduce comparison operators (`==`, `<`, `>`, etc.)
- introduce `input()` or any user-interactive program
- introduce `if`/`elif`/`else` or any conditional logic
- introduce `while`/`for` loops
- introduce functions the student defines themselves (`def`)
- introduce lists, dictionaries, or any other data structure
- introduce type conversion functions (`int()`, `float()`, `str()`,
  `bool()`) beyond a one-line parking-lot mention if asked
- introduce f-strings or `.format()` — commas inside `print()` are the
  only "combining values" technique taught today

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that soon — Class 07 (or the
> relevant later class) is exactly where that lives. Today we're
> planting one seed: a labeled value that can change."

Then return to whichever anchor fits the moment:

```
PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → VARIABLES → RUN → OUTPUT/RESULT
```

See Section 35 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 28. Interaction Philosophy

Class 06 continues Class 05's hands-on-typing emphasis, layered onto
discussion.

**Sample questions to use across the class:**

- "Before I run this — will these two lines show the same thing?"
- "After I reassign this variable, what happened to its old value?"
- "Is this a whole number or a decimal number?"
- "What kind of value should this variable hold — text, a number, or a
  yes/no fact?"
- "How does this connect back to Class 04's bits?"

**Prediction-before-running remains the single most valuable habit** —
carried over directly from Class 05. Ask "what do you think will
happen?" before every run, especially before the `print(name)` vs.
`print("name")` contrast in Section 12.

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 8–12 seconds for the two hardest reasoning
moments — predicting the `print(name)` vs. `print("name")` contrast
(Section 12) and predicting what happens to a variable's old value after
reassignment (Section 13).

**Built-in reasoning opportunities to protect, in priority order:**

1. Predicting `print(name)` vs. `print("name")` before running both
   (Section 12)
2. Predicting what happens to the old value after reassignment (Section
   13)
3. Classifying a number as `int` or `float` (Section 16)
4. The Class 01 → Class 06 bridge reconstruction (Section 21, 24)
5. Every individual choice a student makes in their own Variable Profile
   Card (Section 22)

---

## 29. Visual / Board Plan

Most of this class's "board" is the **live screen**, exactly as in Class
05.

**Screen 1 — The Labeled Box**
Referenced in Section 10 — describe verbally or sketch quickly: a small
box labeled `SCORE`, contents shown as `0`, then contents replaced with
`10`.

**Screen 2 — Assignment Proven Live**
Typed live in Section 11.
`score = 0` → `print(score)` → `score = 10` → `print(score)`.

**Screen 3 — The print(name) vs. print("name") Contrast**
Typed live in Section 12 — the single most important screen of the
class. Both lines, side by side, with their two different outputs shown
directly beneath.

**Screen 4 — Reassignment, Three Steps**
Built live in Section 13. `score = 0` → `10` → `25`, each followed by a
`print()`.

**Screen 5 — Four Data Types**
Typed live in Section 15. `age`, `price`, `name`, `is_student` — one line
each, with their types named alongside.

**Screen 6 — Combining Text and Variables**
Typed live in Section 19. `print("My name is", name, "and I am", age,
"years old.")` with its output directly beneath.

**Drawing 1 — HERO — Full Bridge**
Reserved for Section 21, whiteboard.

```
PROBLEM
    ↓
LOGIC
    ↓
ALGORITHM
    ↓
PYTHON CODE
    ↓
VARIABLES
    ↓
RUN
    ↓
OUTPUT / RESULT
```

Mark this as a **live construction** — do not show the completed
seven-line chain before students have reasoned their way to each new
piece. This is the single most important drawing of Class 06.

Keep every diagram simple — no memory-address diagrams, no pointer
arrows, no internal representation of how Python actually stores
variables under the hood.

---

## 30. Class 01–06 Continuity

**Class 1:**

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**Class 4:**

```
DATA → REPRESENTATION → BITS
```

**Class 5:**

```
ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT
```

**Class 6:**

Inserts **VARIABLES** into Class 05's chain, and explicitly reopens
Class 04's `REPRESENTATION → BITS` idea as the "under the hood" story
behind every variable —
`PYTHON CODE → VARIABLES → RUN → OUTPUT/RESULT`.

**Say this once, clearly (Section 9 or Section 21 are the natural
spots):**

> "We are not starting a new topic. We're opening one more box inside
> Class 05's chain, and reconnecting it to Class 04's bits along the
> way. Every class in this block adds one more real capability to the
> same running program."

This is the same continuity statement pattern used since Class 02 — it
is what turns six separate classes into one staircase instead of six
unrelated topics.

---

## 31. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks throughout the class, and rely heavily on the hands-on
activity (Section 22), exactly as in Class 05.

A student is demonstrating real understanding if they can:

1. Explain why fixed, typed-once text wasn't enough for something like a
   changing score.
2. Create a variable with `=` and explain that it means "store," not
   "equals."
3. Correctly predict the output of `print(name)` vs. `print("name")`.
4. Reassign a variable and explain that the old value is completely
   replaced.
5. Name the four data types covered and give an example of each.
6. Combine literal text and a variable in one `print()` using commas.
7. Connect a variable back to Class 04's bits/representation idea.

**Do not** judge understanding solely from a student successfully
copying the instructor's exact example — the Variable Profile Card
activity (Section 22), where students choose their own values and
deliberately trigger the quotes mistake, is the strongest evidence of
real understanding.

---

## 32. Differentiation

**For students struggling:** Anchor entirely in the fill-in-the-blank
template from Section 22 rather than a blank editor, and walk the
concrete progression one variable at a time:

```
pick a value  →  give it a name  →  assign it  →  print it  →  change it
```

**For students moving quickly:** Let them extend the activity (Section
22's stronger-student extension) — a fifth variable, plus a reassignment
with a before/after `print()`. Do **not** teach arithmetic, `input()`, or
conditionals even for fast movers — deepen *fluency* with variables and
types, not scope. See Section 34 for the full extended-version guidance.

**For students who stay quiet:** The Variable Profile Card (Section 22)
is naturally personal and low-stakes — circulate and read their screen
rather than calling on them verbally, exactly as in Class 05.

---

## 33. Time Management / Timing Safety

**Must cover, in priority order** (matches the non-negotiable list in
Section 7):

1. Assignment and `=` as "store" (Section 11)
2. `print(name)` vs. `print("name")` (Section 12)
3. Reassignment (Section 13)
4. The four data types (Section 15)
5. Combining text and variables with commas (Section 19)
6. The full Class 01 → Class 06 bridge (Section 21)
7. The Variable Profile Card activity (Section 22)

**Can shorten:**

- Naming Variables (Section 14) — state the hard rules only, skip the
  style discussion if time is tight
- Numbers: int vs float (Section 16) — a single example pair is enough
- Strings, Revisited (Section 17) — this is mostly a quick confirmation,
  can be folded into Section 12's transition
- The misconception discussion (Section 23) — pick just one instead of
  2–3

**Can expand** (see Section 34 for detail):

- Let students predict more `print(x)` vs. `print("x")` pairs in Section
  12 before moving on
- Run a second reassignment example in Section 13 with a different data
  type (e.g., a string being reassigned)
- Spend more time circulating during the activity (Section 22)

**Do not cut:** the `print(name)` vs. `print("name")` contrast (Section
12), reassignment (Section 13), the four data types (Section 15), or the
Variable Profile Card activity (Section 22) — these are the load-bearing
walls of the entire class.

### 90-minute version

Trim as follows: Opening Mystery to 4 min, Callback to 4 min, What Is a
Variable? to 5 min, Assignment unchanged (7 min), Variables in print()
unchanged (7 min), Reassignment to 5 min, Naming Variables to 3 min,
Meet the Data Types unchanged (8 min), Numbers int vs float to 4 min,
Strings Revisited folded into Section 12 (0 min separately), Booleans to
4 min, Combining Text and Variables unchanged (7 min), Class 04 Callback
to 4 min, Full Bridge unchanged (7 min), Activity compressed to 10 min,
Misconceptions to 3 min, Recap to 2 min, Final Takeaway unchanged (1
min). Total ≈ 85 minutes.

### 120-minute version

Add time back to: What Is a Variable? (+2 min, let students propose their
own labeled-box examples), Meet the Data Types (+2 min, let students
guess each type before it's named), Combining Text and Variables (+2
min, a second student-built example), Activity (+4 min, let every
student who wants to present their program to the room).

---

## 34. Extended Version

If time allows, deepen fluency — do **not** introduce arithmetic,
`input()`, or conditionals.

- Let students predict the type of several values you show them on
  screen (`7`, `7.0`, `"7"`, `True`) before confirming with `type()`.
- Ask stronger students to reassign every variable in their Variable
  Profile Card once, with a `print()` before and after each change.
- Ask students to find the "odd one out" among a set of variable names
  you present (some valid, one invalid) and explain why.
- Briefly mention, without demonstrating in depth, that Python can
  convert between types on request (`int("7")`, `str(7)`) — enough to
  say "this exists," not enough to teach it.

---

## 35. Advanced Topics Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "How do I add two numbers together?" | "That's an arithmetic operator — real, and coming next class." | "Today's building block is the variable itself, not what you do with it yet." |
| "How do I compare two values, like checking if one is bigger?" | "That's a comparison operator — real, and part of Class 07/08's territory." | Return to: `VARIABLES` hold values; comparing them is a later step. |
| "How do I let the user type in their own value?" | "That's `input()` — real, and coming in a few classes." | Return to: today, every value is typed directly into the code. |
| "How do I make the program choose based on a variable's value?" | "That's `if`/`else` — real conditional logic, a later class's territory." | Return to: today, code just runs top to bottom, using variables. |
| "Can a variable change its data type?" | "Yes — in Python a variable can be reassigned to a completely different type. Real, but not today's focus." | Return to: today, keep one type per variable for clarity. |
| "How do I convert a string to a number, or a number to a string?" | "There are built-in tools for that (`int()`, `str()`) — real, useful, and a natural next step, just not today's scope." | Return to: today's four types, as they naturally occur. |
| "What happens if I use a variable before I've assigned it?" | "Python will tell you it doesn't recognize that name yet — a real and useful error, similar to what you saw in Class 05." | Return to: a variable has to be assigned before it can be used. |
| "Can two variables hold the exact same value?" | "Yes, easily — two different labels can point to the same kind of value, or even the same value." | Return to: each variable is still its own independent label. |

---

## 36. Teacher FAQ

**Q: A student wrote `Age = 18` and then used `age` later and got an
error — what happened?**
A: Python is case-sensitive (Section 14) — `Age` and `age` are two
different variable names. This is a great live example of Section 26's
misconceptions in action; walk through it together rather than just
fixing it for them.

**Q: Should I explain how Python actually stores variables in memory?**
A: No — stay at the labeled-box level (Section 10). Memory addresses,
references, and object identity are well beyond this class's scope and
would only confuse the core idea.

**Q: A student asked about f-strings or `.format()` — did I miss
something?**
A: No — commas inside `print()` are the only combining technique this
class teaches (Section 27). f-strings are a natural later upgrade, not
a gap today.

**Q: What if a student's Variable Profile Card only uses one or two data
types instead of all four?**
A: Gently redirect them to add the missing types before moving on —
using all four is the actual point of the activity (Section 22), not an
optional stretch goal.

**Q: Is it okay if some students finish the activity early?**
A: Yes — use the stronger-student extension in Section 22 (a fifth
variable, a reassignment with before/after prints). Do not let early
finishers pull you into teaching new syntax to the whole room ahead of
schedule.

**Q: What if I only have 90 minutes, not 110?**
A: Use the 90-minute version in Section 33 — it preserves every
non-negotiable block and only trims discussion time and the naming/type
survey.

---

## 37. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Explain why fixed, typed-once text wasn't enough for something like a
   changing score.
2. Create a variable with `=` and explain that it means "store," not
   mathematical equality.
3. Correctly distinguish `print(name)` from `print("name")`.
4. Reassign a variable and explain that the old value is completely
   replaced.
5. Follow basic variable naming rules.
6. Name all four data types covered (`int`, `float`, `str`, `bool`) and
   give an example of each.
7. Combine literal text and a variable in one `print()` using commas.
8. Reconnect a variable to Class 04's bits/representation idea.

A class where most students can do these in plain, imperfect language —
and where every student has personally created and printed at least four
variables of different types — has met the bar.

---

## 38. Source-of-Truth / QA Checklist

Verified against the Foundation Batch 2026 curriculum plan (Block 1,
`C06`) before finalizing this guide:

- [x] Class 01, 04, and 05 continuity is explicit (Sections 3, 9, 20,
      30).
- [x] The class starts with a felt limitation, not a definition (Section
      8).
- [x] Every student creates, prints, and reassigns real variables, not
      just watches (Sections 11–13, 22).
- [x] `=` is explicitly distinguished from mathematical equality
      (Section 11).
- [x] `print(name)` vs. `print("name")` is demonstrated live, not just
      described (Section 12).
- [x] Reassignment is shown to completely replace the old value, not
      retain it (Section 13).
- [x] Naming rules are covered without turning into a PEP 8 lecture
      (Section 14).
- [x] All four data types (`int`, `float`, `str`, `bool`) are introduced
      clearly, each with a concrete example (Sections 15–18).
- [x] Numbers and strings, arithmetic operators are explicitly NOT
      taught (Section 1, Section 27, guarded throughout).
- [x] Comments and `print()` fundamentals from Class 05 are reused, not
      retaught (assumed prerequisite, Section 1).
- [x] No `input()`, conditionals, loops, user-defined functions, lists,
      dictionaries, or type conversion functions are taught (Section 1,
      Section 27).
- [x] Misconceptions are explicitly handled, both in-flow (Section 23)
      and as a full reference (Section 26).
- [x] The Variable Profile Card activity extends Class 05's "About Me"
      activity directly, reinforcing continuity (Section 22).
- [x] The class remains appropriate for students who have completed
      exactly Class 05, no more (Section 1).
- [x] The class has a clear, explicit, unresolved bridge to Class 07
      (Operators & Expressions) (Section 25, Section 35).
- [x] This Master Guide is self-contained and usable by an instructor
      without relying on the Student Notes — every section includes
      instructor wording, questions, expected answers, and transitions.
