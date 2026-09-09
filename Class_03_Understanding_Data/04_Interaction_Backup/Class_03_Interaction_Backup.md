# Class 03 — Interaction Backup

**Bong Study Hub — Foundation Batch 2026**
**Understanding Data** — *From the Real World → Information → Data*

---

## How to Use This

This is a **backup bank**, not a second lesson plan. The real teaching
flow lives in the **Master Instructor Guide** — its sections, timings,
and non-negotiable moments are what actually run the class. Nothing
here is mandatory.

Reach for this document when you want:

- an extra question because the room needs more warm-up
- a different way to ask something that isn't landing
- a fallback for a quiet class, or an extension for a fast one
- one clean rapid-fire pass to check the room before moving on

**Choose based on:** class energy, time remaining, how much students
are already participating, and whether a specific concept needs a
second pass. You will not use most of this in any single class — that's
fine, it's here for whichever moment actually needs it.

**A note on open-ended items:** some prompts below are marked
**(open-ended)** — for these, several different answers are reasonable
and the example directions given are illustrations, not a checklist to
tick off. Don't correct a student toward the listed examples; the goal
is the reasoning, not the list.

---

## 1. Opening Questions

Alternatives to (or extra rounds around) the canteen opening in Guide
§8, all circling the class's central question: *"How do we turn
something happening in the real world into something a computer can
work with?"*

| Question | Purpose | Expected direction | Follow-up |
|---|---|---|---|
| "If I say the canteen is crowded, is that data?" | Surface the naive "data = numbers" assumption early | Split opinions — some say only a number counts | "What if I said '80% full' instead — does that change your answer?" |
| "What could we record about a crowded canteen?" | Open up the range of possible observations | Headcount, a photo, a feeling, a percentage, a queue length | "Which of those would still make sense to someone who wasn't there?" |
| "Is 'very crowded' data? Why?" | Push directly on the numbers-only assumption | Some will say no because it isn't a number | "Is it information about the real world? That's the only test we're using today." |
| "What would make that observation useful later?" | Introduce the "recorded" step before naming it | Writing it down, telling someone, saving it somewhere | "So what's the difference between noticing something and it becoming data?" |

---

## 2. Data or Not Data?

A quick classification warm-up. Read out each item and ask: **"Can
this become data?"** — thumbs up/down or a quick show of hands works
well.

| Item | Likely instinct | What to draw out |
|---|---|---|
| A photograph of the classroom | "Maybe not — it's just a picture" | It's recorded information about a moment — yes, it's data |
| Someone's observation that it is raining, said out loud | Mixed | Only becomes data once it's recorded in some form (even a spoken statement someone notes down counts) |
| A temperature reading | "Yes, obviously" | Confirm — this is the case nobody debates, useful as an anchor |
| An unrecorded thought, never shared or written | "Yes?" | This is the trap item — if it's never recorded, it never became data. Nothing to observe *from the outside* |
| A voice recording | Mixed | Recorded information — yes, even though it isn't text or numbers |
| A student's attendance record | "Yes" | Confirm — a familiar, uncontroversial example |
| A live event nobody observed or recorded (e.g., a tree falling with no one around) | "No" | This is the second trap item — the event is real, but with no observation and no record, there is nothing to call data yet |

**Important:** don't let this become a strict right/wrong quiz. The
point isn't a perfect score — it's landing the one real test:
*was something recorded?* The two "trap" items (an unshared thought, an
unobserved event) exist to make that test concrete, not to catch
students out.

**Instructor wrap-up line:** "Every 'yes' in that list was recorded
information about something real. That's the whole definition — data
is recorded information about something."

---

## 3. Real World → Observation → Data

Extra scenarios beyond rain and the canteen (Guide §11), in case you
want a second or third pass at the same chain.

