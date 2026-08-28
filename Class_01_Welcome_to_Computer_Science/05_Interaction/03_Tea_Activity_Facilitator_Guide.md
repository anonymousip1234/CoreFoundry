# Class 01 — "Teach a Computer How to Make Tea" — Facilitator Guide

**Bong Study Hub — Foundation Batch 2026 · Welcome to Computer Science**

This is the main interactive activity of Class 1 — the emotional and
pedagogical centerpiece (Master Instructor Guide §5.8). Protect its time
above everything except Drawing 3 (Problem → Logic → Algorithm → Program →
Result). This guide expands the Guide's activity description into a
full run-of-show; it does not change what the activity teaches.

**Safety note:** This is a role-play. The instructor never actually boils
water, handles a stove, or performs any physical action — everything
happens through spoken description. If you want a physical prop on camera
for fun (an empty cup, a tea bag), that's optional and never involves
heat, electricity, or anything genuinely hazardous.

**Duration:** ~13–15 minutes (protected — never compressed below the Min
in Guide §4.1, even in the 90-minute version).

---

## Opening

Say, plainly, before anything else:

> "Imagine I am a computer. I will do exactly — and only — what you tell
> me, in the exact order you tell me. Nothing more, nothing assumed. If
> you don't tell me, I don't know it."

Then ask for one volunteer to go first (see "Quiet students" strategies in
`05_Classroom_Interaction_Flow.md` if no hands go up — think-pair-share
works well here: give the room 20 seconds to draft their first instruction
with a partner before asking for a volunteer).

Frame it as low-stakes and a little fun, not a test:

> "There's no way to get this wrong — that's actually the whole point.
> We're about to find out together why it's hard."

---

## Rules (state these explicitly, once)

1. The instructor is a computer: literal, has zero assumptions, and asks
   for anything not explicitly stated.
2. The student gives instructions one step at a time — not the whole
   recipe at once.
3. The instructor does not skip ahead, guess intent, or fill in "obvious"
   details.
4. Nobody is wrong here — every gap the "computer" finds is expected, and
   is the lesson, not a mistake.

---

## Round 1 — Standard flow

### Expected student behavior
Most students start with a natural, human-level instruction, assuming
common sense will fill in the rest: "boil the water," "put the tea in,"
"add sugar." This is exactly correct and exactly the setup needed —
don't ask them to be more precise up front; let the gaps surface
naturally.

### Instructor responses (literal-computer mode)

| Student says | Instructor (as literal computer) asks |
|---|---|
| "Boil water." | "Where is the water?" → "How much water?" → "Where is the container?" → "What should I use to heat it?" |
| "Put the tea in." | "Which tea? Tea leaves, or a tea bag?" → "How much?" → "Put it in where?" |
| "Then add sugar." | "How much sugar?" → "Add it to what, exactly?" |
| "Turn on the stove." | "Where is the stove? Is it already connected to gas or electricity?" |
| "Wait for it to boil." | "How long is 'wait'? How do I know it's boiling?" |

Keep every question short, calm, and genuinely curious — not
interrogative or mocking. One question at a time; let the student respond
before asking the next.

---

## Round 2 — Escalation

Once the room has felt the basic pattern (2–4 exchanges), deliberately
introduce one broken assumption to raise the stakes:

> "There's no gas available. What do I do now? You never told me."

This is the single most important line of the activity — let it land in
silence for a moment before any student jumps in.

**Expected student behavior in Round 2:** Some confusion or laughter,
then attempts to patch the instruction ("use an electric kettle instead,"
"just add hot water from somewhere else"). Some students may try to argue
that "obviously" you'd improvise — this is the exact human instinct being
demonstrated, so name it rather than dismiss it: "you would improvise —
I can't. I only do what I'm told."

**Optional second escalation** (only if time and energy allow, and the
room is enjoying it): introduce one more broken assumption, e.g. "there's
no cup available" or "I don't know what 'a pinch' of sugar means, tell me
a number." Do not stack more than two escalations — the point is made
after one or two, and a third risks the activity feeling repetitive
instead of sharp.

---

## Debrief

Move straight from the escalation into these three questions (also in
`01_Question_Bank.md`, Section 8):

1. "What just happened when you said 'boil the water'?"
2. "Why do you think I kept asking 'where,' 'how much,' 'what if'?"
3. "If you had to rewrite your tea instructions to handle 'there's no gas
   available,' what would you add — without knowing any code?"

