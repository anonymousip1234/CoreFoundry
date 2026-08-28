# Class 01 — Question Bank

**Bong Study Hub — Foundation Batch 2026 · Welcome to Computer Science**

Source of truth: `Class_01_Master_Instructor_Guide.md`, `Class_01_Student_Notes.md`,
`Class_01_Pen_Tablet_Board_Plan.md`. No new terminology or advanced content
is introduced here — every question targets a concept already in those
documents.

**How to use this bank:** these are discovery questions, not quiz
questions. The goal is for a student to *arrive at* a concept through the
question, not to check whether they memorized it. Don't ask every question
in a section — pick 2–3 that fit the room's energy. Not every question
needs to be difficult; each section deliberately mixes Foundation, Builder,
and Challenge.

**Card format:** Question → Purpose → Expected beginner responses →
Possible incorrect responses → How instructor should respond → Follow-up →
Difficulty.

---

## 1. Opening

**Q1.1 — "How many of you used a smartphone today?"**
- **Purpose:** Low-stakes warm-up; establishes that everyone already has a relationship with technology.
- **Expected beginner responses:** Most hands go up.
- **Possible incorrect responses:** None — this is not a content question.
- **How instructor should respond:** Smile, count roughly, move straight to the next question — don't linger.
- **Follow-up:** "How many of you know what happens inside it when you press a button?"
- **Difficulty:** Foundation

**Q1.2 — "What is Computer Science?"**
- **Purpose:** Surface students' existing (partial) mental model before correcting it — this is the anchor question of the whole class.
- **Expected beginner responses:** "Coding," "programming," "computers," "AI," "software," "making apps."
- **Possible incorrect responses:** "Hacking," "fixing computers," "using Excel" — technology-adjacent but not CS.
- **How instructor should respond:** Accept every answer without judgment — write or repeat each one back. Say "you're all partly right" rather than correcting any single answer.
- **Follow-up:** "If Computer Science was only coding, would things like the internet or AI even fit anywhere?"
- **Difficulty:** Foundation

**Q1.3 — "Who here has never written a single line of code — be honest, no judgment?"**
- **Purpose:** Normalizes the range of backgrounds in the room *before* anyone feels behind; sets emotional safety for the rest of class.
- **Expected beginner responses:** Some hands up, some hesitant.
- **Possible incorrect responses:** N/A.
- **How instructor should respond:** Immediately follow with "and who already knows some Python?" — showing both groups exist and both are welcome.
- **Follow-up:** "By the end of today, both groups should understand today's ideas equally well — coding comes later."
- **Difficulty:** Foundation

---

## 2. What is Computer Science?

**Q2.1 — "Looking at this map, which of these have you already touched without realizing it was Computer Science?"**
- **Purpose:** Makes the CS map personally relevant instead of an abstract list.
- **Expected beginner responses:** "Using an app," "playing a game," "connecting to Wi-Fi."
- **Possible incorrect responses:** Silence at first — this is normal, not a wrong answer.
- **How instructor should respond:** If silence continues past ~5 seconds, offer one example yourself ("using a banking app touches security and databases") to prime the room.
- **Follow-up:** "So which one of these boxes is programming?"
- **Difficulty:** Foundation

**Q2.2 — "Is coding all of Computer Science, or one part of it?"**
- **Purpose:** Directly checks whether the CS ≠ Coding idea landed.
- **Expected beginner responses:** "One part of it."
- **Possible incorrect responses:** "It's basically the same thing" — common, expected misconception.
- **How instructor should respond:** "That's what most people think coming in — that's exactly the idea we're correcting today." Point back at the map.
- **Follow-up:** "Name one thing on this map that isn't coding."
- **Difficulty:** Foundation

