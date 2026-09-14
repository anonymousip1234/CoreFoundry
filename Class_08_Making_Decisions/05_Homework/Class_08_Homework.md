# Class 08 — Homework

**Bong Study Hub — Foundation Batch 2026 · Class 08: Making Decisions:
if / elif / else**
*The First Code That "Thinks" Before Acting*

**Estimated time:** 30–45 minutes
**Total:** 30 marks  ·  **Optional Challenge:** up to 3 bonus marks
**Tools needed:** pen and paper, or a simple document. A computer with
Python is helpful for checking your work, but not required to answer any
question.
**Prerequisite:** Classes 05–08. No nested `if` statements, loops, or
`input()` are needed anywhere in this assignment.

---

## What This Assignment Is About

In class, we answered the question Class 07 left open: how do we make a
program actually behave differently depending on what's true? We met
**conditionals** — `if`, `elif`, and `else` — and learned that
**indentation is real Python syntax**, not decoration. We also learned
the class's trickiest lesson: in an `elif` chain, **only the first true
branch runs**, so order matters.

This assignment asks you to **trace code carefully, not just recall
facts about it**. Several questions give you a conditional and ask
exactly which branch runs — the elif-ordering lesson in particular
rewards patient, step-by-step reading rather than guessing.

---

## Instructions

- **Answer in your own words** where a question asks for an explanation.
- For "predict the output" or "trace the code" questions, write the
  **exact** output Python would produce.
- **No nested `if`, loops, or `input()` appear anywhere in this
  homework** — if your answer to any question involves one of those,
  simplify it back down to a flat `if`/`elif`/`else` chain.
- You may refer to your **Student Notes** while answering.
- If you're unsure, **explain your reasoning anyway** rather than
  leaving a blank — partial thinking is worth more than an empty space.

---

## Section A — Core Concepts

### Question 1 — What Is a Conditional? (2 marks)

In your own words, **explain what a conditional is**, and what a
**condition** must evaluate to for an `if` block to run.

<!-- BLANK:3 -->

---

### Question 2 — Why Indentation Matters (2 marks)

**Explain why indentation matters so much in Python**, and what happens
if a line that should be indented isn't.

<!-- BLANK:3 -->

---

### Question 3 — else (2 marks)

**Explain when an `else` block runs.** Does `else` ever take its own
condition?

<!-- BLANK:2 -->

---

### Question 4 — elif (2 marks)

**What does `elif` stand for, and when is its condition actually
checked?**

<!-- BLANK:3 -->

---

### Question 5 — Why Order Matters (2 marks)

In your own words, **explain why the order of conditions in an
`if`/`elif` chain matters**, even when more than one condition is true.

<!-- BLANK:3 -->

---

## Section B — Reading and Reasoning About Code

### Question 6 — Predict the Output (3 marks)

```
temperature = 15

if temperature > 30:
    print("It's hot!")
else:
    print("It's not hot.")
```

**Write the exact output.**

<!-- BLANK:2 -->

---

### Question 7 — Predict the Output (3 marks)

```
grade = 72

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")
```

**Write the exact output**, and briefly explain which condition was the
first one to be `True`.

<!-- BLANK:3 -->

---

### Question 8 — Order Matters (3 marks)

```
points = 100

if points >= 50:
    print("Level 1 complete")
elif points >= 100:
    print("Level 2 complete")
```

**What does this print?** `points` is `100`, which makes *both*
conditions `True` — explain why only one message actually appears, and
which one.

<!-- BLANK:4 -->

---

### Question 9 — Find the Bug (3 marks)

```
is_weekend = True

if is_weekend:
    print("Sleep in!")
   print("Relax today.")
```

**What error would this produce, and why?** Rewrite the code correctly.

<!-- BLANK:4 -->

---

### Question 10 — Comparisons and Logic Inside a Condition (3 marks)

```
temperature = 28
is_sunny = True

if temperature >= 25 and is_sunny:
    print("Perfect beach day!")
else:
    print("Maybe stay in.")
```

**Write the exact output**, and explain why.