| Scenario | Real world | Observation | Recorded data |
|---|---|---|---|
| Traffic | Cars moving on a road | Someone checks how many cars, how fast, how backed up | "Heavy traffic," a car count, a travel-time estimate |
| Classroom attendance | Students physically present today | Someone checks who showed up | A list of names, a headcount, a percentage |
| A hot day | The actual temperature outside | Someone checks a thermometer or just how it feels | "34°C," "really hot today" |

For each: ask **"What's the real-world thing? What got observed? What
got recorded?"** — in that order, without answering ahead of the
students.

---

## 4. One Thing, Many Pieces of Data

**Ask:** "If we wanted to describe a student using recorded
information, what could we record?"

Let the list build freely — name, year, department, attendance, marks,
height, favorite subject, hometown, whatever comes up. **(open-ended)**
There is no fixed list to reach; the point is simply that it keeps
growing.

**Follow-up:** "Did the student change while we were listing all of
that?" → No. "Did the description change?" → Yes, every time we added
one more piece.

**Takeaway:** one real-world thing can be represented by many different
pieces of data at once — none of them alone *is* the student.

---

## 5. Read the Table

Use the Class 03 student table:

| Student | Year | Attendance | Marks |
|---------|------|------------|-------|
| A | 1 | 82% | 76 |
| B | 1 | 91% | 84 |
| C | 1 | 68% | 61 |

| Question | Expected answer |
|---|---|
| What does row A represent? | One student — one example |
| What does the Attendance column represent? | One kind of information, recorded for every student |
| How many examples are there? | Three |
| What makes the whole table a dataset? | It's a collection of related examples |

**Reinforce, said slowly:** `ROW → ONE EXAMPLE`, `COLUMN → ONE KIND OF
INFORMATION`.

---

## 6. Spot the Mess

| Student | Age | City |
|---------|-----|------|
| A | 18 | Kolkata |
| B | "eighteen" | kolkata |
| C | *missing* | Calcutta |

**Ask:** "What problems can you spot?" Give real wait time — let
students hunt before naming anything.

