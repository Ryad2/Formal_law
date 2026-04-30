# One-Page Method Summary: Melody Representation, Alignment, and Similarity Scoring

## Project Goal

This project develops an explainable decision-support prototype for
melody-focused music copyright disputes. The system does not attempt
automated adjudication. Instead, it computes structured melody
similarity using transparent alignment and scoring methods, which are
later combined with a minimal legal rule layer.

The core computational contribution consists of:

1.  A melody representation (interval sequence),
2.  Two alignment strategies (global and local),
3.  Two similarity scoring schemes (strict PMI and tolerant PMI),
4.  A baseline model and an improved model.

------------------------------------------------------------------------

## Melody Representation: Interval Sequence

Each song excerpt is manually curated to contain only the relevant
melody (monophonic MIDI). From each MIDI file:

1.  Notes are sorted by start time.
2.  The ordered pitch sequence is extracted.
3.  The pitch sequence is converted into an **interval sequence**.

Formally, given pitches:

P = \[p1, p2, ..., pn\]

The interval sequence is:

I = \[p2 - p1, p3 - p2, ..., pn - p(n-1)\]

Example:

Pitches:\
60, 62, 65, 64

Intervals:\
+2, +3, −1

This representation is:

-   Transposition-invariant\
-   Focused on melodic contour\
-   Closer to legal notions of "melodic identity"\
-   Independent of key changes

The interval sequence is the input to the alignment stage.

------------------------------------------------------------------------

## Alignment Algorithms

Because melodies may differ in length or contain insertions and
variations, dynamic programming alignment is used.

### 1. Global Alignment (Needleman--Wunsch)

Global alignment forces alignment across the entire sequences.

It answers:

> How similar are these melodies overall?

Characteristics: - Penalizes insertions and deletions - Sensitive to
overall structure - Suitable for whole-work comparison

This forms the backbone of the **baseline model**.

------------------------------------------------------------------------

### 2. Local Alignment (Smith--Waterman)

Local alignment identifies the highest-scoring matching subsequence.

It answers:

> Is there a highly similar fragment embedded somewhere in the melodies?

Characteristics: - Finds best matching motif - Ignores unrelated
surrounding material - Better captures fragment copying

This forms part of the **improved model**.

------------------------------------------------------------------------

## Similarity Scoring

After alignment, similarity is quantified using Percent Melodic Identity
(PMI).

### Strict PMI (Baseline)

PMI = (Exact Matches / Alignment Length) \* 100

An interval counts as a match only if:

A\[i\] = B\[i\]

This approach: - Is conservative - Detects literal melodic identity -
Under-detects ornamented or slightly varied copying

------------------------------------------------------------------------

### Tolerant PMI (Improved)

Instead of exact equality, a tolerance is introduced:

\|A\[i\] - B\[i\]\| ≤ δ

Where δ (e.g., 1 semitone interval difference) allows minor variation.

This captures: - Ornamentation - Slight melodic modifications -
Near-matches

It models the legal concept of substantial similarity rather than
literal duplication.

------------------------------------------------------------------------

## Two Model Configurations

### Baseline Model

Global Alignment\
+\
Strict PMI

Captures: - Quantitative similarity - Whole-work resemblance - Literal
melodic copying

------------------------------------------------------------------------

### Improved Model

Local Alignment\
+\
Tolerant PMI

Captures: - Motif-level similarity - Fragment reuse - Substantial
similarity under variation

------------------------------------------------------------------------

## Conceptual Rationale

The distinction between global and local alignment mirrors a central
doctrinal tension in copyright law:

-   Quantitative similarity vs qualitative importance\
-   Whole-work copying vs fragment copying

The baseline model represents a rigid structural comparison.\
The improved model reflects how courts often evaluate recognizable
melodic fragments rather than entire works.

Together, these models allow empirical testing of the research question:

> Does combining local alignment and tolerant similarity better
> reproduce melody-based copyright dispute outcomes than strict global
> similarity alone?