Let students answer in their own words before supplying the key lesson
yourself.

---

## Key lesson

Say this once, plainly, near the end of debrief:

> "Programming requires us to turn human intentions into precise
> instructions."

Do not paraphrase it into something longer — the line is short and
memorable on purpose. Let it sit for a beat before moving on.

---

## Connection to algorithms

Explicitly link back to the "larger of two numbers" algorithm built
earlier in class:

> "Notice this is the same gap we're about to close when we build an
> algorithm — an algorithm is exactly a set of steps precise enough that
> nothing gets left to assumption."

If Activity 4 ("Build an Algorithm") hasn't happened yet in your section
order, adjust the tense: "this is exactly what we're about to do next,
with numbers instead of tea."

## Connection to programming

> "A program is what happens when those precise steps get translated into
> a language a computer can actually run. The tea activity is programming
> without the syntax — you just experienced the hardest part of it."

---

## Potential funny moments (lean into these, don't suppress them)

- A student says "add water" and the instructor asks "how much — in what
  unit?" and the student has no idea (very common, always gets a laugh).
- A student tries to out-smart the literal computer with an
  over-engineered instruction ("insert H₂O at approximately 100°C") — play
  along, then ask an equally literal follow-up ("how much H₂O?").
- The "no gas available" twist usually produces a genuine "wait, what?!"
  reaction — let that land before continuing.
- If a student instinctively says "just Google it" or "ask Alexa," gently
  point out that's still giving an instruction to *another* system, not
  solving this one — good comic redirect back to the point.

---

## How to maintain classroom control

- Keep a light, playful tone from the opening line onward — students take
  cues from the instructor's energy.
- Address the "computer," not the student, when something goes wrong:
  "the computer doesn't understand that yet" reframes any stumble as the
  system's limitation, not the student's mistake.
- Keep turns short. If one student is mid-instruction and the room starts
  shouting suggestions, say: "hang on — one instruction-giver at a time,
  everyone else, hold your ideas for the debrief."
- If energy dips (quiet room, one-word instructions), inject the "no gas
  available" escalation early to re-energize rather than waiting.

## How to prevent the activity from becoming chaotic

- Cap it at 2–3 student volunteers giving instructions per round, not an
  open floor — chaos in this activity usually comes from too many voices
  at once, not from the concept itself.
- If a side conversation starts, don't stop the whole activity — redirect
  with a quick, friendly "let's bring that back to the group" rather than
  a formal reprimand.
- Never let a student improvise physical actions live (no actual boiling
  water, no real stove) — everything stays spoken. This is a structural
  safeguard, not just a content choice: it keeps the activity fast, safe,
  and impossible to derail into "let's actually go make tea."
- If the escalation ("no gas available") produces an argument about
  realism ("but obviously I'd just..."), acknowledge it once ("you're
  right, a human would improvise") and move to the debrief rather than
  litigating the scenario further.

## How to end the activity strongly

- End on the Key Lesson line, said plainly, not on the last joke or the
  last student's answer — the room's attention should land on the
  sentence, not on whoever spoke last.
- Immediately bridge forward with one sentence connecting to what's next
  (Algorithm, if not yet covered, or the AI section if it has been):
  "That gap between what you meant and what you actually said is exactly
  what separates how we've been programming from something newer" (Board
  Plan §7, Board Transitions).
- Do not linger for extra debrief questions once the key lesson has
  landed — a crisp ending preserves the activity's impact more than
  extending it.

---

## Online Adaptation

This program runs online. A few adjustments keep the activity working
without a physical room:

- **Turn-taking:** Ask for one volunteer to unmute; everyone else stays
  muted during their turn to avoid overlapping audio (see
  `05_Classroom_Interaction_Flow.md` § Online Classroom for full detail).
- **No hands raised:** Use think-pair-share via chat first — ask students
  to type their first instruction in chat, then verbally invite whoever
  wrote something interesting to unmute and continue live.
- **Screen share:** No slide or board is needed for this activity — keep
  the screen on the instructor's camera (or a simple "TEACH THE COMPUTER"
  title card) so students focus on the spoken exchange, not a visual.
- **Large groups (25–30 students):** Cap at 2 volunteers total rather than
  3, and rely more on chat reactions ("type what you think I'll ask next")
  to keep the rest of the class engaged as active predictors, not passive
  watchers.