<!-- BLANK:3 -->

---

## Section C — Class Connection & Your Own Program

### Question 11 — Connecting Class 01 and Class 08 (2 marks)

Fill in the blank below, using ideas from today's class:

```
ALGORITHM   (Class 01 — imagined as a straight line)
    ↓
________________   (Class 08)
```

Briefly explain, in one sentence, **how today's class widens the way we
picture an algorithm.**

<!-- BLANK:2 -->

---

### Question 12 — Write Your Own Conditional Chain (3 marks)

**Write a short program** (on paper is fine) that sorts a temperature
into at least **three** categories of your choice — for example, cold,
mild, and hot. Use an `if`/`elif`/`else` chain, and make sure your
conditions are ordered correctly.

<!-- BLANK:8 -->

---

## Optional Challenge — Bonus (up to 3 marks)

**This section is entirely optional** and will not affect your base
grade.

Trace the program below very carefully.

```
score = 85
bonus = True

if score >= 60:
    result = "Pass"
elif score >= 80 and bonus:
    result = "Pass with Bonus"
elif score >= 90:
    result = "Distinction"
else:
    result = "Fail"

print(result)
```

**What does this print?** Then explain: **what would need to change
about the order of these conditions** for `"Pass with Bonus"` to
actually be reachable for a score like `85` with `bonus = True`?

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
      wrote the exact output.
- [ ] Where unsure, I explained my reasoning instead of leaving a blank.
- [ ] I did not use nested `if` statements, loops, or `input()` anywhere.
- [ ] I reviewed my work before submitting.

<!-- ANSWER KEY BELOW THIS LINE — INSTRUCTOR USE ONLY. DO NOT INCLUDE IN THE STUDENT-FACING PDF. -->

---

# Instructor Answer Key — Do Not Distribute to Students

**Source of truth:** Class_08_Master_Instructor_Guide.md. This key gives
concise expected concepts, not model essays — reward reasoning that fits
the concept over exact wording throughout.

## Marking Guide (30 marks + 3 optional bonus)

| Section | Question | Marks |
|---|---|---|
| A | Q1 — What Is a Conditional? | 2 |
| A | Q2 — Why Indentation Matters | 2 |
| A | Q3 — else | 2 |
| A | Q4 — elif | 2 |
| A | Q5 — Why Order Matters | 2 |
| B | Q6 — Predict the Output | 3 |
| B | Q7 — Predict the Output | 3 |
| B | Q8 — Order Matters | 3 |
| B | Q9 — Find the Bug | 3 |
| B | Q10 — Comparisons and Logic Inside a Condition | 3 |
| C | Q11 — Connecting Class 01 and Class 08 | 2 |
| C | Q12 — Write Your Own Conditional Chain | 3 |
| | **Total** | **30** |
| | Optional Challenge | +3 bonus |

## Marking Principles

- Reward conceptual understanding, not exact wording — accept plainer or
  simpler language freely.
- For "predict the output" / "trace the code" questions (Q6–Q8, Q10,
  Optional Challenge), output must match **exactly** — but do not
  penalize minor spacing differences in the student's handwriting/typing
  of their answer.
- For Q12 (an open-ended original program), **accept any coherent
  three-branch (or more) `if`/`elif`/`else` chain** — do not require a
  specific topic or exact temperature boundaries.
- A student who can recite "elif checks another condition" but cannot
  correctly trace Q7/Q8 should visibly struggle on those questions —
  that gap is the point of this homework's Section B.
- Do not penalize simpler language or shorter phrasing than the key
  below.

## Answers

**Q1 — What Is a Conditional? (2 marks)**
A conditional is a statement that runs a block of code only if a
condition is true. The condition must evaluate to a **boolean** (`True`
or `False`) — if it's `False`, the block is skipped entirely. (1 mark
for the core definition; 1 mark for correctly identifying the condition
must be boolean.)

**Q2 — Why Indentation Matters (2 marks)**
Python uses indentation itself as the syntax that marks which lines
belong to a block — it isn't just for readability, unlike in many other
places. If a line that should be indented isn't, Python raises an
`IndentationError`, because it expected an indented block and didn't
find one. (1 mark for "indentation is syntax, not decoration"; 1 mark
for correctly describing the resulting error.)