**Q2.3 — "Could something on this map belong to more than one area at once? Give an example."**
- **Purpose:** Pushes stronger students to see the map as overlapping fields, not rigid boxes, without adding new vocabulary.
- **Expected beginner responses:** May need a nudge; a good answer is something like "a banking app" — programming + databases + security together.
- **Possible incorrect responses:** Treating it as a trick question with no answer.
- **How instructor should respond:** If no one bites in ~10 seconds, supply the banking-app example yourself and ask them to find one more.
- **Follow-up:** "So is this map really nine separate boxes, or nine overlapping ideas?"
- **Difficulty:** Challenge

---

## 3. Computer / Program / Application

**Q3.1 — "Is a calculator app a program, an application, or both?"**
- **Purpose:** Tests whether the two definitions (Program = instructions, Application = useful packaged tool) are distinguishable, not identical.
- **Expected beginner responses:** "Both," sometimes with hesitation.
- **Possible incorrect responses:** "Just an app" — missing that it's built from instructions underneath.
- **How instructor should respond:** Confirm "both" is right and explain *why* — program is the instructions, application is the packaged, useful version for a user.
- **Follow-up:** "What's the smallest possible 'program' you can imagine — something with almost no real use but it still counts?"
- **Difficulty:** Foundation

**Q3.2 — "What is a computer, in your own words — not the dictionary definition?"**
- **Purpose:** Gets a working definition ("a machine that follows instructions") from the room's own language before giving the formal one.
- **Expected beginner responses:** "A machine," "an electronic device," "something that runs apps."
- **Possible incorrect responses:** Definitions that only describe a laptop/phone physically, missing "executes instructions."
- **How instructor should respond:** Build toward "a machine capable of executing instructions" using their words as the starting material.
- **Follow-up:** "Does that definition only cover laptops and phones, or could it include other things?"
- **Difficulty:** Foundation

**Q3.3 — "Name an application you use daily that is clearly built from many small programs working together."**
- **Purpose:** Stretches the Program → Application relationship toward real complexity, without introducing systems-design vocabulary.
- **Expected beginner responses:** "A messaging app," "a food delivery app."
- **Possible incorrect responses:** Naming something and stopping there without explaining "many small programs."
- **How instructor should respond:** Ask "what are two different jobs that app does?" to surface the idea of multiple parts.
- **Follow-up:** "Could one of those parts work as its own separate program?"
- **Difficulty:** Builder

---

## 4. Input → Process → Output

**Q4.1 — "If I type 15 + 20 into a calculator, where does that number go — which box?"**
- **Purpose:** Anchors the abstract I-P-O model to something concrete before generalizing.
- **Expected beginner responses:** "Input."
- **Possible incorrect responses:** Confusing input with output (saying "35 is the input").
- **How instructor should respond:** Gently trace the arrow with the pen: "input goes in here, comes out as output over here."
- **Follow-up:** "What is the process doing in between?"
- **Difficulty:** Foundation

**Q4.2 — "What's the input and output when you unlock your phone with your face?"**
- **Purpose:** Transfers the I-P-O model to a new, more modern example — checks generalization, not memorization.
- **Expected beginner responses:** Input = face/camera image, Output = unlocked screen.
- **Possible incorrect responses:** Naming the phone itself as the input.
- **How instructor should respond:** Accept the process being unclear — "process = matching, and that's fine, it's still a mystery box today."
- **Follow-up:** "What do you think is happening inside that 'Process' box?"
- **Difficulty:** Foundation

**Q4.3 — "Can a system have more than one input feeding the same process? Give an example."**
- **Purpose:** Extends the three-box model toward realistic complexity for stronger students, while staying inside today's mental model (no new diagram).
- **Expected beginner responses:** May need a nudge; good answer: a login screen takes username *and* password as two inputs into one process.
- **Possible incorrect responses:** Confusing "multiple inputs" with "multiple processes."
- **How instructor should respond:** If nothing comes up in ~10 seconds, offer the login example, then ask them to find a second one.
- **Follow-up:** "Does the calculator example already have two inputs, if you think about it?" (the two numbers)
- **Difficulty:** Challenge

