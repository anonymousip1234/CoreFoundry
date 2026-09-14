# Class 05 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Your First Python Program
**Subtitle:** From English Instructions → Python Code
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 02 — How
Machines Learn, Class 03 — Understanding Data, Class 04 — How Computers
Represent Information

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

**One thing is genuinely new about this class:** it is the first time
students touch a keyboard and run real code. Everything in Sections 8–24
is written assuming students have a working Python 3 environment open in
front of them (see the Pre-Class Setup box in Section 1). If your room
cannot guarantee that, read Section 31's "no-computer" fallback before you
walk in.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01, 02, 03, and 04](#3-relationship-to-class-01-02-03-and-04)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening Mystery (0–5)](#8-opening-mystery-0-5)
9. [Class 01 Callback (5–10)](#9-class-01-callback-5-10)
10. [What Is a Programming Language? (10–16)](#10-what-is-a-programming-language-10-16)
11. [Meet Python (16–21)](#11-meet-python-16-21)
12. [Setup — Where Code Runs (21–25)](#12-setup--where-code-runs-21-25)
13. [Your First Line: print() (25–33)](#13-your-first-line-print-25-33)
14. [Running the Program (33–40)](#14-running-the-program-33-40)
15. [Strings Need Quotes (40–46)](#15-strings-need-quotes-40-46)
16. [Multiple Instructions, In Order (46–53)](#16-multiple-instructions-in-order-46-53)
17. [Comments (53–60)](#17-comments-53-60)
18. [When Syntax Breaks: Errors (60–68)](#18-when-syntax-breaks-errors-60-68)
19. [The Write–Run–Read–Fix Loop (68–75)](#19-the-writerunreadfix-loop-68-75)
20. [Full Class 01 → Class 05 Bridge (75–82)](#20-full-class-01--class-05-bridge-75-82)
21. [Interactive Activity — My First Program (82–100)](#21-interactive-activity--my-first-program-82-100)
22. [Misconceptions — In-Class Handling (100–105)](#22-misconceptions--in-class-handling-100-105)
23. [Recap (105–109)](#23-recap-105-109)
24. [Final Takeaway (109–110)](#24-final-takeaway-109-110)
25. [Common Misconceptions — Full Reference](#25-common-misconceptions--full-reference)
26. [Instructor Language / Teaching Guardrails](#26-instructor-language--teaching-guardrails)
27. [Interaction Philosophy](#27-interaction-philosophy)
28. [Visual / Board Plan](#28-visual--board-plan)
29. [Class 01–05 Continuity](#29-class-01-05-continuity)
30. [Assessment of Understanding](#30-assessment-of-understanding)
31. [Differentiation](#31-differentiation)
32. [Time Management / Timing Safety](#32-time-management--timing-safety)
33. [Extended Version](#33-extended-version)
34. [Advanced Topics Parking Lot](#34-advanced-topics-parking-lot)
35. [Teacher FAQ](#35-teacher-faq)
36. [Class Success Check](#36-class-success-check)
37. [Source-of-Truth / QA Checklist](#37-source-of-truth--qa-checklist)

---

## 1. Class Identity

| Field | Value |
|---|---|
| Class number | 05 |
| Title | Your First Python Program |
| Subtitle | From English Instructions → Python Code |
| Audience | First-year college students, mixed backgrounds. Most have never written a line of code. A few may have dabbled in Scratch, HTML, or a school BASIC/C exercise — treat that as a small head start, not a different track. |
| Prerequisites | Class 01 (`PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT`), Class 02 (`DATA → LEARNING → MODEL → PREDICTION`), Class 03 (`REAL WORLD → OBSERVATION → DATA`), Class 04 (`REPRESENTATION → BITS`). No prior programming assumed or required. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Classes 01–04 talked *about* programs, data, and representation without ever writing one. Class 05 is where "PROGRAM" — a box Class 01 drew on the board four classes ago — stops being an abstract word and becomes something every student personally types and runs. |
| Core question | **"If a computer only does exactly what it's told, how do we tell it something — in a way it can actually follow?"** |
| Core concept | `ENGLISH INSTRUCTIONS → PYTHON CODE → RUN → OUTPUT`, landing inside Class 01's existing chain as `ALGORITHM → PROGRAM → RESULT` made literal. |
| Class success metric | Without prompting, most students can: (1) explain why a computer needs an unambiguous, precisely-formatted language rather than plain English; (2) write and run a `print()` statement that displays their own text; (3) explain that text inside `print()` needs quotes; (4) write several `print()` statements and explain that Python runs them in order, top to bottom; (5) write a comment with `#` and explain that Python ignores it; (6) read a simple syntax error message without panicking and identify roughly what it's complaining about; (7) connect today's work back to Class 01's `PROGRAM` box. |

**Pre-Class Setup (read before the class, not during it):** Every student
needs a working Python 3 environment open before Section 13. Two options,
either is fine — do not spend in-class time installing software:

- **Recommended:** [Thonny](https://thonny.org/) — free, starts in
  seconds, and its editor/output split matches exactly what this guide
  describes ("type on top, run, see output below").
- **No-install fallback:** any trusted browser-based Python runner (e.g.
  the official [Python.org Shell](https://www.python.org/shell/) or a
  classroom-approved online IDE) for students without admin rights to
  install software, or the machine-bundled **IDLE** if Python is already
  installed.

If your room genuinely cannot guarantee this for everyone, see the
no-computer fallback in Section 31 before you walk in — do not skip the
class, adapt it.

This class is entirely about `print()`, comments, and running code. **No
variables. No data types beyond "text needs quotes." No input(). No
if/else, loops, or functions of your own. No lists or dictionaries. No
indentation rules (nothing here needs an indented block). No string
formatting beyond commas inside `print()`.** If you feel tempted to show
a variable to "make an example cleaner," that is the signal to simplify
further, not to go deeper — Class 06 owns that.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one feeling in a student's head with another.
Before this class: *"Programming is something other people do — it looks
like a wall of confusing symbols."* After this class: *"I already wrote
and ran a real program. It didn't look like magic — it looked like giving
very precise instructions, one line at a time."* Every example, every
error message shown on purpose, every minute of the hands-on activity
exists to land that one replacement.

**Teaching philosophy, in one line:** identical in spirit to Classes
01–04 — intuition before syntax, example before rule, ask before
explaining — with one addition unique to this class: **let students type
it themselves.** A slide showing `print("Hello")` teaches far less than a
student typing it, running it, and watching text appear because of
something *they* wrote.

**What students should feel by the end:**

- A beginner should feel: *"I wrote a program. It ran. It did exactly
  what I told it to. I can do this again."*
- A stronger student should feel: *"I can already see how this scales up
  — more lines, more instructions, more control."*
- Everyone should feel the specific, small thrill of the **first error
  message** landing without panic — because Section 18 deliberately
  shows one before any student hits one by accident.

**State this to yourself before you walk in:**

> This is **not** a class about becoming a programmer by the end of the
> hour. Nobody needs to leave able to build anything complex. This class
> exists so that "writing code" stops being an intimidating, unfamiliar
> act and becomes something students have personally done — the same way
> Class 04 turned "binary" from a mysterious word into something
> understood from the inside.

If a question drifts toward "how do I make the program ask *me*
something" or "how do I store a value," that is Class 10's and Class 06's
job respectively — redirect warmly using the parking-lot response in
Section 34. This is not a cop-out; it is the actual scope of the class.

---

## 3. Relationship to Class 01, 02, 03, and 04

Class 01 built:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
INPUT → PROCESS → OUTPUT
```

Class 02 built:

```
DATA → LEARNING → MODEL → PREDICTION
```

Class 03 built:

```
REAL WORLD → OBSERVATION → DATA
DATA → EXAMPLES → FEATURES → LABELS → DATASET
```

Class 04 built:

```
DATA → REPRESENTATION → BITS
```

...and landed on: **binary is a representation system, and meaning comes
from interpretation.** All four classes stayed conceptual — no class so
far has asked a student to write a single instruction a computer actually
carries out. Class 05 is where that changes.

**Say this explicitly, early (Section 9 is the natural spot):**

> "Four classes ago, we drew a box labeled PROGRAM and moved on. We've
> talked about problems, algorithms, data, and bits — but not once have
> we actually written a program ourselves. Today, that box stops being a
> word on a board."

**The relationship is not new content bolted on — it is finally opening a
box that has sat on the board since Class 01:**

```
Class 1 chain:   PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
Class 5 opens:                                    ▲▲▲▲▲
                                    ENGLISH → PYTHON CODE → RUN → OUTPUT
```

Frame it exactly like this:

> "We're not starting a new subject. We're finally doing the one step of
> Class 01's chain we've never actually done: turning an algorithm into a
> real program."

This is the same staircase framing Classes 01–04 all used — see Section
29 for the full continuity treatment.

---

## 4. Learning Objectives

Taken directly from the batch curriculum's Block 1 opening brief. For
each, the bar is **can do it and explain it in plain language** — this is
a hands-on class, so "can do" carries more weight here than in Classes
01–04.

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | A computer needs unambiguous, precisely-formatted instructions | Can explain, in their own words, that a computer does exactly what's written — no filling in gaps like a person would | Formal grammar theory, parsers, compilers |
| 2 | Python is a programming language for writing those instructions | Can say "Python is one of the languages we use to write precise instructions for a computer" | Comparisons to other languages, history of Python |
| 3 | `print()` displays text | Can write `print("...")` with their own text and predict what it will show | The word "function" as a formal concept (introduced lightly, owned fully by Class 11) |
| 4 | Text needs quotes | Can explain that Python needs to know where text starts and ends, and that's what quotes do | String escaping, single vs. double quote rules beyond "pick one and match it" |
| 5 | Instructions run in order, top to bottom | Can write 3+ `print()` lines and correctly predict the output order | Any control-flow concept (loops, conditionals) |
| 6 | Comments (`#`) are ignored by Python | Can write a comment and explain that it's for humans, not the computer | Docstrings, multi-line comment conventions |
| 7 | Errors are normal, readable feedback | Can look at a simple syntax error and say roughly what's wrong without panic | Reading a full traceback, exception types beyond "syntax error" and "name error" |
| 8 | Running code is a loop: write → run → read → fix | Can describe this cycle in their own words | Formal debugging techniques (Class 14's territory) |
| 9 | Connect Class 01's PROGRAM box to real code | Can restate `ALGORITHM → PYTHON CODE → RUN → OUTPUT` as what happened today | Any new algorithmic content |

---

## 5. Key Terminology

Small and durable beats large and forgettable — same principle as every
prior class. These are the **only** terms this class needs, and even
these are earned through example first.

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Program** | A precise sequence of instructions a computer can carry out. | "What Class 01 called a program — except now it's real, typed code." | — | Loosely — already known |
| **Python** | A programming language: a precise, readable way to write instructions for a computer. | "One language among several we could have chosen — readable and widely used." | "The only real programming language" | Loosely — name only |
| **Code / Source code** | The actual text of the instructions we write. | "What you type — the instructions themselves." | — | Yes |
| **`print()`** | A built-in instruction that displays text as output. | "Tells Python: show this." | "It sends a message somewhere" (it displays locally) | Yes — core term |
| **Function call** | The `name(...)` pattern that tells Python to run a piece of built-in behavior. | "Parentheses mean: do something, using whatever's inside." | Formal function theory | Loosely — name only, owned by Class 11 |
| **String** | Text data, written between matching quotes. | "Text, wrapped in quotes so Python knows where it starts and ends." | "A special complicated data type" (it will be, later — not today) | Loosely — name only, owned by Class 06 |
| **Comment (`#`)** | A line, or part of a line, that Python completely ignores — notes for humans. | "Anything after `#` on that line — Python skips it entirely." | — | Yes |
| **Run / Execute** | Telling the computer to actually carry out the program's instructions. | "Pressing the button that makes it happen." | — | Loosely |
| **Syntax** | The precise rules for how Python code must be written. | "The exact grammar Python insists on." | — | Loosely |
| **Syntax error** | What Python reports when code breaks those rules. | "Python's way of saying 'I can't understand this line as written.'" | "You broke the program/computer" | Yes — concept, not the message wording |
| **Output** | What the program displays as a result of running. | "What appears after you press run." | — | Loosely |

---

## 6. Class at a Glance

Canonical **110-minute** flow.

| Time | Dur. | Section | Objective | Teaching mode | Board/Screen | Interaction |
|---|---|---|---|---|---|---|
| 0–5 | 5 | Opening Mystery | A genuinely ambiguous instruction fails | Ask → demonstrate → hold | None yet | High |
| 5–10 | 5 | Class 01 Callback | Re-open the PROGRAM box | Recall → question | Class 01's chain | Medium |
| 10–16 | 6 | What Is a Programming Language? | Precision, not English, is the point | Ask → land | None new | Medium |
| 16–21 | 5 | Meet Python | Name the tool, briefly | Reveal → reassure | Screen: Python open | Low |
| 21–25 | 4 | Setup — Where Code Runs | 60-second orientation to the editor | Show → point | Live screen | Low |
| 25–33 | 8 | Your First Line: print() | Type and run the first program | Type-along | Live screen | Very high |
| 33–40 | 7 | Running the Program | See output appear, land the concept | Do → confirm | Live screen | High |
| 40–46 | 6 | Strings Need Quotes | Why the quotes exist, what breaks without them | Ask → break it on purpose | Live screen | High |
| 46–53 | 7 | Multiple Instructions, In Order | Sequencing, tied to Class 01's ALGORITHM | Build live | Live screen | High |
| 53–60 | 7 | Comments | `#`, ignored by Python, for humans | Ask → demonstrate | Live screen | Medium |
| 60–68 | 8 | When Syntax Breaks: Errors | Read an error calmly, on purpose | Break it → read together | Live screen | High |
| 68–75 | 7 | The Write–Run–Read–Fix Loop | Name the cycle they just lived through | Reveal → label | Diagram | Medium |
| 75–82 | 7 | Full Class 01 → Class 05 Bridge | Install the hero chain | Build live | **Hero diagram** | High |
| 82–100 | 18 | Interactive Activity — My First Program | Students write and run their own program | Facilitated hands-on | Circulate | Very high |
| 100–105 | 5 | Misconceptions | Directly address 2–3 common misreadings | Ask → reframe | None | Medium |
| 105–109 | 4 | Recap | Consolidate, verify | Ask → students answer | Reuse hero diagram | High |
| 109–110 | 1 | Final Takeaway | Close on one memorable line | State → bridge forward | None | Low |

**Non-negotiable blocks** (never compressed away — see Section 32): Your
First Line: print(), Multiple Instructions In Order, Comments, When
Syntax Breaks: Errors, the Class 01 → Class 05 bridge, and the My First
Program activity.

---

## 7. Section-by-Section Teaching Guide

Quick **A–D** index for every block; full teaching notes for each live in
Sections 8–24 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening Mystery | Show that vague instructions fail | Students see why "be precise" isn't optional | No |
| 2 | Class 01 Callback | Re-open the unopened PROGRAM box | Students state that PROGRAM has never been written for real | No |
| 3 | What Is a Programming Language? | Precision over plain English | Students explain why we can't just type English at a computer | No |
| 4 | Meet Python | Name the tool without fear | Students can say what Python is in one sentence | No |
| 5 | Setup — Where Code Runs | Orient to the editor | Students can point to where they type vs. where output shows | No |
| 6 | Your First Line: print() | Write and run real code | Every student runs a working `print()` | **Yes** |
| 7 | Running the Program | Output appears because of their code | Students describe what "running" a program means | **Yes** |
| 8 | Strings Need Quotes | Text needs delimiters | Students explain why quotes matter, by seeing it break | No |
| 9 | Multiple Instructions, In Order | Sequencing | Students predict output order from several `print()` lines | **Yes** |
| 10 | Comments | Notes for humans, invisible to Python | Students write a comment and explain it's ignored | **Yes** |
| 11 | When Syntax Breaks: Errors | Errors are normal feedback | Students read a simple error without panicking | **Yes** |
| 12 | The Write–Run–Read–Fix Loop | Name the cycle | Students describe the loop in their own words | No |
| 13 | Full Class 01 → Class 05 Bridge | Consolidate the whole continuity chain | Students restate the bridged chain | **Yes** |
| 14 | Interactive Activity | Write and run an original program | Every student produces a working multi-line program | **Yes** |
| 15 | Misconceptions | Directly defuse common wrong models | Students can correct at least one misconception aloud | No |
| 16 | Recap | Verify understanding | Students answer recap questions in their own words | **Yes** |
| 17 | Final Takeaway | Close memorably, bridge forward | Students can repeat the final line's idea, not its wording | No |

---

## 8. Opening Mystery (0–5)

Do **not** open with "Today we will learn Python." Open with a genuine,
slightly funny failure, exactly as Classes 01–04 opened with a puzzle
before naming anything.

**Exact opening approach:**

1. Say: *"I'm going to give an instruction, and I want you to follow it
   completely literally — do exactly what I say, nothing more."*
2. Give a deliberately ambiguous or overly literal instruction, e.g.:
   *"Everyone, please 'stand up.'"* — then, once they do, say *"Wait — I
   didn't say when to sit back down. I didn't say how. A person fills in
   the gaps I left. Would a computer?"*
3. A cleaner version if you prefer: ask a student to give you directions
   to the door using only the words they'd use with a friend (*"just go
   that way and turn"*), then point out how many gaps you, a human,
   silently filled in to follow it.
4. **Do not resolve it yet.** Let the gap between "instructions a person
   can follow" and "instructions a computer can follow" sit for a moment.
5. Bridge: *"A computer doesn't fill in gaps. It does exactly, and only,
   what it's told — nothing more, nothing less. Today we learn how to
   actually talk to one."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "Would a computer be able to follow that same vague instruction?" | "No," "it would need to know exactly what to do," "it doesn't guess" | Narrow it: "If I told a computer to 'go that way,' what's missing that a person would just figure out?" |

**How to handle silence:** This should land quickly — most students
immediately sense the gap once you point at it. If it doesn't, make the
instruction more absurd (e.g., "make me a sandwich" with zero further
detail) until the gap is obvious.

**Transition:** *"We've actually been dancing around this exact idea
since Class 01. Let's go back to something we drew in Week 1."*

---

## 9. Class 01 Callback (5–10)

Bring back Class 01's core chain exactly as it was left:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**What the instructor says:**

> "In Class 01, we built this chain. We talked about problems, logic,
> algorithms — even resu­lts. But one box in the middle — PROGRAM — we
> never actually opened. We described it. We never wrote one."

**Ask directly:**

> "In four classes, have we ever once written an actual program — real
> instructions a computer runs?"

Expected: **no** — most students will realize this immediately once
asked directly.

> "That changes today. An algorithm is the plan, written in a language
> like English, that a *person* can follow. A program is that same plan,
> rewritten so precisely that a *computer* can follow it, with zero gaps
> left to fill in."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What's the chain from Class 01?" | `PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT` |
| "Have we ever written a real program in this course?" | No |
| "What's the difference between an algorithm and a program?" | An algorithm is steps a person can follow; a program is those steps written precisely enough for a computer to follow |

**Transition:** *"So — if a computer only does exactly what it's told,
how do we tell it something in a way it can actually follow?"*

---

## 10. What Is a Programming Language? (10–16)

**Ask first, before naming Python:**

> "If English is too loose for a computer — too many gaps, too many
> assumed meanings — what would a language built *for* computers need to
> be like?"

Guide toward: **exact, unambiguous, with strict rules about how things
must be written.**

**Land the core statement:**

> "A programming language is a language with strict, precise rules —
> rules a computer can follow with zero guessing. It's still a language
> humans read and write; it's just far less forgiving about *exactly*
> how you write it than English is."

**Use a small, concrete contrast:**

> "In English, 'Print Hello World', 'print hello, world!', and 'go on,
> print Hello World for me' probably all mean the same thing to a human
> listener. To a computer, only one exact form will work at all — and
> we're about to see what that form is."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What would a language built for computers need to be like?" | Exact, precise, strict about rules |
| "Does that mean programming languages aren't 'real' languages?" | No — they're real languages, just much less forgiving about form |

**Transition:** *"There are many programming languages. Today we're
using one built to be about as readable as a language like this can be —
Python."*

---

## 11. Meet Python (16–21)

**Keep this short and reassuring — this is a naming section, not a
history lecture.**

> "Python is a programming language. It was deliberately designed to
> read almost like plain instructions, which is exactly why we're
> starting with it — the ideas underneath any programming language show
> through more clearly in Python than in most others."

**Say explicitly, an important guardrail:**

> "Python isn't 'the' programming language — it's one of many. Different
> languages exist for different jobs. We're starting here because it
> gets out of the way and lets you focus on how instructions for a
> computer actually work, not on complicated formatting rules."

Do **not** get into a language-comparison discussion (Python vs. Java vs.
C, "which is better") — if asked, park it (Section 34).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "In one sentence, what is Python?" | A programming language, designed to be readable |
| "Is Python the only programming language that exists?" | No — one of many |

**Transition:** *"Let's open it up and see where we'll actually be
typing."*

---

## 12. Setup — Where Code Runs (21–25)

**This is logistics, not concept — keep it under 4 minutes.** Software
should already be open from before class (see the Pre-Class Setup box in
Section 1); this section is a 60-second orientation, not an install
session.

**Point at the two regions of the screen, live:**

> "There are two areas you'll care about. Up here is the **editor** —
> where you type your instructions. Down here is the **output** — where
> you'll see what happens after you run them. That's genuinely the whole
> mental model for today."

**If anyone's setup failed:** pair them immediately with a neighbor
rather than troubleshooting solo in front of the room — do not let setup
problems eat into the non-negotiable blocks ahead. A pair sharing one
working environment for today is completely fine; each person still
writes and reasons about the code together.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Which area is where you type? Which shows what happened?" | Editor (top); output (bottom/console) |

**Transition:** *"Let's write the very first line of code any of you
will ever run."*

---

## 13. Your First Line: print() (25–33) — NON-NEGOTIABLE

**Type this live, slowly, narrating every character — do not paste it
in.**

```
print("Hello, World!")
```

> "This is one instruction. `print` tells Python 'display something.'
> The parentheses hold *what* to display. The quotes mark the text as
> text — we'll come back to exactly why in a few minutes."

**Have every student type this exact line themselves before moving on.**
Walk the room. This is the single most important 60 seconds of the
class — do not rush past it even if some students finish quickly.

**Ask before running it:**

> "Before I run this — what do you think will happen?"

Expected: *"It'll show 'Hello, World!'"* — most will guess correctly;
that's fine, the point is the prediction habit, not the difficulty.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What do you think `print(...)` will do?" | Display/show whatever is inside the parentheses |
| "Why are there quotes around the text?" | Uncertain guesses are fine here — Section 15 answers this properly |

**Transition:** *"Let's actually run it and see."*

---

## 14. Running the Program (33–40) — NON-NEGOTIABLE

**Run it live. Point at the output the moment it appears.**

> "There it is — `Hello, World!` appeared in the output area. That
> happened because of one line *you* wrote. That's a real, complete
> program. It's small, but it's not a toy — it's the same basic act
> every program you'll ever write does: instructions in, output out."

**Land the core statement, explicitly connecting back to Class 01:**

> "Remember `INPUT → PROCESS → OUTPUT` from Class 01? You just watched
> it happen for real. Your typed code was the process. The text on
> screen is the output."

**Have every student personalize and re-run it:**

```
print("Hello, my name is ___!")
```

(fill in their own name) — then run it again and confirm their own
output appears.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What just happened when you pressed run?" | The computer carried out the instruction and displayed the text |
| "Whose program produced that exact output?" | Mine — I wrote it |

**Transition:** *"Let's go back to those quotes — what happens if we
leave them out?"*

---

## 15. Strings Need Quotes (40–46)

**Break it on purpose, live, and let students watch:**

```
print(Hello, World!)
```

> "Watch what happens if I remove the quotes."

Run it. An error appears (something like a `SyntaxError` or `NameError`
depending on exact form — don't worry about the exact wording yet,
Section 18 handles reading errors properly).

**Land the core statement:**

> "Without quotes, Python doesn't know 'Hello, World!' is just text to
> display — it tries to treat those words as if they were more
> instructions, and gets confused. Quotes are how we tell Python 'this
> part is literal text, not more code.'"

**Say explicitly, a useful precision note:**

> "Single quotes `'...'` and double quotes `\"...\"` both work in Python
> — just make sure the one you open with matches the one you close with."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Why did removing the quotes cause a problem?" | Python no longer knows that text is literal text, not code |
| "What do the quotes actually mark?" | Where the text starts and where it ends |

**Transition:** *"One instruction is great. But real programs have many.
Let's add more lines."*

---

## 16. Multiple Instructions, In Order (46–53) — NON-NEGOTIABLE

**Build this live, one line at a time — do not reveal it finished.**

```
print("Hello, my name is Priya.")
print("I am learning Python.")
print("This is my very first program!")
```

**Ask before running:**

> "Before I run this — in what order do you think these three lines will
> appear?"

Expected: **top to bottom, in the order they're written.**

**Run it. Confirm the order matches the prediction exactly.**

**Land the core statement, tying back to Class 01's ALGORITHM:**

> "This is exactly what 'algorithm' meant in Class 01 — a sequence of
> steps, followed *in order*. Python doesn't pick and choose, and it
> doesn't guess a 'smarter' order. It runs your instructions top to
> bottom, exactly as written."

**Ask a probing follow-up:**

> "What do you think would happen if I swapped lines 1 and 3?"

Expected: the output order swaps too — try it live if time allows.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "In what order will these three lines run?" | Top to bottom, exactly as written |
| "What happens if I reorder the lines?" | The output order changes to match |

**Transition:** *"Sometimes you want to leave yourself a note in the
code that Python should completely ignore. There's a way to do that."*

---

## 17. Comments (53–60) — NON-NEGOTIABLE

**Type this live:**

```
# This program introduces me
print("Hello, my name is Priya.")   # prints my name
print("I am learning Python.")
```

> "Anything after a `#` on a line is a **comment.** Python skips it
> completely — it's not an instruction at all. It's a note, left for
> whoever reads the code next. That might be your teammate. It might be
> you, in six months, wondering what your own code does."

**Run it to prove the point:**

> "Notice the output didn't change at all — the comments produced
> nothing, because Python never even looked at them as instructions."

**Ask:**

> "Why might a programmer want to leave notes in code that the computer
> completely ignores?"

Expected: to explain what the code does, to leave reminders, to help
someone else (or future-you) understand it later.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does Python do with a comment?" | Ignores it completely — it's not an instruction |
| "Who are comments actually for?" | People reading the code, not the computer |

**Transition:** *"Let's deliberately break something else — because
you're going to see error messages constantly from here on, and the
first one should happen on purpose, in a safe moment."*

---

## 18. When Syntax Breaks: Errors (60–68) — NON-NEGOTIABLE

**Break it on purpose, live. Two small, clear examples:**

**Example 1 — a missing closing quote:**

```
print("Hello, World!)
```

Run it. An error appears (roughly: `SyntaxError: unterminated string
literal`).

> "Read this out loud with me, slowly. It's not yelling at you — it's
> telling you, quite specifically, what rule got broken: a piece of text
> that started with a quote never found its matching closing quote."

**Example 2 — wrong capitalization:**

```
Print("Hello, World!")
```

Run it. An error appears (roughly: `NameError: name 'Print' is not
defined`).

> "Python is case-sensitive — `print` and `Print` are two completely
> different words to it. This error is Python saying 'I don't know
> anything called `Print`.'"

**Land the core statement — this is the emotional heart of the
section:**

> "Every single person who has ever written code has seen hundreds of
> these. An error is not a judgment on you. It's the most useful thing
> Python can possibly do for you: tell you exactly where it got confused,
> instead of just failing silently."

**Explicitly avoid teaching the full anatomy of a traceback** — stay at
"read the last line, it usually tells you the actual problem in plain
words." Deeper error-reading is a later class's territory (see Section
34).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Does an error mean you broke the computer?" | No — it's normal, expected feedback |
| "What's the fastest way to start understanding an error?" | Read the last line — it usually names the actual problem |

**Transition:** *"Notice what you just did without even thinking about
it: write code, run it, read what happened, fix it, run again. That
cycle has a name."*

---

## 19. The Write–Run–Read–Fix Loop (68–75)

**Name the pattern students have already lived through several times in
the last 30 minutes:**

```
WRITE  →  RUN  →  READ  →  FIX  →  (RUN again)
```

> "This loop is what programming actually *feels* like, day to day — far
> more than any single clever trick. Write some instructions. Run them.
> Read what happened — output, or an error. Fix whatever needs fixing.
> Run again. You've already done this loop four or five times in the
> last half hour without a name for it."

**Say explicitly, an important reassurance:**

> "Nobody writes a perfect program on the first try — not beginners, not
> experienced programmers. The loop *is* the normal way this works, not
> a sign something's going wrong."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What are the steps of this loop, in your own words?" | Write, run, read the result, fix if needed, run again |
| "Is needing to fix something a sign you did it wrong?" | No — it's the normal, expected cycle |

**Transition:** *"Let's put the whole day on one chain — starting all
the way back at Class 01."*

---

## 20. Full Class 01 → Class 05 Bridge (75–82) — NON-NEGOTIABLE, HERO MOMENT

**This is the HERO MOMENT of the class.** Build it live, top to bottom,
one line at a time — never reveal it finished.

1. Write **PROBLEM** — *"Something we're trying to solve."* (Class 01)
2. Arrow down, write **LOGIC** — *"Reasoning about how to solve it."*
   (Class 01)
3. Arrow down, write **ALGORITHM** — *"The plan, as steps a person could
   follow."* (Class 01)
4. Arrow down, write **PYTHON CODE** — *"That same plan, written
   precisely enough for a computer to follow — today's work."*
5. Arrow down, write **RUN** — *"Telling the computer to actually carry
   it out."* (today)
6. Arrow down, write **OUTPUT / RESULT** — *"What the program produces —
   Class 01's RESULT box, now something you can actually see appear on
   screen."*

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
RUN
    ↓
OUTPUT / RESULT
```

**Say explicitly, this is the whole point of the diagram:**

> "The top three lines are exactly Class 01's chain. Today we opened the
> box that used to just say PROGRAM — it's PYTHON CODE, then RUN, then
> the RESULT you can actually watch happen. Nothing about Class 01
> changed. We just finally did it."

**Do not compress this block below 5 minutes**, even under time
pressure — see Section 32.

---

## 21. Interactive Activity — My First Program (82–100) — NON-NEGOTIABLE

**This is the HERO ACTIVITY.** Every student writes and runs an original
multi-line program — no copying the class example verbatim.

### Facilitator instructions (timed, ~18 minutes at canonical pace)

1. **(2 min) Set up:** "Write a short program called 'About Me.' It
   needs: at least **three** `print()` lines, and at least **one**
   comment. It's entirely up to you what it says."
2. **(10 min) Let students write and run independently (or in pairs, if
   sharing a machine).** Circulate constantly — this block only works if
   you are walking the room, not standing at the front. Prompt stuck
   students with: "What are three true things about you a stranger
   couldn't guess?"
3. **(3 min) Deliberately encourage at least one error.** Ask each
   student (or pair) to remove a quote or misspell `print` on purpose,
   run it, read the error together, then put it back. This normalizes
   errors one more time, on their *own* code, which lands differently
   than watching the instructor's.
4. **(3 min) Invite 2–3 students to run their program for the room** (out
   loud is fine — no need to show the screen if that's uncomfortable).
   Celebrate variety: no two "About Me" programs will look the same, and
   that's the point.

### Questions and expected responses

| Question | Expected response |
|---|---|
| "What does your program do, in your own words?" | Displays several lines of text about themselves, in the order written |
| "What happened when you broke it on purpose?" | An error appeared, explaining roughly what was wrong |
| "Did the computer do anything you didn't tell it to?" | No — only exactly what was written |

**Do not introduce new syntax during this activity** (no variables, no
`input()`) — if a student asks for one, use the parking-lot response
(Section 34) and let their program stay simple.

### Timing, extension, and support

- **Canonical timing:** ~18 minutes, per the breakdown above.
- **Stronger-student extension:** Ask them to add a comment above *every*
  `print()` line explaining what it does, or to try printing something
  with a comma inside the parentheses (e.g.
  `print("Score:", 10)`) purely as a curiosity, without formally
  explaining commas or numbers yet.
- **Weaker-student support:** Provide a fill-in-the-blank template:
  `print("Hello, my name is ___.")` / `print("I am ___ years old.")` /
  `print("My favorite ___ is ___.")` — and let them fill in the blanks
  rather than writing from a blank editor.
- **No-computer fallback (see Section 31):** students write their
  program on paper exactly as they would type it, then trade with a
  neighbor and "run" it by hand — reading each line aloud and stating
  what it would output.
- **Transition back to the main lesson:** "You just wrote, ran, broke,
  and fixed a real program — completely on your own. That's the whole
  loop from Section 19, start to finish."

---

## 22. Misconceptions — In-Class Handling (100–105)

Pick 2–3 of the misconceptions most likely to have surfaced already today
(see Section 25 for the full reference table) and address them directly
and briefly. Use this pattern for each: **name it → reframe it → return
to the day's core diagram.**

Suggested priority order for in-class handling:

1. "The computer understands English, it's just picky" (likely surfaced
   around Section 10 or 15).
2. "An error means I did something badly wrong" (very likely surfaced
   during Section 18 or the activity).
3. "The order of the lines doesn't really matter" (worth pre-empting if
   any student reordered lines in the activity without noticing).

Keep this to 5 minutes — this is a quick defusal pass, not a new lecture.

---

## 23. Recap (105–109) — NON-NEGOTIABLE

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last several minutes:

1. **"Why can't we just type plain English at a computer?"** *Expected:*
   a computer doesn't fill in gaps the way a person does — it needs
   precise, unambiguous instructions.
2. **"What does `print(...)` do?"** *Expected:* displays whatever is
   inside the parentheses.
3. **"Why does text need quotes?"** *Expected:* so Python knows exactly
   where the literal text starts and ends.
4. **"If you write five `print()` lines, in what order do they run?"**
   *Expected:* top to bottom, exactly as written.
5. **"What does Python do with a comment?"** *Expected:* ignores it
   completely — it's for humans, not the computer.
6. **"Is getting an error a sign something is badly wrong?"** *Expected:*
   no — it's normal, expected feedback, and part of the write-run-read-
   fix loop.
7. **"How does this connect to Class 01?"** *Expected:*
   `PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT`.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 24. Final Takeaway (109–110)

**Close with the final statement, said slowly:**

> "You didn't just learn about programming today — you did it. Every
> program you will ever write, no matter how large, is built from
> exactly this: precise instructions, run in order, read carefully when
> they go wrong."

**Then leave the bridge-forward question open, explicitly not answered
today:**

> "Right now, every piece of text in your programs is fixed — typed once
> and never changing. What if a program needed to remember something, or
> work with a value that changes? That's exactly where we pick up next
> class."

Do not resolve this — it is intentionally a hook into Class 06
(Variables & Data Types).

---

## 25. Common Misconceptions — Full Reference

For each: **listen for** it, use a **short reframe**, never shame the
student who raised it, and **return to the mental model** rather than
arguing the point in the abstract.

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "The computer understands English, it's just picky about grammar." | Treating Python as "strict English" | "Python isn't English with rules bolted on — it's a different kind of language entirely, built to remove every gap English leaves open." | Section 10 |
| 2 | "Getting an error means I did something badly wrong / broke something." | Visible embarrassment or panic at an error | "An error is Python's most helpful response — it's telling you exactly what it couldn't understand, not judging you." | Section 18 |
| 3 | "`print` and `Print` (or any different capitalization) are the same to Python." | Casual capitalization while typing | "Python is case-sensitive — different capitalization is, to Python, a completely different word." | Section 18 |
| 4 | "The order of the lines doesn't really matter, Python figures out what I meant." | Reordering code without expecting a different result | "Python runs your instructions exactly top to bottom — no reordering, no guessing a 'better' order." | Section 16 |
| 5 | "Comments are extra instructions that also run, just less important ones." | Treating `#` lines as optional-but-executed code | "A comment isn't a lesser instruction — Python doesn't execute it at all. It's invisible to the computer, visible only to people." | Section 17 |

---

## 26. Instructor Language / Teaching Guardrails

**Prefer:**

- "Python runs your instructions exactly as written, top to bottom" —
  **over** "Python is strict."
- "An error is feedback, not a failure" — **over** any language that
  frames an error as something to avoid at all costs.

**Avoid:**

- "Coding is easy, anyone can pick it up in a day" — sets a dismissive
  tone toward students who find the syntax genuinely unfamiliar; prefer
  "coding is learnable, and today is real progress, not the whole
  journey."
- "Just memorize the syntax" — prefer reasoning about *why* the rule
  exists (e.g., quotes mark text boundaries) over rote memorization.

**The instructor must NOT**, at any point in this class:

- introduce variables, assignment, or the `=` operator
- introduce `input()` or any user-interactive program
- introduce `if`/`elif`/`else` or any conditional logic
- introduce `while`/`for` loops
- introduce functions the student defines themselves (`def`)
- introduce lists, dictionaries, or any other data structure
- introduce indentation rules (nothing today requires an indented block)
- introduce f-strings or `.format()` — a comma inside `print()` is the
  only "combining values" trick shown, and only as an optional curiosity
  in the extension (Section 21)
- teach the full anatomy of a Python traceback

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that soon — Class 06 (or the
> relevant later class) is exactly where that lives. Today we're
> planting the very first seed: instructions, run in order, read
> carefully."

Then return to whichever anchor fits the moment:

```
PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT
```

See Section 34 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 27. Interaction Philosophy

Class 05 should be interactive throughout, and unlike Classes 01–04, a
large share of that interaction is **hands-on typing**, not only
discussion — use both deliberately.

**Sample questions to use across the class** (for quick reference):

- "What do you think will happen if I run this — before I run it?"
- "In what order will these lines run?"
- "What changed in the output when I changed the code?"
- "What is this error actually telling us, in plain words?"
- "What's one thing your program does that no one else's does?"

**Prediction-before-running is the single most valuable habit this class
can install.** Ask "what do you think will happen?" before every run,
every single time, even when the answer feels obvious — it is what turns
typing into reasoning.

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 8–12 seconds for the two hardest reasoning
moments — the opening mystery (Section 8) and reading the first error
message aloud together (Section 18). Do not rescue students from
uncertainty too early on these.

**Built-in reasoning opportunities to protect, in priority order:**

1. Predicting output before every run (Sections 13, 14, 16)
2. Predicting what breaking the quotes will do (Section 15)
3. Reading the first error message together, unhurried (Section 18)
4. The Class 01 → Class 05 bridge reconstruction (Section 20, 23)
5. Every individual choice a student makes in their own "About Me"
   program (Section 21)

---

## 28. Visual / Board Plan

These are the key drawings later Pen-Tablet and Presentation artifacts
will build on. Do not create those artifacts now — this section only
specifies what they must contain. Unlike Classes 01–04, most of this
class's "board" is the **live screen**, not a whiteboard drawing — call
that out explicitly below.

**Screen 1 — The Editor/Output Split**
Shown live in Section 12. Two labeled regions: "EDITOR (you type here)"
and "OUTPUT (you see results here)."

**Screen 2 — First print() Line**
Typed live in Section 13, run in Section 14.
`print("Hello, World!")` → output: `Hello, World!`

**Screen 3 — Broken Quotes**
Broken live in Section 15. `print(Hello, World!)` → an error appears.

**Screen 4 — Three Lines, In Order**
Built live in Section 16. Three `print()` lines, output appearing in the
same order.

**Screen 5 — Comments**
Typed live in Section 17. A `#` comment line plus an inline `#` comment,
with output showing the comments produced nothing.

**Screen 6 — Two Errors, Read Aloud**
Broken live in Section 18. A missing-quote `SyntaxError`, then a
wrong-capitalization `NameError`.

**Drawing 1 — Write–Run–Read–Fix Loop**
Built live in Section 19, on the whiteboard (the one non-screen drawing
before the hero diagram).

```
WRITE → RUN → READ → FIX → (RUN again)
```

**Drawing 2 — HERO — Full Bridge**
Reserved for Section 20, whiteboard.

```
PROBLEM
    ↓
LOGIC
    ↓
ALGORITHM
    ↓
PYTHON CODE
    ↓
RUN
    ↓
OUTPUT / RESULT
```

Mark this as a **live construction** — do not show the completed
six-line chain before students have reasoned their way to each new piece
across the class. This is the single most important drawing of Class 05,
the same way the hero drawing anchored every prior class.

Keep every diagram simple — no IDE screenshots beyond what's actually
live on screen, no invented syntax not covered in this guide.

---

## 29. Class 01–05 Continuity

Explicitly narrate where Class 05 sits in the course staircase — this
prevents students from experiencing each class as an unrelated topic, and
matters even more here since this is the first class in a new block.

**Class 1:**

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**Class 2:**

```
DATA → LEARNING → MODEL → PREDICTION
```

**Class 3:**

```
REAL WORLD → OBSERVATION → DATA
DATA → EXAMPLES → FEATURES → LABELS → DATASET
```

**Class 4:**

```
DATA → REPRESENTATION → BITS
```

**Class 5:**

Opens the **PROGRAM** box from Class 01's chain for the first time —
`ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT`.

**Say this once, clearly (Section 9 or Section 20 are the natural
spots):**

> "We are not starting a new course. We're opening a box that's been
> sitting on the board, unopened, since Class 01. Everything from here
> through Class 14 is about filling in that PROGRAM box, one idea at a
> time."

This is the same continuity statement pattern used in Classes 02–04 — it
is what turns five separate classes into one staircase instead of five
unrelated topics, and it explicitly frames the whole of Block 1 (Classes
05–14) as one long elaboration of a single Class 01 box.

---

## 30. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks throughout the class, and rely heavily on the hands-on
activity (Section 21) as the strongest real-time signal, more so than in
any prior class.

A student is demonstrating real understanding if they can:

1. Write a working `print()` statement with their own text.
2. Explain why the text needs quotes.
3. Correctly predict the output order of several `print()` lines before
   running them.
4. Write a comment and explain that Python ignores it.
5. Read a simple error message and describe, in plain words, roughly
   what it's complaining about — without distress.
6. Explain the write-run-read-fix loop in their own words.
7. Connect today's work back to Class 01's `PROGRAM` box.

**Do not** judge understanding solely from a student successfully copying
the instructor's exact example — the "About Me" activity (Section 21),
where students write original lines and deliberately break their own
code, is the strongest evidence in this class of real understanding
rather than pattern-copying.

---

## 31. Differentiation

**For students struggling:** Anchor entirely in the fill-in-the-blank
template from Section 21 rather than a blank editor, and slow the
existing progression down rather than introducing a different
explanation:

```
type it  →  predict the output  →  run it  →  compare
```

Walk this exact loop with them on one line at a time before asking them
to write a second line independently.

**For students moving quickly:** Let them extend the activity (Section
21's stronger-student extension) — a comment above every line, or a
curious peek at `print()` with a comma and a number. Do **not** teach
variables, `input()`, or any new syntax even for fast movers — deepen
*fluency* with what's covered today, not scope. See Section 33 for the
full extended-version guidance.

**For students who stay quiet:** The "About Me" activity (Section 21) is
naturally low-stakes and highly personal — most quiet students engage
more freely here than in a discussion-only class, because there's no
risk of a publicly "wrong" spoken answer. Circulate and read their screen
rather than calling on them verbally.

**No-computer fallback (if hardware genuinely cannot be guaranteed for
every student):** Run Sections 8–20 exactly as written using only the
instructor's live screen — every student watches, predicts, and reasons
aloud, just without typing themselves. For Section 21, have every student
write their "About Me" program on paper, in the exact syntax they'd type,
then trade papers with a neighbor and "run" the program by hand — reading
each line aloud in order and stating what it would output, including a
deliberately "broken" line to trace through as a paper error. This
preserves the write-run-read-fix loop conceptually even without hardware,
though it is a genuine downgrade — flag it to a coordinator so hardware
access is fixed before Class 06, where hands-on typing matters even more.

---

## 32. Time Management / Timing Safety

**Must cover, in priority order** (matches the non-negotiable list in
Section 7):

1. Writing and running a working `print()` (Sections 13–14)
2. Multiple instructions running in order (Section 16)
3. Comments (Section 17)
4. Reading a simple error calmly (Section 18)
5. The full Class 01 → Class 05 bridge (Section 20)
6. The "About Me" hands-on activity (Section 21)

**Can shorten:**

- The opening mystery (Section 8) — compress to one quick example instead
  of two
- Meet Python (Section 11) — a single sentence is enough if time is tight
- The write-run-read-fix loop naming (Section 19) — can be folded into
  the transition out of Section 18 instead of its own block
- The misconception discussion (Section 22) — pick just one instead of
  2–3

**Can expand** (see Section 33 for detail):

- Let stronger students explore the comma-inside-`print()` curiosity
  further during the activity
- Run a second round of "break it on purpose" in Section 18 with a
  student-suggested mistake
- Spend more time circulating during the activity (Section 21) if the
  room is large or setups are uneven

**Do not cut:** the hands-on typing in Sections 13–14 (every student must
personally run a program), the "About Me" activity (Section 21), or the
Class 01 bridge (Section 20) — these are the load-bearing walls of the
entire class, and unlike prior classes, cutting the hands-on portions
here defeats the class's entire purpose.

### 90-minute version

Trim as follows: Opening Mystery to 4 min, Class 01 Callback to 4 min,
What Is a Programming Language? to 4 min, Meet Python to 3 min, Setup
unchanged (4 min), Your First Line unchanged (8 min), Running the Program
to 5 min, Strings Need Quotes to 4 min, Multiple Instructions unchanged
(7 min), Comments to 5 min, Errors unchanged (8 min), Write-Run-Read-Fix
Loop folded into Errors' transition (0 min separately), Full Bridge to 6
min, Activity compressed to 14 min, Misconceptions to 3 min, Recap to 3
min, Final Takeaway unchanged (1 min). Total ≈ 83 minutes, leaving a
buffer for setup issues.

### 120-minute version

Add time back to: What Is a Programming Language? (+2 min, let students
generate their own "vague instruction" examples), Strings Need Quotes (+2
min, try a second broken example students suggest), Errors (+2 min, a
third student-suggested mistake), Activity (+4 min, let every student who
wants to present their program to the room).

---

## 33. Extended Version

If time allows, deepen fluency — do **not** introduce any new technical
scope beyond `print()`, comments, and reading simple errors.

- Let students try `print()` with a comma and a second value purely as a
  curiosity (e.g. `print("Score:", 10)`), without formally naming what a
  comma does yet — that belongs to later classes.
- Ask stronger students to write a five- or six-line "About Me" program
  with a comment above every single line, explaining their own code as
  if to someone who has never seen it.
- Run a second "break it on purpose" round in Section 18, using a mistake
  a student suggests rather than the instructor's two prepared examples —
  this builds the read-the-error habit on genuinely novel input.
- Ask students to predict, before you run it, what would happen if two
  `print()` lines used mismatched quote types (e.g. `print('Hello")`) —
  then confirm live.

---

## 34. Advanced Topics Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "How do I store a value so I can use it again?" | "That's a variable — a real and very useful idea, coming next class." | "Today's building block is the instruction itself." |
| "How do I ask the user to type something in?" | "That's `input()` — real, and coming in a few classes." | Return to: `WRITE → RUN → READ → FIX`. |
| "How do I make the program choose between two things?" | "That's `if`/`else` — real conditional logic, a later class's territory." | Return to: instructions run top to bottom, no branching yet. |
| "How do I make something repeat without retyping it?" | "That's a loop — a real and powerful idea, coming soon." | Same as above. |
| "Can I make my own function like `print()`?" | "Yes, eventually — writing your own reusable instructions is `def`, a later class." | Return to: `print()` is one function Python already built for us. |
| "What's a list / how do I store many things?" | "A real and useful structure — a later class's territory." | Return to: today is about single lines of text. |
| "Why do some errors say 'SyntaxError' and others say something else?" | "Different error types describe different kinds of mistakes — real, but not today's focus; today, just read the last line." | Return to: errors are normal, readable feedback. |
| "Can I combine text and a comment on one line?" | "Yes — that's the inline comment you just saw in Section 17's second example." | Answer directly; this one is in scope. |
| "What if I want the text to include a quote mark itself?" | "There's a way (escaping, or mixing quote types) — real, but a level of polish for a later class." | Return to: quotes mark where text starts and ends. |

---

## 35. Teacher FAQ

**Q: What if a student's setup won't run at all?**
A: Pair them with a neighbor immediately rather than troubleshooting
solo in front of the room — see Section 12. Flag hardware/software
access issues to a coordinator before Class 06.

**Q: Should I explain what a "function" formally is when I introduce
`print()`?**
A: No — say "print is a built-in instruction; the parentheses hold what
to do something with" and move on. The formal idea of a function is
Class 11's job.

**Q: A student asked about variables/input()/loops — did I do something
wrong by not covering it?**
A: No — that's the parking lot working exactly as intended (Section 34).
Curiosity ahead of the curriculum is a good sign, not a gap to fill
today.

**Q: What if a student's program "works" but doesn't do what they
described?**
A: That's a genuinely great teaching moment — walk through their code
line by line together and let them find the mismatch themselves before
you point it out. This is the write-run-read-fix loop in action.

**Q: Is it okay if some students finish the activity early?**
A: Yes — use the stronger-student extension in Section 21 (comment every
line, try a comma inside `print()`). Do not let early finishers pull you
into teaching new syntax to the whole room ahead of schedule.

**Q: What if I only have 90 minutes, not 110?**
A: Use the 90-minute version in Section 32 — it preserves every
non-negotiable block and only trims discussion time and the size of the
activity.

**Q: A student asked "is Python better than [other language]?" — how do
I handle it?**
A: Briefly: "Different languages suit different jobs — Python isn't
'the best,' it's a great one to start with because it's readable." Then
return to the lesson; a language-comparison debate is out of scope today.

---

## 36. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Explain why a computer needs precise, unambiguous instructions rather
   than plain English.
2. Write and run a `print()` statement that displays their own text.
3. Explain why the text inside `print()` needs quotes.
4. Write several `print()` statements and correctly predict that they
   run in order, top to bottom.
5. Write a comment with `#` and explain that Python ignores it.
6. Read a simple syntax error without panic and describe, roughly, what
   it's complaining about.
7. Reconnect today's work to Class 01's `PROGRAM` box, restating the
   bridged chain `PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → RUN →
   OUTPUT/RESULT`.

A class where most students can do these in plain, imperfect language —
and where every student has personally run at least one working program —
has met the bar.

---

## 37. Source-of-Truth / QA Checklist

Verified against the Foundation Batch 2026 curriculum plan (Block 1,
`C05`) before finalizing this guide:

- [x] Class 01–04 continuity is explicit (Sections 3, 9, 20, 29).
- [x] The class starts with intuition, not syntax (Section 8).
- [x] Every student writes and runs real code, not just watches
      (Sections 13, 14, 21).
- [x] `print()` is introduced clearly and only after the "why precise
      instructions" intuition is built (Section 13).
- [x] Quotes are explained by breaking them on purpose, not just stated
      as a rule (Section 15).
- [x] Sequencing (top-to-bottom execution) is explicitly tied back to
      Class 01's ALGORITHM concept (Section 16).
- [x] Comments are introduced with a live demonstration that they
      produce no output (Section 17).
- [x] A first error is shown deliberately, in a safe moment, before any
      student hits one by accident (Section 18).
- [x] No variables, `input()`, conditionals, loops, user-defined
      functions, lists, dictionaries, indentation rules, or string
      formatting are taught (Section 1, Section 26, guarded throughout).
- [x] Misconceptions are explicitly handled, both in-flow (Section 22)
      and as a full reference (Section 25).
- [x] The "About Me" hands-on activity reinforces writing, running, and
      calmly breaking/fixing original code (Section 21).
- [x] A no-computer fallback exists for rooms without guaranteed
      hardware access (Section 31).
- [x] The class remains appropriate for first-year students with zero
      assumed programming background (Section 1, Section 31).
- [x] The class has a clear, explicit, unresolved bridge to Class 06
      (Variables & Data Types) (Section 24, Section 34).
- [x] This Master Guide is self-contained and usable by an instructor
      without relying on the Student Notes — every section includes
      instructor wording, questions, expected answers, and transitions.
