# Class 07 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** Operators & Expressions
**Subtitle:** Class 01's LOGIC, Made Literal
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 05 —
Your First Python Program, Class 06 — Variables & Data Types

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

**This class assumes Class 06's environment and habits are already in
place** for every student — variables, `print()`, and comfort typing and
running code. Nothing new needs installing.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01, 05, and 06](#3-relationship-to-class-01-05-and-06)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening Mystery (0–5)](#8-opening-mystery-0-5)
9. [Callback — Two Boxes Reopened (5–10)](#9-callback--two-boxes-reopened-5-10)
10. [What Is an Operator? (10–15)](#10-what-is-an-operator-10-15)
11. [Arithmetic Operators: The Basics (15–23)](#11-arithmetic-operators-the-basics-15-23)
12. [Two Special Operators: // and % (23–30)](#12-two-special-operators--and--23-30)
13. [Order of Operations (30–36)](#13-order-of-operations-30-36)
14. [Expressions: Building Bigger Values (36–42)](#14-expressions-building-bigger-values-36-42)
15. [Comparison Operators (42–50)](#15-comparison-operators-42-50)
16. [A Common Trap: = vs == (50–56)](#16-a-common-trap--vs--50-56)
17. [Logical Operators: and, or, not (56–65)](#17-logical-operators-and-or-not-56-65)
18. [Combining Comparisons with Logical Operators (65–72)](#18-combining-comparisons-with-logical-operators-65-72)
19. [The Class 01 Callback — LOGIC, Made Literal (72–78)](#19-the-class-01-callback--logic-made-literal-72-78)
20. [Full Class 01 → Class 07 Bridge (78–85)](#20-full-class-01--class-07-bridge-78-85)
21. [Interactive Activity — Level Up Your Profile Card (85–100)](#21-interactive-activity--level-up-your-profile-card-85-100)
22. [Misconceptions — In-Class Handling (100–104)](#22-misconceptions--in-class-handling-100-104)
23. [Recap (104–108)](#23-recap-104-108)
24. [Final Takeaway (108–110)](#24-final-takeaway-108-110)
25. [Common Misconceptions — Full Reference](#25-common-misconceptions--full-reference)
26. [Instructor Language / Teaching Guardrails](#26-instructor-language--teaching-guardrails)
27. [Interaction Philosophy](#27-interaction-philosophy)
28. [Visual / Board Plan](#28-visual--board-plan)
29. [Class 01–07 Continuity](#29-class-01-07-continuity)
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
| Class number | 07 |
| Title | Operators & Expressions |
| Subtitle | Class 01's LOGIC, Made Literal |
| Audience | First-year college students, mixed backgrounds. Every student created, printed, and reassigned variables of four data types last class — this class assumes that comfort level, not more. |
| Prerequisites | Class 01 (`PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT`), Class 05 (`print()`, quotes/strings, comments), Class 06 (variables, assignment, `int`/`float`/`str`/`bool`). No prior use of operators assumed or required. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 06 ended on a deliberate, unresolved question: we can print numbers now, but we haven't done any math with them. Class 07 answers it, and reopens something older still — Class 01's `LOGIC` box, which has sat on the board since Week 1 as an abstract word. Today, "reasoning about how to solve a problem" becomes literal Python: arithmetic, comparison, and logical operators. |
| Core question | **"Now that we can store values, how do we actually compute, compare, and combine them?"** |
| Core concept | `VALUES → OPERATORS → EXPRESSIONS (new values)`, landing inside Class 06's chain as a new box between `VARIABLES` and `RUN` — and reconnecting directly to Class 01's `LOGIC`. |
| Class success metric | Without prompting, most students can: (1) use `+ - * /` to compute a new value from variables; (2) explain what `//` and `%` do, with one example each; (3) predict the result of a multi-operator expression using order of operations; (4) explain what an expression is; (5) use comparison operators (`== != < > <= >=`) and state that each produces a boolean; (6) explain the difference between `=` and `==`; (7) use `and`, `or`, and `not` to combine boolean values; (8) explain that today's operators are Class 01's `LOGIC` box, made literal. |

This class is entirely about arithmetic, comparison, and logical
operators, and the expressions built from them. **No `if`/`elif`/`else`
— today's comparisons and logical results are only ever printed, never
used to branch a program. No loops. No `input()`. No functions students
define. No lists, dictionaries, or any other data structure. No
compound assignment (`+=`, `-=`, etc.). No string concatenation with
`+`, beyond a one-line acknowledgment that it exists. No bitwise
operators, no chained comparisons (`a < b < c`), no exponent operator
beyond a passing mention.** If you feel tempted to show
`if age >= 18:` to "make an example useful," that is the signal to
simplify further, not to go deeper — Class 08 owns that.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one very specific limitation with a toolkit.
Since Class 05, every program could only ever print things — never
compute, never compare, never decide anything about its own values.
Today, values stop being inert. Every example, every "predict the
result before I run it" moment exists to make arithmetic, comparison,
and logical operators feel like natural extensions of what a variable
already is, not a new unrelated topic.

**Teaching philosophy, in one line:** identical in spirit to Classes
01–06 — intuition before syntax, example before rule, ask before
explaining, and (continuing since Class 05) **let students type it
themselves and predict before running.**

**What students should feel by the end:**

- A beginner should feel: *"I can finally make Python actually compute
  something, not just say it."*
- A stronger student should feel: *"I can see how a real program would
  check a rule — like whether someone qualifies for something — even
  though we haven't written an `if` yet."*
- Everyone should feel the specific "click" of realizing `==` isn't a
  typo of `=` but an entirely different question (Section 16) — this is
  the single most important guardrail in the class.

**State this to yourself before you walk in:**

> This is **not** a math class, and it is **not** a class about
> decision-making programs. By the end, nobody needs to have written an
> `if` statement or a loop. This class exists so that "operator" stops
> being a vague word and becomes a small, concrete toolkit students have
> personally used to compute, compare, and combine values — the same way
> Class 06 turned "variable" from an abstract idea into something
> personally created and changed.

If a question drifts toward "how do I make the program actually *do*
something different based on this comparison," that is Class 08's job —
redirect warmly using the parking-lot response in Section 34.

---

## 3. Relationship to Class 01, 05, and 06

Class 01 built:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

...where `LOGIC` was described only abstractly, as "reasoning about how
to solve the problem." It was never made literal.

Class 06 ended on a deliberate, unresolved hook:

> "We can print numbers now — but we haven't done any math with them.
> What if a program needed to add a score, calculate a total, or
> compare two values?"

Class 07 is the direct answer to that hook, **and** it is the class
where `LOGIC` finally stops being an abstract word.

**Say this explicitly, early (Section 9 is the natural spot):**

> "Last class ended with a question about doing math with values. Today
> answers it. But it also reopens something from Week 1 — remember
> `LOGIC`, in Class 01's very first chain? We never said what that
> actually looks like in code. Today, it does."

**The relationship is not new content bolted on — it is Class 06's
`VARIABLES` box, put to work:**

```
Class 6 chain:   ... → VARIABLES → RUN → OUTPUT/RESULT
Class 7 opens:            ▲▲▲▲▲
                  OPERATORS turn values into new values: EXPRESSIONS
```

This is the same staircase framing every prior class used — see Section
29 for the full continuity treatment.

---

## 4. Learning Objectives

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | Use arithmetic operators (`+ - * /`) to compute a value from variables | Can write `total = price1 + price2` and predict/explain the result | Operator precedence beyond basic PEMDAS-style rules |
| 2 | Explain `//` and `%` | Can state that `//` gives a whole-number result and `%` gives the remainder, with one example each | Negative-number edge cases, formal modular arithmetic |
| 3 | Apply order of operations | Can correctly predict the result of a two-or-three-operator expression, and use parentheses to change it | Full formal operator-precedence table |
| 4 | Explain what an expression is | Can say "any piece of code that produces a value" and give an example | Formal grammar/parsing concepts |
| 5 | Use comparison operators (`== != < > <= >=`) | Can write a comparison and correctly predict `True`/`False` | Comparing across mismatched data types |
| 6 | Distinguish `=` from `==` | Can explain, unprompted, that one stores and one asks a question | — |
| 7 | Use `and`, `or`, `not` | Can combine two boolean values or comparisons and predict the result | Short-circuit evaluation, truthy/falsy values beyond booleans |
| 8 | Connect operators to Class 01's `LOGIC` | Can restate that today's operators are what "reasoning about a problem" actually looks like in code | Any new algorithmic content |

---

## 5. Key Terminology

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Operator** | A symbol that does something with one or more values. | "The verbs of programming — they act on values." | — | Yes — core term |
| **Operand** | A value an operator acts on. | "What the operator is working with." | — | Loosely |
| **Expression** | Any piece of code that produces a value. | "Something Python can work out and hand you a value for." | "Only math counts as an expression" | Yes — core term |
| **Arithmetic operator** | `+ - * / // %`, doing math with numbers. | "The math operators." | — | Yes — names, not deep theory |
| **Floor division (`//`)** | Division that keeps only the whole-number part. | "Divide, then drop anything after the decimal point." | — | Yes |
| **Modulus (`%`)** | The remainder left over after division. | "What's left over." | — | Yes |
| **Comparison operator** | `== != < > <= >=`, asking a true/false question about two values. | "A question about two values, answered with a boolean." | "The same thing as `=`" | Yes — core term |
| **Logical operator** | `and`, `or`, `not`, combining boolean values into one boolean answer. | "Combining yes/no facts into one yes/no answer." | — | Yes — core term |
| **Order of operations** | The fixed order Python uses to evaluate an expression with multiple operators. | "What happens first when there's more than one operator." | — | Loosely — the idea, not a formal table |

---

## 6. Class at a Glance

Canonical **110-minute** flow.

| Time | Dur. | Section | Objective | Teaching mode | Board/Screen | Interaction |
|---|---|---|---|---|---|---|
| 0–5 | 5 | Opening Mystery | Feel the limitation: no way to compute yet | Ask → demonstrate → hold | Live screen | High |
| 5–10 | 5 | Callback | Reopen Class 06's hook and Class 01's LOGIC | Recall → question | None | Medium |
| 10–15 | 5 | What Is an Operator? | Name the toolkit | Reveal → define | Live screen | Medium |
| 15–23 | 8 | Arithmetic Operators: The Basics | `+ - * /` | Type-along | Live screen | Very high |
| 23–30 | 7 | Two Special Operators | `//` and `%` | Type-along → preview hook | Live screen | High |
| 30–36 | 6 | Order of Operations | Predict before revealing | Ask → predict → reveal | Live screen | High |
| 36–42 | 6 | Expressions | Name what's been happening all along | Reveal → define | Live screen | Medium |
| 42–50 | 8 | Comparison Operators | `== != < > <= >=` produce booleans | Type-along → contrast | Live screen | Very high |
| 50–56 | 6 | A Common Trap: = vs == | The single most important guardrail | Ask → contrast live | Live screen | High |
| 56–65 | 9 | Logical Operators | `and`, `or`, `not` | Type-along | Live screen | High |
| 65–72 | 7 | Combining Comparisons with Logical Operators | Build a real-feeling rule | Build live | Live screen | High |
| 72–78 | 6 | The Class 01 Callback | LOGIC, made literal | Explain → connect | None | Medium |
| 78–85 | 7 | Full Class 01 → 07 Bridge | Install the hero chain | Build live | **Hero diagram** | High |
| 85–100 | 15 | Interactive Activity — Level Up Your Profile Card | Extend Class 06's own program | Facilitated hands-on | Circulate | Very high |
| 100–104 | 4 | Misconceptions | Directly address 2–3 common misreadings | Ask → reframe | None | Medium |
| 104–108 | 4 | Recap | Consolidate, verify | Ask → students answer | Reuse hero diagram | High |
| 108–110 | 2 | Final Takeaway | Close on one memorable line | State → bridge forward | None | Low |

**Non-negotiable blocks** (never compressed away — see Section 32):
Arithmetic Operators: The Basics, Two Special Operators, Comparison
Operators, A Common Trap: = vs ==, Logical Operators, the Class 01 →
Class 07 bridge, and the Level Up Your Profile Card activity.

---

## 7. Section-by-Section Teaching Guide

Quick **A–D** index for every block; full teaching notes for each live in
Sections 8–24 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening Mystery | Feel the limitation before naming the fix | Students recognize print()+variables alone can't compute | No |
| 2 | Callback | Reopen Class 06's hook and Class 01's LOGIC | Students state both connections | No |
| 3 | What Is an Operator? | Name the toolkit | Students define operator/operand in their own words | No |
| 4 | Arithmetic Operators: The Basics | Compute with `+ - * /` | Students write and predict an arithmetic expression | **Yes** |
| 5 | Two Special Operators | `//` and `%` | Students state what each returns, with an example | **Yes** |
| 6 | Order of Operations | Predict multi-operator results | Students correctly predict a two-operator expression | No |
| 7 | Expressions | Name what's been happening | Students define "expression" in their own words | No |
| 8 | Comparison Operators | Produce booleans from comparisons | Students write a comparison and predict True/False | **Yes** |
| 9 | A Common Trap: = vs == | Prevent the single most common bug | Students explain the difference unprompted | **Yes** |
| 10 | Logical Operators | Combine booleans with `and`/`or`/`not` | Students predict the result of a logical expression | **Yes** |
| 11 | Combining Comparisons with Logical Operators | Build a realistic rule | Students build and evaluate a combined expression | No |
| 12 | The Class 01 Callback | LOGIC, made literal | Students restate the connection to Class 01 | No |
| 13 | Full Class 01 → 07 Bridge | Consolidate the whole continuity chain | Students restate the bridged chain | **Yes** |
| 14 | Interactive Activity | Extend an existing program with real computation | Every student adds working expressions to their profile card | **Yes** |
| 15 | Misconceptions | Directly defuse common wrong models | Students can correct at least one misconception aloud | No |
| 16 | Recap | Verify understanding | Students answer recap questions in their own words | **Yes** |
| 17 | Final Takeaway | Close memorably, bridge forward | Students can repeat the final line's idea, not its wording | No |

---

## 8. Opening Mystery (0–5)

Do **not** open with "Today we will learn about operators." Open with a
live, felt limitation.

**Exact opening approach:**

1. Type live: `price1 = 50` then `price2 = 30`.
2. Ask: *"I want the total. Using only what we know — `print()`,
   variables, commas — how do I get Python to add these together?"*
3. Let students try `print(price1, price2)` if they suggest it — run it,
   and point out: *"That shows both numbers side by side. It didn't add
   them. We genuinely don't have a way to compute a new value yet."*
4. **Do not resolve it yet.** Let the gap sit for a moment.
5. Bridge: *"There's a whole toolkit for exactly this, and it's today's
   entire class."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "How do we get Python to actually add these two numbers?" | Genuine uncertainty is expected — that's the point | Narrow it: "Everything we know how to do is print things or store things. Neither one computes anything new — yet." |

**Transition:** *"Let's go back to exactly where Class 06 left off — and
to something even older, from Class 01."*

---

## 9. Callback — Two Boxes Reopened (5–10)

Bring back Class 06's closing hook exactly as it was left:

> "We can print numbers now — but we haven't done any math with them.
> What if a program needed to add a score, calculate a total, or
> compare two values?"

**What the instructor says:**

> "That's exactly today. And it reopens something even older. Class 01
> — Week 1 — gave us this chain."

Write:

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

> "`LOGIC` meant 'reasoning about how to solve the problem.' We never
> once showed what that reasoning actually looks like written down. By
> the end of today, it will."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did Class 06 leave unanswered?" | How to compute/compare values, not just store and print them |
| "What did Class 01's LOGIC box actually mean, concretely?" | Most will admit it was always a bit abstract |

**Transition:** *"Let's name the toolkit that does both."*

---

## 10. What Is an Operator? (10–15)

**Land the core statement directly:**

> "An **operator** is a symbol that does something with one or more
> values. If variables are the nouns of programming — the things — then
> operators are the **verbs.** They act on values and hand you back a
> new one."

**Introduce the word "operand" lightly:**

> "The values an operator acts on are called its **operands.** In
> `price1 + price2`, `price1` and `price2` are the operands; `+` is the
> operator."

**Preview the three families, without teaching them yet:**

> "Today we'll meet three families: **arithmetic** operators, which do
> math; **comparison** operators, which ask true/false questions; and
> **logical** operators, which combine true/false answers."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What is an operator, in your own words?" | A symbol that acts on values to produce a new one |
| "What are the values an operator acts on called?" | Operands |

**Transition:** *"Let's start with the family you already know from
math class."*

---

## 11. Arithmetic Operators: The Basics (15–23) — NON-NEGOTIABLE

**Type this live, one line at a time:**

```
price1 = 50
price2 = 30
total = price1 + price2
print(total)
```

Run it — `80` appears.

> "`+` computed a brand-new value from two variables, and we stored that
> new value in `total`. This is genuinely new — Class 06's variables
> could only ever hold what you typed in directly. Today, a variable can
> hold the *result* of a computation."

**Continue live, one operator at a time, predicting before each run:**

```
print(10 - 3)    # subtraction
print(4 * 5)     # multiplication
print(9 / 2)     # division
```

**Land an important precision point on division:**

> "Notice `9 / 2` gives `4.5` — division in Python always gives you a
> `float` result, even if the numbers divide evenly. `10 / 2` gives
> `5.0`, not `5`."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does `total = price1 + price2` actually do?" | Computes the sum and stores it in `total` |
| "What data type does `/` always produce?" | A float |

**Transition:** *"Two more arithmetic operators exist, and they behave a
little differently from what you're used to."*

---

## 12. Two Special Operators: // and % (23–30) — NON-NEGOTIABLE

**Type this live:**

```
print(9 // 2)
print(9 % 2)
```

Run both. `4`, then `1`.

> "**`//`** is floor division — divide, then keep only the whole-number
> part, dropping anything after the decimal point. `9 // 2` is `4.5`,
> floored down to `4`. **`%`** is the modulus — it gives you the
> *remainder* left over. `9 % 2` is `1`, because `9` is `4` groups of `2`
> with `1` left over."

**Offer a genuinely motivating preview, without teaching it today:**

> "Here's something `%` is famous for: `number % 2 == 0` is exactly how
> programs check whether a number is even. We're not writing that check
> today — that needs an `if`, which is Class 08 — but now you know
> exactly where that tool comes from."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does `//` do?" | Divides and keeps only the whole-number part |
| "What does `%` give you?" | The remainder after division |

**Transition:** *"Now — what happens when an expression uses more than
one operator at once?"*

---

## 13. Order of Operations (30–36)

**Ask students to predict before revealing:**

```
print(2 + 3 * 4)
```

> "Before I run this — is the answer 20, or something else?"

Let guesses happen — some will say 20 (adding first).

**Run it — `14` appears.**

> "Python follows the same order of operations you learned in math
> class: multiplication and division happen before addition and
> subtraction. `3 * 4` happens first, giving `12`, then `2 + 12` gives
> `14`."

**Show how parentheses change it:**

```
print((2 + 3) * 4)
```

→ `20`.

> "Parentheses force a part of the expression to happen first — exactly
> like in math. When in doubt, use parentheses to make your intent
> explicit, even where they aren't strictly required."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Does `2 + 3 * 4` give 20 or 14?" | 14 — multiplication happens before addition |
| "How do you force addition to happen first?" | Wrap it in parentheses |

**Transition:** *"Let's name what all of these lines actually are —
because you've been building them all along."*

---

## 14. Expressions: Building Bigger Values (36–42)

**Land the core definition:**

> "Every line we've written today — `price1 + price2`, `9 // 2`,
> `(2 + 3) * 4` — is called an **expression**: any piece of code that
> Python can evaluate down to a single value. A plain value like `18` is
> the simplest possible expression. `price1 + price2` is a bigger one."

**Show that expressions can build on each other:**

```
subtotal = price1 + price2
tax = subtotal * 0.1
total = subtotal + tax
print(total)
```

> "Each line's expression can use the result of a previous line. That's
> how real programs build up complicated calculations — one small,
> understandable expression at a time."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What is an expression, in your own words?" | Any piece of code that produces a value |
| "Can an expression use the result of an earlier variable?" | Yes |

**Transition:** *"So far every expression has produced a number. Let's
meet a family of operators whose expressions always produce a boolean."*

---

## 15. Comparison Operators (42–50) — NON-NEGOTIABLE

**Type this live, one at a time, predicting before each run:**

```
age = 18
print(age == 18)
print(age > 21)
print(age != 20)
print(age <= 18)
```

Run each — `True`, `False`, `True`, `True`.

> "Each of these is a **comparison** — a question about two values. And
> notice the data type of every single answer: a **boolean**, exactly
> like Class 06. Comparison operators are literally where booleans come
> from in a real program."

**List the full set:**

```
==   equal to
!=   not equal to
<    less than
>    greater than
<=   less than or equal to
>=   greater than or equal to
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What data type does every comparison produce?" | A boolean |
| "What does `!=` ask?" | Whether two values are *not* equal |

**Transition:** *"Look very closely at the first line I typed —
`age == 18`. Count the equals signs. This is the single easiest mistake
to make from here on."*

---

## 16. A Common Trap: = vs == (50–56) — NON-NEGOTIABLE

**Put both side by side, live:**

```
age = 18
age == 18
```

> "One equals sign **stores** — `age = 18` means 'put 18 into age.'
> Two equals signs **ask a question** — `age == 18` means 'is age equal
> to 18?' and hands back `True` or `False`. They look almost identical
> and mean completely different things."

**Say explicitly, an important guardrail:**

> "This mix-up is so common that even experienced programmers still
> catch themselves doing it. If your code isn't behaving the way you
> expect, checking your `=` versus `==` is one of the first things to
> check."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does one `=` do? What does `==` do?" | One stores a value; two asks whether two values are equal |
| "Do `=` and `==` ever mean the same thing?" | No — never |

**Transition:** *"Sometimes one true/false question isn't enough. What
if you need to combine two of them?"*

---

## 17. Logical Operators: and, or, not (56–65) — NON-NEGOTIABLE

**Type this live, predicting before each run:**

```
age = 16
print(age >= 13 and age <= 19)
print(age < 13 or age > 19)
print(not (age == 16))
```

Run each — `True`, `False`, `False`.

> "**`and`** gives `True` only if *both* sides are true. **`or`** gives
> `True` if *at least one* side is true. **`not`** flips a boolean —
> `True` becomes `False` and vice versa."

**Reinforce with a plain-language mapping:**

```
age >= 13 and age <= 19    →  "age is at least 13 AND at most 19"
age < 13 or age > 19       →  "age is younger than 13 OR older than 19"
not (age == 16)            →  "age is NOT 16"
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "When does `and` give `True`?" | Only when both sides are true |
| "When does `or` give `True`?" | When at least one side is true |
| "What does `not` do?" | Flips a boolean's value |

**Transition:** *"Let's build something that actually feels like a real
rule."*

---

## 18. Combining Comparisons with Logical Operators (65–72)

**Build this live:**

```
is_weekend = True
is_raining = False
print(is_weekend and not is_raining)
```

> "This reads almost like English: 'is it the weekend, and is it *not*
> raining?' That's a real rule a real program might check before
> suggesting a picnic — and we just wrote it, using nothing but variables
> and operators from the last two classes."

**Ask students to build one themselves, verbally or on paper first:**

> "Using `age`, write a condition for 'is a teenager' — 13 through 19,
> inclusive."

Expected: `age >= 13 and age <= 19`.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What does `is_weekend and not is_raining` ask, in plain English?" | Is it the weekend and also not raining |

**Transition:** *"Let's connect this whole idea to something from Week
1."*

---

## 19. The Class 01 Callback — LOGIC, Made Literal (72–78)

**Land the core reframe of the whole class:**

> "Remember Class 01's `LOGIC` box — 'reasoning about how to solve a
> problem'? Every time you've ever reasoned 'this has to be true AND
> that has to be true' or 'check whether this equals that,' you were
> doing exactly what today's operators do. Arithmetic, comparison, and
> logical operators *are* reasoning, written down precisely enough for a
> computer to carry out."

**Draw the connecting idea:**

```
LOGIC  (Class 01 — reasoning about a problem)
    ↓
OPERATORS & EXPRESSIONS  (today — that reasoning, in code)
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What did Class 01's LOGIC box actually mean?" | Reasoning about how to solve a problem |
| "What does today's class turn that reasoning into?" | Real code — operators and expressions |

**Transition:** *"Let's put the entire day's reasoning on one board —
starting all the way back at Class 01."*

---

## 20. Full Class 01 → Class 07 Bridge (78–85) — NON-NEGOTIABLE, HERO MOMENT

**This is the HERO MOMENT of the class.** Build it live, top to bottom,
one line at a time — never reveal it finished.

1. Write **PROBLEM** — *"Something we're trying to solve."* (Class 01)
2. Arrow down, write **LOGIC** — *"Reasoning about how to solve it —
   today, made literal."* (Class 01, reopened today)
3. Arrow down, write **ALGORITHM** — *"The plan, as steps a person could
   follow."* (Class 01)
4. Arrow down, write **PYTHON CODE** — *"That plan, written precisely
   enough for a computer to follow."* (Class 05)
5. Arrow down, write **VARIABLES** — *"Labeled, changeable values the
   code can hold and use."* (Class 06)
6. Arrow down, write **EXPRESSIONS** — *"Operators combining values into
   new values — arithmetic, comparison, logical."* (today)
7. Arrow down, write **RUN** — *"Telling the computer to actually carry
   it out."* (Class 05)
8. Arrow down, write **OUTPUT / RESULT** — *"What the program
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
EXPRESSIONS
    ↓
RUN
    ↓
OUTPUT / RESULT
```

**Say explicitly, this is the whole point of the diagram:**

> "Notice something special about this diagram: `EXPRESSIONS` isn't just
> new — it's the literal, coded-up version of `LOGIC`, all the way at
> the top. This class connects the very first box we ever drew to the
> newest one."

**Do not compress this block below 5 minutes**, even under time
pressure — see Section 32.

---

## 21. Interactive Activity — Level Up Your Profile Card (85–100) — NON-NEGOTIABLE

**This is the HERO ACTIVITY.** Every student extends their own Class 06
Variable Profile Card with real computation — no copying the class
example verbatim.

### Facilitator instructions (timed, ~15 minutes at canonical pace)

1. **(2 min) Set up:** "Open your Variable Profile Card from last class
   — or rebuild it quickly if needed. Add: **one arithmetic
   expression** using one of your existing number variables (e.g.
   `age_in_months = age * 12`), **one comparison** that produces a
   boolean (e.g. `is_adult = age >= 18`), and **one logical expression**
   combining two comparisons (e.g. `is_teenager = age >= 13 and
   age <= 19`)."
2. **(9 min) Let students write and run independently (or in pairs).**
   Circulate constantly. Prompt stuck students with: "What's a number
   you could multiply or divide from your card? What's a true/false
   question about your own age or height?"
3. **(2 min) Ask everyone to predict one result before running it** —
   pick their trickiest new line and guess its value first.
4. **(2 min) Invite 2–3 students to share one new line and its result
   with the room.** Celebrate different choices of expression.

### Questions and expected responses

| Question | Expected response |
|---|---|
| "Which of your new lines is arithmetic? Comparison? Logical?" | Any coherent, correctly classified answer |
| "What data type does your comparison line produce?" | A boolean |
| "If you got this wrong, was it a `=`/`==` mix-up?" | A genuinely common, expected answer — normalize it |

**Do not introduce new syntax during this activity** (no `if`, no
`input()`, no loops) — if a student asks for one, use the parking-lot
response (Section 34) and let their program stay simple.

### Timing, extension, and support

- **Canonical timing:** ~15 minutes, per the breakdown above.
- **Stronger-student extension:** Ask them to add a second arithmetic
  expression that uses `//` or `%`, and a logical expression using `or`
  or `not` instead of `and`.
- **Weaker-student support:** Provide the three example lines from
  Section 21's setup directly, and let them adapt the variable names to
  their own card rather than inventing new expressions from scratch.
- **Transition back to the main lesson:** "You just made your own
  program compute and reason about its own values — for the first time,
  not just store and display them. That's the entire idea of today's
  class."

---

## 22. Misconceptions — In-Class Handling (100–104)

Pick 2–3 of the misconceptions most likely to have surfaced already today
(see Section 25 for the full reference table) and address them directly
and briefly.

Suggested priority order for in-class handling:

1. "`/` and `//` are basically the same" (likely surfaced in Section
   12).
2. "`=` and `==` do the same thing" (very likely surfaced in Section
   16, or the activity).
3. "Order of operations doesn't really matter" (worth pre-empting if it
   came up in Section 13).

Keep this to 4 minutes — this is a quick defusal pass, not a new lecture.

---

## 23. Recap (104–108) — NON-NEGOTIABLE

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last several minutes:

1. **"What's the difference between `/` and `//`?"** *Expected:* `/`
   always gives a float; `//` keeps only the whole-number part.
2. **"What does `%` give you?"** *Expected:* the remainder after
   division.
3. **"What data type does a comparison always produce?"** *Expected:* a
   boolean.
4. **"What's the difference between `=` and `==`?"** *Expected:* one
   stores a value, the other asks whether two values are equal.
5. **"When does `and` give `True`?"** *Expected:* only when both sides
   are true.
6. **"How does this class connect back to Class 01?"** *Expected:*
   today's operators are Class 01's `LOGIC` box, made literal.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 24. Final Takeaway (108–110)

**Close with the final statement, said slowly:**

> "For six classes, `LOGIC` was just a word on a board. Today, it has a
> shape: arithmetic operators that compute, comparison operators that
> ask true/false questions, and logical operators that combine those
> answers. Every rule you will ever teach a computer to follow starts
> with exactly these tools."

**Then leave the bridge-forward question open, explicitly not answered
today:**

> "Right now, every comparison and every logical result just gets
> printed — it doesn't actually change what the program does next. What
> if a program needed to behave differently depending on the answer?
> That's exactly where we pick up next class."

Do not resolve this — it is intentionally a hook into Class 08 (Making
Decisions: if / elif / else).

---

## 25. Common Misconceptions — Full Reference

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "`/` and `//` are basically the same operator." | Using them interchangeably, or surprise at `9 / 2` giving `4.5` | "`/` always gives a float, even when it divides evenly. `//` deliberately keeps only the whole-number part." | Section 11–12 |
| 2 | "`=` and `==` do the same thing." | Writing `age = 18` when meaning to ask a question, or vice versa | "One `=` stores a value. Two `==` asks a true/false question. They're never interchangeable." | Section 16 |
| 3 | "Order of operations doesn't really matter — Python just goes left to right." | Predicting `2 + 3 * 4` as `20` | "Python follows the same math-class order of operations: multiplication/division before addition/subtraction, unless parentheses say otherwise." | Section 13 |
| 4 | "`and`/`or` work like casual English, so `or` sometimes means 'both'." | Treating `or` as exclusive ("either, but not both") | "In Python, `or` gives `True` if *at least one* side is true — including when both are true. That's different from how 'either...or' sometimes sounds in English." | Section 17 |
| 5 | "A comparison like `age > 21` actually changes what the program does." | Expecting the program to branch or skip lines based on a printed `True`/`False` | "Today, a comparison just produces a boolean value we print — it doesn't yet make the program behave differently. That's Class 08's `if` statement." | Section 15, Section 24 |

---

## 26. Instructor Language / Teaching Guardrails

**Prefer:**

- "A comparison produces a boolean" — **over** "a comparison checks if
  something is true" alone (the data-type framing ties directly back to
  Class 06).
- "Read `==` as 'is equal to,' a question" — **over** letting `==` be
  read the same way as `=`.

**Avoid:**

- "This is just like math class" — true for arithmetic, misleading for
  `//`, `%`, and especially `==` vs `=`, which have no direct math-class
  equivalent taught the same way.
- Demonstrating an `if` statement "just to show why comparisons matter"
  — even briefly, this steals Class 08's reveal and confuses today's
  scope boundary.

**The instructor must NOT**, at any point in this class:

- introduce `if`/`elif`/`else` or any conditional logic, even as a
  preview
- introduce `while`/`for` loops
- introduce `input()`
- introduce functions the student defines themselves (`def`)
- introduce lists, dictionaries, or any other data structure
- introduce compound assignment (`+=`, `-=`, `*=`, `/=`)
- introduce string concatenation with `+` as a taught skill (a one-line
  acknowledgment that it exists is fine if asked; see Section 34)
- introduce chained comparisons (`a < b < c`), bitwise operators, or the
  exponent operator (`**`) as taught content

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that soon — Class 08 (or the
> relevant later class) is exactly where that lives. Today we're
> building the toolkit; next class we'll actually use it to make
> decisions."

Then return to whichever anchor fits the moment:

```
PROBLEM → LOGIC → ALGORITHM → PYTHON CODE → VARIABLES → EXPRESSIONS → RUN → OUTPUT/RESULT
```

See Section 34 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 27. Interaction Philosophy

Class 07 continues the hands-on-typing emphasis from Classes 05–06,
layered onto discussion — with more "predict before you run" moments
than any class so far, because operators are where predictions are
easiest to make and most satisfying to confirm.

**Sample questions to use across the class:**

- "Before I run this — what do you think the result will be?"
- "What data type does this expression produce?"
- "Is this asking a question, or storing a value?"
- "In plain English, what is this comparison actually asking?"
- "How does this connect back to Class 01's LOGIC?"

**Prediction-before-running remains the single most valuable habit.**
Ask "what do you think will happen?" before every run, especially before
the order-of-operations reveal (Section 13) and the `=` vs `==` contrast
(Section 16).

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 8–12 seconds for the two hardest reasoning
moments — predicting `2 + 3 * 4` before revealing order of operations
(Section 13), and predicting the result of a combined comparison +
logical expression (Section 18).

**Built-in reasoning opportunities to protect, in priority order:**

1. Predicting each arithmetic result before running (Section 11)
2. Predicting the order-of-operations result (Section 13)
3. Predicting each comparison's `True`/`False` before running (Section
   15)
4. Predicting the combined logical expression (Section 18)
5. Every individual choice a student makes extending their own Profile
   Card (Section 21)

---

## 28. Visual / Board Plan

Most of this class's "board" is the **live screen**, exactly as in
Classes 05–06.

**Screen 1 — Arithmetic, Live**
Typed live in Section 11. `price1 = 50`, `price2 = 30`, `total = price1
+ price2`, `print(total)`, plus `-`, `*`, `/` examples.

**Screen 2 — Floor Division and Modulus**
Typed live in Section 12. `print(9 // 2)` and `print(9 % 2)`, with their
results shown directly beneath.

**Screen 3 — Order of Operations**
Typed live in Section 13. `print(2 + 3 * 4)` then `print((2 + 3) * 4)`,
contrasting `14` and `20`.

**Screen 4 — Building Expressions**
Typed live in Section 14. `subtotal`, `tax`, `total`, each building on
the last.

**Screen 5 — Comparison Operators**
Typed live in Section 15. Four comparisons on `age`, each with its
boolean result shown.

**Screen 6 — = vs ==**
Typed live in Section 16, side by side — the single most important
screen of the class alongside Screen 5.

**Screen 7 — Logical Operators**
Typed live in Section 17. `and`, `or`, `not`, each with a plain-English
translation alongside.

**Drawing 1 — HERO — Full Bridge**
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
VARIABLES
    ↓
EXPRESSIONS
    ↓
RUN
    ↓
OUTPUT / RESULT
```

Mark this as a **live construction** — do not show the completed
eight-line chain before students have reasoned their way to each new
piece. This is the single most important drawing of Class 07, and the
first one to visually connect all the way back to Class 01's very first
box.

Keep every diagram simple — no formal operator-precedence tables, no
truth tables beyond the plain-English translations already used.

---

## 29. Class 01–07 Continuity

**Class 1:**

```
PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT
```

**Class 5:**

```
ALGORITHM → PYTHON CODE → RUN → OUTPUT/RESULT
```

**Class 6:**

```
PYTHON CODE → VARIABLES → RUN → OUTPUT/RESULT
```

**Class 7:**

Inserts **EXPRESSIONS** into Class 06's chain, and — uniquely among
Classes 05–07 — reopens Class 01's `LOGIC` box directly, showing that
today's operators *are* what "reasoning about a problem" looks like in
real code:

```
LOGIC (Class 01) → OPERATORS & EXPRESSIONS (today)
```

**Say this once, clearly (Section 9 or Section 19 are the natural
spots):**

> "We are not starting a new topic. We're opening one more box inside
> Class 06's chain — and, for the first time since Week 1, we're also
> going back and finally opening Class 01's very first abstract box."

This is the same continuity statement pattern used since Class 02 — it
is what turns seven separate classes into one staircase instead of seven
unrelated topics.

---

## 30. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks throughout the class, and rely heavily on the hands-on
activity (Section 21), exactly as in Classes 05–06.

A student is demonstrating real understanding if they can:

1. Use `+ - * /` to compute a new value from variables.
2. Explain `//` and `%` with an example each.
3. Correctly predict a multi-operator expression's result using order of
   operations.
4. Define an expression in their own words.
5. Use comparison operators and correctly predict `True`/`False`.
6. Explain the difference between `=` and `==` unprompted.
7. Use `and`, `or`, `not` to combine boolean values correctly.
8. Connect today's operators back to Class 01's `LOGIC` box.

**Do not** judge understanding solely from a student successfully
copying the instructor's exact example — the Level Up Your Profile Card
activity (Section 21), where students choose their own values and
predict results before running, is the strongest evidence of real
understanding.

---

## 31. Differentiation

**For students struggling:** Anchor entirely in the worked examples from
Section 21's setup, adapting only the variable names to their own
Profile Card rather than inventing new expressions from scratch. Walk
the concrete progression one operator family at a time:

```
arithmetic (compute)  →  comparison (ask true/false)  →  logical (combine)
```

**For students moving quickly:** Let them extend the activity (Section
21's stronger-student extension) — a second arithmetic expression using
`//` or `%`, and a logical expression using `or`/`not`. Do **not** teach
`if`, `input()`, or loops even for fast movers — deepen *fluency* with
operators, not scope. See Section 33 for the full extended-version
guidance.

**For students who stay quiet:** The Level Up Your Profile Card activity
(Section 21) is naturally personal and low-stakes — circulate and read
their screen rather than calling on them verbally, exactly as in
Classes 05–06.

---

## 32. Time Management / Timing Safety

**Must cover, in priority order** (matches the non-negotiable list in
Section 7):

1. Arithmetic Operators: The Basics (Section 11)
2. Two Special Operators — `//` and `%` (Section 12)
3. Comparison Operators (Section 15)
4. A Common Trap: `=` vs `==` (Section 16)
5. Logical Operators (Section 17)
6. The full Class 01 → Class 07 bridge (Section 20)
7. The Level Up Your Profile Card activity (Section 21)

**Can shorten:**

- Order of Operations (Section 13) — a single example pair is enough
- Expressions (Section 14) — this is mostly a naming/consolidation
  block, can be folded into Section 13's transition
- Combining Comparisons with Logical Operators (Section 18) — one
  worked example instead of two
- The misconception discussion (Section 22) — pick just one instead of
  2–3

**Can expand** (see Section 33 for detail):

- Let students predict more arithmetic results in Section 11 before
  moving on
- Run a second order-of-operations example with three operators in
  Section 13
- Spend more time circulating during the activity (Section 21)

**Do not cut:** Comparison Operators (Section 15), the `=` vs `==`
contrast (Section 16), Logical Operators (Section 17), or the Level Up
Your Profile Card activity (Section 21) — these are the load-bearing
walls of the entire class.

### 90-minute version

Trim as follows: Opening Mystery to 4 min, Callback to 4 min, What Is an
Operator? to 4 min, Arithmetic Basics unchanged (8 min), Two Special
Operators to 6 min, Order of Operations to 4 min, Expressions folded
into Order of Operations' transition (0 min separately), Comparison
Operators unchanged (8 min), = vs == unchanged (6 min), Logical Operators
to 7 min, Combining Comparisons to 5 min, Class 01 Callback to 4 min,
Full Bridge unchanged (7 min), Activity compressed to 11 min,
Misconceptions to 3 min, Recap to 3 min, Final Takeaway unchanged (2
min). Total ≈ 86 minutes.

### 120-minute version

Add time back to: Arithmetic Basics (+2 min, let students predict more
results), Order of Operations (+2 min, a three-operator example),
Combining Comparisons with Logical Operators (+2 min, a second
student-built example), Activity (+4 min, let every student who wants
to present their program to the room).

---

## 33. Extended Version

If time allows, deepen fluency — do **not** introduce `if`, `input()`,
or loops.

- Let students predict the result of a three-operator expression (e.g.
  `10 + 2 * 3 - 4 // 2`) before revealing it.
- Ask stronger students to write a comparison and a logical expression
  using a data point they haven't used yet in their Profile Card.
- Briefly mention, without demonstrating in depth, that `+` also works
  on strings ("concatenation" — joining two pieces of text) — enough to
  say "this exists," not enough to teach it today.
- Ask students to translate a plain-English rule of their own invention
  ("it's a good day for a picnic if it's the weekend and not raining")
  into a logical expression, using variables they define themselves.

---

## 34. Advanced Topics Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "How do I make the program actually do something different based on a comparison?" | "That's `if`/`else` — real conditional logic, coming next class." | "Today's building block is the expression itself, not what it changes." |
| "Is there a shortcut for `score = score + 10`?" | "Yes — `score += 10` does the same thing. Real, useful, and a natural next step, just not today's scope." | Return to: today, use `=` explicitly. |
| "Can I use `+` to join two pieces of text together?" | "Yes — that's called concatenation, and it's real. Today we're only using `+` for numbers." | Return to: today's arithmetic operators work on numbers. |
| "What does `**` do?" | "That's exponentiation — real, and a small, easy addition to your toolkit once you're ready, just not today's focus." | Return to: today's four core arithmetic operators. |
| "Can I chain comparisons, like `13 <= age <= 19`?" | "Python actually allows that shorthand — real and handy, but we're building the full-length version first so the logic is crystal clear." | Return to: `age >= 13 and age <= 19`. |
| "What happens if I compare two different data types, like a number and text?" | "Usually Python will tell you it doesn't know how to compare them — a real and useful error, similar to ones you've seen before." | Return to: today, compare values of the same type. |
| "Does `and`/`or` always check both sides?" | "Sometimes Python can skip checking the second side once it already knows the answer — a real optimization called short-circuiting, for later." | Return to: today, both sides are simple enough to just reason through directly. |

---

## 35. Teacher FAQ

**Q: A student wrote `age = 18` when they meant to ask a question — what
happened?**
A: This is Section 16's exact trap in the wild — walk through what `=`
actually did (silently overwrote `age`'s value) versus what they
intended (`==`, a comparison). This is one of the most valuable live
teaching moments in the class; don't just fix it for them.

**Q: Should I explain truthy/falsy values (e.g., that `0` behaves like
`False`)?**
A: No — stay at the level of actual `bool` values (Section 15).
Truthy/falsy is a later-class refinement that would blur today's clean
"comparisons produce booleans" story.

**Q: A student asked about `if` — did I do something wrong by not
covering it?**
A: No — that's the parking lot working exactly as intended (Section 34).
Today deliberately builds the toolkit `if` will use next class, without
using it yet.

**Q: What if a student's Level Up expression produces an error?**
A: A great real moment — walk through it together using the Class 05
write-run-read-fix loop. A very common cause: comparing a variable that
doesn't exist yet, or a `=`/`==` mix-up (Section 16).

**Q: Is it okay if some students finish the activity early?**
A: Yes — use the stronger-student extension in Section 21 (a `//`/`%`
expression, an `or`/`not` logical expression). Do not let early
finishers pull you into teaching `if` ahead of schedule.

**Q: What if I only have 90 minutes, not 110?**
A: Use the 90-minute version in Section 32 — it preserves every
non-negotiable block and only trims discussion time and the
order-of-operations/expressions material.

---

## 36. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Use `+ - * /` to compute a new value from variables.
2. Explain `//` and `%`, each with an example.
3. Correctly predict a multi-operator expression's result.
4. Define an expression in their own words.
5. Use comparison operators and correctly predict `True`/`False`.
6. Explain the difference between `=` and `==`.
7. Use `and`, `or`, `not` to combine boolean values correctly.
8. Reconnect today's operators to Class 01's `LOGIC` box.

A class where most students can do these in plain, imperfect language —
and where every student has personally extended their own program with
real computation — has met the bar.

---

## 37. Source-of-Truth / QA Checklist

Verified against the Foundation Batch 2026 curriculum plan (Block 1,
`C07`) before finalizing this guide:

- [x] Class 01, 05, and 06 continuity is explicit (Sections 3, 9, 19,
      29).
- [x] The class starts with a felt limitation, not a definition (Section
      8).
- [x] Every student computes, compares, and combines real values, not
      just watches (Sections 11, 12, 15, 17, 21).
- [x] Arithmetic operators (`+ - * / // %`) are all covered, with `/`
      vs. `//` explicitly contrasted (Sections 11–12).
- [x] Order of operations is demonstrated by prediction, not stated as a
      rule to memorize (Section 13).
- [x] "Expression" is explicitly named and defined (Section 14).
- [x] Comparison operators are explicitly tied to Class 06's boolean
      type (Section 15).
- [x] `=` vs. `==` is a dedicated, non-negotiable section (Section 16).
- [x] Logical operators (`and`, `or`, `not`) are covered with
      plain-English translations (Section 17).
- [x] No `if`/`elif`/`else`, loops, `input()`, user-defined functions,
      compound assignment, or data structures are taught (Section 1,
      Section 26, guarded throughout).
- [x] Misconceptions are explicitly handled, both in-flow (Section 22)
      and as a full reference (Section 25).
- [x] The Level Up Your Profile Card activity extends Class 06's
      activity directly, reinforcing continuity (Section 21).
- [x] The class explicitly reopens and resolves Class 01's `LOGIC` box
      (Section 19, Section 29) — the first class since Class 01 to do
      so this directly.
- [x] The class has a clear, explicit, unresolved bridge to Class 08
      (Making Decisions: if/elif/else) (Section 24, Section 34).
- [x] This Master Guide is self-contained and usable by an instructor
      without relying on the Student Notes — every section includes
      instructor wording, questions, expected answers, and transitions.
