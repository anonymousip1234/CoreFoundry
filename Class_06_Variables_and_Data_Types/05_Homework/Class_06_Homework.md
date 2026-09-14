# Class 06 — Homework

**Bong Study Hub — Foundation Batch 2026 · Class 06: Variables & Data
Types**
*Giving Values a Label That Can Change*

**Estimated time:** 30–45 minutes
**Total:** 30 marks  ·  **Optional Challenge:** up to 3 bonus marks
**Tools needed:** pen and paper, or a simple document. A computer with
Python is helpful for checking your work, but not required to answer any
question.
**Prerequisite:** Classes 05 and 06. No arithmetic operators, `input()`,
loops, or conditionals are needed anywhere in this assignment.

---

## What This Assignment Is About

In class, we answered a question Class 05 left open: how does a program
hold onto something that changes? We met the **variable** — a named,
changeable place to store a value — created variables with `=`, learned
that `=` means "store" and not mathematical equality, saw why
`print(name)` and `print("name")` produce completely different output,
watched reassignment completely replace an old value, and met four data
types: `int`, `float`, `str`, and `bool`.

This assignment asks you to **read and trace code, not just recall
facts about it**. Several questions give you a snippet of Python and ask
what it does, exactly like the write-run-read-fix loop from Class 05,
just on paper.

---

## Instructions

- **Answer in your own words** where a question asks for an explanation.
- For "predict the output" or "trace the code" questions, write the
  **exact** text Python would display, in order.
- **No arithmetic operators, `input()`, conditionals, or loops appear
  anywhere in this homework** — if your answer to any question involves
  one of those, simplify it back down to variables, assignment, and
  `print()`.
- You may refer to your **Student Notes** while answering.
- If you're unsure, **explain your reasoning anyway** rather than
  leaving a blank — partial thinking is worth more than an empty space.

---

## Section A — Core Concepts

### Question 1 — Why Variables? (2 marks)

In your own words, explain **why Class 05's fixed, typed-once text
wasn't enough for something like a scoreboard that changes during a
game.**

<!-- BLANK:3 -->

---

### Question 2 — What Is a Variable? (2 marks)

In your own words, **explain what a variable is**, using the labeled-box
idea from class if it helps.

<!-- BLANK:2 -->

---

### Question 3 — Assignment vs. Equals (2 marks)

**Explain why `=` in Python is not the same as the `=` you use in math
class.**

<!-- BLANK:3 -->

---

### Question 4 — Variables in print() (2 marks)

**Explain the difference** between what `print(city)` and `print("city")`
would each display, assuming `city` is a variable that holds the value
`"Kolkata"`.

<!-- BLANK:3 -->

---

### Question 5 — The Four Data Types (2 marks)

**Name the four data types covered in class**, and give one example
value of each.

<!-- BLANK:4 -->

---

## Section B — Reading and Reasoning About Code

### Question 6 — Predict the Output (3 marks)

```
name = "Rohan"
score = 42
print("Player:", name)
print("Score:", score)
```

**Write the exact output**, line by line, in the order it would appear.

<!-- BLANK:3 -->

---

### Question 7 — Find the Bug (3 marks)

A student wanted to print the value stored in `city`, but got this
output instead of the city's name:

```
city = "Kolkata"
print("city")
```

Output:
```
city
```

**What's wrong with the second line?** Rewrite it so it correctly
displays the value stored in `city`.

<!-- BLANK:3 -->

---

### Question 8 — Reassignment Trace (3 marks)

```
temperature = 20
print(temperature)
temperature = 25
print(temperature)
temperature = 18
print(temperature)
```

**Write the exact output**, in order, and explain in one sentence what
happened to each earlier value once the next line reassigned
`temperature`.

<!-- BLANK:4 -->

---

### Question 9 — Identify the Data Type (3 marks)

For each value below, **write whether it is an `int`, a `float`, a
`str`, or a `bool`:**

| Value | Data type |
|---|---|
| `42` | |
| `3.14` | |
| `"hello"` | |
| `True` | |
| `"True"` | |
| `0.0` | |

<!-- BLANK:2 -->

---

### Question 10 — Fix the Variable Name (3 marks)

Each of these variable names has a problem. **Identify what's wrong with
each one, and rewrite it as a valid variable name:**

```
1st_place = "Aisha"
student age = 20
class = "Foundation Batch"
```

