# Class 07 — Homework

**Bong Study Hub — Foundation Batch 2026 · Class 07: Operators &
Expressions**
*Class 01's LOGIC, Made Literal*

**Estimated time:** 30–45 minutes
**Total:** 30 marks  ·  **Optional Challenge:** up to 3 bonus marks
**Tools needed:** pen and paper, or a simple document. A computer with
Python is helpful for checking your work, but not required to answer any
question.
**Prerequisite:** Classes 05, 06, and 07. No `if`, `input()`, loops, or
compound assignment (`+=`) are needed anywhere in this assignment.

---

## What This Assignment Is About

In class, we built the toolkit that turns Class 01's abstract `LOGIC`
box into real code: **arithmetic operators** (`+ - * / // %`) that
compute, **comparison operators** (`== != < > <= >=`) that ask
true/false questions and produce booleans, and **logical operators**
(`and`, `or`, `not`) that combine those booleans. We also met the single
most common beginner trap: confusing `=` (store) with `==` (ask).

This assignment asks you to **trace code carefully, not just recall
facts about it**. Several questions give you an expression or a short
program and ask exactly what it produces — order of operations and the
`=`/`==` distinction both reward careful, patient reading.

---

## Instructions

- **Answer in your own words** where a question asks for an explanation.
- For "predict the result" or "trace the code" questions, write the
  **exact** value(s) Python would produce, including `True`/`False`
  capitalized exactly as Python writes them.
- **No `if`, `input()`, loops, or `+=` appear anywhere in this
  homework** — if your answer to any question involves one of those,
  simplify it back down to operators and expressions.
- You may refer to your **Student Notes** while answering.
- If you're unsure, **explain your reasoning anyway** rather than
  leaving a blank — partial thinking is worth more than an empty space.

---

## Section A — Core Concepts

### Question 1 — What Is an Operator? (2 marks)

In your own words, **explain what an operator is**, and what the word
**"operand"** means.

<!-- BLANK:3 -->

---

### Question 2 — / vs // (2 marks)

**Explain the difference** between `/` and `//` in Python, using one
short example of each.

<!-- BLANK:3 -->

---

### Question 3 — What Does % Give You? (2 marks)

In your own words, **explain what the `%` operator produces**, with one
example.

<!-- BLANK:2 -->

---

### Question 4 — Comparisons and Data Types (2 marks)

**What data type does every comparison operator (`== != < > <= >=`)
always produce?** Explain how this connects to Class 06.

<!-- BLANK:2 -->

---

### Question 5 — = vs == (2 marks)

**Explain the difference** between `=` and `==` in Python. Why is
mixing them up such a common — and risky — mistake?

<!-- BLANK:3 -->

---

## Section B — Reading and Reasoning About Code

### Question 6 — Predict the Output (3 marks)

```
a = 12
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

**Write the exact output**, line by line, in order.

<!-- BLANK:4 -->

---

### Question 7 — Order of Operations (3 marks)

```
print(3 + 4 * 2)
print((3 + 4) * 2)
```

**Write the exact output** of both lines, and explain in one sentence
why they differ.

<!-- BLANK:3 -->

---

### Question 8 — Predict the Comparisons (3 marks)

```
x = 10
print(x == 10)
print(x != 5)
print(x < 5)
print(x >= 10)
```

**Write the exact output**, line by line, in order.

<!-- BLANK:4 -->

---

### Question 9 — Predict the Logical Results (3 marks)

```
p = True
q = False
print(p and q)
print(p or q)
print(not q)
```

**Write the exact output**, line by line, in order.

<!-- BLANK:3 -->

---

### Question 10 — Find the Bug (3 marks)

A student wanted to check whether `age` equals `18` and store the
true/false answer in `result`. Here is what they actually wrote:

```
age = 18
result = age = 18
print(result)
```

**What does this actually print?** (Hint: it will not crash — that's
what makes this bug dangerous.) **What did the student probably mean to
write instead**, and what would that corrected version print?

<!-- BLANK:4 -->

---

## Section C — Class Connection & Your Own Program

### Question 11 — Connecting Class 01 and Class 07 (2 marks)

Fill in the blank below, using ideas from today's class:

```
LOGIC   (Class 01)
    ↓
