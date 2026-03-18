# Legal Variables

We use a deliberately small set of legal variables in order to keep the prototype explainable and manageable.

## 1. access
Possible values: `yes`, `no`, `unclear`

Meaning:
This variable captures whether there is evidence or a plausible finding that the defendant had access to the plaintiff's work.

Coding rule:
- `yes` if access is established, admitted, strongly supported, or treated as sufficiently plausible in the dispute
- `no` if there is no evidence of access, or if the case materials strongly point toward independent creation without access
- `unclear` if the available material does not allow a confident coding

## 2. melody_scope
Possible values: `yes`, `no`

Meaning:
This variable captures whether the dispute is meaningfully about melodic similarity.

Coding rule:
- `yes` if the allegedly copied material is principally melodic
- `no` if the dispute is mainly about something else, such as lyrics, sampling, timbre, groove, harmony, arrangement, production, or overall vibe

## 3. protectable_material
Possible values: `yes`, `no`, `unclear`

Meaning:
This variable captures whether the similar material appears to concern arguably protectable melodic expression rather than trivial, generic, or commonplace material.

Coding rule:
- `yes` if the allegedly similar material appears sufficiently distinctive or central to the protected expression
- `no` if the similarity concerns material that appears too generic, too short, too conventional, or otherwise weakly protectable
- `unclear` if the available material does not allow a confident coding

## 4. context_override
Possible values: `yes`, `no`

Meaning:
This variable flags cases where the computational score should not be taken at face value because the legal or procedural context is unusual.

Coding rule:
- `yes` if there is a strong reason why the score alone is misleading, for example because the case is dominated by non-melodic issues, procedural posture, evidentiary asymmetry, or contextual features outside the model
- `no` otherwise