Expected finds: a missing value (C's age), an inconsistent format
(B's age written as a word), inconsistent naming (Kolkata / kolkata /
Calcutta all referring to the same city).

**Do not** turn this into a data-cleaning lesson — no fixing, no rules
for what to do about it. The only takeaway is: **real-world data can be
messy.**

---

## 7. More Data vs. Better Data

**Ask:** "Would one million examples always be better than one
thousand?"

Then contrast:

| Dataset A | Dataset B |
|---|---|
| 1,000,000 examples | 1,000 examples |
| Mostly incorrect or repetitive | Accurate, covering useful variety |

**Ask:** "Which would you rather use, and why?"

**Expected direction:** quantity alone doesn't determine usefulness —
Dataset B is better despite being much smaller.

**Reinforce:** `MORE DATA ≠ AUTOMATICALLY BETTER DATA`. If useful,
callback: "this is the same idea behind Class 02's cats-vs-dogs
example — the issue was never purely how many photos there were."

---

## 8. Feature or Label?

Email: *"Win free money!"* · Sender: Unknown · Time: 2:14 AM · Known
category: Spam

| Question | Expected answer |
|---|---|
| Which information describes the email? | The email text, the sender, the time — the features |
| Which piece tells us the known category? | "Spam" |
| What would be the label here? | "Spam" |
| Would every dataset necessarily have a label? | No — some datasets are just examples described by features, with no label at all |

**Do not** introduce the term "supervised learning" here — that's a
later class. "Feature" and "label" are as far as today goes.

---

## 9. The Canteen Question **(open-ended)**

**Central prompt:** "Can we predict when the college canteen will be
crowded?" — "What information might help?"

Let the list grow freely: time of day, day of the week, number of
students on campus, whether there's a class break, weather, past
crowd patterns. **This list is illustrative, not exhaustive or
official** — a reasonable suggestion outside it should never be waved
off just because it isn't listed here.

**Teaching point, not a fact to memorize:** `THE QUESTION DETERMINES
WHAT DATA IS USEFUL.`

---

## 10. Change the Question **(open-ended)**

**Ask:** "If our question changes from 'Can we predict canteen
crowding?' to 'Will a student like this movie?', would the same data
still be useful?" → No, mostly not.

**Then:** "What information might become useful instead?" — genre,
reviews, previous ratings, favorite actors, mood. Again, illustrative
only.

**Takeaway:** `DIFFERENT QUESTION → DIFFERENT USEFUL DATA.`

---

## 11. Data as a Lens

Student example: Name, Year, Attendance, Department, Marks.

**Ask:** "Does this completely describe the student?" → No.
**Then:** "What important things are missing?" — interests,
personality, hobbies, friendships, and so on.

Keep this at the level of the *category* of thing left out (interests,
personality) rather than asking about any real student's own life —
this is a conceptual point about representation, not a prompt to
discuss individual students' personal details.

**Takeaway:** `DATA IS A REPRESENTATION OF REALITY. EVERY
REPRESENTATION LEAVES SOMETHING OUT.`

---

## 12. Class 02 Callback

One of the strongest items in this backup — use it whenever you want a
fast, satisfying connection back to last class.

1. Ask students to reconstruct, from memory: `DATA → LEARNING → MODEL
   → PREDICTION`.
2. Ask: "Where does the DATA come from?"
3. Guide toward: `REAL WORLD → OBSERVATION → DATA`.
4. Reveal the full chain together: `REAL WORLD → OBSERVATION → DATA →
   LEARNING → MODEL → PREDICTION`.

---

## 13. Rapid-Fire Concept Check

Read these one at a time, 10–20 seconds each, verbally answered — no
need to go in order, and no need to use all eight.

1. Is data always a number?
2. What makes an observation become data?
3. Give one example of non-numeric data.
4. What does one row represent?
5. What does one column represent?
6. What is a dataset?
7. What is a feature?
8. What is a label?
9. Does every dataset have a label?
10. Does more data always mean better data?

**Answer key** *(for the instructor only — don't reveal until after
students answer)*:

1. No — it's recorded information about something; numbers are one
   form it can take.
2. Being recorded in some form that can be stored or worked with.
3. A photo, a voice recording, a sentence, a location — any one.
4. One example.
5. One kind of information, recorded across all examples.
6. A collection of related examples.
7. A piece of information describing an example.
8. The known answer or category attached to an example, when one
   exists.
9. No.
10. No — quality and variety matter more than raw quantity.

---

## 14. If Students Are Quiet

- Ask for a show of hands instead of a spoken answer.
- Give 20 seconds of silent thinking time before taking any answer.
- Ask them to turn to the person beside them for 30 seconds first.
- Ask for two different answers rather than "the" correct one.
- Re-anchor in an everyday example before repeating the conceptual
  question.

---

## 15. If Students Are Moving Too Fast

Deepen the same concepts — do not introduce new scope.

- "Can the same piece of data be useful for one question but useless
  for another?" **(open-ended)**
- "Can two different observations produce different representations of
  the same real-world event?" **(open-ended)**
- "If we record only one aspect of something, what might we miss?"
  **(open-ended)**
- "Can a dataset contain examples but no labels?" *(conceptual — yes)*

---

## 16. If Time Is Running Short

If you can only run a handful of interactions today, keep these six —
they cover every non-negotiable concept in the Master Guide:

1. Data or Not Data? (§2)
2. Real World → Observation → Data (§3)
3. Read the Table (§5)
4. Feature or Label? (§8)
5. The Canteen Question (§9)
6. Class 02 Callback — full pipeline reconstruction (§12)

Used selectively rather than in full, this set runs roughly
15–20 minutes.

---

## 17. Final Verbal Check

Close with five questions, answered in the students' own words:

1. What is data?
2. Where does data come from?
3. What is a dataset?
4. What is the difference between a feature and a label?
5. Why does the question determine what data is useful?

Then ask the class to reconstruct, together, one last time:

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

If most students can get through this without prompting, the core
Class 03 concepts have landed.