**Q3 — else (2 marks)**
An `else` block runs only when every condition above it (the `if`, and
any `elif`s) was `False`. `else` never takes its own condition — it's
simply "otherwise."

**Q4 — elif (2 marks)**
`elif` stands for "else if." Its condition is only checked if every
condition above it in the chain was `False` — Python never checks an
`elif`'s condition once an earlier branch in the same chain has already
matched.

**Q5 — Why Order Matters (2 marks)**
In an `if`/`elif` chain, Python stops at the first condition that
evaluates to `True`, runs only that block, and never checks anything
below it — even if a later condition is also true. So if a more general
condition is placed before a more specific one, the specific one may
never be reached. Full credit requires the student to explain that later
conditions are skipped once an earlier one matches, not just that
"order matters" as a fact.

**Q6 — Predict the Output (3 marks)**
```
It's not hot.
```
`temperature` is `15`, which is not `> 30`, so the `else` block runs.

**Q7 — Predict the Output (3 marks)**
```
C
```
`grade` is `72`: not `>= 90`, not `>= 80`, but `>= 70` is `True` — so
the third branch runs. (1.5 marks for the correct output; 1.5 marks for
correctly identifying `grade >= 70` as the first true condition.)

**Q8 — Order Matters (3 marks)**
```
Level 1 complete
```
Even though `points >= 100` is also `True`, Python checks `points >= 50`
first, finds it `True`, runs that block, and never even evaluates the
`elif` below it. Full credit requires explicitly stating that the
`elif`'s condition is never checked once the `if` has already matched.

**Q9 — Find the Bug (3 marks)**
This produces an `IndentationError` — the second `print` line uses a
different amount of indentation (3 spaces) than the first line inside
the same block (4 spaces), so Python cannot tell they belong to the same
block. Corrected version:
```
is_weekend = True

if is_weekend:
    print("Sleep in!")
    print("Relax today.")
```
(1 mark for correctly naming the error type; 1 mark for correctly
explaining the mismatched indentation; 1 mark for a correct fix.)

**Q10 — Comparisons and Logic Inside a Condition (3 marks)**
```
Perfect beach day!
```
`temperature >= 25` is `True` (28 is at least 25) and `is_sunny` is
`True`, so `and` makes the whole condition `True`, and the `if` block
runs.

**Q11 — Connecting Class 01 and Class 08 (2 marks)**
Blank = **DECISIONS** (or equivalent wording, e.g. "algorithms can
branch"). The one-sentence explanation should convey that an algorithm
is no longer just a straight line of steps — it can now follow different
paths depending on its data.

**Q12 — Write Your Own Conditional Chain (3 marks)**
Accept any coherent `if`/`elif`/`else` chain with at least three
distinct outcomes, sorting a temperature (or similar single numeric
variable) into categories, with conditions in a sensible, non-overlapping
order. Check for: (1) correct `if`/`elif`/`else` syntax including
colons, (2) at least three reachable branches, (3) conditions ordered so
each branch is actually reachable (i.e., not shadowed by an earlier,
broader condition). (1 mark per criterion.)

**Optional Challenge (up to 3 bonus marks)**
Prints:
```
Pass
```
`score >= 60` is the first condition checked, and `85 >= 60` is `True`,
so `result` is set to `"Pass"` and the rest of the chain — including the
`"Pass with Bonus"` branch, whose condition is also `True` — is never
evaluated. For `"Pass with Bonus"` to be reachable, the
`elif score >= 80 and bonus:` branch would need to come **before** the
`if score >= 60:` branch (or the general `score >= 60` check would need
to be moved later/turned into a broader catch-all at the end) — more
specific conditions need to be checked first. 1 mark for the correct
output, 1 mark for correctly explaining why the bonus branch is
unreachable as written, 1 mark for a valid reordering that fixes it.

<!-- ANSWER KEY ABOVE THIS LINE -->
