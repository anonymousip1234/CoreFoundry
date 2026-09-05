# Class 02 — Student Notes

**Bong Study Hub — Foundation Batch 2026**
**How Machines Learn**
*From Rules → Data → Intelligence*

These notes summarize what we covered in class. Use them to revise, not to
learn the topic for the first time — the real learning happened in the
room, with the discussion and the cats-vs-dogs activity. No programming
and no mathematics appear anywhere in this class — everything here is
conceptual.

<!-- PAGE BREAK -->

## 1. The Big Question

Everything today builds toward one question:

> **"How can a machine make a decision when nobody explicitly wrote the
> rule for every situation?"**

This matters because a huge number of things you use every day — spam
filters, recommendations, maps, face unlock, ChatGPT — clearly make
decisions or predictions. But no one could realistically sit down and
write a rule for *every* possible email, *every* possible user's taste,
or *every* possible face. So how do these systems work at all? Today
answers that.



## 2. From Class 01 to Class 02

Class 01 gave you this chain:

```
PROBLEM  →  LOGIC  →  ALGORITHM  →  PROGRAM  →  RESULT
```

That chain is about a **human** working out a solution and writing it
down as precise instructions for a computer to follow. It's a powerful
idea, and it still applies to most software.

But today we ask: **what happens when writing every rule by hand becomes
impractical?** Not impossible in principle — just unrealistic, because
the situations are too varied, too numerous, or keep changing. That
question is where Class 02 begins.



## 3. What Is AI?

For this class, use a simple working idea — not a textbook definition:

> **Artificial Intelligence (AI)** is the broad field of building
> computer systems that do things which normally seem to require some
> kind of intelligence — recognizing a face, recommending a movie,
> understanding a sentence, predicting traffic.

It isn't about robots, and we're not going to debate whether a machine
"truly" thinks — that's a philosophical question outside today's scope.
What matters is the *kind of task* being done: something that adapts its
output based on patterns it has seen, rather than always doing the exact
same fixed thing.



## 4. AI Around Us

You already use AI every day, often without noticing. For each example
below: what we observe, what the system receives, and what it produces.

| Example | What we observe | What it receives | What it produces |
|---|---|---|---|
| **Spam detection** | Junk mail is already sorted away before you open your inbox | The email's content and patterns learned from millions of past emails | A spam / not-spam decision |
| **Recommendation systems** (movies, social media) | Everyone's Netflix/Spotify/feed looks different | What you (and similar users) watched, liked, or skipped | A ranked list of suggestions |
| **Maps / navigation** | A suggested route and an arrival time | Current and past traffic, road data, other users' locations | A route and a time estimate |
| **Face unlock** | Your phone unlocks instantly, in different lighting, with or without glasses | Many earlier images of your face, then a new camera image | A match / no-match decision |
| **Generative AI** (e.g., ChatGPT) | A fluent, relevant written reply to your question | Patterns learned from enormous amounts of text, plus your question | A newly generated response |

We don't know — and don't need to know — the exact proprietary details of
how any specific company builds these. What matters is the shared idea
underneath all five: **none of them work by someone hand-writing a rule
for every possible case.**



## 5. The Traditional Approach

Before Machine Learning, here's how you'd normally get a computer to make
a decision:

```
   INPUT   →   HUMAN-WRITTEN RULES   →   OUTPUT
```

A **human** thinks of the rules, in advance. The **computer** just
follows them, exactly, every time.

### Example — building a spam filter by hand

If you were writing a spam filter yourself, you might come up with rules
like:

- If the email contains "you have won" → spam
- If the sender is unknown and asks for money → spam
- If the subject is in ALL CAPS with lots of "!!!" → spam

This is a completely reasonable first attempt. It's exactly how
traditional programming works — and it's exactly where Class 01's
Input → Process → Output idea applies.



## 6. The Problem with Rules

Now let's stress-test those rules with real-world cases.

```
        One rule
           ↓
     A new exception appears
           ↓
      Add another rule
           ↓
     Another exception appears
           ↓
   The rule list keeps growing...
```

- A real spam email arrives that doesn't contain any flagged word.
- A genuine airline email says "Your booking is urgent — confirm now!"
  and gets wrongly blocked.
- Spammers deliberately misspell words ("fr33", "amaz0n") to dodge
  keyword rules.
- Spammers write in different languages, or keep changing their wording
  every week.

Every one of these forces you to add *yet another* rule — and there is
always another case waiting. In class, we called this feeling **"rule
explosion"** — not a formal term, just a label for what happens when a
rule list keeps growing and still keeps missing cases.

**Important:** this doesn't mean rules are *impossible*. It means some
real-world situations contain too many changing cases for a human to
realistically manage by hand.

That leaves one honest question:

> **If humans cannot realistically write every rule, what could we give
> the computer instead?**



## 7. The Machine Learning Idea

Here's the shift:

```
Instead of manually writing every rule...

           give the system examples (data)

                        ↓

     let a learning process find useful patterns
```

> **Machine Learning** is an approach where a computer gets better at a
> task by finding patterns in examples, instead of following rules a
> human typed in.