________________   (Class 07)
```

Briefly explain, in one sentence, **how today's operators make Class
01's `LOGIC` box literal.**

<!-- BLANK:2 -->

---

### Question 12 — Write Your Own Expressions (3 marks)

Imagine you're planning a small trip. **Write a short program** (on
paper is fine) with:

- At least **two number variables** (e.g. a budget and a cost).
- **One arithmetic expression** combining them (e.g. money left over).
- **One comparison** that produces a boolean (e.g. whether you're within
  budget).
- **One logical expression** combining two comparisons (e.g. whether the
  trip is both affordable and long enough).

Print each result.

<!-- BLANK:8 -->

---

## Optional Challenge — Bonus (up to 3 marks)

**This section is entirely optional** and will not affect your base
grade.

Trace the program below very carefully — it combines arithmetic, order
of operations, comparison, and logical operators. **Write the exact
output**, in order.

```
a = 17
b = 5
c = 2

result1 = a // b + c * 2
result2 = a % b == 2
result3 = result2 and (result1 > 5)

print(result1)
print(result2)
print(result3)
```

<!-- BLANK:5 -->

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
      wrote the exact value(s), including `True`/`False` capitalized
      correctly.
- [ ] Where unsure, I explained my reasoning instead of leaving a blank.
- [ ] I did not use `if`, `input()`, loops, or `+=` anywhere.
- [ ] I reviewed my work before submitting.

<!-- ANSWER KEY BELOW THIS LINE — INSTRUCTOR USE ONLY. DO NOT INCLUDE IN THE STUDENT-FACING PDF. -->

---

# Instructor Answer Key — Do Not Distribute to Students

**Source of truth:** Class_07_Master_Instructor_Guide.md. This key gives
concise expected concepts, not model essays — reward reasoning that fits
the concept over exact wording throughout.

## Marking Guide (30 marks + 3 optional bonus)

| Section | Question | Marks |
|---|---|---|
| A | Q1 — What Is an Operator? | 2 |
| A | Q2 — / vs // | 2 |
| A | Q3 — What Does % Give You? | 2 |
| A | Q4 — Comparisons and Data Types | 2 |
| A | Q5 — = vs == | 2 |
| B | Q6 — Predict the Output | 3 |
| B | Q7 — Order of Operations | 3 |
| B | Q8 — Predict the Comparisons | 3 |
| B | Q9 — Predict the Logical Results | 3 |
| B | Q10 — Find the Bug | 3 |
| C | Q11 — Connecting Class 01 and Class 07 | 2 |
| C | Q12 — Write Your Own Expressions | 3 |
| | **Total** | **30** |
| | Optional Challenge | +3 bonus |

## Marking Principles

- Reward conceptual understanding, not exact wording — accept plainer or
  simpler language freely.
- For "predict the output" / "trace the code" questions (Q6–Q9,
  Optional Challenge), values must match **exactly**, including
  `True`/`False` capitalized correctly — but do not penalize minor
  spacing differences in the student's handwriting/typing of their
  answer.
- For Q12 (an open-ended original program), **accept any coherent
  program** meeting the stated requirements — do not require a specific
  topic or wording.
- A student who can recite "`==` compares" but cannot correctly trace
  Q6–Q9 or Q10 should visibly struggle on those questions — that gap is
  the point of this homework's Section B.
- Do not penalize simpler language or shorter phrasing than the key
  below.

## Answers

**Q1 — What Is an Operator? (2 marks)**
An operator is a symbol that does something with one or more values,
producing a new value. The values it acts on are called operands. (1
mark for defining operator; 1 mark for correctly defining operand.)

**Q2 — / vs // (2 marks)**
`/` always produces a float result, even when the division is exact
(e.g. `10 / 2` gives `5.0`). `//` performs floor division — it divides
and keeps only the whole-number part, dropping anything after the
decimal point (e.g. `9 // 2` gives `4`). Full credit requires a correct
example of each.

