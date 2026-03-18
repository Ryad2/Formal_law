# Legal Rules v0

The prototype does not output a legal judgment. It outputs a structured recommendation supported by transparent reasoning.

## Rule 1
If `melody_scope = no`, output:

**outside melodic scope**

Rationale:
The prototype is designed only for disputes where melodic similarity is central. If the case is mainly about something else, the system should explicitly say that it falls outside its intended scope.

## Rule 2
If `melody_scope = yes` and `access = no`, output:

**no strong prima facie concern**

Rationale:
Even a relatively high similarity score should be treated cautiously if there is no meaningful evidence of access.

## Rule 3
If `melody_scope = yes`, `access != no`, and `similarity < threshold`, output:

**threshold not met**

Rationale:
The computational score does not support a strong concern under the current threshold.

## Rule 4
If `melody_scope = yes`, `access != no`, `similarity >= threshold`, and `protectable_material = no`, output:

**similarity in non-protectable material**

Rationale:
The score may indicate resemblance, but not necessarily resemblance in material that is legally strong enough to matter.

## Rule 5
If `melody_scope = yes`, `access != no`, `similarity >= threshold`, and `protectable_material != no`, output:

**prima facie concern**

Rationale:
The combined score and legal coding suggest that the case deserves closer legal scrutiny.

## Rule 6
If `context_override = yes`, append:

**manual legal review required**

Rationale:
This reminds the user that the prototype is only a support tool and that some cases cannot be responsibly summarized by score-based reasoning alone.