<!-- BLANK:5 -->

---

## Section C — Class Connection & Your Own Program

### Question 11 — Connecting Class 04 and Class 06 (2 marks)

Fill in the blank below, using ideas from today's class:

```
INFORMATION
    ↓
REPRESENTATION   (Class 04)
    ↓
BITS   (Class 04)
    ↓
________________   (Class 06)
```

Briefly explain, in one sentence, **what a variable gives you that raw
bits don't.**

<!-- BLANK:2 -->

---

### Question 12 — Write Your Own Variable Profile Card (3 marks)

**Write a short program** (on paper is fine) with **at least four
variables** — one string, one integer, one float, and one boolean —
describing a person, animal, or character of your choice. Then write at
least two `print()` lines that combine literal text and variables using
commas.

<!-- BLANK:8 -->

---

## Optional Challenge — Bonus (up to 3 marks)

**This section is entirely optional** and will not affect your base
grade.

Trace the program below very carefully — it reassigns some variables and
leaves others untouched. **Write the exact output**, in order.

```
name = "Meera"
score = 10
is_winner = False

print(name, "starts with a score of", score)

score = 10
score = 30
is_winner = True

print(name, "now has a score of", score)
print("Is", name, "the winner?", is_winner)

name = "Meera R."
print(name, "is the final name on record.")
```

<!-- BLANK:6 -->

---

## Submission Format

Choose whichever is easiest for you:

- **Option A:** Handwrite your answers, then photograph or scan them.
- **Option B:** Type your answers in a simple document.
- **Option C:** Submit as a simple PDF.

Please label each answer with its question number.

---

## Before You Submit — Self-Check

- [ ] I answered all 12 questions.
- [ ] For every "predict the output" or "trace the code" question, I
      wrote the exact text, in the exact order.
- [ ] Where unsure, I explained my reasoning instead of leaving a blank.
- [ ] I did not use arithmetic operators, `input()`, conditionals, or
      loops anywhere.
- [ ] I reviewed my work before submitting.

<!-- ANSWER KEY BELOW THIS LINE — INSTRUCTOR USE ONLY. DO NOT INCLUDE IN THE STUDENT-FACING PDF. -->

---

# Instructor Answer Key — Do Not Distribute to Students

**Source of truth:** Class_06_Master_Instructor_Guide.md. This key gives
concise expected concepts, not model essays — reward reasoning that fits
the concept over exact wording throughout.

## Marking Guide (30 marks + 3 optional bonus)

| Section | Question | Marks |
|---|---|---|
| A | Q1 — Why Variables? | 2 |
| A | Q2 — What Is a Variable? | 2 |
| A | Q3 — Assignment vs. Equals | 2 |
| A | Q4 — Variables in print() | 2 |
| A | Q5 — The Four Data Types | 2 |
| B | Q6 — Predict the Output | 3 |
| B | Q7 — Find the Bug | 3 |
| B | Q8 — Reassignment Trace | 3 |
| B | Q9 — Identify the Data Type | 3 |
| B | Q10 — Fix the Variable Name | 3 |
| C | Q11 — Connecting Class 04 and Class 06 | 2 |
| C | Q12 — Write Your Own Variable Profile Card | 3 |
| | **Total** | **30** |
| | Optional Challenge | +3 bonus |

## Marking Principles

- Reward conceptual understanding, not exact wording — accept plainer or
  simpler language freely.
- For "predict the output" / "trace the code" questions (Q6, Q8,
  Optional Challenge), the output text must match **exactly**, including
  capitalization and punctuation as written in the `print()` calls — but
  do not penalize minor spacing differences in the student's
  handwriting/typing of their answer.
- For Q12 (an open-ended original program), **accept any coherent
  four-variable program** covering all four data types — do not require
  a specific topic or wording.
- A student who can recite "a variable can change" but cannot correctly
  trace Q6/Q8/the Optional Challenge should visibly struggle on those
  questions — that gap is the point of this homework's Section B.
- Do not penalize simpler language or shorter phrasing than the key
  below.

## Answers

**Q1 — Why Variables? (2 marks)**
Fixed text can only ever show the exact same thing every time the
program runs — updating it means editing the code and running it again,
which isn't practical for something that changes many times, like a
live scoreboard. (1 mark for stating fixed text can't change without
editing code; 1 mark for connecting this to why that's impractical for
something that changes often.)