---

## 5. Problem → Logic → Algorithm → Program → Result

**Q5.1 — "Everything starts with a real problem. Give me one — anything."**
- **Purpose:** Opens the most important diagram of the class by letting students supply the starting point, not the instructor.
- **Expected beginner responses:** Anything concrete — "finding the largest of two numbers," "sorting my playlist," "splitting a bill."
- **Possible incorrect responses:** A "problem" that's really a solution already ("use an app") — redirect toward the underlying need.
- **How instructor should respond:** Accept it, then steer toward (or directly use) "find the larger of two numbers, A = 15, B = 21" so the rest of the chain has one consistent worked example.
- **Follow-up:** "Before I touch a computer, what's the very first thing I have to do?"
- **Difficulty:** Foundation

**Q5.2 — "I've thought it through in my head. What do I need to do to make that thinking usable — so someone else could follow it?"**
- **Purpose:** Drives the Logic → Algorithm transition from the room's own reasoning, not a definition.
- **Expected beginner responses:** "Write it down," "explain the steps," "make a list."
- **Possible incorrect responses:** Jumping straight to "write code" — skips the algorithm step entirely.
- **How instructor should respond:** If someone jumps to code, say "close — but before code, what do we write first, in plain words?"
- **Follow-up:** "So what would step 1 of those written-down steps actually say?"
- **Difficulty:** Foundation

**Q5.3 — "This is still just words on a board. What has to happen before a computer can actually do this?"**
- **Purpose:** Drives the Algorithm → Program transition, reinforcing that an algorithm alone doesn't run.
- **Expected beginner responses:** "Turn it into code," "translate it into a programming language."
- **Possible incorrect responses:** "The computer just understands it" — a common but incorrect assumption.
- **How instructor should respond:** "Computers don't understand English or our steps directly — someone has to translate them into a language it runs. That's called a program."
- **Follow-up:** "Could two different languages both implement this same algorithm? What would stay the same, what would change?"
- **Difficulty:** Builder

**Q5.4 — "Could two completely different algorithms solve the exact same problem, and both be correct?"**
- **Purpose:** Pushes stronger students to see "algorithm" as a strategy space, not a single fixed answer — without introducing efficiency/complexity vocabulary.
- **Expected beginner responses:** Uncertain at first; a good example is comparing A and B in either order, or checking "is A ≥ B" vs. "is B ≥ A."
- **Possible incorrect responses:** "No, there's only one way to do it."
- **How instructor should respond:** "Let's test that idea — can anyone describe a different (but still correct) way to find the larger of two numbers?"
- **Follow-up:** "So is there one correct algorithm for a problem, or can there be several?"
- **Difficulty:** Challenge

---

## 6. Algorithm

**Q6.1 — "Given A = 15 and B = 21, how would you find the larger number? Talk me through it."**
- **Purpose:** The core worked example — builds the algorithm from student reasoning instead of presenting it finished.
- **Expected beginner responses:** "Compare them," "check which is bigger."
- **Possible incorrect responses:** Skipping the comparison and guessing the answer outright ("21") without stating the *method*.
- **How instructor should respond:** "21 is right — but I need the method, not just the answer. What's the rule that gets us there every time?"
- **Follow-up:** "What if A and B were different numbers — would your same steps still work?"
- **Difficulty:** Foundation

**Q6.2 — "What is an algorithm, in your own words?"**
- **Purpose:** Checks whether the formal definition ("a finite sequence of clear steps used to solve a problem") is understandable in student language, not just memorized.
- **Expected beginner responses:** "A set of steps," "instructions to solve something," "a plan."
- **Possible incorrect responses:** "It's code" (conflating algorithm with program).
- **How instructor should respond:** "Close — code is one way to *write down* an algorithm, but the algorithm itself is just the steps, in any language, even plain English."
- **Follow-up:** "So is an algorithm closer to a recipe, or closer to the finished dish?"
- **Difficulty:** Foundation

