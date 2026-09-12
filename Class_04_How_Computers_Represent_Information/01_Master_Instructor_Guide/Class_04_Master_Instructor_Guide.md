# Class 04 — Master Instructor Guide

**Bong Study Hub — Foundation Batch 2026**
**Class title:** How Computers Represent Information
**Subtitle:** From Information → Bits → Binary
**Target duration:** 90–120 minutes (canonical ≈110 minutes)
**Prerequisites:** Class 01 — Welcome to Computer Science, Class 02 — How
Machines Learn, Class 03 — Understanding Data

This is a playbook, not a script. It tells you *what* to teach, *why*, *in
what order*, and *what to say if you get stuck* — not sentences to
memorize and read aloud. Use your own voice. Every wording sample below is
a **suggestion**, not a mandatory line.

---

## Table of Contents

1. [Class Identity](#1-class-identity)
2. [Instructor's Mental Model](#2-instructors-mental-model)
3. [Relationship to Class 01, 02, and 03](#3-relationship-to-class-01-02-and-03)
4. [Learning Objectives](#4-learning-objectives)
5. [Key Terminology](#5-key-terminology)
6. [Class at a Glance](#6-class-at-a-glance)
7. [Section-by-Section Teaching Guide](#7-section-by-section-teaching-guide)
8. [Opening Mystery (0–6)](#8-opening-mystery-0-6)
9. [Class 03 Callback (6–12)](#9-class-03-callback-6-12)
10. [Information Needs Representation (12–21)](#10-information-needs-representation-12-21)
11. [Everyday Two-State Systems (21–29)](#11-everyday-two-state-systems-21-29)
12. [What Is a Bit? (29–35)](#12-what-is-a-bit-29-35)
13. [Why Two States? (35–41)](#13-why-two-states-35-41)
14. [One Bit (41–46)](#14-one-bit-41-46)
15. [Multiple Bits (46–53)](#15-multiple-bits-46-53)
16. [Binary Combinations (53–61)](#16-binary-combinations-53-61)
17. [Binary as a Representation System (61–68)](#17-binary-as-a-representation-system-61-68)
18. [Numbers, Text, Images, and Sound (68–76)](#18-numbers-text-images-and-sound-68-76)
19. [Same Bits, Different Interpretation (76–83)](#19-same-bits-different-interpretation-76-83)
20. [Full Class 03 → Class 04 Bridge (83–89)](#20-full-class-03--class-04-bridge-83-89)
21. [Interactive Reasoning Activity — Tiny Binary Communication System (89–99)](#21-interactive-reasoning-activity--tiny-binary-communication-system-89-99)
22. [Misconceptions — In-Class Handling (99–104)](#22-misconceptions--in-class-handling-99-104)
23. [Recap (104–108)](#23-recap-104-108)
24. [Final Takeaway (108–110)](#24-final-takeaway-108-110)
25. [Common Misconceptions — Full Reference](#25-common-misconceptions--full-reference)
26. [Instructor Language / Teaching Guardrails](#26-instructor-language--teaching-guardrails)
27. [Interaction Philosophy](#27-interaction-philosophy)
28. [Visual / Board Plan](#28-visual--board-plan)
29. [Class 01–04 Continuity](#29-class-01-04-continuity)
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
| Class number | 04 |
| Title | How Computers Represent Information |
| Subtitle | From Information → Bits → Binary |
| Audience | First-year college students, mixed backgrounds. Some have never programmed; some know that computers "use 0 and 1" without understanding why; some have heard "binary" without understanding it. No prior binary knowledge assumed. |
| Prerequisites | Class 01 (Problem → Logic → Algorithm → Program → Result), Class 02 (Data → Learning → Model → Prediction), Class 03 (Real World → Observation → Data; Data → Examples → Features → Labels → Dataset). No new prerequisite beyond those three classes. |
| Duration | ~90–120 minutes. Canonical version: **110 minutes**. Compressed: 90. Expanded: 120. |
| Class purpose | Class 03 established that data is recorded information about something. Class 04 asks the next natural question: once information is recorded, how does a computer actually *represent* it inside itself? This class installs the idea of the **bit** as the fundamental building block of digital representation — not as a fact to memorize, but as something students reason their way into. |
| Core question | **"If computers work with information like text, images, and sound, how do they actually represent that information?"** |
| Core concept | `REAL-WORLD INFORMATION → REPRESENTATION → BITS → 0s AND 1s`, and separately `BITS → COMBINATIONS → MORE POSSIBLE REPRESENTATIONS` |
| Class success metric | Without prompting, most students can: (1) explain why information needs a representation before a computer can work with it; (2) define a bit as one of two possible states; (3) explain why one bit gives two possibilities and why more bits give more; (4) state that binary is a representation system, not a special kind of number or "the language computers understand"; (5) name at least two different kinds of information (beyond numbers) that can be represented digitally; (6) explain that the same bits mean different things depending on how they're interpreted; (7) connect Class 03's `DATA` box to Class 04's `REPRESENTATION → BITS` chain. |

This class is entirely conceptual. **No digital logic. No Boolean
algebra. No logic gates. No computer architecture. No electronics or
transistor physics. No encoding standards (ASCII/Unicode/UTF-8). No
hexadecimal. No binary arithmetic drilling. No programming.** If you
ever feel tempted to explain *how* a voltage becomes a 0 or a 1, or
*exactly* how a byte becomes a letter, that is the signal to simplify
further, not to go deeper — those are later classes' jobs.

---

## 2. Instructor's Mental Model

**What is this class really trying to accomplish?**

It is trying to replace one sentence in a student's head with another.
Before this class: *"Computers use 0s and 1s because that's just how
computers work."* After this class: *"Computers represent information
using two reliably distinguishable states, because a system built from
simple, reliable states can be combined to represent almost anything —
and more of those states means more possible things you can represent."*
That's it. Every switch, every combination table, every example in this
guide exists to land that one replacement cleanly.

**Teaching philosophy, in one line:** identical in spirit to Classes 01–03
— intuition before terminology, example before definition, ask before
explaining, let students predict before revealing, everyday analogies
over invented ones.

**What students should feel by the end:**

- A beginner should feel: *"Oh — binary isn't some special 'computer
  math.' It's just two states, combined a lot of times. I get why that
  works now."*
- A stronger student should feel: *"I can see how you'd build up to
  representing text or images from nothing but on/off — I don't know
  the exact mechanism yet, but I believe it's possible and I'm curious
  how."*
- Everyone should feel a small thrill at the "invent your own binary
  code" activity (Section 21) — the moment where they personally assign
  meaning to `00`, `01`, `10`, `11` and realize *they* just did the thing
  computers do.

**State this to yourself before you walk in:**

> This is **not** a digital logic or computer architecture class. Nobody
> in this room is wiring a circuit today. This class exists so that the
> word "binary" stops being a mysterious, faintly intimidating word and
> becomes something students understand from the inside — the same way
> Class 03 turned "data" from a vague buzzword into something they can
> reason about.

If a question drifts toward "but how does a wire actually become a 0 or
a 1," pull it back to "how many states does this system reliably have,
and what can we build from that" — that redirect is always available and
is never a cop-out; it is the actual scope of the class. See Section 34
for a full parking-lot script.

---

## 3. Relationship to Class 01, 02, and 03

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

...and landed on: **`DATA = RECORDED INFORMATION ABOUT SOMETHING`**.
Class 03 deliberately never asked *how* that recorded information
actually sits inside a computer — it stayed entirely at the conceptual
level of "information about the real world." Class 04 is where that
next, natural question finally gets asked.

**Say this explicitly, early (Section 9 is the natural spot):**

> "Last class, we agreed that data is recorded information about
> something — a number, a photo, a sentence, whatever. But we never
> asked: once it's recorded, how does it actually sit *inside* a
> computer? Today we go one level deeper."

**The relationship is not new content bolted on — it is zooming in
again, exactly like Class 03 zoomed into Class 02's DATA box:**

```
Class 3 pipeline:     REAL WORLD → OBSERVATION → DATA
Class 4 opens this:                              ▲▲▲▲
                                    REPRESENTATION → BITS
```

Frame it exactly like this, because it matters for how students file the
class away mentally:

> "We are not changing anything from Class 3. We're looking even more
> closely at one part of it — what happens to data once a computer
> actually has to hold onto it."

This is the same staircase framing Class 01–03 all used — see Section 29
for the full continuity treatment.

---

## 4. Learning Objectives

Taken directly from the class brief's Core Concepts and Assessment of
Understanding sections. For each, the bar is **conceptual understanding
and curiosity** — the same bar every prior class set. Nothing here needs
to survive an exam.

| # | Objective | Sufficient mastery | Does NOT need to be mastered |
|---|---|---|---|
| 1 | Information needs a representation before a computer can work with it | Can explain, in their own words, that a computer can't "just understand" a photo or a number the way a person does | Any notion of how a CPU or memory actually works |
| 2 | Computers use digital (discrete-state) representation | Can name an everyday two-state example (light switch, yes/no) and connect it to "on/off" in a computer | Electronics, voltage, transistors |
| 3 | Bit = one of two possible states | Can say "a bit is a 0 or a 1 — one of two states" unprompted | Physical implementation of a bit |
| 4 | Why two states, specifically | Can explain that two reliably distinguishable states are simple to build and combine | Formal information theory, signal reliability |
| 5 | One bit → two possibilities | Can state this and give an example (one switch, one yes/no question) | Any arithmetic beyond "two" |
| 6 | More bits → more possibilities, roughly doubling each time | Can say "each extra bit roughly doubles what you can represent" and show 2 bits → 4 combinations | Exponent notation, 2ⁿ formalism, arithmetic drills |
| 7 | Binary is a representation system, not "the thing itself" | Can explain, using the Class 03 "80% full" analogy, that bits represent information rather than being the information | Any encoding standard |
| 8 | Many kinds of information can be represented digitally | Can name at least two of: numbers, text, images, sound, video | ASCII, Unicode, pixels, sampling, compression |
| 9 | The same bits mean different things depending on interpretation | Can explain that a sequence of bits needs an agreed-upon system to mean anything | Formal encoding/decoding mechanisms |
| 10 | Connect Class 03's DATA to Class 04's REPRESENTATION → BITS | Can restate the combined chain `REAL WORLD → OBSERVATION → DATA → REPRESENTATION → BITS → COMPUTER PROCESSING` | Any new ML or data-structure mechanics |

---

## 5. Key Terminology

Small and durable beats large and forgettable. These are the **only**
terms this class needs — and even these should be earned through example
first, not opened with.

| Term | Beginner-friendly explanation | Instructor wording | What NOT to say | Memorize? |
|---|---|---|---|---|
| **Information** | Anything meaningful we might want to record or work with — a number, a word, a picture, a sound. | "Whatever we're trying to represent." | — | Loosely |
| **Representation** | A form that stands in for the real information so it can be stored or processed. | "A stand-in a computer can hold onto." | "The exact same thing as the real object." | Yes |
| **Digital** | Built from a limited number of distinct, reliably distinguishable states, rather than a smooth continuous range. | "Built from clear, distinct states." | Deep signal-processing definitions | Loosely — name only |
| **Bit** | One binary digit — a single unit that can be in one of two possible states. | "One switch: 0 or 1." | "The smallest possible thing in a computer" (true but not the point today), transistor talk | Yes — core term |
| **State** | One of the possible conditions a system can be in (e.g., off/on). | "Which of the possible options it's currently in." | — | Loosely |
| **Combination** | A specific sequence of multiple bits' states taken together (e.g., `01`). | "Several switches, read together." | "Binary number" as the only framing (it's more general than numbers) | Yes |
| **Binary** | A representation system built entirely from two-state units (bits). | "The two-state building system." | "The language computers understand" (misleading — see Section 26) | Yes |
| **Interpretation** | The agreed-upon rule for what a given sequence of bits is supposed to mean. | "The rule that gives the bits meaning." | Formal encoding-standard names | Loosely |

---

## 6. Class at a Glance

Canonical **110-minute** flow, following the class brief's suggested
17-section sequence exactly, with minutes allocated so the total lands
at 110.

| Time | Dur. | Section | Objective | Teaching mode | Pen-tablet | Interaction |
|---|---|---|---|---|---|---|
| 0–6 | 6 | Opening Mystery | Spark curiosity: how can 0 and 1 represent a photo? | Ask → speculate → hold | None yet | High — cold-open speculation |
| 6–12 | 6 | Class 03 Callback | Re-anchor "data = recorded information," pose today's question | Recall → question | None | Medium |
| 12–21 | 9 | Information Needs Representation | A computer can't "just understand" real things | Ask → example → land | Optional | High |
| 21–29 | 8 | Everyday Two-State Systems | Ground "digital" in familiar on/off examples | Ask → build together | Drawing #1 | High |
| 29–35 | 6 | What Is a Bit? | Name the building block | Reveal → define | Drawing #2 | Medium |
| 35–41 | 6 | Why Two States? | Two reliable states are simple to build/combine | Explain → reinforce | None | Medium |
| 41–46 | 5 | One Bit | One bit = two possibilities | Ask → confirm | Reuse Drawing #2 | High |
| 46–53 | 7 | Multiple Bits | Two bits = four combinations, built live | Build live | Drawing #3 | High |
| 53–61 | 8 | Binary Combinations | The doubling pattern, intuitively | Ask → predict → reveal | Drawing #4 | Very high |
| 61–68 | 7 | Binary as a Representation System | Bits represent; they are not "the thing itself" | Explain → Class 03 callback | None new | Medium |
| 68–76 | 8 | Numbers, Text, Images, and Sound | Very different information, same building block | Ask → survey | Drawing #6 (partial) | High |
| 76–83 | 7 | Same Bits, Different Interpretation | Meaning comes from agreed interpretation | Ask → analogy | None | High |
| 83–89 | 6 | Full Class 03 → Class 04 Bridge | Install the hero chain | Build live | **Drawing #5 (hero)** | High |
| 89–99 | 10 | Interactive Activity — Tiny Binary Communication System | Students invent meaning for 2–3 bit codes | Facilitated activity | Record student answers | Very high |
| 99–104 | 5 | Misconceptions | Directly address 3–5 common misreadings | Ask → reframe | None | Medium |
| 104–108 | 4 | Recap | Consolidate, verify | Ask → students answer | Reuse Drawing #5 | High |
| 108–110 | 2 | Final Takeaway | Close on one memorable line | State → bridge forward | None | Low |

**Non-negotiable blocks** (never compressed away — see Section 32): What
Is a Bit?, Multiple Bits / Binary Combinations, Binary as a
Representation System, Numbers/Text/Images/Sound survey, the Class 03 →
Class 04 bridge, and the tiny binary communication activity.

---

## 7. Section-by-Section Teaching Guide

Quick **A–D** index for every block; full teaching notes for each live in
Sections 8–24 below.

| # | Block | A. Purpose | B. One-line objective | Non-negotiable? |
|---|---|---|---|---|
| 1 | Opening Mystery | Create a genuine puzzle before naming anything | Students speculate about how 0/1 could represent a photo | No |
| 2 | Class 03 Callback | Create a felt reason for today's class | Students state that Class 03 never asked how data is stored | No |
| 3 | Information Needs Representation | Establish the core need | Students explain why a computer can't "just understand" a real thing | No |
| 4 | Everyday Two-State Systems | Ground "digital" in familiar examples | Students name an everyday on/off system unprompted | No |
| 5 | What Is a Bit? | Name the building block | Students define a bit as one of two states | **Yes** |
| 6 | Why Two States? | Justify the choice intuitively | Students explain why two reliable states are easy to build/combine | No |
| 7 | One Bit | One bit = two possibilities | Students state this without prompting | **Yes** |
| 8 | Multiple Bits | Build combinations live | Students can list all 4 two-bit combinations | **Yes** |
| 9 | Binary Combinations | Install the doubling pattern intuitively | Students predict how many combinations 3 bits give | **Yes** |
| 10 | Binary as a Representation System | Bits represent, they aren't "the thing" | Students restate the Class 03 "80% full" analogy for bits | **Yes** |
| 11 | Numbers, Text, Images, and Sound | Survey the breadth of what bits can represent | Students name 2+ kinds of digitally-represented information | **Yes** |
| 12 | Same Bits, Different Interpretation | Meaning requires agreement | Students explain that the same bits could mean different things | No |
| 13 | Full Class 03 → Class 04 Bridge | Consolidate the whole continuity chain | Students restate the six-step chain | **Yes** |
| 14 | Interactive Activity | Let students build meaning themselves | Students invent and defend a 2–3 bit code | **Yes** |
| 15 | Misconceptions | Directly defuse common wrong models | Students can correct at least one misconception aloud | No |
| 16 | Recap | Verify understanding | Students answer recap questions in their own words | **Yes** |
| 17 | Final Takeaway | Close memorably, bridge forward | Students can repeat the final line's idea, not its wording | No |

---

## 8. Opening Mystery (0–6)

Do **not** open with "Today we will learn about binary." Open with a
genuine puzzle, exactly as Class 01 opened with smartphone use and Class
03 opened with the canteen question.

**Exact opening approach:**

1. Write, or simply say, two symbols: **0** and **1**.
2. Ask: *"These are just two symbols. How could a computer possibly use
   only these two symbols to represent something as complicated as a
   photograph?"*
3. **Do not answer.** Let students speculate freely for a minute or two.
4. Collect 2–3 guesses without judging any of them — even "I don't
   know, it just does" is a fine opening answer to bank.
5. Bridge: *"Hold onto your guess — by the end of today, you'll be able
   to actually explain this, not just believe it."*

**Questions and expected answers:**

| Question | Expected answers | If silence |
|---|---|---|
| "How could a computer represent a photo using only 0 and 1?" | "Lots of them combined somehow," "I don't know," "each pixel is a number" | Narrow it: "What if you had a thousand of these symbols instead of two — does that feel like it could hold more?" |

**How to handle silence:** Never let this hang more than ~10 seconds
unaddressed — this is a genuinely hard question to guess cold, so a
narrower nudge is expected, not a failure.

**Transition:** *"Let's back up. Last class we spent the whole time on
one word — data. Let's pick up exactly where we left off."*

---

## 9. Class 03 Callback (6–12)

Bring back Class 03's core statement exactly as it was left:

```
DATA = RECORDED INFORMATION ABOUT SOMETHING
```

**What the instructor says:**

> "Last class, what did we agree data actually is?"

Expected: **recorded information about something.**

> "Right. But we never asked one obvious follow-up question: once
> information is recorded, how does it actually sit *inside* a computer?
> A photo is information. A number is information. How does a machine
> that's really just electronics end up holding onto either one?"

**Do not answer this yet.** Let it stand as the reason the whole class
exists:

> "That's exactly today's question."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What is data, from last class?" | "Recorded information about something" |
| "Did we ever ask how that information sits inside a computer?" | Most will realize: "not really" |

**Transition:** *"So — if computers work with information like text,
images, and sound, how do they actually represent that information?
Let's start with something even more basic than a computer."*

---

## 10. Information Needs Representation (12–21)

**Ask first, before defining anything:**

> "A computer has to work with all kinds of things — numbers, letters,
> photographs, sounds, videos. Can a computer just 'look at' a photograph
> the way you do, and understand it?"

Expected: most students will correctly sense "no," even if they can't
articulate why yet.

**Push further:**

> "So if it can't just 'understand' it the way we do, what does it need
> instead?"

Guide toward: **some kind of stored form** — a representation.

**Land the core statement:**

> "A computer cannot simply *understand* a real-world object or idea.
> Information has to be represented in some form the computer can
> actually store and work with."

**Ask the big framing question and let it sit:**

> **"How can one machine represent so many different kinds of things —
> numbers, letters, photographs, sound, video — using the same
> hardware?"**

Do not resolve this yet — it is the thread the entire class pulls on.
Bank it visibly (say it out loud again later in Section 18).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Can a computer just 'understand' a photo like we do?" | No |
| "What does it need instead?" | Some kind of stored representation |
| "How can one machine represent so many different kinds of things?" | Genuine uncertainty — that's the point |

**Transition:** *"Let's not start with computers at all. Let's start with
something you already use every day: a light switch."*

---

## 11. Everyday Two-State Systems (21–29)

**Use a simple, universal example:**

> "A light switch. How many states does it have?"

Expected: **two — off and on.**

**Build a short list together of other two-state, everyday systems:**

- A light switch: off / on
- A yes/no question: no / yes
- A door: closed / open
- A coin: heads / tails

**Ask, and let it land:**

> "None of these are computers. But notice something: each one only
> needs *two* clearly different states to be useful. You never get
> confused about whether a light switch is 'sort of on.'"

**Land the core statement:**

> "Computers are built the same way — from things that reliably sit in
> one of two clear states. That's what we mean by **digital**: built from
> a small number of clearly distinct states, not a smooth, blurry range."

**Important nuance — say this explicitly:**

> "This doesn't mean everything in the real world is naturally
> two-state. A dimmer switch isn't off/on — it's a whole range. The point
> isn't that reality is binary. It's that computers *build* complex
> representations out of many simple, reliable two-state pieces."

Do **not** introduce voltage, transistors, or circuits — stay entirely
at the level of "clearly distinguishable states."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How many states does a light switch have?" | Two |
| "Name another everyday two-state system." | Yes/no, open/closed, heads/tails |
| "Does this mean everything in reality is naturally two-state?" | No — a dimmer switch isn't |

**Transition:** *"Computers use exactly this idea. There's a name for
one of these two-state units inside a computer — let's name it."*

---

## 12. What Is a Bit? (29–35) — NON-NEGOTIABLE

**Introduce the term directly now that the intuition is built:**

> "One of these simple, two-state units, inside a computer, is called a
> **bit** — short for *binary digit*. A bit can be in one of exactly two
> possible states. We write those states as **0** and **1**."

**Draw it plainly:**

```
0 | 1
```

**Say explicitly, this is an important guardrail:**

> "A bit isn't a special kind of number. It's just a label for 'one of
> two states.' We could just as easily call the two states 'off/on' or
> 'no/yes' — 0 and 1 are just the conventional symbols."

Do **not** explain the physical implementation (voltage levels,
transistors, magnetic states). If asked, use the parking-lot response
from Section 34.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "What is a bit?" | One of two possible states, written 0 or 1 |
| "Is a bit a special kind of number?" | No — just a label for one of two states |

**Transition:** *"Okay, but why two? Why not three states, or ten, like
our normal counting system?"*

---

## 13. Why Two States? (35–41)

**Ask directly:**

> "Why do you think computers settled on exactly two states, instead of,
> say, ten states like our decimal numbers?"

Let students guess — accept anything reasonable.

**Explain intuitively, without electronics:**

> "A system with two clearly, reliably distinguishable states is simple
> to build and simple to combine. Think about the light switch again —
> you never mistake 'off' for 'on.' Now imagine a switch with ten
> subtly different positions you had to tell apart reliably, every
> time, billions of times a second. Two clear states are just much
> easier to get right, over and over, at massive scale."

**Land the preferred phrasing (see Section 26 for the full guardrail
list):**

> "Prefer saying: *digital computers represent information using
> combinations of binary states.* Avoid saying computers 'only
> understand 0 and 1' as if that were some kind of limitation — it's a
> deliberate design choice because two reliable states are easy to build
> and combine."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Why two states instead of ten?" | Two reliable states are simpler and easier to build/combine at scale |

**Transition:** *"So we've got this one simple building block — a bit.
Let's see what it can actually do, starting with just one."*

---

## 14. One Bit (41–46) — NON-NEGOTIABLE

**Ask, and give real wait time:**

> "If we only have one switch — one bit — how many different messages
> can we send with it?"

Expected: **two.**

**Confirm and draw:**

```
1 bit → 2 possible states (0 or 1)
```

**Ask a grounding follow-up:**

> "Can you think of a real message that only needs two options? A yes/no
> answer to a single question, maybe?"

Expected: yes/no answers, yes/no light, a single true/false quiz
question.

**Land the limitation honestly — this sets up the next section:**

> "One bit is genuinely limited. Two options is not a lot. So what do we
> do if we need more than two possible messages?"

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How many different messages can one bit send?" | Two |
| "What's a real example of a two-option message?" | A yes/no answer, true/false |

**Transition:** *"Let's try adding a second switch and see what
happens."*

---

## 15. Multiple Bits (46–53) — NON-NEGOTIABLE

**Build this live, do not reveal it finished.**

> "Now imagine we have **two** switches instead of one. Each one can
> still only be 0 or 1. Let's list every possible combination of the
> two, together."

Build the list on the board, one at a time, ideally letting students
call them out:

```
00
01
10
11
```

**Ask, and let it land:**

> "How many combinations did we just find?"

Expected: **four.**

**Say explicitly:**

> "Two bits give us four possible combinations — four possible distinct
> messages, instead of just two."

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "List all the combinations two bits can make." | 00, 01, 10, 11 |
| "How many combinations is that?" | Four |

**Transition:** *"Notice something — we didn't just add two more
options, we *doubled* them. What do you think happens if we add a third
bit?"*

---

## 16. Binary Combinations (53–61) — NON-NEGOTIABLE

**Ask students to predict before revealing:**

> "If two bits give four combinations, how many do you think three bits
> will give?"

Let guesses happen — some will guess 6 (adding 2 again), some may guess
8. **Don't correct immediately** — reveal it by actually building the
list, or by extending the pattern visually:

```
1 bit  → 2 combinations
2 bits → 4 combinations
3 bits → 8 combinations
```

**Land the pattern intuitively — this is the whole point of the
section:**

> "Each extra bit *doubles* the number of possible combinations. That's
> the whole idea — you don't need to memorize a formula today. Just
> notice: one more switch means everything you had before, but now paired
> with both a 0 *and* a 1 for the new switch — so it doubles."

**Explicitly avoid turning this into arithmetic practice.** If a
stronger student pushes for the general rule, it's fine to briefly say
"this keeps doubling — n bits give 2 multiplied by itself n times — but
we're not going to drill that today," and move on. Do not write "2ⁿ" as
a formula to be memorized by the whole class.

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "How many combinations do 3 bits give?" | Eight |
| "What's the pattern as we add each bit?" | It roughly doubles each time |

**Transition:** *"So more bits give us more possible combinations. But
combinations of what? A combination like '01' doesn't mean anything on
its own yet — let's talk about that."*

---

## 17. Binary as a Representation System (61–68) — NON-NEGOTIABLE

**Land the core reframe of the whole class:**

> "Binary is not 'the thing itself.' A pattern like `01` doesn't *mean*
> anything by itself — it *represents* something, the same way a number
> or a word represents something."

**Explicit callback to Class 03 — do this, it's one of the strongest
connective threads in the class:**

> "Remember Class 3? The canteen being crowded was a real, physical
> fact. '80% full' was just our *recorded representation* of that fact —
> not the canteen itself. Binary works exactly the same way: a bit
> pattern is a representation of information, not the information
> itself, and definitely not the real-world thing the information is
> about."

**Draw the connecting chain (partial — the full version comes in Section
20):**

```
REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
    ↓
COMPUTER REPRESENTATION
    ↓
BITS
```

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Is a bit pattern the same thing as the information it represents?" | No — it's a representation of it |
| "What was Class 3's version of this same idea?" | "80% full" representing the crowded canteen |

**Transition:** *"So bits represent things. But what kinds of things,
exactly? Just numbers? Let's find out how far this idea stretches."*

---

## 18. Numbers, Text, Images, and Sound (68–76) — NON-NEGOTIABLE

**Return explicitly to the question banked in Section 10:**

> "Earlier I asked: how can one machine represent so many different
> kinds of things — numbers, letters, photographs, sound, video — using
> the same hardware? Let's actually list them out."

Build a simple list live:

```
NUMBER
TEXT
IMAGE
SOUND
VIDEO
      ↓
   BITS
```

**For each, ask briefly (don't over-explain any one):**

> "Do you think a *number* could be represented with combinations of
> bits?" → Yes, most will sense this already.
> "What about a *letter*, or a whole word?" → Let students reason —
> "maybe each letter gets its own pattern of bits?"
> "What about a *photograph*?" → This is the hardest one to intuit —
> let it stay a little mysterious: "somehow, yes — we're not going to
> learn exactly how today, but the short version is that a photo is
> broken into many tiny pieces, and each piece gets its own bit
> pattern."
> "What about *sound*, or *video*?" → Similar: "yes, in principle — very
> different information, same underlying building block."

**Land the surprising idea, said plainly:**

> "Very different kinds of information — a number, a word, a photograph,
> a song — can all ultimately be represented using combinations of the
> exact same building block: bits. That's genuinely surprising the first
> time you really sit with it."

**Do NOT teach the actual encoding mechanisms.** If pixels, sampling, or
character encoding come up, use the parking-lot response (Section 34).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Could a number be represented with bits?" | Yes |
| "Could a letter or word?" | Yes, plausibly — each gets some pattern |
| "Could a photograph?" | Yes, though the mechanism stays a mystery today |
| "What's surprising about all of this?" | Totally different information types share the same building block |

**Transition:** *"If the exact same bit pattern could theoretically be
used for a number or a letter, how do we know which one it actually is?
What decides the meaning?"*

---

## 19. Same Bits, Different Interpretation (76–83)

**Pose the key question:**

> "Does a sequence of bits carry its meaning by itself, or does something
> else decide what it means?"

**Use a simple non-computer analogy:**

> "Think about the marks 'S O S.' Those three marks mean something very
> specific to us — a distress signal — because we've all agreed on that
> meaning. The same three letters, in a different context, might just be
> someone's initials. The marks didn't change. What changed?"

Expected: **the system of interpretation, the agreed-upon rule, changed
— not the marks themselves.**

**Land the core statement:**

> "A sequence of bits has meaning because we agree on how to interpret
> it. The exact same pattern, say `01000001`, means nothing on its own —
> it only means something once some system says 'when you see this
> pattern, treat it as ___.'"

**Do not introduce formal encoding standards** (ASCII, Unicode) by name
here — this is preparation for a *later* class, not this one. If a
student already knows the term, acknowledge briefly and move on (see
Section 34).

**Questions and expected responses:**

| Question | Expected response |
|---|---|
| "Does a bit pattern carry its own meaning?" | No — meaning comes from an agreed interpretation |
| "What matters more: the bits themselves, or how we interpret them?" | Both matter, but the interpretation is what turns a pattern into meaning |

**Transition:** *"Let's put the entire day's reasoning on one board —
starting all the way back at Class 3."*

---

## 20. Full Class 03 → Class 04 Bridge (83–89) — NON-NEGOTIABLE, HERO MOMENT

**This is the HERO MOMENT of the class.** Build it live, top to bottom,
one line at a time — never reveal it finished.

1. Write **REAL WORLD** — *"Something real is happening — a crowded
   canteen, a photograph, a sound."*
2. Arrow down, write **OBSERVATION** — *"Someone notices or checks
   something about it."* (Class 3)
3. Arrow down, write **DATA** — *"That gets recorded — data is recorded
   information about something."* (Class 3)
4. Arrow down, write **REPRESENTATION** — *"The computer needs some form
   it can actually hold onto."* (today)
5. Arrow down, write **BITS** — *"That representation is ultimately
   built from combinations of two-state units."* (today)
6. Arrow down, write **COMPUTER PROCESSING** — *"Only now can the
   computer actually do something with it."* (today, opens the door to
   future classes)

Finished board:

```
REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
    ↓
REPRESENTATION
    ↓
BITS
    ↓
COMPUTER PROCESSING
```

**Say explicitly, this is the whole point of the diagram:**

> "The top three lines are exactly what Class 3 taught you. Today we
> extended the chain — data doesn't just sit there, it has to become a
> representation, and that representation is built out of bits, before a
> computer can process it at all."

**Do not compress this block below 5 minutes**, even under time
pressure — see Section 32.

---

## 21. Interactive Reasoning Activity — Tiny Binary Communication System (89–99) — NON-NEGOTIABLE

**This is the HERO ACTIVITY.** No electronics, no real encoding — this is
a reasoning and invention activity.

### Facilitator instructions (timed, ~10 minutes at canonical pace)

1. **(1 min) Set up:** "You have 2 bits to work with. That gives you 4
   possible combinations: `00`, `01`, `10`, `11`. Your job: invent a
   meaning for each one."
2. **(3 min) Let students invent, individually or in pairs.** Offer a
   theme if they're stuck — e.g., "invent a tiny traffic-light-style
   signal," "invent a code for four moods," "invent a code for four
   colors." A concrete example to unstick a stuck group: `00 = RED`,
   `01 = GREEN`, `10 = BLUE`, `11 = YELLOW`.
3. **(3 min) Collect 2–3 different inventions from different
   students/pairs.** Write a couple on the board side by side — it's
   valuable for students to see that two people can assign *different*
   meanings to the identical four patterns.
4. **(2 min) Ask the key question:** *"Did the bits themselves contain
   the meaning?"*
5. **(1 min) Land the realization:** *"No — the meaning came from the
   system you agreed on. The bits were the same for everyone; the
   meaning wasn't, until you decided it."*

### Questions and expected responses

| Question | Expected response |
|---|---|
| "Did the bits themselves contain the meaning?" | No |
| "Where did the meaning actually come from?" | The rule/agreement the student invented |
| "If two people used the same 2 bits for different meanings, whose is 'right'?" | Neither/both — meaning is a matter of agreement, not something built into the bits |

**Do not introduce formal encoding terminology** here (no "encoding
scheme," no "protocol") — plain language only: "invented meaning,"
"agreed system."

### Timing, extension, and support

- **Canonical timing:** ~10 minutes, per the breakdown above.
- **Stronger-student extension:** Ask them to design a 3-bit code (8
  combinations) for something with 8 categories, e.g., days worth
  tracking or a small set of subjects.
- **Weaker-student support:** Give them a fully worked example (the
  RED/GREEN/BLUE/YELLOW one above) and ask them to just invent one
  *different* assignment of the same four patterns to four other
  things.
- **Transition back to the main lesson:** "You just did, by invention,
  exactly what real computer systems do at a much larger scale — agree
  on what a pattern of bits means, then use that agreement consistently."

---

## 22. Misconceptions — In-Class Handling (99–104)

Pick 2–3 of the misconceptions most likely to have surfaced already
today (see Section 25 for the full reference table) and address them
directly and briefly. Use this pattern for each: **name it → reframe it
→ return to the day's core diagram.**

Suggested priority order for in-class handling:

1. "Computers only understand 0 and 1" (very likely to have come up in
   Section 8 or 13).
2. "A photograph is made of 0s and 1s in the real world" (likely surfaced
   in Section 18).
3. "More bits automatically means better information" (worth pre-empting
   before students over-generalize Section 16's doubling pattern).

Keep this to 5 minutes — this is a quick defusal pass, not a new lecture.

---

## 23. Recap (104–108) — NON-NEGOTIABLE

Do **not** repeat definitions. Ask students to *explain*, in their own
words, in the last several minutes:

1. **"Why does a computer need a representation of information at
   all?"** *Expected:* it can't "just understand" a real-world thing the
   way a person does.
2. **"What is a bit?"** *Expected:* one of two possible states, written
   0 or 1.
3. **"How many combinations do 2 bits give? 3 bits?"** *Expected:* four;
   eight.
4. **"Is binary 'the thing itself,' or a representation?"** *Expected:*
   a representation — like "80% full" represented the canteen.
5. **"Name two different kinds of information that can be represented
   with bits."** *Expected:* any two of number, text, image, sound,
   video.
6. **"Where does meaning actually come from?"** *Expected:* an agreed
   interpretation, not the bits themselves.
7. **"How does this connect to Class 3?"** *Expected:* `REAL WORLD →
   OBSERVATION → DATA → REPRESENTATION → BITS → COMPUTER PROCESSING`.

Accept answers in the student's own words — this is a formative check,
not a graded quiz.

---

## 24. Final Takeaway (108–110)

**Close with the final statement, said slowly:**

> "Computers do not need a different kind of machine for every kind of
> information. They can build many kinds of digital information from the
> same basic building block: bits."

**Then leave the bridge-forward question open, explicitly not answered
today:**

> "If the same building blocks can represent numbers, text, images, and
> sound, what determines what those bits actually mean? That question is
> exactly where we'll pick up next."

Do not resolve this — it is intentionally a hook into a future class.

---

## 25. Common Misconceptions — Full Reference

For each: **listen for** it, use a **short reframe**, never shame the
student who raised it, and **return to the mental model** rather than
arguing the point in the abstract.

| # | Misconception | Listen for | Short reframe | Return to |
|---|---|---|---|---|
| 1 | "Computers only understand 0 and 1." | "Isn't that a limitation?" | "Computers *represent and process* information using binary states — it's a deliberate design choice, not a limitation, because two reliable states are simple to build and combine." | Section 13 |
| 2 | "Binary is just a weird way of writing numbers." | Treating binary as decimal-with-extra-steps | "Binary is a representation system that can be used for many kinds of information — numbers, text, images, sound — not only numbers." | Section 18 |
| 3 | "One bit can represent anything." | Overgeneralizing from "a bit is powerful" | "One bit has only two possible states. More bits allow more possible combinations — that's exactly why we needed more than one." | Section 14–16 |
| 4 | "A photograph is made of 0s and 1s in the real world." | Confusing the representation with the real thing | "The photograph — the real-world moment — is not made of bits. The *computer's stored representation* of it is built from bits. The two are not the same thing." | Section 17 |
| 5 | "More bits automatically means better information." | Assuming quantity of bits alone improves quality | "More bits give more possible *combinations* — whether that actually improves a representation depends entirely on how those bits are used, not just how many there are." | Section 16 |

---

## 26. Instructor Language / Teaching Guardrails

**Prefer:**

- "Computers represent information using binary states" — **over** "computers understand only 0 and 1."
- "Bits are building blocks of digital representation" — **over** "everything is literally 0 and 1."

**Avoid:**

- "Binary is the language of computers" — unless immediately qualified
  (it invites the misconception that binary carries meaning by itself;
  Section 19 exists specifically to correct this).
- Any deep physical/electrical explanation of what a bit "really is"
  inside hardware.

**The instructor must NOT**, at any point in this class:

- teach digital logic, Boolean algebra, or logic gates
- explain computer architecture or CPU internals
- explain transistor physics or electronics
- explain memory or storage architecture
- teach ASCII, Unicode, UTF-8, or any character-encoding standard
- teach hexadecimal
- drill binary-to-decimal arithmetic
- teach programming of any kind
- teach data structures, algorithms, networking, file formats,
  compression, or cryptography

**If students ask advanced questions**, use this exact redirect pattern:

> "Good question. We'll build toward that later. Today we're
> understanding *why* computers represent information the way they do —
> not the exact mechanism."

Then return to whichever anchor fits the moment:

```
REAL WORLD → OBSERVATION → DATA → REPRESENTATION → BITS → COMPUTER PROCESSING
```

See Section 34 for a fuller parking-lot script for specific advanced
questions likely to come up.

---

## 27. Interaction Philosophy

Class 04 should be interactive throughout, but **not every section needs
to be a formal activity** — use questions strategically rather than
turning each block into a structured exercise.

**Sample questions to use across the class** (from the brief, reproduced
here for quick reference):

- "If one switch has two states, how many different messages can it
  represent?"
- "What happens when we add another switch?"
- "If computers can represent numbers with bits, could they represent
  letters?"
- "What about a photograph?"
- "How could millions of tiny binary decisions possibly describe an
  image?"
- "What matters more: the bits themselves, or how we interpret them?"

**Not every question needs a single correct answer.** Some — especially
"how could millions of tiny binary decisions describe an image?" — exist
purely to generate curiosity and should be allowed to remain a little
unresolved, on purpose, as a hook toward later classes.

**Default wait time:** 3–5 seconds for ordinary comprehension questions.

**Extended wait time:** 8–12 seconds for the two hardest reasoning
moments — the opening mystery (Section 8) and "how could a photograph
possibly be represented this way?" (Section 18). Do not rescue students
from silence too early on these.

**Built-in reasoning opportunities to protect, in priority order:**

1. The opening mystery (Section 8)
2. One bit → two states, two bits → four (Sections 14–15)
3. Predicting the doubling pattern (Section 16)
4. "Did the bits themselves contain the meaning?" (Section 21)
5. The Class 03 → Class 04 bridge reconstruction (Section 20, 23)

---

## 28. Visual / Board Plan

These are the key drawings later Pen-Tablet and Presentation artifacts
will build on. Do not create those artifacts now — this section only
specifies what they must contain.

**Drawing 1 — A Two-State Switch**
Built live in Section 11. `OFF ↔ ON`, plus 2–3 other everyday two-state
examples listed alongside it.

**Drawing 2 — One Bit**
Built live in Section 12, reused in Section 14. `0 | 1`, labeled "one
bit — one of two possible states."

**Drawing 3 — Two Bits**
Built live in Section 15. The four combinations `00, 01, 10, 11`,
revealed one at a time.

**Drawing 4 — Growth Pattern**
Built live in Section 16.

```
1 bit  → 2 combinations
2 bits → 4 combinations
3 bits → 8 combinations
```

**Drawing 5 — HERO — Full Bridge**
Reserved for Section 20.

```
REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
    ↓
REPRESENTATION
    ↓
BITS
    ↓
COMPUTER PROCESSING
```

Mark this as a **live construction** — do not show the completed
six-line chain before students have reasoned their way to each new piece
across the class. This is the single most important drawing of Class
04, the same way the six-line chain was the hero drawing of Class 03.

**Drawing 6 — Many Information Types, One Building Block**
Built live in Section 18.

```
NUMBER
TEXT
IMAGE
SOUND
VIDEO
      ↓
   BITS
```

Keep every diagram simple — no electronics symbols, no circuit
diagrams, no pixel grids.

---

## 29. Class 01–04 Continuity

Explicitly narrate where Class 04 sits in the course staircase — this
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

```
REAL WORLD → OBSERVATION → DATA
DATA → EXAMPLES → FEATURES → LABELS → DATASET
```

**Class 4:**

Opens up what happens to **DATA** once a computer actually has to hold
onto it — `DATA → REPRESENTATION → BITS`.

**Say this once, clearly (Section 9 or Section 20 are the natural
spots):**

> "We are not changing anything from Class 3. We're looking even more
> closely at one part of it — what happens to data once a computer has
> to actually store and process it."

This is the same continuity statement pattern used in Classes 02 and 03
— it is what turns four separate classes into one staircase instead of
four unrelated topics.

---

## 30. Assessment of Understanding

There is no separate formal assessment artifact at this stage — use
informal checks only, throughout the class, not at the end alone.

A student is demonstrating real understanding if they can:

1. Explain why computers need representations.
2. Explain what a bit is.
3. Explain why one bit has two possible states.
4. Explain why more bits allow more combinations.
5. Explain why binary is not limited to numbers.
6. Give examples of information that can be represented digitally.
7. Explain that meaning depends on interpretation/representation.
8. Connect Class 03's DATA concept to Class 04's computer representation
   concept.

**Do not** judge understanding solely from students correctly repeating
the definitions in Section 5 — repeating "a bit is 0 or 1" proves
memorization, not understanding. The tiny binary communication activity
(Section 21) and the doubling-pattern prediction (Section 16) are the
two strongest real-time understanding signals in the class.

---

## 31. Differentiation

**For students struggling:** Anchor entirely in the concrete progression
already built into the class — don't add new material, just slow the
existing one down:

```
OFF / ON
   ↓
 0 / 1
   ↓
ONE BIT
   ↓
MORE BITS
   ↓
MORE POSSIBILITIES
```

Walk this exact chain with them step by step rather than introducing a
different explanation.

**For students moving quickly:** Ask deeper conceptual questions about
representation and interpretation rather than accelerating into
implementation detail:

- "Could two completely different pieces of information ever end up
  with the exact same bit pattern? What would that require?"
- "If meaning comes from interpretation, what has to happen for two
  different computers to understand each other's bits the same way?"
- "Why do you think the same building blocks (bits) work for such
  different information types, instead of each type needing its own
  special hardware?"

Do **not** introduce advanced implementation details (encoding
standards, hardware) even for fast movers — deepen the *concept*, not
the *mechanism*. See Section 33 for the full extended-version guidance.

**For students who stay quiet:** The tiny binary communication activity
(Section 21) and the everyday two-state examples (Section 11) are the
easiest re-entry points — both are low-stakes and have no risk of a
starkly "wrong" answer.

---

## 32. Time Management / Timing Safety

**Must cover, in priority order** (matches the non-negotiable list in
Section 7):

1. The need for representation (Section 10)
2. What a bit is (Section 12)
3. One bit → two states, more bits → more combinations (Sections 14–16)
4. Binary as a representation system (Section 17)
5. Many information types share the same building block (Section 18)
6. The full Class 03 → Class 04 bridge (Section 20)

**Can shorten:**

- Extended examples in Sections 11 and 18 (use 2–3 examples instead of
  the full list)
- The tiny binary communication activity (Section 21) — compress to a
  single quick round with one theme instead of open invention
- The misconception discussion (Section 22) — pick just one instead of
  2–3

**Can expand** (see Section 33 for detail):

- Let students discover the binary combination pattern themselves for a
  4-bit case before revealing it
- Run a second round of the tiny communication-system activity with a
  3-bit code
- Spend more time on the interpretation discussion (Section 19)

**Do not cut:** the Class 03 connection (Sections 9 and 20), the
one-bit/two-bit build-up (Sections 14–15), or the tiny binary
communication activity (Section 21) — these are the load-bearing walls
of the entire class.

### 90-minute version

Trim as follows: Opening Mystery to 4 min, Class 03 Callback to 4 min,
Information Needs Representation to 7 min, Everyday Two-State Systems to
6 min, What Is a Bit? unchanged (6 min), Why Two States? to 4 min, One
Bit to 4 min, Multiple Bits unchanged (7 min), Binary Combinations to 6
min, Binary as a Representation System unchanged (7 min), Numbers/Text/
Images/Sound to 6 min, Same Bits Different Interpretation to 5 min, Full
Bridge unchanged (6 min), Interactive Activity compressed to 6 min,
Misconceptions to 3 min, Recap to 3 min, Final Takeaway unchanged (2
min). Total ≈ 86 minutes.

### 120-minute version

Add time back to: Everyday Two-State Systems (+2 min, let students
generate more examples), Binary Combinations (+3 min, let students work
out the 4-bit case themselves before revealing it), Numbers/Text/Images/
Sound (+2 min, spend longer letting students reason about the
photograph case specifically), Interactive Activity (+3 min, run a
second round with a 3-bit code per Section 33).

---

## 33. Extended Version

If time allows, deepen reasoning — do **not** introduce any new
technical scope.

- Let students work out the 4-bit combination count themselves
  (`16`) before you confirm it, extending the doubling pattern from
  Section 16.
- Run a second round of the tiny binary communication-system activity
  (Section 21) using 3 bits (8 combinations) instead of 2.
- Spend longer on the interpretation discussion (Section 19) — ask
  students to invent their own version of the "S O S" analogy from
  everyday life (a marks/symbols example whose meaning depends entirely
  on agreed context).
- Ask students to compare two different pairs' inventions from the
  activity in more depth: "if you had to combine your two systems into
  one, what would you need to agree on first?"

---

## 34. Advanced Topics Parking Lot

| If a student asks... | Short answer | Park with |
|---|---|---|
| "What is ASCII / Unicode / UTF-8?" | "Those are specific, real systems for turning text into bits — real, and coming later." | "Today we're only asking *why* representation works this way, not the exact standards." |
| "How many bits are in a byte?" | "A byte is a small group of bits — a real and useful idea, just not today's focus." | Return to: "today's building block is the bit itself." |
| "How do you convert binary to decimal?" | "That's a real, learnable skill — a later class's territory." | Return to: `MORE BITS → MORE POSSIBLE COMBINATIONS`. |
| "What's hexadecimal?" | "Another way of writing groups of bits compactly — real, but not today." | Same as above. |
| "How do pixels actually work?" | "A photo gets broken into many tiny pieces, each represented with bits — the exact mechanism is a later class." | Return to Section 18's list. |
| "How does audio get turned into bits?" | "Sound gets measured very rapidly and each measurement becomes a bit pattern — real, but a later class's detail." | Same as above. |
| "How does image/file compression work?" | "A real and clever topic — about making representations smaller — for later." | Return to: representation vs. the thing itself (Section 17). |
| "What is memory / storage, physically?" | "Where bits actually get held onto physically — real hardware topic, later class." | Return to: "today we're not going inside the machine." |
| "What are logic gates / transistors?" | "The actual physical building blocks that make bits work — a real and fascinating topic, just not today's altitude." | Return to: "today we stay at the level of *what* a bit is, not *how* it's physically built." |

---

## 35. Teacher FAQ

**Q: Why does a computer use two states?**
A: Two clearly, reliably distinguishable states are simple to build and
simple to combine at massive scale — see Section 13.

**Q: Why not use ten states like decimal numbers?**
A: In principle you could design a ten-state system, but reliably
telling ten subtly different states apart, billions of times a second,
is much harder than telling two clearly different states apart. Two
states is a deliberate engineering choice, not a limitation.

**Q: Is a bit always physically a voltage?**
A: In most modern computers, yes, typically — but that physical detail
is intentionally out of scope for this class. Today's bit is a
conceptual "one of two states," not a circuit lesson.

**Q: Is everything on a computer really 0s and 1s?**
A: At the level of representation, yes — but say it carefully: "computers
represent and process information using combinations of binary states,"
not "everything IS 0 and 1" as if the 0s and 1s themselves were the
content.

**Q: Can images really be represented with bits?**
A: Yes — conceptually, an image gets broken into many tiny pieces, and
each piece's information is represented as a bit pattern. The exact
mechanism is a later class's topic.

**Q: How can text become bits?**
A: Conceptually, each letter or character gets assigned its own bit
pattern by an agreed system — exactly like the "invent your own code"
activity in Section 21, just at a much larger, standardized scale. The
specific systems (ASCII, Unicode) are for a later class.

**Q: Does more bits mean better quality?**
A: More bits give more possible *combinations* — whether that improves
quality depends entirely on how those combinations are used, not the
raw count. See Misconception 5 in Section 25.

**Q: Why do different things (numbers, text, images) use the same
bits?**
A: Because a bit is just a building block — a two-state unit. What
turns a bit pattern into "a number" versus "a letter" versus "part of a
photo" is the system of interpretation applied to it, not anything
different about the bits themselves. See Section 19.

---

## 36. Class Success Check

By the criteria in Section 1, this class has succeeded if, without
prompting, most students can:

1. Explain why a computer needs a representation of information before
   it can work with it.
2. Define a bit as one of two possible states.
3. Explain why one bit gives two possibilities and why more bits give
   more, roughly doubling each time.
4. State that binary is a representation system, not "the thing itself"
   and not a special kind of number.
5. Name at least two different kinds of information (beyond numbers)
   that can be represented digitally.
6. Explain that the same bits mean different things depending on how
   they're interpreted.
7. Reconnect today's ideas to Class 03's `DATA` box, restating the full
   chain `REAL WORLD → OBSERVATION → DATA → REPRESENTATION → BITS →
   COMPUTER PROCESSING`.

A class where most students can do these in plain, imperfect language —
not exact textbook wording — has met the bar.

---

## 37. Source-of-Truth / QA Checklist

Verified against the class brief before finalizing this guide:

- [x] Class 03 continuity is explicit (Sections 3, 9, 17, 20, 29).
- [x] The class starts with intuition, not a definition (Section 8).
- [x] Bit is introduced clearly and only after intuition is built
      (Section 12).
- [x] One bit = two possible states (Section 14).
- [x] More bits = more possible combinations, introduced intuitively as
      doubling, not as a formula to drill (Sections 15–16).
- [x] Binary is presented as a representation system (Section 17).
- [x] Binary is explicitly not restricted to numbers (Section 18).
- [x] Numbers, text, images, sound, and video are introduced only
      conceptually, with mechanisms explicitly parked (Section 18,
      Section 34).
- [x] Meaning/interpretation is explained (Section 19, Section 21).
- [x] No advanced encoding standards are taught (guarded in Sections 1,
      26, 34).
- [x] No programming is required or taught (Section 1, Section 26).
- [x] No digital logic is taught in depth (Section 1, Section 26).
- [x] No computer architecture is taught (Section 1, Section 26).
- [x] No electronics/transistor details are taught (Section 1, Section
      12, Section 26).
- [x] No binary arithmetic drill dominates the class (Section 16
      explicitly warns against this).
- [x] Misconceptions are explicitly handled, both in-flow (Section 22)
      and as a full reference (Section 25).
- [x] The tiny binary communication activity reinforces representation
      and interpretation (Section 21).
- [x] The class remains appropriate for first-year students with no
      assumed binary knowledge (Section 1, Section 31).
- [x] The class has a clear, explicit, unresolved bridge to future
      Computer Science topics (Section 24, Section 34).
- [x] This Master Guide is self-contained and usable by an instructor
      without relying on the Student Notes — every section includes
      instructor wording, questions, expected answers, and transitions.