**Q3 — What Does % Give You? (2 marks)**
`%` (modulus) gives the remainder left over after division — e.g.
`9 % 2` gives `1`, because `9` is `4` groups of `2` with `1` left over.
Accept any correct example.

**Q4 — Comparisons and Data Types (2 marks)**
Every comparison produces a **boolean** (`True` or `False`). This
connects to Class 06 because `bool` was one of the four data types
introduced there — comparison operators are where booleans actually come
from in a running program. (1 mark for "boolean"; 1 mark for the Class
06 connection.)

**Q5 — = vs == (2 marks)**
`=` stores a value in a variable (assignment). `==` asks whether two
values are equal, producing a boolean (comparison). They look almost
identical but do completely different things — mixing them up is risky
because, as Q10 shows, Python often doesn't crash when you use `=` where
you meant `==`; it just silently does the wrong thing. (1 mark for the
correct distinction; 1 mark for a sound explanation of the risk.)

**Q6 — Predict the Output (3 marks)**
```
17
7
60
2.4
```
Full credit requires all four values exactly correct. (0.75 marks per
line, or equivalent partial credit per your grading scale.)

**Q7 — Order of Operations (3 marks)**
```
11
14
```
The first line computes `4 * 2` (= `8`) before adding `3`, giving `11`.
The second line's parentheses force `3 + 4` (= `7`) to happen first,
then multiply by `2`, giving `14`. (1 mark per correct value; 1 mark for
the explanation.)

**Q8 — Predict the Comparisons (3 marks)**
```
True
True
False
True
```
Full credit requires all four values exactly correct, capitalized as
Python writes them. (0.75 marks per line.)

**Q9 — Predict the Logical Results (3 marks)**
```
False
True
True
```
`p and q` is `False` because `q` is `False` (both must be true for
`and`). `p or q` is `True` because at least one side (`p`) is true.
`not q` flips `False` to `True`. (1 mark per correct line.)

**Q10 — Find the Bug (3 marks)**
This prints `18`, not a boolean. `result = age = 18` is a **chained
assignment** — it sets both `age` and `result` to `18` — it does not
compare anything, even though it looks similar to a comparison. The
student almost certainly meant to write `result = age == 18`, which
would correctly print `True`. Full credit requires: (1) correctly
identifying the actual printed value (`18`); (2) recognizing this as a
silent bug, not a crash; (3) the correct intended fix and its output
(`True`).

**Q11 — Connecting Class 01 and Class 07 (2 marks)**
Blank = **OPERATORS & EXPRESSIONS** (or equivalent wording). The
one-sentence explanation should convey that arithmetic, comparison, and
logical operators are what "reasoning about how to solve a problem"
actually looks like once it's written as real, precise code.

**Q12 — Write Your Own Expressions (3 marks)**
Accept any coherent program with at least two number variables, one
arithmetic expression, one comparison producing a boolean, and one
logical expression combining two comparisons, on any trip-planning
scenario the student chooses. Check for: (1) the arithmetic expression
correctly uses the two number variables, (2) the comparison is
syntactically valid and produces a boolean, (3) the logical expression
correctly combines two comparisons with `and`/`or`/`not`. (1 mark per
correctly formed category.)

**Optional Challenge (up to 3 bonus marks)**
```
7
True
True
```
Trace: `a // b` = `17 // 5` = `3`; `c * 2` = `4`; `result1` = `3 + 4` =
`7`. `a % b` = `17 % 5` = `2`; `result2` = `(2 == 2)` = `True`.
`result1 > 5` = `(7 > 5)` = `True`; `result3` = `True and True` =
`True`. 1 mark per correctly traced value, with partial credit for
correct intermediate reasoning even if a final value is off due to an
arithmetic slip.

<!-- ANSWER KEY ABOVE THIS LINE -->