**Q6.3 — "Could two different programming languages implement the exact same algorithm?"**
- **Purpose:** Cements Algorithm ≠ Program by testing language-independence directly.
- **Expected beginner responses:** Uncertain — "maybe," "I don't know."
- **Possible incorrect responses:** "No, each language would need a different algorithm."
- **How instructor should respond:** "Let's test that — if the *steps* don't change, what's actually different between the Python version and the C version?"
- **Follow-up:** "So what's the one thing that changes when you move from algorithm to program?"
- **Difficulty:** Builder

**Q6.4 — "How would your algorithm for 'larger of two numbers' need to change if A and B were equal?"**
- **Purpose:** Forces students to notice an edge case in their own algorithm — a genuine discovery moment, not a trick.
- **Expected beginner responses:** "Add a rule for when they're equal," "say they're the same."
- **Possible incorrect responses:** "It doesn't need to change" (missing the edge case).
- **How instructor should respond:** "Run your algorithm with A = 15, B = 15 — what does it output right now? Is that what you want?"
- **Follow-up:** "What assumption did your original algorithm quietly make?"
- **Difficulty:** Challenge

---

## 7. Computational Thinking

**Q7.1 — "If I asked you to plan a birthday party, would you do it as one giant task, or break it into pieces?"**
- **Purpose:** Introduces Decomposition through a relatable non-technical example.
- **Expected beginner responses:** "Break it into pieces — invitations, food, venue."
- **Possible incorrect responses:** N/A — this is intuitive for almost everyone.
- **How instructor should respond:** Confirm quickly and name it: "that's called decomposition."
- **Follow-up:** "Can you decompose one everyday task of your own into 3–4 smaller pieces?"
- **Difficulty:** Foundation

**Q7.2 — "What's similar between comparing two numbers and comparing two people's height?"**
- **Purpose:** Introduces Pattern Recognition by connecting two superficially different problems.
- **Expected beginner responses:** "You're comparing which one is bigger/taller — same idea."
- **Possible incorrect responses:** Focusing on surface differences ("one is numbers, one is people") instead of the underlying comparison.
- **How instructor should respond:** "Right — different subject, same underlying action. That's pattern recognition."
- **Follow-up:** "Can you find a pattern between two problems that look completely unrelated on the surface?"
- **Difficulty:** Builder

**Q7.3 — "When you drive a car, do you think about the engine's combustion cycle, or just 'accelerator = go'?"**
- **Purpose:** Introduces Abstraction — ignoring irrelevant detail to focus on what matters.
- **Expected beginner responses:** "Just accelerator = go."
- **Possible incorrect responses:** Overthinking the question and describing actual engine mechanics.
- **How instructor should respond:** "Exactly — you're ignoring huge amounts of detail on purpose. That's abstraction."
- **Follow-up:** "What's something else you use every day where you ignore how it works internally?"
- **Difficulty:** Foundation

**Q7.4 — "Which of today's earlier activities was already an example of algorithmic thinking?"**
- **Purpose:** Connects Computational Thinking's fourth quadrant back to Drawing 3 / the "larger of two numbers" exercise — reinforcement, not new content.
- **Expected beginner responses:** "The larger-of-two-numbers algorithm we built."
- **Possible incorrect responses:** Naming the CS map or the I-P-O diagram (those are models, not algorithms).
- **How instructor should respond:** Confirm and tie it back explicitly: "you did this twenty minutes ago without a label for it."
- **Follow-up:** "So you've already used all four computational thinking ideas today — which was your favorite?"
- **Difficulty:** Foundation

---

## 8. Tea Activity

These are debrief/reflection prompts to use *around* the activity — not
the in-character clarifying questions the instructor asks while
role-playing the computer (those live entirely in
`03_Tea_Activity_Facilitator_Guide.md`).

