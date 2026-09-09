# Class 03 — Student Notes

**Bong Study Hub — Foundation Batch 2026**
**Understanding Data**
*From the Real World → Information → Data*

These notes summarize what we covered in class. Use them to revise, not
to learn the topic for the first time — the real learning happened in
the room, through the debates and activities. No coding, no databases,
and no statistics appear anywhere in this class — everything here is
conceptual.

<!-- PAGE BREAK -->

## The Big Question

In Class 02, everything started with one word: **Data**. We moved past
it quickly, because the exciting part was what came next — Learning,
Model, Prediction. We never actually stopped and asked what data *is*.

Today we go back and open that box:

> **"How do we turn something happening in the real world into
> something a computer can work with?"**

Think about how you'd answer a simple question like *"how crowded is
your college canteen right now?"* You might say "very crowded," "around
50 people," "almost empty," or "80% full." All of these are different
*forms* of the same thing — and figuring out exactly what that thing is,
and where it comes from, is what this class is about.



## 1. What Is Data?

Ask most people what "data" means, and they'll say numbers, spreadsheets,
tables, or graphs. That's not wrong — but it's incomplete. Here's the
working definition we'll use for the whole class:

> **DATA = RECORDED INFORMATION ABOUT SOMETHING**

Notice what's missing from that definition: no mention of numbers,
computers, or spreadsheets. A photo is recorded information about a
moment. A voice note is recorded information about what someone said. A
sentence like "the canteen felt almost empty" is recorded information
about a place at a point in time. All of it is data.

Numbers are just **one form** data can take — not the definition of
data.



## 2. Data Is Not Just Numbers

Once you drop the "data = numbers" assumption, data turns out to be
everywhere. It can be:

- **Numbers** — 92%, 76 marks, 18 years old
- **Text** — an email, a message, a review
- **Photographs** — a picture of a whiteboard, a face, a street
- **Audio** — a voice recording, a song
- **Location** — GPS coordinates, "Kolkata," "third floor"
- **Measurements** — temperature, height, distance
- **Records** — an attendance sheet, a purchase history

> **Think about it:** Can a photograph be data? Why or why not?

If your first instinct was "no, a photo isn't data until it's *inside* a
computer somehow" — you're noticing something real. There is a real
difference between "a photo exists" and "a computer can process it." But
that's a different, more technical question (about file formats and
storage) that we're not covering today. For this class, the only
question that matters is: *is it recorded information about something
real?* If yes, it's data.

> **Remember:** Data isn't defined by its format. A spreadsheet is one
> convenient *container* for data — it isn't what data *means*.



## 3. From the Real World to Data

So where does data actually come from? Let's trace it, using something
as simple as "it is raining outside."

- Something is happening in the **real world** — it's raining.
- Someone **observes** it — checks whether it's raining, how hard, at
  what time.
- That observation gets **recorded** — written down, said aloud, typed,
  photographed, saved in some way.
- Once it's recorded, it has become **data**.

```
REAL WORLD
    ↓
OBSERVATION
    ↓
DATA
```

The step that's easy to overlook is *recording*. If you notice it's
raining but never write it down, say it, or save it anywhere, that
observation disappears — it never became data. **Recording is what makes
an observation stick around** long enough to be used later.

This works exactly the same way for the canteen example from the start
of class: the real world is the canteen right now; observing means
looking around or checking a crowd-tracking app; recording means saying
"80% full" or typing a number somewhere. Whatever gets recorded — a
number, a sentence, or a photo — is the data.

An important idea follows directly from this chain:

> **DATA IS A REPRESENTATION OF REALITY — NOT REALITY ITSELF.**

The canteen being crowded is a real, physical fact. "80% full" is just
our *recorded description* of that fact. The two are not the same
thing — and keeping that distinction in mind will matter for the rest
of this class.



## 4. One Thing Can Give Us Many Pieces of Data

Here's something worth noticing: a single real-world thing can be
described by many different pieces of data at once.

Take a student. We could record:

```
STUDENT
  ↓
Name
Year
Attendance
Department
Marks
```

Did the student change while we listed all of that? No. Did the way we
*describe* the student change? Yes — we now have five separate pieces of
recorded information about the same one person.

