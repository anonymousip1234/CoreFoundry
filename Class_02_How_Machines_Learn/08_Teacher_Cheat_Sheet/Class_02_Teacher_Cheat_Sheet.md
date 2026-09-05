# Class 02 — Teacher Cheat Sheet

**Bong Study Hub — Foundation Batch 2026 · How Machines Learn**
*From Rules → Data → Intelligence*

Live-use operational reference, derived entirely from the approved
Class 02 artifacts (Instructor Guide → Student Notes → Pen Tablet →
Presentation → Interaction Pack → Homework → Assessment). **This is
not a second Instructor Guide** — it's what you glance at mid-sentence.
Full teaching language lives in the Master Instructor Guide.

---

## 1. Class at a Glance

| | |
|---|---|
| **Title** | How Machines Learn |
| **Subtitle** | From Rules → Data → Intelligence |
| **Duration** | 110 min canonical (90 / 120 variants — §14–15) |
| **Core question** | "How can a machine make a decision when nobody explicitly wrote the rule for every situation?" |
| **Core pipeline** | `DATA → LEARNING → MODEL → PREDICTION` |
| **Traditional pipeline** | `INPUT → HUMAN-WRITTEN RULES → OUTPUT` |
| **Primary outcome** | Most students can explain *why* ML was needed for one real example, state the pipeline vs. rules, reason through cats-vs-dogs, and state that predictions aren't certainties and data quality matters. |

> **CLASS NARRATIVE**
> A COMPUTER CAN FOLLOW RULES → BUT WHAT IF WE DON'T KNOW ALL THE
> RULES? → CAN WE GIVE IT EXAMPLES INSTEAD? →
> `DATA → LEARNING → MODEL → PREDICTION`

**3–5 ideas that matter most today:**
1. The Rule Problem must be *felt*, not stated — protect the escalation.
2. Machine Learning is named only *after* the rule problem lands.
3. The Core Pipeline is built live, box by box — never shown finished first.
4. A prediction is a best guess, not a guarantee.
5. AI depends entirely on data — poor/narrow data → poor predictions.

**Class 01 callback:** `PROBLEM → LOGIC → ALGORITHM → PROGRAM → RESULT`
and the learning staircase — today is a *preview from the top*, not a
shortcut past the steps underneath.

> **DO NOT GO DEEPER TODAY:** No code, no math, no implementation
> detail. See §11 for the full guardrail list.

---

## 2. Live Flow Table (110-min canonical)

| Time | Section | Purpose | Ask / Do | Draw / Show | Watch For |
|---|---|---|---|---|---|
| 0–8 | Opening + AI perception | Activate existing AI experience | "Where have you noticed something 'smart' like this?" → state core question | None yet | "AI is just a robot" — bank it, don't correct yet |
| 8–19 | What is AI? | Working, non-philosophical notion | "Is a calculator AI? A thermostat?" | Light icon slide | Drifting into consciousness/philosophy debate |
| 19–31 | AI Around Us | Ground AI in 5 daily examples | "What does it receive? What does it produce?" per example | Drawing 1 (optional light list) | Claims about real products' internals |
| 31–43 | Traditional Programming | Re-anchor Input→Rules→Output | "What's your first rule?" | **Drawing 2** — build live, empty → filled | Students sliding into code/`if-else` syntax |
| 43–59 | **Rule Problem** (non-negotiable) | Feel the limitation directly | Escalating counter-examples → scaling Q → pivot Q | **Drawing 3** — crowd the rule box | "Just need more rules" — let the crowding answer it |
| 59–70 | Introducing ML | Name ML only now | "What does 'learning a pattern' mean here?" | None yet (bare title) | "The computer thinks/understands" language |
| 70–78 | **Core Pipeline** (HERO, non-negotiable) | Install the pipeline live | 4 questions, one per box | **Drawing 4 — BUILD LIVE, never pre-drawn** | "Patterns" as a 5th stage; Model/Prediction swap |
| 78–90 | **Cats vs Dogs** (HERO, non-negotiable) | Reason through the pipeline concretely | 5-level question ladder (§7) | None — point back to Drawing 4 if useful | Technical computer-vision vocabulary |
| 90–95 | Prediction ≠ Certainty (non-negotiable) | Best guess, not guarantee | "Was that a prediction or a guarantee?" | Point at Drawing 4's PREDICTION box | "If it's ML it should always be right" |
| 95–99 | AI Is Not Magic | Data quality → prediction quality | "What if it only ever saw English emails?" | Reuse Drawing 4, annotate DATA box | Reaching for "bias" as a buzzword with no reasoning |
| 99–104 | AI/ML/DL/GenAI Map | Orientation, not taxonomy | "Where does ChatGPT belong on this map?" | **Drawing 5** — nested circles, ring by ring | Requests for neural-net/transformer detail |
| 104–107 | Return to Staircase | Preview from the top, not a shortcut | "Which chain have we built all class?" | **Drawing 6** — quick callback, faster than Class 1's build | Framing today as contradicting Class 1's roadmap |
| 107–110 | Recap + Exit Check + Homework Bridge (non-negotiable) | Consolidate, verify, hand off | Recap + exit-check Qs (§13) | None | Recited definitions without own-words explanation |