**Q8.1 — "What just happened when you said 'boil the water'?"**
- **Purpose:** Immediate post-instruction reflection — gets students to name the gap themselves.
- **Expected beginner responses:** "You kept asking me questions," "I thought that was enough detail but it wasn't."
- **Possible incorrect responses:** "You were just being difficult" (understandable in the moment — redirect gently, see below).
- **How instructor should respond:** "I was — on purpose. I only did exactly what you told me. What did I actually need to know that you didn't say?"
- **Follow-up:** "If you had to say it again, what would you add?"
- **Difficulty:** Foundation

**Q8.2 — "Why do you think I kept asking 'where,' 'how much,' 'what if'?"**
- **Purpose:** Makes the literal-computer behavior explicit and connects it to the class's core theme.
- **Expected beginner responses:** "Because computers need exact instructions," "because you don't assume anything."
- **Possible incorrect responses:** "Because you wanted to make it hard" (again, understandable — redirect toward the lesson).
- **How instructor should respond:** "Right — I wasn't being difficult, I was being *precise*. That's what a computer actually does."
- **Follow-up:** "What's one assumption you made that a computer wouldn't make?"
- **Difficulty:** Foundation

**Q8.3 — "If you had to rewrite your tea instructions to handle 'there's no gas available,' what would you add — without knowing any code?"**
- **Purpose:** Seeds the idea of a decision/condition in an algorithm without introducing formal branching syntax — matches the guide's "seed, not a lesson" framing.
- **Expected beginner responses:** "Say what to do instead — use an electric kettle, or stop and tell someone."
- **Possible incorrect responses:** Trying to write actual code syntax (if/else) — gently redirect to plain English.
- **How instructor should respond:** "Good — notice your algorithm just grew a decision: 'if this, do that, otherwise do this other thing.' You'll meet that properly when we start programming."
- **Follow-up:** "Can you think of another everyday instruction that secretly has a decision hidden inside it?"
- **Difficulty:** Challenge

---

## 9. Traditional Programming vs. Machine Learning vs. Generative AI

**Q9.1 — "Look at the left-most box in each of these three rows. What changed, row by row?"**
- **Purpose:** The core discovery question of Drawing 5 — surfaces the rules → data → prompt shift directly from observation.
- **Expected beginner responses:** "It goes from rules, to data, to a prompt."
- **Possible incorrect responses:** Focusing on the output box instead of the input box.
- **How instructor should respond:** "Exactly — that's the whole story of this slide in one sentence."
- **Follow-up:** "Who writes the rules in traditional programming? Who — or what — supplies them in machine learning?"
- **Difficulty:** Foundation

**Q9.2 — "Which pipeline uses a prompt — traditional programming, ML, or GenAI?"**
- **Purpose:** Simple recall/anchoring check before moving to the staircase.
- **Expected beginner responses:** "Generative AI."
- **Possible incorrect responses:** Confusing "prompt" with "input" generally and picking traditional programming.
- **How instructor should respond:** "Right — and notice traditional programming also has an input, just not a prompt to a model. What's the difference?"
- **Follow-up:** N/A (short check question).
- **Difficulty:** Foundation

**Q9.3 — "Why might 'rules written by a human' struggle for a problem like recognizing handwriting, where machine learning tends to work better?"**
- **Purpose:** Challenge-level conceptual bridge — no ML math, just intuition about why some problems resist hand-written rules.
- **Expected beginner responses:** "Handwriting is too different from person to person to write exact rules for," "there are too many variations."
- **Possible incorrect responses:** "Because rules are old-fashioned" (vague, not reasoned).
- **How instructor should respond:** "Good instinct — push further: what would you have to write a *rule* for, exactly, to catch every possible handwriting style?"
- **Follow-up:** "So is machine learning replacing programming, or building on top of it?"
- **Difficulty:** Challenge

