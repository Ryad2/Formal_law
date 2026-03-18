# Legal Annotation Notes

Our legal annotations are designed to support a narrow, explainable prototype rather than to encode the full complexity of copyright law.

## Purpose of the annotations

The goal of the annotation layer is to connect the similarity score to a small number of legally relevant questions. These annotations do not determine liability. They simply structure how computational output should be interpreted in context.

## Annotation principles

### 1. Narrow scope
We only annotate what is necessary for the prototype:
- whether the case is actually about melody
- whether access appears supported
- whether the similar material appears protectable
- whether the broader context makes automated interpretation unreliable

### 2. Conservative coding
If the available material does not support a confident legal coding, we use `unclear` rather than overstate certainty.

### 3. Explainability over completeness
The purpose of the rule layer is not doctrinal exhaustiveness. It is to make the output interpretable and to prevent misleading conclusions from raw similarity scores alone.

## Coding guidance by variable

### access
We code `yes` when access is admitted, established, or strongly supported in the case materials. We code `no` when there is no meaningful evidence of access or when independent creation is strongly foregrounded. We code `unclear` when the available materials do not support a confident conclusion.

### melody_scope
We code `yes` when the disputed similarity is substantially melodic. We code `no` when the case is mainly driven by lyrics, production, timbre, groove, harmony, arrangement, sampling, or other non-melodic dimensions.

### protectable_material
We code `yes` when the allegedly similar material appears distinctive enough to plausibly matter as protected melodic expression. We code `no` when the resemblance concerns generic, trivial, or weakly protectable material. We code `unclear` when the available material does not support a stable conclusion.

### context_override
We code `yes` when the legal or procedural context makes the score especially unreliable in isolation, for example because the dispute turns on issues beyond melody or because the materials are too incomplete for a clean interpretation. Otherwise we code `no`.

## Why melody-only reasoning is useful but limited

Melody-focused similarity measures are useful because they make one important component of the dispute measurable, comparable, and transparent. They can therefore support legal analysis by showing where resemblance appears weak, moderate, or strong under a defined method.

At the same time, melody-only reasoning is limited because copyright disputes are not resolved by similarity alone. Access, the nature of the material, and broader contextual issues can significantly affect how similarity should be interpreted. For that reason, our prototype is designed as decision support rather than auto-adjudication.

## Annotation output in the corpus

Each case row should contain:
- one value for each legal variable
- a short explanatory note if needed
- consistent coding across similar situations

The notes column should be used to justify ambiguous or non-obvious codings in one or two short sentences.