---

## 3. Opening Script — First 5 Minutes

1. **Opening move:** "Quick show of hands — who used Instagram,
   YouTube, Netflix, or Google Maps in the last 24 hours?"
2. **First question:** "How many of you have actually thought about
   how it knows what to show you?" *(expect very few hands — that's
   the point)*
3. **State the core question, slowly:** "How can a machine make a
   decision when nobody explicitly wrote the rule for every
   situation?"
4. **Collect 2–4 quick answers**, without correcting any of them yet.
5. **Bridge:** "By the end of today, you'll be able to answer that
   yourself."

**Expected responses:** Instagram/YouTube/Netflix feed, Google Maps,
ChatGPT, face unlock, autocorrect.

**If silence:** rephrase narrower within 5–7 seconds, or answer
yourself first and toss it back ("I'll start us off — anyone else?").

**Transition:** straight into "What Is AI?" (§2 row 2).

---

## 4. Core Explanation Cards

### Card A — Traditional Programming

```
INPUT  →  HUMAN-WRITTEN RULES  →  OUTPUT
```
- **One-sentence:** A human thinks of the rule; the computer just
  follows it, exactly, every time.
- **Approved example:** Spam filter — "contains 'you have won' → spam."
- **Key question:** "What's your first rule?"
- **Watch for:** Sliding into code/`if-else` syntax — keep it plain English.

### Card B — Rule Problem

- **Students should notice:** The rule list keeps growing and still
  misses cases.
- **Role of variety / exceptions / change:** Real cases vary; spammers
  change wording; legitimate emails trip innocent-looking rules.
- **Approved example:** Legit — *"Your booking is urgent — confirm
  now!"* vs. Spam — *"fr33 amaz0n..."*
- **Pivot question:** "If humans cannot realistically write every
  rule, what could we give the computer instead?" *(wait 10–15 sec)*

### Card C — Machine Learning

- **Conceptual explanation:** Give the system examples instead of
  rules, and let a learning process find useful patterns.
- **Framing phrase:** "Examples instead of every rule."
- **Wording care:** Say "notices patterns," never "understands" or
  "thinks."
- **Transition into pipeline:** "Let's build out what 'learning from
  examples' looks like, step by step."

### Card D — Core Pipeline (HERO CARD)

```
DATA  →  LEARNING  →  MODEL  →  PREDICTION
```

| Stage | Means | You say | Students should say | Common confusion |
|---|---|---|---|---|
| **DATA** | Examples given to the system | "Past emails already labeled spam or not spam" | "The examples we give it" | Confusing data with rules |
| **LEARNING** | The process of finding useful patterns | "Looks across the examples, finds what separates spam from not-spam" | "It looks for patterns" | Thinking Learning *is* the model |
| **MODEL** | What the system builds from learning | "Something that's picked up the patterns" | "What it built after learning" | **Confusing Model with Prediction** |
| **PREDICTION** | The model's best guess on a new example | "Its best guess for a brand-new email" | "A guess, not a fact" | Treating prediction as guaranteed |