A careful note on wording: the system doesn't "understand" spam the way
you do. Think of learning here as **finding useful patterns in data** —
not understanding the way a person understands something.



## 8. The Core Pipeline

This is the single most important idea in today's class:

```
   DATA   →   LEARNING   →   MODEL   →   PREDICTION
```

| Box | What it means |
|---|---|
| **DATA** | The examples given to the system (e.g., past emails already labeled spam / not spam). |
| **LEARNING** | The process of looking across all those examples and finding useful patterns. |
| **MODEL** | What the system builds from what it learned — something it can now use on new, unseen examples. |
| **PREDICTION** | The model's best guess for a brand-new example it has never seen before. |

### Worked example — the spam filter, all four boxes

| Box | Spam filter |
|---|---|
| Data | Past emails, already labeled spam / not spam |
| Learning | Finding useful patterns across all those labeled emails |
| Model | The learned spam-filter model |
| Prediction | Spam or not spam, for a brand-new email |

Keep this diagram in your notes — we'll refer back to it constantly for
the rest of the program.



## 9. Traditional Programming vs. Machine Learning

Side by side, this is the core contrast of the entire class:

```
TRADITIONAL PROGRAMMING

   INPUT
     ↓
   HUMAN-WRITTEN RULES
     ↓
   OUTPUT


MACHINE LEARNING

   DATA
     ↓
   LEARNING
     ↓
   MODEL
     ↓
   PREDICTION
```

| | Traditional Programming | Machine Learning |
|---|---|---|
| Who provides the "rule"? | A human, explicitly | Nobody — it's learned from examples |
| What's in the middle box? | Rules someone thought of and wrote down | A learning process that finds patterns |
| Best suited for | Problems where the rule is knowable and stable | Problems where the rule is too varied, fuzzy, or large to write by hand |

**Important:** Machine Learning does **not** replace programming, and
traditional programming isn't obsolete. Most software you use every day
still runs on Input → Rules → Output — Machine Learning is the extra tool
you reach for specifically when hand-written rules stop being practical.



## 10. Cats-vs-Dogs Example

In class, we reasoned through this activity together — no code, no math,
just reasoning.

```
  Labeled cat & dog examples
            ↓
        Learning
            ↓
          Model
            ↓
      A new, unlabeled image
            ↓
        Prediction
```

**The idea:** if you look at many labeled cat photos and many labeled dog
photos, you start noticing patterns — ear shape, size, face shape, tail,
typical posture — without anyone telling you those patterns directly. A
system shown enough labeled examples can pick up on similar patterns.

When a **new** photo arrives — one the system has never seen — it uses
the patterns it picked up to make its best guess: cat, or dog.

**The important catch:** that guess is not guaranteed to be correct.
Some animals are genuinely ambiguous-looking (remember the tricky example
from class), and a reasonable guess can still be wrong.



## 11. Prediction ≠ Certainty

> **A prediction is a best guess based on learned patterns. It is not a
> guarantee.**

Examples you already know from real life:

- A streaming app recommends something you end up not liking at all.
- A spam filter occasionally lets through a scam email, or blocks a real
  one.
- The ambiguous cat/dog photo from class — a reasonable guess that could
  still be wrong.

A wrong guess doesn't mean the system is "broken" — the same way a
person's reasonable guess can turn out wrong without them being broken.



## 12. AI Is Not Magic

Everything comes back to the same chain:

```
   DATA
     ↓
  PATTERNS
     ↓
   MODEL
     ↓
 PREDICTION
```

A few grounded facts worth remembering:

- **Data matters.** A model only knows what its examples showed it.
- **Examples matter.** Limited or one-sided examples produce limited or
  one-sided patterns.
- **Poor data can lead to poor predictions.** A spam filter trained only
  on English emails will likely struggle with a different language.
- **AI systems have real, explainable limitations.** Nothing here is
  mysterious once you see the pipeline behind it.

AI isn't magic — it's data, patterns, a model, and a prediction.



## 13. AI / ML / Deep Learning / Generative AI

A simple orientation map — broad to narrow:

```
   ┌───────────────────────────────────────┐
   │        ARTIFICIAL INTELLIGENCE         │
   │   ┌─────────────────────────────┐     │
   │   │      MACHINE LEARNING        │     │
   │   │   ┌───────────────────┐      │     │
   │   │   │   DEEP LEARNING    │      │     │
   │   │   └───────────────────┘      │     │
   │   └─────────────────────────────┘     │
   │                                         │
   │        ✦ GENERATIVE AI                 │
   │  (a major modern application area)      │
   └───────────────────────────────────────┘
```