**Q2 — What Is a Variable? (2 marks)**
A variable is a named place to store a value, where the value can be
changed later — like a labeled box whose contents can be swapped out
while keeping the same label. Full credit for any phrasing capturing
"named/labeled" plus "can change."

**Q3 — Assignment vs. Equals (2 marks)**
In math, `=` means both sides are permanently the same. In Python, `=`
means "store this value under this name" — a one-time instruction, not
a lasting equation. This is why a variable can be reassigned to a
completely different value later without contradiction. (1 mark for
identifying `=` as "store," not "equals"; 1 mark for explaining why that
matters, e.g. reassignment wouldn't make sense otherwise.)

**Q4 — Variables in print() (2 marks)**
`print(city)` displays the value stored in the variable `city` —
`Kolkata`. `print("city")` displays the literal text `city`, because the
quotes mark it as literal text rather than a variable reference. Full
credit requires the student to correctly state both outputs and connect
the difference to the presence/absence of quotes.

**Q5 — The Four Data Types (2 marks)**
`int` (e.g. `18`), `float` (e.g. `3.14`), `str` (e.g. `"hello"`), `bool`
(e.g. `True`). Accept any correct example value per type. (0.5 marks per
correctly named and exemplified type, rounded to nearest 0.5 or 1 as
your grading scale allows.)

**Q6 — Predict the Output (3 marks)**
```
Player: Rohan
Score: 42
```
Full credit requires the exact text, in the exact order, matching
capitalization. (1.5 marks per correct line.)

**Q7 — Find the Bug (3 marks)**
The second line has `city` in quotes, so Python treats it as literal
text instead of looking up the variable's stored value. Corrected line:
```
print(city)
```
(1 mark for identifying the quotes as the issue; 2 marks for the correct
rewritten line.)

**Q8 — Reassignment Trace (3 marks)**
```
20
25
18
```
Each earlier value is completely replaced/overwritten the moment the
next line reassigns `temperature` — nothing is kept or remembered. (1.5
marks for the correct three-line output; 1.5 marks for a sound
explanation of replacement.)

**Q9 — Identify the Data Type (3 marks)**
`42` → int; `3.14` → float; `"hello"` → str; `True` → bool; `"True"` →
str (it's in quotes, so it's just text, not a boolean); `0.0` → float
(it has a decimal point, even though its value is zero). Full credit
requires all six correct, with particular attention to `"True"` being
str, not bool — that's the row testing real understanding. (0.5 marks
per correct row.)

**Q10 — Fix the Variable Name (3 marks)**
`1st_place` is invalid because it starts with a digit — e.g.
`first_place` fixes it. `student age` is invalid because it contains a
space — e.g. `student_age` fixes it. `class` is invalid because it's a
reserved Python keyword — e.g. `class_name` or `batch_name` fixes it.
(1 mark per correctly identified problem and valid fix.)

**Q11 — Connecting Class 04 and Class 06 (2 marks)**
Blank = **VARIABLE** (or "a variable, a human-readable label for it").
The one-sentence explanation should convey that a variable gives you a
meaningful, readable name for stored information, so you never have to
think about or manage the underlying bits directly.

**Q12 — Write Your Own Variable Profile Card (3 marks)**
Accept any coherent program with at least four variables covering all
four data types (`int`, `float`, `str`, `bool`), on any subject the
student chooses, plus at least two `print()` lines combining literal
text and variables with commas. Check for: (1) all four data types are
present and correctly formed (e.g. boolean values are `True`/`False`,
unquoted), (2) at least two `print()` lines use commas to mix text and
variables. (1 mark for correct variables/types; 2 marks for correct
combined `print()` lines.)

**Optional Challenge (up to 3 bonus marks)**
```
Meera starts with a score of 10
Meera now has a score of 30
Is Meera the winner? True
Meera R. is the final name on record.
```
Key reasoning points: the first `score = 10` (repeated) changes nothing
visible; `score = 30` is what actually shows in the second print; the
`name` reassignment to `"Meera R."` only affects the print statement
that comes after it — the earlier print statements already used the
older value of `name` before it changed. 1 mark for the correct first
line, 1 mark for correctly tracking the score's reassignment, 1 mark for
correctly tracking that `name` only changes for the final line.

<!-- ANSWER KEY ABOVE THIS LINE -->