> **"Patterns are what Learning finds — patterns are NOT a fifth
> stage."**
>
> **MODEL = what the learning process builds. PREDICTION = what the
> model produces for something new.**

### Card E — Prediction ≠ Certainty

- **Core message:** A prediction is a best guess based on learned
  patterns — not a guarantee.
- **Cats/dogs connection:** Same as the ambiguous cat/dog guess — a
  reasonable guess that could still be wrong.
- **Watch for:** "If it's really ML, it should always be right."
- **Question:** "Was that a prediction, or a guarantee?"

### Card F — Data Quality

- **Core message:** A model only knows what its examples showed it —
  poor or narrow data leads to poor predictions.
- **Pattern:** Narrow/one-sided examples → difficulty with unfamiliar
  cases (e.g., a spam filter that only ever saw English emails).
- **Do not require the word "bias."**
- **Question:** "What would happen if it only ever saw X?"

### Card G — AI / ML / Deep Learning / GenAI

```
Artificial Intelligence
        ↓
Machine Learning
        ↓
Deep Learning
```
Generative AI = a major modern application area, strongly associated
with deep learning — shown touching the ML/Deep-Learning boundary, not
as a strict fourth nested ring.

> **"This is a learning map, not a complete technical taxonomy."**

**DO NOT GO DEEPER:** neural-network architecture, transformers,
embeddings, tokens, LLM internals.

---

## 5. Pen Tablet Quick Cues

| Drawing | When | Purpose | Build | Must Appear | Do NOT Pre-Draw | Transition |
|---|---|---|---|---|---|---|
| **1 — AI Around Us** | 19–31 min | Ground AI in daily life | One line per named example, live | 5-line flat list (spam, recs, maps, face unlock, GenAI) | The list itself | "None of these work by hand-writing a rule for every case." |
| **2 — Traditional Programming** | 31–43 min | Human writes the rule | 3-box skeleton, rules filled live by students | `INPUT → HUMAN-WRITTEN RULES → OUTPUT` + 3–4 rules | Any rules | "Let's throw some real emails at it." |
| **3 — Rule Problem** | 43–59 min | Felt struggle | Crowd rules into/around Drawing 2's box, per counter-example | A visibly overcrowded box | A finished crowded box | Pivot question (spoken, not drawn) |
| **4 — CORE PIPELINE** | 70–78 min | Install the pipeline | **BUILD LIVE — DO NOT SHOW AS A FINISHED DRAWING BEFORE STUDENTS REASON TOWARD IT.** One box per question, then stack Drawing 2's chain beneath for contrast | `DATA → LEARNING → MODEL → PREDICTION` + stacked comparison | Any part, at all, before the live build | Ground in spam example → "Let's reason through this with cats and dogs." |
| **5 — AI/ML/DL/GenAI** | 99–104 min | Orientation map | 3 nested circles ring by ring + GenAI star at the ML/DL boundary | 3 rings + star, no 4th ring | The full map in advance | "Let's put today in context of Class 1's bigger picture." |
| **6 — Staircase / Class 1 Callback** | 104–107 min | Preview from the top | Quick 8-step redraw, faster than Class 1's original build | 8 labels: Programming → CS → Math → Data → ML → Deep Learning → LLMs → Agents | Month numbers / course names | Straight into Recap |

**Drawing 4 stays live and reachable from minute 70 through minute
107** — it's reused (pointed back to, never redrawn) for Prediction ≠
Certainty and AI Is Not Magic.

---

## 6. Activity Cues (Interaction Pack)