- **Artificial Intelligence** — the broad field.
- **Machine Learning** — one major approach inside AI (today's topic).
- **Deep Learning** — a more powerful style of machine learning, used for
  very complex patterns like images, speech, and language.
- **Generative AI** (like ChatGPT) — a major modern application area,
  strongly associated with deep learning, that generates new content
  instead of just picking a category.

**This is a simple learning map, not a complete technical taxonomy.** You
do not need to memorize formal definitions of any of these — just have a
rough sense of how broad each one is compared to the others.



## 14. Everyday Mental Model

Keep this one line in your head — it's the most useful takeaway of the
whole class:

> **When humans already know the rules:**
> `INPUT → RULES → OUTPUT`
>
> **When the rules are too hard to write by hand:**
> `DATA → LEARNING → MODEL → PREDICTION`



## 15. What We Learned Today

- Some problems can't realistically be solved by writing every rule by
  hand — not because it's impossible, but because the cases are too
  numerous or keep changing.
- Machine Learning is the alternative: give the system examples, and let
  a learning process find useful patterns.
- The core pipeline is `DATA → LEARNING → MODEL → PREDICTION`.
- Traditional programming (`INPUT → HUMAN-WRITTEN RULES → OUTPUT`) and
  Machine Learning are two different strategies — one doesn't replace
  the other.
- Spam filters, recommendations, maps, face unlock, and generative AI are
  all everyday examples of learning from data.
- A system can learn to tell cats from dogs by noticing patterns across
  many labeled examples — the same way we reasoned through it in class.
- A prediction is a best guess, not a certainty — it can be wrong.
- Poor or limited data can lead to poor predictions.
- AI is not magic — it depends entirely on data, patterns, and a model.
- AI, Machine Learning, Deep Learning, and Generative AI relate broad to
  narrow — this is an orientation map, not something to memorize exactly.



## 16. Common Misconceptions

| Misconception | Correction |
|---|---|
| "AI is just a robot." | AI mostly lives inside ordinary apps you already use — no body required. |
| "Machine learning means the computer thinks exactly like a human." | It notices patterns in data — it doesn't understand meaning the way a person does. |
| "More data always means better AI." | More *good, relevant* data usually helps — messy or irrelevant data can teach the wrong patterns. |
| "A prediction is a guaranteed truth." | A prediction is a best guess based on learned patterns — it can be wrong. |
| "Machine learning replaces programming." | It doesn't — most software still runs on hand-written rules; ML is an extra tool for a specific kind of problem. |
| "AI is magic." | AI depends entirely on data, patterns, and a model — nothing about it is mysterious once you see the pipeline. |



## 17. Looking Ahead

Remember Class 01's learning staircase:

```
Programming → Computer Science → Mathematics → Data →
Machine Learning → Deep Learning → LLMs → Agents
```

Today was a **conceptual preview** — we stood at one of the higher steps
of that staircase for a little while and looked down. We did not skip
anything. The program will now go back and build the programming,
mathematics, data, and engineering foundations needed to actually
understand and build AI systems properly.

> **We are not skipping the steps. We are learning where the staircase
> leads.**



## 18. Quick Self-Check

Try answering these in your own words before looking at the answer key.
You don't need exact wording — just the right idea.

1. Why can hand-written rules become difficult to manage?
2. What is the difference between traditional programming and machine
   learning?
3. What does the Data → Learning → Model → Prediction pipeline mean?
4. How could a system learn to tell cats and dogs apart?
5. Why isn't a prediction guaranteed to be correct?
6. Why does data quality matter for a machine learning system?



## 19. Mini Glossary

| Term | Meaning |
|---|---|
| **AI (Artificial Intelligence)** | The broad field of building computer systems that do things which normally seem to need some kind of intelligence. |
| **Machine Learning** | An approach where a computer improves at a task by finding patterns in examples, instead of following hand-written rules. |
| **Data** | The examples given to a system, like labeled cat and dog photos. |
| **Learning** | The process of looking across many examples and finding useful patterns. |
| **Model** | What the system builds after learning — something it can use to handle new examples. |
| **Prediction** | The model's best guess about a new example it hasn't seen before. |
| **Pattern** | Something that shows up repeatedly across examples and helps tell one category from another. |
| **Deep Learning** | A more powerful, layered style of machine learning, used for very complex patterns. |
| **Generative AI** | AI that generates new content — like text or images — instead of just predicting a category. |



## Answer Key — Quick Self-Check

Use this only after attempting the questions in Section 18 yourself.

1. **Why can hand-written rules become difficult to manage?** Real-world
   situations (like spam) contain too many varying, changing cases for a
   human to realistically list every rule for — new exceptions keep
   appearing. See Section 6.

2. **Traditional programming vs. machine learning?** In traditional
   programming, a human writes the rules and the computer follows them.
   In machine learning, the computer is given examples and a learning
   process finds the patterns instead. See Section 9.

3. **What does Data → Learning → Model → Prediction mean?** Data is the
   examples given to the system; Learning finds useful patterns across
   them; the Model is what results from that learning; Prediction is the
   model's best guess on a new example. See Section 8.

4. **How could a system learn cats vs. dogs?** By looking at many labeled
   cat and dog examples and picking up on patterns (like ear shape or
   size) that tend to separate the two — then applying those patterns to
   guess on a new, unlabeled photo. See Section 10.

5. **Why isn't a prediction guaranteed to be correct?** A prediction is
   only a best guess based on patterns learned from examples — not a
   certainty, the same way a reasonable human guess can still be wrong.
   See Section 11.

6. **Why does data quality matter?** A model only knows what its
   examples showed it — limited, one-sided, or poor-quality data leads to
   limited or poor predictions. See Section 12.
