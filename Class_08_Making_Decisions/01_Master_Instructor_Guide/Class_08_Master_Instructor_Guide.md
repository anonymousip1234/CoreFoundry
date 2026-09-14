# Class 08 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Making Decisions: if / elif / else
**Subtitle:** The First Code That "Thinks" Before Acting
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 05 —
Your First Python Program, Class 06 — Variables & Data Types, Class 07 —
Operators & Expressions

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

**This class introduces a genuinely new mechanical concept: indentation
as syntax.** Every prior class's syntax lesson (quotes, `=` vs `==`) was
about a single line. This one is about the shape of the code on the page.
Budget real time for it — Section 12 is not a quick aside.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01, 06, and 07](#3-relationship-to-class-01-06-and-07)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening Mystery (0–5)](#8-opening-mystery-0-5)
9. [Callback — The Missing Piece (5–10)](#9-callback--the-missing-piece-5-10)
10. [What Is a Conditional? (10–15)](#10-what-is-a-conditional-10-15)
11. [Your First if Statement (15–24)](#11-your-first-if-statement-15-24)
12. [Indentation: Not Just Style (24–32)](#12-indentation-not-just-style-24-32)
13. [else: The Otherwise (32–39)](#13-else-the-otherwise-32-39)
14. [elif: More Than Two Paths (39–48)](#14-elif-more-than-two-paths-39-48)
15. [Order Matters in elif Chains (48–54)](#15-order-matters-in-elif-chains-48-54)
16. [Comparisons and Logical Operators Inside Conditions (54–62)](#16-comparisons-and-logical-operators-inside-conditions-54-62)
17. [Common Structure Patterns (62–68)](#17-common-structure-patterns-62-68)
18. [The Class 01 Callback — Algorithms Can Branch (68–75)](#18-the-class-01-callback--algorithms-can-branch-68-75)
19. [Full Class 01 → Class 08 Bridge (75–83)](#19-full-class-01--class-08-bridge-75-83)
20. [Interactive Activity — Your Profile Card Decides (83–98)](#20-interactive-activity--your-profile-card-decides-83-98)
21. [Misconceptions — In-Class Handling (98–103)](#21-misconceptions--in-class-handling-98-103)
22. [Recap (103–108)](#22-recap-103-108)
23. [Final Takeaway (108–110)](#23-final-takeaway-108-110)
24. [Common Misconceptions — Full Reference](#24-common-misconceptions--full-reference)
25. [Instructor Language / Teaching Guardrails](#25-instructor-language--teaching-guardrails)
26. [Interaction Philosophy](#26-interaction-philosophy)
27. [Visual / Board Plan](#27-visual--board-plan)
28. [Class 01–08 Continuity](#28-class-01-08-continuity)
29. [Assessment of Understanding](#29-assessment-of-understanding)
30. [Differentiation](#30-differentiation)
31. [Time Management / Timing Safety](#31-time-management--timing-safety)
32. [Extended Version](#32-extended-version)
33. [Advanced Topics Parking Lot](#33-advanced-topics-parking-lot)
34. [Teacher FAQ](#34-teacher-faq)
35. [Class Success Check](#35-class-success-check)
36. [Source-of-Truth / QA Checklist](#36-source-of-truth--qa-checklist)

---

## 1. Class Identity

| Field | Value |
|---|---|
| Class number | 08 |
| Title | Making Decisions: if / elif / else |
| Subtitle | The First Code That "Thinks" Before Acting |
| Audience | First-year college students, mixed backgrounds. Every student computed, compared, and combined values with operators last class — this class assumes that comfort level, not more. |
| Prerequisites | Class 01 (`PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT`), Class 06 (variables, `bool`), Class 07 (comparison and logical operators, `=` vs `==`). No prior use of conditionals assumed or required. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 07 ended on a deliberate, unresolved question: every comparison and logical result just gets printed — it never actually changes what the program does next. Class 08 answers it. This is the class where a program stops running the exact same lines every single time and starts **branching** — genuinely behaving differently depending on its data. |
| Core question | **"How do we make a program actually behave differently depending on what's true?"** |
| Core concept | `CONDITION (a boolean expression) → BRANCH (which block runs)`, landing inside Class 07's chain as a new box between `EXPRESSIONS` and `RUN` — and widening Class 01's `ALGORITHM` from "a straight sequence of steps" to "a sequence that can branch." |
| Class success metric | Without prompting, most students can: (1) write a working `if` statement and explain that its indented block only runs when the condition is `True`; (2) explain that indentation in Python is syntax, not decoration; (3) add an `else` block and explain it runs only when the `if` condition is `False`; (4) chain `elif` for more than two paths; (5) explain that only the *first* true branch in an `if`/`elif` chain runs, and state why ordering matters; (6) use comparison and logical operators from Class 07 directly inside a condition; (7) explain that today widens Class 01's `ALGORITHM` idea — algorithms aren't just straight lines, they can branch. |

This class is entirely about `if`, `elif`, `else`, and the indentation
that defines their blocks. **No nested conditionals (an `if` inside
another `if`). No `while`/`for` loops. No `input()`. No functions
students define. No lists, dictionaries, or any other data structure.
No ternary/conditional expressions (`x if cond else y`). No `match`/
`case`. No combining conditionals with loops.** If you feel tempted to
show an `if` inside an `if` "to make an example more realistic," that is
the signal to simplify further, not to go deeper — a later class owns
that.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one very specific limitation with the single
most important structural idea in programming. Since Class 05, every
program has run the exact same lines, top to bottom, every single time —
Class 07's comparisons and logical operators could only ever be printed,
never *acted on*. Today, for the first time, a program's own data
decides which lines actually run. Every example, every "run it twice
with two different values and watch it behave differently" moment exists
to make that feel like the natural, obvious next step it is.

**Teaching philosophy, in one line:** identical in spirit to Classes
01–07 — intuition before syntax, example before rule, ask before
explaining, and (continuing since Class 05) **let students type it
themselves and predict before running.**

**What students should feel by the end:**

- A beginner should feel: *"I just watched the exact same program do two
  completely different things, because I changed one value. That's the
  first time my code has felt alive."*
- A stronger student should feel: *"I can already see how a real
  decision — eligibility, pricing tiers, pass/fail — gets built from
  exactly this."*
- Everyone should feel the specific, slightly uncomfortable "click" of
  the first `IndentationError` (Section 12) — deliberately shown before
  anyone hits one by accident, exactly like Class 05's first syntax
  error.

**State this to yourself before you walk in:**

> This is **not** a class about building a complete decision-making
> application. By the end, nobody needs to have written more than a
> short `if`/`elif`/`else` chain. This class exists so that "the program
> can decide" stops being a vague phrase and becomes something a student
> has personally watched happen, twice, with two different inputs — the
> same way Class 07 turned "operator" from an abstract word into a
> personally-used toolkit.

If a question drifts toward "how do I check something inside another
check" or "how do I do this many times," that is a later class's job —
redirect warmly using the parking-lot response in Section 33.

---

## 3. Relationship to Class 01, 06, and 07

Class 01 built:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

...where `ALGORITHM` was described as "the plan, as steps a person could
follow" — implicitly, a straight sequence.

Class 07 ended on a deliberate, unresolved hook:

> "Every comparison and logical result just gets printed right now — it
> doesn't change what the program does next. What if it needed to?"

Class 08 is the direct answer to that hook, **and** it is the class
where `ALGORITHM` stops meaning only "a straight line of steps."

**Say this explicitly, early (Section 9 is the natural spot):**

> "Last class ended with a question about acting on a comparison, not
> just printing it. Today answers it. And it changes something about
> Class 01, too — an algorithm was always 'steps in order.' Today, it
> can branch."

**The relationship is not new content bolted on — it is Class 07's
`EXPRESSIONS` box, finally used for something:**

```
Class 7 chain:   ... → EXPRESSIONS → RUN → OUTPUT/RESULT
Class 8 opens:            ▲▲▲▲▲
                 A boolean EXPRESSION now decides which block runs
```

This is the same staircase framing every prior class used — see Section
28 for the full continuity treatment.

---

## 4. Learning Objectives

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | Write a working `if` statement | Can write `if condition:` followed by an indented block, and explain when it runs | Complex or compound conditions |
| 2 | Explain that indentation is syntax, not style | Can state that Python uses indentation to define which lines belong to a block, and that inconsistent indentation causes an error | The exact number of spaces required (4 is conventional, not magic) |
| 3 | Add an `else` block | Can write `if`/`else` and explain that exactly one of the two blocks runs | — |
| 4 | Chain `elif` for more than two paths | Can write `if`/`elif`/`elif`/`else` and explain the flow | An arbitrary number of `elif`s — three or four is enough to prove the point |
| 5 | Explain that only the first true branch runs | Can predict the output of an `elif` chain where more than one condition would be true, and explain why only one branch executes | Short-circuit evaluation theory |
| 6 | Use Class 07's operators inside a condition | Can write `if age >= 13 and age <= 19:` and explain it | New operators beyond what Class 07 taught |
| 7 | Recognize the three canonical patterns | Can name `if` alone, `if`/`else`, and `if`/`elif`/`else` and describe when each fits | Formal control-flow theory |
| 8 | Connect today to Class 01's `ALGORITHM` | Can explain that an algorithm can branch, not just proceed in a straight line | Any new algorithmic content beyond branching |

---

## 5. Key Terminology

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Conditional** | A statement that runs a block of code only if a condition is true. | "Code that only runs when something is true." | — | Yes — core term |
| **Condition** | A boolean expression that controls whether a block runs. | "The true/false question guarding a block." | — | Yes — core term |
| **Block** | A group of statements, indented consistently, that belong together. | "The lines that live inside the if." | — | Yes |
| **Indentation** | The whitespace before a line, which in Python defines which block that line belongs to. | "Where the line sits, and that's not decoration — it's the actual syntax." | "Just for neatness" | Yes — core term |
| **`if`** | Runs its block only when its condition is `True`. | "Do this, only if this is true." | — | Yes — core term |
| **`else`** | Runs its block only when every condition above it was `False`. | "Otherwise, do this instead." | "else also needs a condition" | Yes — core term |
| **`elif`** | Short for "else if" — checks another condition, only if the ones above it were `False`. | "Otherwise, check this next thing." | — | Yes — core term |
| **Branch / Branching** | A program following one of several possible paths, depending on data. | "The program's path forks, depending on what's true." | — | Yes |
| **Colon (`:`)** | Marks the start of a block, required after `if`, `elif`, and `else`. | "Signals 'here comes an indented block.'" | — | Loosely |

---

## 6. Class at a Glance

Canonical **110-minute** flow.

| Time | Dur. | Section | Objective | Teaching mode | Board/Screen | Interaction |
|---|---|---|---|---|---|---|
| 0–5 | 5 | Opening Mystery | Feel the limitation: can't skip a line yet | Ask → demonstrate → hold | Live screen | High |
| 5–10 | 5 | Callback | Reopen Class 07's hook | Recall → question | None | Medium |
| 10–15 | 5 | What Is a Conditional? | Name the fix | Reveal → define | Live screen | Medium |
| 15–24 | 9 | Your First if Statement | Same code, two behaviors | Type-along → run twice | Live screen | Very high |
| 24–32 | 8 | Indentation: Not Just Style | Break it on purpose | Ask → break → explain | Live screen | High |
| 32–39 | 7 | else: The Otherwise | Exactly one of two paths | Type-along → run twice | Live screen | High |
| 39–48 | 9 | elif: More Than Two Paths | Exactly one of several paths | Build live | Live screen | High |
| 48–54 | 6 | Order Matters in elif Chains | Only the first true branch runs | Ask → predict → reveal | Live screen | High |
| 54–62 | 8 | Comparisons and Logical Operators Inside Conditions | Reconnect to Class 07 | Type-along | Live screen | Medium |
| 62–68 | 6 | Common Structure Patterns | Survey the three shapes | Reveal → compare | Live screen | Medium |
| 68–75 | 7 | The Class 01 Callback | Algorithms can branch | Explain → connect | None | Medium |
| 75–83 | 8 | Full Class 01 → 08 Bridge | Install the hero chain | Build live | **Hero diagram** | High |
| 83–98 | 15 | Interactive Activity — Your Profile Card Decides | Extend Class 06/07's own program | Facilitated hands-on | Circulate | Very high |
| 98–103 | 5 | Misconceptions | Directly address 2–3 common misreadings | Ask → reframe | None | Medium |
| 103–108 | 5 | Recap | Consolidate, verify | Ask → students answer | Reuse hero diagram | High |
| 108–110 | 2 | Final Takeaway | Close on one memorable line | State → bridge forward | None | Low |

**Non-negotiable blocks** (never compressed away — see Section 31): Your
First if Statement, Indentation: Not Just Style, else: The Otherwise,
elif: More Than Two Paths, the Class 01 → Class 08 bridge, and the Your
Profile Card Decides activity.

---

## 7. Section-by-Section Teaching Guide

Quick **A–D** index for every block; full teaching notes for each live in
Sections 8–23 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening Mystery | Feel the limitation before naming the fix | Students recognize nothing can skip a line yet | No |
| 2 | Callback | Reopen Class 07's hook | Students state what Class 07 left unanswered | No |
| 3 | What Is a Conditional? | Name the fix | Students define "conditional" in their own words | No |
| 4 | Your First if Statement | Same code, two behaviors | Students run one program twice and see two outcomes | **Yes** |
| 5 | Indentation: Not Just Style | Syntax, not decoration | Students explain why an unindented line causes an error | **Yes** |
| 6 | else: The Otherwise | Exactly one of two paths | Students write and run an if/else | **Yes** |
| 7 | elif: More Than Two Paths | Exactly one of several paths | Students write and run an if/elif/else chain | **Yes** |
| 8 | Order Matters in elif Chains | Only the first true branch runs | Students predict an elif-ordering result correctly | No |
| 9 | Comparisons and Logical Operators Inside Conditions | Reuse Class 07 directly | Students write a condition using and/or | No |
| 10 | Common Structure Patterns | Survey the three shapes | Students name all three patterns | No |
| 11 | The Class 01 Callback | Algorithms can branch | Students restate the connection to Class 01 | No |
| 12 | Full Class 01 → 08 Bridge | Consolidate the whole continuity chain | Students restate the bridged chain | **Yes** |
| 13 | Interactive Activity | Make an existing program decide something | Every student adds a working conditional to their own program | **Yes** |
| 14 | Misconceptions | Directly defuse common wrong models | Students can correct at least one misconception aloud | No |
| 15 | Recap | Verify understanding | Students answer recap questions in their own words | **Yes** |
| 16 | Final Takeaway | Close memorably, bridge forward | Students can repeat the final line's idea, not its wording | No |

---

## 8. Opening Mystery (0–5)

Do **not** open with "Today we will learn about if statements." Open
with a live, felt limitation.

**Exact opening approach:**

1. Type live: `is_raining = True`, then `print("Bring an umbrella!")`.
2. Ask: *"Now let's say it's actually sunny —
   `is_raining = False`. What happens to this print line?"*
3. Run it — the message prints regardless. *"It printed anyway. Nothing
   we've learned so far can make a line only run sometimes."*
4. **Do not resolve it yet.** Let the gap sit for a moment.
5. Bridge: *"Real programs skip lines, or choose between them, constantly.
   There's a whole set of tools for exactly this, and it's today's
   entire class."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "How would we make this line only print when it's actually raining?" | Genuine uncertainty is expected — that's the point | Narrow it: "Everything we know how to do just runs, every time, no matter what. We need a way to make a line conditional." |

**Transition:** *"Let's go back to exactly where Class 07 left off."*

---

## 9. Callback — The Missing Piece (5–10)

Bring back Class 07's closing hook exactly as it was left:

> "Every comparison and logical result just gets printed right now — it
> doesn't change what the program does next. What if it needed to?"

**What the instructor says:**

> "That's exactly today. We spent all of last class building booleans —
> `True` and `False` answers to real questions. Today, those answers
> finally get to *do* something."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did Class 07 leave unanswered?" | How to make a comparison actually change what the program does |

**Transition:** *"Let's name the fix."*

---

## 10. What Is a Conditional? (10–15)

**Land the core statement directly:**

> "A **conditional** is a statement that runs a block of code only if a
> **condition** — a boolean expression — is `True`. If the condition is
> `False`, that block is skipped entirely."

**Preview the shape, without full syntax yet:**

> "In Python, the most common conditional starts with the word `if`,
> followed by a condition, a colon, and then an indented block of code
> underneath. We'll build one together right now."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What is a conditional, in your own words?" | Code that only runs a block if a condition is true |

**Transition:** *"Let's write one."*

---

## 11. Your First if Statement (15–24) — NON-NEGOTIABLE

**Type this live, slowly, narrating every character:**

```
is_raining = True

if is_raining:
    print("Bring an umbrella!")
```

> "`if is_raining:` — a condition, then a colon. The line underneath is
> indented — that tells Python it belongs *inside* the if. Right now,
> `is_raining` is `True`, so I expect this to print."

**Run it — confirm the message appears.**

**Now change the value live and run again:**

```
is_raining = False
```

> "Before I run this — what do you think happens now?"

Run it — **nothing prints.**

> "Same code. Different data. Completely different behavior. That's
> never happened before in this course — every program until today ran
> identically, every single time."

**Every student types this exact example themselves before moving on.**
Walk the room.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "When does the indented line actually run?" | Only when `is_raining` is `True` |
| "What happened when `is_raining` was `False`?" | Nothing — that line was skipped entirely |

**Transition:** *"Notice that indented line very closely — that
indentation isn't optional, and it isn't just for looks."*

---

## 12. Indentation: Not Just Style (24–32) — NON-NEGOTIABLE

**Land the core statement:**

> "In many languages, blocks are marked with curly braces `{ }` or words
> like `end`. Python uses **indentation** instead — the whitespace
> before a line *is* the syntax that says 'this line belongs to the
> block above.' This is the first time in this course indentation has
> been more than a formatting choice."

**Break it on purpose, live:**

```
if is_raining:
print("Bring an umbrella!")
```

Run it — an error appears (`IndentationError: expected an indented
block`).

> "Read this calmly, exactly like Class 05's first error. Python is
> telling us it expected an indented line after the colon and didn't get
> one."

**Show a second common break — inconsistent indentation:**

```
if is_raining:
    print("Bring an umbrella!")
      print("Don't forget your boots!")
```

Run it — another `IndentationError`.

> "Every line in the same block needs the *same* indentation. Most
> editors indent four spaces automatically when you press Enter after a
> colon — let your editor help you, and stay consistent."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does indentation actually mean in Python?" | It's the syntax that shows which lines belong to a block — not decoration |
| "What happens if a block isn't indented at all?" | An `IndentationError` |

**Transition:** *"So far our program only does something when a
condition is true. What if we also want it to do something when it's
false?"*

---

## 13. else: The Otherwise (32–39) — NON-NEGOTIABLE

**Type this live:**

```
is_raining = False

if is_raining:
    print("Bring an umbrella!")
else:
    print("Enjoy the sunshine!")
```

> "`else:` means 'otherwise' — its block runs only when the `if`
> condition was `False`. It never takes its own condition — it's simply
> whatever's left."

**Run it — confirm "Enjoy the sunshine!" appears.**

**Change `is_raining` back to `True` and run again — confirm the other
message appears.**

> "Exactly one of these two blocks runs, every time — never both, never
> neither."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "When does the else block run?" | Only when the if condition was False |
| "Does else ever have its own condition?" | No — never |

**Transition:** *"What if there are more than two possible paths?"*

---

## 14. elif: More Than Two Paths (39–48) — NON-NEGOTIABLE

**Build this live, one branch at a time:**

```
age = 15

if age < 13:
    print("Child ticket")
elif age < 20:
    print("Teen ticket")
elif age < 65:
    print("Adult ticket")
else:
    print("Senior ticket")
```

> "`elif` is short for 'else if' — check another condition, but only if
> every condition above it was `False`. With `age = 15`: is it under 13?
> No. Is it under 20? Yes — `Teen ticket` prints, and Python never even
> looks at the remaining conditions."

**Run it. Then change `age` to a few other values and re-run, predicting
each time.**

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does elif stand for?" | Else if |
| "With age = 15, which branch runs?" | "Teen ticket" |
| "Does Python check the remaining elif/else once one branch has already run?" | No |

**Transition:** *"That last point is worth its own moment — let's see
exactly what happens when more than one condition would technically be
true."*

---

## 15. Order Matters in elif Chains (48–54)

**Ask students to predict before revealing:**

```
score = 95

if score >= 60:
    print("Pass")
elif score >= 90:
    print("Pass with Distinction")
```

> "`score` is 95 — that's both `>= 60` and `>= 90`. Before I run this —
> which message prints?"

Let guesses happen — many will guess "Pass with Distinction," since it
feels more specific/correct.

**Run it — `Pass` prints.**

> "Python checked the *first* condition, found it `True`, ran that block,
> and never even looked at the `elif` below it — even though that
> condition was also true. **Order matters.** The more specific
> condition needed to come first."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Why did 'Pass' print instead of 'Pass with Distinction'?" | The first true condition's block ran, and Python never checked the rest |
| "How would you fix this chain?" | Put the more specific condition (`score >= 90`) first |

**Transition:** *"Let's bring back last class's toolkit — comparisons
and logical operators work perfectly inside a condition."*

---

## 16. Comparisons and Logical Operators Inside Conditions (54–62)

**Type this live:**

```
age = 16
is_student = True

if age >= 13 and age <= 19 and is_student:
    print("Eligible for the student teen discount!")
```

> "This condition is built entirely from Class 07's toolkit — two
> comparisons and a logical `and`, combined into one boolean expression.
> An `if` doesn't need anything new here; it just needs *a* boolean
> expression, however it's built."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What kind of value does an if's condition need to be?" | A boolean — True or False |
| "Can a condition use `and`/`or`/`not` from last class?" | Yes, directly |

**Transition:** *"Let's step back and look at the three shapes we've
built today, side by side."*

---

## 17. Common Structure Patterns (62–68)

**Survey the three canonical shapes:**

```
if alone           →  do something, or nothing
if / else          →  exactly one of two paths
if / elif / else   →  exactly one of several paths
```

> "Every conditional you write will be one of these three shapes.
> Choosing between them is about how many distinct outcomes your problem
> actually has — two, or more than two, or 'maybe nothing at all.'"

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "If a problem has exactly two outcomes, which shape fits?" | if/else |
| "If a problem has three or more outcomes?" | if/elif/.../else |

**Transition:** *"Let's connect this whole idea to something from Class
01."*

---

## 18. The Class 01 Callback — Algorithms Can Branch (68–75)

**Land the core reframe of the whole class:**

> "Remember Class 01's `ALGORITHM` — 'the plan, as steps a person could
> follow'? We've always drawn it as a straight line, one step after
> another. Today, that picture gets wider: an algorithm can **branch** —
> different data can send it down a different path entirely."

**Draw the connecting idea:**

```
ALGORITHM  (Class 01 — imagined as a straight line of steps)
    ↓
ALGORITHMS CAN BRANCH  (today — different paths for different data)
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How did Class 01 describe an algorithm?" | Steps a person could follow, in order |
| "What does today add to that picture?" | Algorithms can branch, not just proceed straight through |

**Transition:** *"Let's put the entire day's reasoning on one board —
starting all the way back at Class 01."*

---

## 19. Full Class 01 → Class 08 Bridge (75–83) — NON-NEGOTIABLE, HERO MOMENT

**This is the HERO MOMENT of the class.** Build it live, top to bottom,
one line at a time — never reveal it finished.

1. Write **PROBLEM** — *"Something we're trying to solve."* (Class 01)
2. Arrow down, write **LOGIC** — *"Reasoning about how to solve it."*
   (Class 01)
3. Arrow down, write **ALGORITHM** — *"The plan — and now we know it can
   branch."* (Class 01, widened today)
4. Arrow down, write **PYTHON CODE** — *"That plan, written precisely
   enough for a computer to follow."* (Class 05)
5. Arrow down, write **VARIABLES** — *"Labeled, changeable values."*
   (Class 06)
6. Arrow down, write **EXPRESSIONS** — *"Operators combining values into
   new values, including booleans."* (Class 07)
7. Arrow down, write **DECISIONS** — *"if / elif / else — booleans that
   actually choose which code runs."* (today)
8. Arrow down, write **RUN** — *"Telling the computer to carry it
   out."* (Class 05)
9. Arrow down, write **OUTPUT / RESULT** — *"What the program
   produces — now, one of potentially several different results."*
   (Class 05)

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
EXPRESSIONS
    ↓
DECISIONS
    ↓
RUN
    ↓
OUTPUT / RESULT
```

**Say explicitly, this is the whole point of the diagram:**

> "`DECISIONS` sits right on top of `RUN` for a reason — it's the very
> last thing that happens before the computer actually carries the
> program out, and it's what decides *which* version of 'carrying it
> out' actually happens."

**Do not compress this block below 6 minutes**, even under time
pressure — see Section 31.

---

## 20. Interactive Activity — Your Profile Card Decides (83–98) — NON-NEGOTIABLE

**This is the HERO ACTIVITY.** Every student extends their own running
Profile Card (from Classes 06–07) with real branching — no copying the
class example verbatim.

### Facilitator instructions (timed, ~15 minutes at canonical pace)

1. **(2 min) Set up:** "Open your Profile Card. Add **two** things: (1)
   an `if`/`else` using your `is_student` boolean — one message if
   `True`, a different message if `False`; (2) an `if`/`elif`/`else`
   chain using your `age` variable, with at least three branches (e.g.
   child/teen/adult, or any categories you choose)."
2. **(8 min) Let students write and run independently (or in pairs).**
   Circulate constantly — check indentation first for anyone with an
   error. Prompt stuck students with: "What are two different messages
   that could depend on whether you're a student? What are three age
   categories you could sort yourself into?"
3. **(3 min) Ask everyone to change one variable's value and re-run,
   confirming a *different* branch executes.** This is the single most
   important confirmation in the activity.
4. **(2 min) Invite 2–3 students to share one conditional and both of
   its possible outcomes with the room.**

### Questions and expected responses

| Question | Expected response |
|---|---|
| "Which branch ran, and why?" | Any coherent answer correctly tracing the condition that was true |
| "What happened when you changed the variable and re-ran it?" | A different branch executed |
| "If you got an IndentationError, what usually causes it?" | Inconsistent or missing indentation after a colon |

**Do not introduce new syntax during this activity** (no nested `if`, no
loops, no `input()`) — if a student asks for one, use the parking-lot
response (Section 33) and let their program stay simple.

### Timing, extension, and support

- **Canonical timing:** ~15 minutes, per the breakdown above.
- **Stronger-student extension:** Ask them to add a fourth `elif` branch,
  or combine two comparisons with `and`/`or` inside one of their
  conditions.
- **Weaker-student support:** Provide the Section 20 template directly
  (see Student Notes), and let them adapt the variable names and
  messages to their own card.
- **Transition back to the main lesson:** "You just watched your own
  program behave differently because of your own data — for the first
  time. That's the entire idea of today's class."

---

## 21. Misconceptions — In-Class Handling (98–103)

Pick 2–3 of the misconceptions most likely to have surfaced already today
(see Section 24 for the full reference table) and address them directly
and briefly.

Suggested priority order for in-class handling:

1. "Python checks every elif, even after one matches" (very likely
   surfaced in Section 15).
2. "Indentation is just neat formatting" (likely surfaced in Section
   12, or the activity's errors).
3. "else needs its own condition" (worth pre-empting if any student
   tried to write `else age > 5:`).

Keep this to 5 minutes — this is a quick defusal pass, not a new lecture.

---

## 22. Recap (103–108) — NON-NEGOTIABLE

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last several minutes:

1. **"When does an if block's indented line actually run?"** *Expected:*
   only when the condition is `True`.
2. **"Why does indentation matter so much in Python?"** *Expected:* it's
   the actual syntax that defines a block, not decoration.
3. **"When does an else block run?"** *Expected:* only when every
   condition above it was `False`.
4. **"If more than one elif condition is true, which one actually
   runs?"** *Expected:* only the first true one — the rest are never
   checked.
5. **"Can a condition use and/or/not from Class 07?"** *Expected:* yes,
   directly.
6. **"How does this connect back to Class 01?"** *Expected:* an
   algorithm isn't just a straight line of steps — it can branch.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 23. Final Takeaway (108–110)

**Close with the final statement, said slowly:**

> "Every program before today ran the same way, every single time. Today,
> for the first time, your code actually **thinks** before it acts — it
> looks at its own data and chooses a path. That single idea —
> branching — is the foundation of almost everything a real program
> does."

**Then leave the bridge-forward question open, explicitly not answered
today:**

> "Right now, every decision only runs once. What if a program needed to
> make the same decision — or repeat the same action — over and over,
> without you writing it out by hand each time? That's exactly where we
> pick up next class."

Do not resolve this — it is intentionally a hook into Class 09
(Repetition: while and for Loops).

---

## 24. Common Misconceptions — Full Reference

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "Python checks every elif, even after one has already matched." | Confusion when a later, also-true elif doesn't run | "Python stops at the first true condition in the chain and runs only that block — it never even looks at what comes after." | Section 15 |
| 2 | "Indentation is just neat formatting, like extra spaces anywhere else." | Inconsistent indentation, or surprise at an `IndentationError` | "Indentation is Python's actual syntax for marking a block — it's not optional, and it's not just for readability." | Section 12 |
| 3 | "else needs its own condition, just like if and elif." | Writing `else some_condition:` | "else never takes a condition — it's simply 'otherwise,' whatever's left after every condition above it was False." | Section 13 |
| 4 | "If no condition matches and there's no else, something still happens." | Expecting a default action with no else present | "If nothing matches and there's no else, nothing in that conditional runs at all — the program just continues to the next line after it." | Section 14 |
| 5 | "Once you write an if, the rest of the program only runs if the condition is true." | Confusing a conditional's scope with the whole program | "Only the indented block belongs to the if. Any line after it, back at the original indentation level, always runs regardless." | Section 11–12 |

---

## 25. Instructor Language / Teaching Guardrails

**Prefer:**

- "The indented block runs only when the condition is True" — **over**
  "the if does something."
- "Only the first true branch runs" — **over** leaving elif ordering
  unaddressed.

**Avoid:**

- "Just indent it and it'll work" — without explaining *why* indentation
  matters, this invites Misconception 2.
- Demonstrating a nested `if` "just to show it's possible" — even
  briefly, this adds a full extra layer of complexity this class
  deliberately avoids.

**The instructor must NOT**, at any point in this class:

- introduce an `if` nested inside another `if`
- introduce `while`/`for` loops
- introduce `input()`
- introduce functions the student defines themselves (`def`)
- introduce lists, dictionaries, or any other data structure
- introduce ternary/conditional expressions (`x if cond else y`)
- introduce `match`/`case`
- combine conditionals with any loop construct

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that soon — a later class is
> exactly where that lives. Today we're building one clean decision at a
> time."

Then return to whichever anchor fits the moment:

```
PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → VARIABLES → EXPRESSIONS → DECISIONS → RUN → OUTPUT/RESULT
```

See Section 33 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 26. Interaction Philosophy

Class 08 continues the hands-on-typing emphasis from Classes 05–07, with
one addition: **running the same program twice with different data** is
this class's signature move, used repeatedly.

**Sample questions to use across the class:**

- "Before I change this value and run it again — what do you think will
  happen?"
- "Which block actually ran, and why?"
- "Why didn't Python check the remaining elif/else once one branch
  matched?"
- "What would happen if I removed the indentation from this line?"
- "How many possible outcomes does this conditional have?"

**Prediction-before-running remains the single most valuable habit.**
This class's best version of it: predicting a program's *second* run
after only one value changed (Sections 11, 14, 15).

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 8–12 seconds for the two hardest reasoning
moments — predicting the elif-ordering result in Section 15, and
predicting the effect of the second run in Section 11.

**Built-in reasoning opportunities to protect, in priority order:**

1. Predicting the second run after changing `is_raining` (Section 11)
2. Predicting the `IndentationError` before it's shown, if a student
   suggests removing the indent (Section 12)
3. Predicting the elif-ordering result (Section 15)
4. Every individual choice a student makes extending their own Profile
   Card (Section 20)

---

## 27. Visual / Board Plan

Most of this class's "board" is the **live screen**, exactly as in
Classes 05–07.

**Screen 1 — Your First if, Run Twice**
Typed live in Section 11. `is_raining = True` → message prints;
`is_raining = False` → nothing prints.

**Screen 2 — IndentationError, On Purpose**
Broken live in Section 12. The unindented block, then the inconsistently
indented block, each producing an `IndentationError`.

**Screen 3 — if / else, Run Twice**
Typed live in Section 13. Both branches shown by flipping
`is_raining`.

**Screen 4 — if / elif / elif / else**
Built live in Section 14. The ticket-pricing example, re-run with
several different `age` values.

**Screen 5 — Order Matters**
Typed live in Section 15. The `score = 95` example, "Pass" printing
instead of "Pass with Distinction."

**Screen 6 — Comparisons and Logic Inside a Condition**
Typed live in Section 16. The teen-discount example.

**Drawing 1 — HERO — Full Bridge**
Reserved for Section 19, whiteboard.

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
EXPRESSIONS
    ↓
DECISIONS
    ↓
RUN
    ↓
OUTPUT / RESULT
```

Mark this as a **live construction** — do not show the completed
nine-line chain before students have reasoned their way to each new
piece. This is the single most important drawing of Class 08.

Keep every diagram simple — no formal flowchart symbols, no nested-box
diagrams.

---

## 28. Class 01–08 Continuity

**Class 1:**

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**Class 6:**

```
PYTHON CODE → VARIABLES → RUN → OUTPUT/RESULT
```

**Class 7:**

```
VARIABLES → EXPRESSIONS → RUN → OUTPUT/RESULT
```

**Class 8:**

Inserts **DECISIONS** into Class 07's chain, and widens Class 01's
`ALGORITHM` box — from "a straight line of steps" to "a plan that can
branch":

```
EXPRESSIONS → DECISIONS → RUN → OUTPUT/RESULT
```

**Say this once, clearly (Section 9 or Section 18 are the natural
spots):**

> "We are not starting a new topic. We're opening one more box inside
> Class 07's chain — and, for the second time since Week 1, we're
> reshaping how we picture one of Class 01's very first boxes."

This is the same continuity statement pattern used since Class 02 — it
is what turns eight separate classes into one staircase instead of eight
unrelated topics.

---

## 29. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks throughout the class, and rely heavily on the hands-on
activity (Section 20), exactly as in Classes 05–07.

A student is demonstrating real understanding if they can:

1. Write a working `if` statement and explain when its block runs.
2. Explain why indentation matters, not just that it's required.
3. Add an `else` block and explain when it runs.
4. Chain `elif` for more than two paths.
5. Correctly predict which branch runs in an elif chain where more than
   one condition is true.
6. Use Class 07's comparison and logical operators inside a condition.
7. Connect today's branching idea back to Class 01's `ALGORITHM`.

**Do not** judge understanding solely from a student successfully
copying the instructor's exact example — running their own program
twice with two different values and correctly predicting both outcomes
(Section 20) is the strongest evidence of real understanding.

---

## 30. Differentiation

**For students struggling:** Anchor entirely in the two-run pattern —
run once, see one outcome; change one value, run again, see the other.
Walk the concrete progression one branch at a time:

```
write the condition  →  predict  →  run  →  change the value  →  predict again  →  run again
```

**For students moving quickly:** Let them extend the activity (Section
20's stronger-student extension) — a fourth `elif` branch, or a
condition combining `and`/`or`. Do **not** teach nested conditionals,
loops, or `input()` even for fast movers — deepen *fluency* with
branching, not scope. See Section 32 for the full extended-version
guidance.

**For students who stay quiet:** The Profile Card activity (Section 20)
is naturally personal and low-stakes — circulate and read their screen
rather than calling on them verbally, exactly as in Classes 05–07.

---

## 31. Time Management / Timing Safety

**Must cover, in priority order** (matches the non-negotiable list in
Section 7):

1. Your First if Statement (Section 11)
2. Indentation: Not Just Style (Section 12)
3. else: The Otherwise (Section 13)
4. elif: More Than Two Paths (Section 14)
5. The full Class 01 → Class 08 bridge (Section 19)
6. The Your Profile Card Decides activity (Section 20)

**Can shorten:**

- Order of elif Matters (Section 15) — a single example is enough, skip
  the "how would you fix it" follow-up
- Common Structure Patterns (Section 17) — state the three shapes
  quickly, no separate discussion needed
- Comparisons and Logical Operators Inside Conditions (Section 16) — one
  quick example instead of building it up live
- The misconception discussion (Section 21) — pick just one instead of
  2–3

**Can expand** (see Section 32 for detail):

- Let students predict more elif-chain outcomes in Section 14 before
  moving on
- Run a second "order matters" example in Section 15 with a
  student-suggested pair of conditions
- Spend more time circulating during the activity (Section 20)

**Do not cut:** Your First if Statement (Section 11), Indentation
(Section 12), else (Section 13), elif (Section 14), or the Your Profile
Card Decides activity (Section 20) — these are the load-bearing walls of
the entire class.

### 90-minute version

Trim as follows: Opening Mystery to 4 min, Callback to 4 min, What Is a
Conditional? to 4 min, Your First if unchanged (9 min), Indentation to 6
min, else unchanged (7 min), elif to 7 min, Order Matters to 4 min,
Comparisons/Logic in Conditions to 5 min, Common Patterns to 3 min,
Class 01 Callback to 5 min, Full Bridge unchanged (8 min), Activity
compressed to 11 min, Misconceptions to 3 min, Recap to 3 min, Final
Takeaway unchanged (2 min). Total ≈ 85 minutes.

### 120-minute version

Add time back to: Your First if Statement (+2 min, let more students
narrate their own prediction before each run), elif (+2 min, a second
worked example with a different theme), Order Matters (+2 min, a
student-suggested pair of conditions), Activity (+4 min, let every
student who wants to present their program to the room).

---

## 32. Extended Version

If time allows, deepen fluency — do **not** introduce nested
conditionals, loops, or `input()`.

- Let students predict the outcome of a four-branch `elif` chain with a
  value that matches the *last* `elif`, reinforcing that Python really
  does check in order.
- Ask stronger students to rewrite an `if`/`elif`/`elif`/`else` chain
  using different condition boundaries and confirm the categorization
  logic still works for edge values (e.g., exactly 13, exactly 20).
- Ask students to translate a plain-English rule with three or more
  outcomes of their own invention into a full `if`/`elif`/else chain.

---

## 33. Advanced Topics Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "Can I put an if inside another if?" | "Yes — that's nesting, a real and useful technique, just not today's focus." | "Today's building block is one clean decision at a time." |
| "How do I repeat a decision many times, like for a list of people?" | "That's a loop — real, and coming very soon." | Return to: today, every decision runs exactly once. |
| "How do I let the user's own typed answer decide the branch?" | "That's input() combined with if — both real, and this combination is a natural next step once you've met input()." | Return to: today, all values are set directly in the code. |
| "Is there a shorter way to write a simple if/else in one line?" | "Yes — a conditional expression (`x if cond else y`) — real, handy, and easy to add once the full version is second nature." | Return to: today's full, explicit form. |
| "Does Python have a switch/case statement like some other languages?" | "It has something similar called `match`/`case` — real, newer, and a natural alternative to a long elif chain, for later." | Return to: today's `if`/`elif`/`else` chain. |
| "What if two elif conditions are both true — can both run?" | "No — only the first true one ever runs. That's exactly Section 15's point." | Answer directly; this one is in scope. |

---

## 34. Teacher FAQ

**Q: A student's block didn't run and they don't see why — what's the
first thing to check?**
A: Indentation, first — is the block actually indented, and is it
consistent? Then the condition itself — is it actually `True` given the
current variable values? This mirrors Class 05's debugging loop.

**Q: Should I explain how many spaces of indentation Python requires?**
A: No exact number is magic — four spaces is conventional and what most
editors auto-insert. The point (Section 12) is that indentation must be
*consistent within a block*, not a specific count to memorize.

**Q: A student asked about nested if statements — did I do something
wrong by not covering it?**
A: No — that's the parking lot working exactly as intended (Section 33).
Nesting is a natural, very soon extension, not a gap in today's class.

**Q: What if a student's elif chain "works" but always hits the wrong
branch?**
A: This is almost always an ordering issue (Section 15) — walk through
the chain top to bottom together and ask which condition is actually
checked first.

**Q: Is it okay if some students finish the activity early?**
A: Yes — use the stronger-student extension in Section 20 (a fourth
`elif`, a combined `and`/`or` condition). Do not let early finishers
pull you into teaching loops or nesting ahead of schedule.

**Q: What if I only have 90 minutes, not 110?**
A: Use the 90-minute version in Section 31 — it preserves every
non-negotiable block and only trims discussion time and the
common-patterns survey.

---

## 35. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Write a working `if` statement and explain when its block runs.
2. Explain that indentation is syntax, not decoration.
3. Add an `else` block and explain when it runs.
4. Chain `elif` for more than two paths.
5. Explain that only the first true branch in a chain runs, and why
   ordering matters.
6. Use comparison and logical operators from Class 07 inside a
   condition.
7. Reconnect today's branching idea to Class 01's `ALGORITHM`.

A class where most students can do these in plain, imperfect language —
and where every student has personally watched their own program behave
two different ways — has met the bar.

---

## 36. Source-of-Truth / QA Checklist

Verified against the Foundation Batch 2026 curriculum plan (Block 1,
`C08`) before finalizing this guide:

- [x] Class 01, 06, and 07 continuity is explicit (Sections 3, 9, 18,
      28).
- [x] The class starts with a felt limitation, not a definition (Section
      8).
- [x] Every student writes, runs, and re-runs real conditionals with
      changed data, not just watches (Sections 11, 13, 14, 20).
- [x] Indentation is explicitly taught as syntax, including a
      deliberate, on-purpose error (Section 12).
- [x] `else` is explicitly shown to take no condition (Section 13).
- [x] `elif` chains are built live with three or more branches (Section
      14).
- [x] Elif-ordering — only the first true branch runs — is explicitly
      demonstrated, not just stated (Section 15).
- [x] Comparison and logical operators from Class 07 are explicitly
      reused inside a condition (Section 16).
- [x] No nested conditionals, loops, `input()`, user-defined functions,
      data structures, or ternary expressions are taught (Section 1,
      Section 25, guarded throughout).
- [x] Misconceptions are explicitly handled, both in-flow (Section 21)
      and as a full reference (Section 24).
- [x] The Your Profile Card Decides activity extends Classes 06–07's
      activities directly, reinforcing continuity (Section 20).
- [x] The class explicitly widens Class 01's `ALGORITHM` box from a
      straight line to something that can branch (Section 18, Section
      28).
- [x] The class has a clear, explicit, unresolved bridge to Class 09
      (Repetition: while and for Loops) (Section 23, Section 33).
- [x] This Master Guide is self-contained and usable by an instructor
      without relying on the Student Notes — every section includes
      instructor wording, questions, expected answers, and transitions.