| # | Activity | Time | Purpose | Prompt | Listen For | Move On When |
|---|---|---|---|---|---|---|
| 1 | AI Quick Reaction | 5 min | Activate experience | "Which have you used? What makes something 'smart'?" | Ordinary-language answers ("it knows what I want") | 3–4 answers collected |
| 2 | Build a Rule | 6 min | Feel rule-based thinking | "What rule could identify spam?" | "Who decided this was a rule?" → "A human" | 3–4 rules on board + authorship point made |
| 3 | Break the Rule | 8 min | Create the need for a different approach | "Would our rules handle these correctly?" | Hesitation / patch attempts | 2–3 challenges have landed |
| 4 | Rule Explosion | 5 min | Make the growing-rule problem memorable | "If we keep doing this, what happens?" | "Too many rules / confusing / impossible" | "Rule explosion" label lands |
| 5 | Pivot Question | 4 min | Let students arrive at "data" themselves | "What could we give the computer instead?" — **STOP** | "Examples / data / past cases" | Only after a student-sourced answer (wait 5–10 sec min.) |
| 6 | Predict the Pipeline | 8 min | Construct the pipeline live | 4 sequential questions (Card D) | Box-appropriate answers | All 4 boxes built + grounded in spam example |
| 7 | **Cats vs Dogs** | 12 min | See §7 — HERO activity | — | — | — |
| 8 | Prediction or Certainty? | 5 min | Correct "AI = always right" | "Prediction, or guarantee?" | "Prediction" | Best-guess-not-guarantee stated |
| 9 | Data Quality Thought Experiment | 4 min | Poor data → poor predictions | "Small white cats / large black dogs → large white cat?" | "Confused / wrong pattern" | "Does data matter?" → "Yes" lands |
| 10 | AI/ML/DL/GenAI Check | 4 min | Orientation check | "Which is broader — AI or ML? Where's GenAI?" | Broad-to-narrow reasoning | Map completed + "not a taxonomy" reminder given |
| 11 | Exit Check | 5 min | Formative check | 4 questions (§13) | Own-words explanation vs. recited definition | Most students have attempted |

---

## 7. Hero Activity — Cats vs. Dogs

**Purpose:** Reason through the Machine Learning idea via a visual
classification example — no code, no math.

**Setup:** Many labeled cat examples + many labeled dog examples,
deliberately varied (breed, color, pose, background). Presentation
Slide 17.

**Ask (question ladder):**
1. Observation — "What do you notice?"
2. Comparison — "What seems similar across the cat examples? Across
   the dog examples?"
3. Generalization — "If the next cat looks very different, could the
   system still recognize it?"
4. Ambiguity — "What if the new image is difficult to classify?"
5. Limitation — "Could the system make a mistake?"

**Wait:** 5–10 seconds per question — longer than usual.

**Follow-up:** "Now imagine a brand-new image — what would the system
do?" → "Could it still get it wrong?" → **Yes.**

**What good reasoning sounds like:** Names a visual pattern (ear
shape, size, face shape) **and** connects it to "if it saw enough
examples, it could notice this too" **and** acknowledges the guess
could still be wrong.