---

## 10. Learning Staircase

**Q10.1 — "Which two steps are we circling, and why those two?"**
- **Purpose:** Confirms students understand today's position on the roadmap.
- **Expected beginner responses:** "Programming and Computer Science — because that's where we're starting."
- **Possible incorrect responses:** Naming a later step (Machine Learning, LLMs) as "where we are."
- **How instructor should respond:** "Right — everything above those two steps is still ahead of us, and that's exactly the point."
- **Follow-up:** "Why not start at step 5 or 6 and learn AI directly?"
- **Difficulty:** Foundation

**Q10.2 — "If we skipped straight to step 8 (Agents) today, what problems do you think we'd run into?"**
- **Purpose:** Builder-level reasoning about *why* the staircase order matters, reinforcing the "build the staircase" message without new content.
- **Expected beginner responses:** "We wouldn't understand the basics underneath it," "we'd be lost."
- **Possible incorrect responses:** "Nothing, AI tools are easy to use" (conflating *using* AI with *building* AI systems).
- **How instructor should respond:** "Using a tool and building one are different things — which one is this four-month program teaching?"
- **Follow-up:** N/A.
- **Difficulty:** Builder

---

## 11. Final Recap

These five questions are the class's official recap (also in the Master
Instructor Guide §11) — ask them in the last 6–8 minutes, cold-call or
open-floor.

**Q11.1 — "In your own words — what is Computer Science?"**
- **Purpose:** Tests whether "CS ≠ Coding" actually landed, in the student's own language.
- **Expected beginner responses:** "The study of how computers solve problems / handle information," possibly naming 1–2 subfields.
- **Possible incorrect responses:** "It's coding," stated without qualification.
- **How instructor should respond:** "Coding is part of it — what else is part of it?"
- **Follow-up:** N/A (closing recap question).
- **Difficulty:** Foundation

**Q11.2 — "What's the difference between an algorithm and a program?"**
- **Purpose:** Tests the single most important distinction of the class.
- **Expected beginner responses:** "Algorithm is the steps/strategy, program is the steps written in a programming language."
- **Possible incorrect responses:** "They're the same thing."
- **How instructor should respond:** Redirect with the recipe/dish analogy.
- **Follow-up:** N/A.
- **Difficulty:** Foundation

**Q11.3 — "Give me an input, a process, and an output for something you did this morning."**
- **Purpose:** Tests transfer of the I-P-O model to a brand-new, personal example.
- **Expected beginner responses:** Any coherent triple (e.g., alarm sound = input, waking up = process, getting out of bed = output).
- **Possible incorrect responses:** Naming only two of the three, or an output with no clear input.
- **How instructor should respond:** Probe with "what triggered that?" if a piece is missing.
- **Follow-up:** N/A.
- **Difficulty:** Builder

**Q11.4 — "Why does a computer need very precise instructions, more precise than a human usually needs?"**
- **Purpose:** Tests whether the tea activity's lesson generalized beyond the activity itself.
- **Expected beginner responses:** Callback to the tea activity — computers don't fill in unstated assumptions the way humans do.
- **Possible incorrect responses:** "Because computers are dumb."
- **How instructor should respond:** "Not dumb — literal. It only does exactly what it's told. Sharpen that for me."
- **Follow-up:** N/A.
- **Difficulty:** Foundation

**Q11.5 — "Where does today's lesson eventually connect to AI?"**
- **Purpose:** Tests the CS → AI bridge — the one misconception that must not stand uncorrected before dismissing class.
- **Expected beginner responses:** "AI is built on top of programming and CS — we're building the foundation first" / mentions the staircase.
- **Possible incorrect responses:** "AI is unrelated to what we learned today."
- **How instructor should respond:** If this misconception surfaces, correct it directly and plainly before ending class — do not let the session close on it.
- **Follow-up:** N/A.
- **Difficulty:** Builder