This is the same idea from Section 3, applied more concretely: **data is
a representation of something**, and one real thing can be represented
by several different pieces of data at the same time — none of them
*is* the student; each is just one angle on the student.

Each one of these pieces of information — Name, Year, Attendance — is
something you'll later hear called a **feature** or an **attribute**.
For now, just notice the pattern: one real thing, many possible pieces
of data describing it.



## 5. From Examples to a Dataset

Once we start describing several students the same way, something
useful happens — we can put them in a table:

| Student | Year | Attendance | Marks |
|---------|------|------------|-------|
| A       | 1    | 82%        | 76    |
| B       | 1    | 91%        | 84    |
| C       | 1    | 68%        | 61    |

This small table introduces two ideas at once:

- **Example (or record):** one real thing, described by its data — here,
  one student.
- **Dataset:** a collection of related examples — here, the whole table.

And the table also has a visual structure worth remembering for the
rest of the course:

```
ROW    →  ONE EXAMPLE
COLUMN →  ONE KIND OF INFORMATION
```

Row A represents one student, described across every column. The
"Attendance" column represents one kind of information, recorded for
every student in the table.

> **Remember:** A column describing an example is usually called a
> **feature**. But not every dataset has a column that holds a *known
> answer* — that special kind of column is called a **label**, and it's
> a separate idea we'll cover in Section 8. Not every column is
> automatically a feature *or* a label — it depends on what role that
> column is playing.



## 6. Real-World Data Can Be Messy

Here's a table that looks a lot like the one above, but with a problem:

| Student | Age        | City       |
|---------|------------|------------|
| A       | 18         | Kolkata    |
| B       | "eighteen" | kolkata    |
| C       | *(missing)*| Calcutta   |

Look closely and you'll spot several issues:

- **Student B's age** is written as the word "eighteen" instead of the
  number 18 — same information, inconsistent form.
- **Student C's age** is missing entirely.
- **The city name** appears three different ways — "Kolkata,"
  "kolkata," and "Calcutta" — even though it's the same place.

> **REAL-WORLD DATA IS OFTEN MESSY.**

Missing values, inconsistent formats, and even outright mistakes are
completely normal. Almost no dataset arrives perfectly clean. This class
isn't about *fixing* messy data — that's a real skill called data
cleaning, and it belongs to a later part of the course. Today, the goal
is simply to be able to **recognize** messiness when you see it.



## 7. More Data Does Not Automatically Mean Better Data

Quick question: if you had one million examples, would that
automatically be good data?

Not necessarily. If every one of those million examples is wrong, or
they're all nearly identical to each other, the sheer quantity doesn't
help. On the other hand, 1,000 examples that are accurate and cover a
good variety of real situations can be far more useful than a much
bigger pile of bad or repetitive ones.

Good data needs to be:

- **relevant** to the question being asked
- **useful** for the specific problem
- **representative** — covering the different situations you actually
  care about, not just one narrow slice of them

> **Remember Class 02's cats-vs-dogs example?** If that system ever
> struggled, the issue was rarely "not enough photos" alone — it was
> often that the photos weren't *varied* enough (say, only small dogs
> and only big cats). More data helps, but only if it's the right kind
> of data.



## 8. Features and Labels

Some datasets contain a special kind of column: one that holds an
answer we already know. Let's look at an example — emails that someone
has already sorted:

| Email                          | Sender  | Time    | Label    |
|---------------------------------|---------|---------|----------|
| "Congratulations! You won a prize." | Unknown | 2:14 AM | Spam     |
| "Meeting at 3 PM"                   | Colleague | 9:02 AM | Not Spam |

Here, two different kinds of columns are doing two different jobs:

> **FEATURE** — a piece of information *describing* an example.
> In the table above: the email's words, the sender, and the time are
> all features.

> **LABEL** — the *known answer or category* attached to an example,
> when one exists.
> In the table above: "Spam" and "Not Spam" are labels — someone already
> decided the answer for each email.

**Not every dataset has a label.** Plenty of datasets are just a
collection of examples described by features, with no known answer
attached at all. Today, we're only learning what the word *label* means
for the datasets that do have one.



## 9. Useful Data Depends on the Question

Here's one of the most important ideas from today. Suppose our college
wants to answer this question:

> **"Can we predict when the college canteen will be crowded?"**

What data might actually help? Some reasonable options:

- the time of day
- the day of the week
- how many students are on campus
- whether there's a class break happening
- the weather, if it affects footfall

Now ask a different question: would that same data — time, day, class
breaks — be useful for predicting whether a student will enjoy a movie?
Clearly not. The two questions need almost completely different
information.

> **USEFUL DATA DEPENDS ON THE QUESTION.**

There's no such thing as "good data" that exists on its own, separate
from a purpose. Data is useful *relative to* the specific thing you're
trying to understand or predict.

> **Think about it:** If the college canteen becomes crowded at 1 PM,
> what information could we record that might help us understand why?

There's no single "correct" list here — that's the point. The real
skill is learning to ask: *what's the question, and what might actually
matter for answering it?*



## 10. Data Is a Representation of Reality

Go back to the student example from Section 4 — Name, Year, Attendance,
Department, Marks. Does that list completely describe the student as a
person?

Obviously not. It says nothing about their personality, interests,
friendships, or health. And that's not a mistake — it's simply true of
*any* data, always:

> **EVERY REPRESENTATION LEAVES SOMETHING OUT.**

This means **REAL WORLD ≠ DATA**. Data is a lens we choose to look
through — and whatever we don't choose to observe and record simply
isn't available later, to a person or to a machine. That's exactly why
deciding *what to record* is such an important decision in the first
place.



## 11. Connecting Data Back to Machine Learning

Let's put the whole day on one chain. Class 02 gave you the bottom four
steps. Today, we filled in what comes before them:

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

Nothing from Class 02 has changed — Data → Learning → Model → Prediction
is exactly what it always was. We simply opened up where **Data**
actually comes from.

And inside that same DATA box, today also built this:

```
DATA
    ↓
EXAMPLES
    ↓
FEATURES
    ↓
LABELS
    ↓
DATASET
```

Examples get described by features. Some examples also carry a label.
A collection of related examples is a dataset. "Data" was never one
abstract, magic ingredient — it's built out of pieces you now know by
name.



## 12. Data ≠ Machine Learning

One last, important distinction: if someone hands you a dataset right
now, do you automatically have Machine Learning?

**No.**

> **DATA ≠ MACHINE LEARNING**

Data is an *ingredient*. Machine Learning is the *process* — covered in
Class 02 — that uses data to learn patterns and build a model. Today's
entire class lived inside that first ingredient.



## Quick Recap

- **Data** is recorded information about something — not just numbers.
- Data comes from the real world through **observation** and
  **recording**: `REAL WORLD → OBSERVATION → DATA`.
- One real-world thing can be described by many different pieces of
  data at once.
- An **example** (or record) is one real thing, described by its data.
  A **dataset** is a collection of related examples.
- In a table: a **row** is one example; a **column** is one kind of
  information.
- Real-world data can be **messy** — missing, inconsistent, or wrong.
- **More data isn't automatically better data** — relevance, usefulness,
  and variety matter more than raw quantity.
- A **feature** describes an example. A **label** is the known
  answer/category for an example, when one exists. Not every dataset
  has a label.
- **Useful data depends on the question** being asked — there's no such
  thing as universally "good" data.
- Data is a **representation** of reality, not reality itself — every
  representation leaves something out.
- **Data ≠ Machine Learning** — data is the ingredient; learning is the
  process.



## Key Terms

| Term | Meaning |
|---|---|
| **Data** | Recorded information about something in the real world. |
| **Dataset** | A collection of related examples. |
| **Example** | One real thing, described by its data (also called a record). |
| **Feature** | A piece of information describing an example. |
| **Label** | The known answer or category attached to an example, when one exists. |



## Think About It

Try answering these in your own words — you don't need exact wording,
just the right idea.

1. What is data, in your own words?
2. Can you name a piece of data that isn't a number?
3. How does an everyday observation turn into recorded data?
4. In a data table, what does one row mean? What does one column mean?
5. What's the difference between a feature and a label?
6. Why can real-world data be messy?
7. Why doesn't having more data automatically make it better data?



## Final Takeaway

> **"Before we can teach a machine from data, we first have to
> understand what data we're giving it."**