**Common wrong answers:** A hand-written-rule answer ("if pointy ears
→ cat"); technical computer-vision jargon; assuming guaranteed
correctness.

**How to handle a wrong answer:** Don't grade "correct features" —
accept any reasonable pattern. Redirect a rule-based answer gently
toward "pattern from examples" framing, not "wrong, try again."

**When to move on:** Once "prediction, could be wrong" is reached —
this is the direct bridge into Prediction ≠ Certainty.

**Pen-tablet / slide connection:** No new drawing. If useful, point
back to Drawing 4 and trace the same four boxes with the cat/dog
framing.

---

## 8. Misconception Radar

| Misconception | Listen For | Response / Reframe |
|---|---|---|
| "AI is just a robot / ChatGPT." | "AI means robots," or reducing AI to one product | "AI mostly lives inside ordinary apps you already use — no body required." |
| "Surely we could just write enough rules to cover it." | "We just need more rules" | Let the crowding on Drawing 3 answer this visually — "and there's always another case waiting." |
| "Rules are difficult only because writing them takes time." | Treating the Rule Problem as an effort problem | "It's not about how long it takes — it's that the situations and exceptions keep growing faster than any list can." |
| "Machine Learning means no programming is needed." | "So we don't need programmers anymore?" | "Someone still has to build, prepare data for, and deploy these systems — ML is an extra tool, not a replacement." |
| "Patterns are a separate, fifth pipeline stage." | Student adds "patterns" as its own box | "Patterns are what Learning *finds* — the pipeline stays four stages." |
| "Model and Prediction are the same thing." | Swapping the two in an explanation | "Model = what the learning process builds. Prediction = what the model produces for something new." |
| "A prediction means certainty." | "If it predicted it, it must be right" | "A prediction is a best guess based on learned patterns — not a guarantee." |
| "If ML makes a mistake, it wasn't really using ML." | "That can't be real Machine Learning, it got it wrong" | "A wrong guess doesn't mean the system is broken — reasonable guesses can still be wrong." |
| "AI thinks/understands like a human." | "The AI knows/understands X" | "Think of it as noticing patterns, not understanding the way you do." |
| "More data automatically means better AI." | "Just give it more data and it'll be better" | "More *good, relevant* data usually helps — messy or irrelevant data can teach the wrong patterns faster." |

Address these opportunistically as they surface — never read this
table aloud as a block, and never let a correction feel like a
callout of the student personally.

---

## 9. Quiet-Class Protocol

```
ASK
 ↓
WAIT 3–5 SEC   (5–10 sec for the Pivot Question and Cats-vs-Dogs)
 ↓
NO RESPONSE?
 ↓
MAKE THE QUESTION EASIER / NARROWER
 ↓
TRY CHAT, HAND-RAISE, OR A QUICK PAIR CHECK
 ↓
TAKE ONE RESPONSE
 ↓
BUILD FROM IT — DO NOT ANSWER IT YOURSELF
```

Example narrowing: instead of "What pattern should the system learn?"
ask "Do you think it should look at the words, the sender, or both?"

---

## 10. Advanced-Student Parking Lot

If a student raises any of the following, **do not answer technically**
— acknowledge and park it:

- Neural-network math
- Gradient descent / optimization
- Transformers
- Embeddings / tokens
- RAG
- Agents (as a technical mechanism)
- Formal ML metrics (accuracy, precision, recall)
- Model-training implementation
- Deep prompt engineering

**Standard response:**

> "Good question. We're going to build toward that later. Today we're
> staying with the mental model."

Then return directly to `DATA → LEARNING → MODEL → PREDICTION`. Don't
let one advanced student pull the whole class into a later topic.

---

## 11. DO NOT GO DEEPER TODAY

- No code, no pseudocode, no programming syntax
- No mathematics, no formulas
- No implementation details
- No proprietary product internals (don't claim to know how a real
  company's system actually works)
- No neural-network architecture explanation
- No formal ML terminology beyond class level (no probability,
  confidence scores, accuracy/precision/recall, loss functions,
  gradient descent, transformers, embeddings, RAG)
- "Agents" may appear **only** as a future staircase-step label —
  never explained

*Glance here the moment discussion starts drifting technical.*

---

## 12. Transition Cues

| From | To | Say |
|---|---|---|
| Rules (built) | Rule Problem | "Let's throw some real emails at it." |
| Rule Problem | Pivot | "So if writing every rule becomes impractical, what else could we give the computer?" |
| Pivot (answered) | Machine Learning | "That instinct has a name." |
| Machine Learning | Core Pipeline | "Let's build out what 'learning from examples' looks like, step by step." |
| Core Pipeline | Cats vs Dogs | "Let's reason through this with something concrete: cats and dogs." |
| Cats vs Dogs | Prediction ≠ Certainty | "Could it still get it wrong?" → *(yes)* |
| Prediction ≠ Certainty | AI Is Not Magic | "This connects to something bigger: AI isn't magic." |
| AI Is Not Magic | AI/ML/DL/GenAI Map | "Let's zoom out and see how all the AI terms you've heard fit together." |
| AI Map | Staircase | "Let's put today in context of the bigger picture from Class 1." |
| Staircase | Recap | *(straight in — no new drawing or slide)* |

---

## 13. Final 5 Minutes

- [ ] Return to the core question — ask students to answer it now, in
      their own words.
- [ ] Restate the core pipeline: `DATA → LEARNING → MODEL → PREDICTION`.
- [ ] Ask the exit-check questions:
  1. Why might hand-written rules become difficult?
  2. What is the alternative?
  3. What is the four-stage pipeline?
  4. Why isn't prediction certainty?
  5. Why does the data matter?
- [ ] Connect back to Class 1 — the staircase, "preview from the top."
- [ ] Preview what comes next — Month 1/2 foundations build the steps
      underneath the staircase.
- [ ] Point to the **Homework** package (`06_Homework/`) — 10
      questions, 30–45 min, no coding.
- [ ] If assigned, point to the **Assessment** (`07_Assessment/`) — 7
      questions, 25–35 min, fresh scenarios.

Accept answers in the student's own words — this is a formative close,
not a lecture.

---

## 14. Emergency Time-Cut Version (~90 Minutes)

**Always protect:** Rule Problem · Pivot · Core Pipeline · Cats-vs-Dogs
reasoning · Prediction ≠ Certainty · AI/ML/DL/GenAI map · Recap.

**Compress:**
- Opening + AI perception → 2–3 examples collected instead of open-ended.
- What Is AI? → skip the calculator/thermostat debate, state the
  working idea directly.
- AI Around Us → 3 examples (spam, recommendations, face unlock)
  instead of 5.
- Traditional Programming → cap rule collection at 3 rules.
- Rule Problem → 3 escalating counter-examples instead of 4–5 — the
  felt struggle must still land.
- Introducing ML → one clean statement + one check-in question.
- Cats vs Dogs → drop the extension round only; keep the full core
  sequence.
- AI Is Not Magic → one example only (language), not a second.

**Last-resort further cut** (only if still over time after the Rule
Problem): deliver the AI/ML/DL/GenAI map as a 2-minute **spoken**
version instead of live-drawn — never cut the Core Pipeline or the
Recap.

---

## 15. Extended Version (~120 Minutes)

Every added minute goes to **interaction and reasoning**, never new
technical content:

- Opening → one more student describes their example in more detail.
- AI Around Us → add a 6th example students suggest themselves.
- Rule Problem → let students try to patch their own rules for 2–3
  more rounds before the reveal.
- Cats vs Dogs → add a stronger-student extension round (a harder
  ambiguous example, student-proposed).
- AI/ML/DL/GenAI Map → 1–2 extra "where does X belong?" questions
  (e.g., self-driving cars, voice assistants).
- Staircase → only if time genuinely allows, redraw the
  Traditional-vs-ML comparison next to the staircase instead of
  pointing back to Drawing 4.

---

## 16. Pre-Class 2-Minute Checklist

- [ ] Presentation ready (`03_Presentation/Class_02_How_Machines_Learn.pptx`)
- [ ] Pen tablet / canvas ready — 5 pages set up (see §5)
- [ ] Core Pipeline page (Drawing 4) reachable and empty — not pre-drawn
- [ ] Cats-vs-Dogs example images/descriptions ready
- [ ] Interaction Pack open for quick reference
- [ ] Homework package ready to share (`06_Homework/`)
- [ ] Assessment ready if applicable (`07_Assessment/`)
- [ ] No advanced material planned or prepared
- [ ] Remember: **ask before explaining**

---

## 17. Post-Class Capture

*Not the full Reflection artifact — that belongs in `10_Reflection/`.
This is just a quick note to yourself before you forget.*

**TODAY I NOTICED:**

Most common misconception:
_________________________________________________

Question students struggled with:
_________________________________________________

Question that produced strong reasoning:
_________________________________________________

Timing that ran long:
_________________________________________________

What to revisit next class:
_________________________________________________
