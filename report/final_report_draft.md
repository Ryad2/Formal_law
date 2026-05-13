# Formalizing Copyright Law through Melody Similarity

An explainable decision-support prototype for music copyright disputes

Ryad Mohamed Aouak, Romain Greub, Gresi Alejandra Velasco-Miranda, Zichun Zhou

Law and Computation II, EPFL

13 May 2026

## Abstract

Music copyright disputes often depend on whether two works are substantially similar, yet similarity is not a self-contained legal conclusion. Courts and parties also consider access, protectability, scope, and context. This project studies that gap through a narrow decision-support prototype for melody-focused copyright cases. It does not automate adjudication. Instead, it makes one evidence layer explicit: whether two songs share a recognizable melodic fragment under computational assumptions. We built a corpus of 128 music copyright disputes, identified 15 cases with usable MIDI files, converted curated monophonic melodies into interval sequences, and compared each pair through global, local, and hybrid Percent Melodic Identity (PMI) scores. Global PMI captures whole-excerpt resemblance, while local PMI detects strong matching fragments that may be legally important even when full melodies differ. Under exploratory thresholds, global PMI flags 4 of 15 pairs, local PMI flags 11 of 15, and hybrid PMI flags 9 of 15. These results suggest that local alignment better fits the legal intuition that a recognizable fragment can matter. The project also proposes a minimal legal rule layer using access, melody scope, protectability, and context. Its main contribution is explainability: transforming melodic similarity from a black-box number into auditable evidence for legal reasoning.

## 1. Introduction

Music copyright disputes are difficult because they sit between legal judgment, musical perception, and technical comparison. A court must decide whether a defendant copied protectable expression from a plaintiff's work, but the evidence often includes musical resemblance that is hard to describe in ordinary legal language. In popular music, parties may argue over melodies, hooks, bass lines, samples, timbre, production choices, rhythmic patterns, or an overall impression of similarity. Some of these elements are more legally central than others. Some are easier to formalize computationally than others. The difficulty is not only that music is complex. It is also that legal concepts such as substantial similarity are deliberately open-textured and fact-sensitive.

This project focuses on a narrower question: how can computational melody similarity support legal reasoning without pretending to replace it? We start from the observation that many well-known music copyright disputes involve a claim that two songs share a relevant melodic passage. Melody is not the whole of music, and copyright law does not reduce infringement to a simple note-counting exercise. However, melody remains a recurring and legally intelligible object of comparison. It can be represented as an ordered sequence, aligned with another melody, and scored in a transparent way. This makes melody a useful test case for a law-and-computation capstone project.

The central research gap is that raw similarity scores are not legally meaningful by themselves. A high score does not automatically mean infringement. A low score does not automatically defeat a claim. The legal significance of a score depends on surrounding factors, including whether the defendant had access to the earlier work, whether the allegedly copied material is protectable, whether the dispute is genuinely about melody, and whether procedural or contextual features make computational comparison misleading. Existing computational approaches to melodic similarity can help quantify resemblance, but they do not by themselves explain how that resemblance should be interpreted in legal terms.

Our research question is therefore:

Can local melodic alignment capture legally relevant fragment similarity better than global comparison while remaining explainable enough for legal decision support?

The project originally aimed at a broad formalization of music copyright reasoning. During implementation, we narrowed the scope to the part that could be defended with available data and code: an explainable similarity layer for melody-focused disputes, plus a minimal legal interpretation framework. This narrowing is important. It prevents the project from making an exaggerated claim about automated legal judgment, and it makes the achieved contribution clearer. The prototype is not a judge, a legal expert system, or a complete model of copyright doctrine. It is a structured evidence tool that helps answer a smaller question: do the melodies share a whole-excerpt resemblance, a strong local fragment resemblance, or both?

The report is organized as follows. Section 2 presents the legal and computational background, including the role of substantial similarity, the importance and limits of melody, and prior work on melodic similarity algorithms. Section 3 explains the dataset, MIDI preparation, melody representation, alignment methods, PMI scores, hybrid score, and legal rule layer. Section 4 presents and discusses the results on the 15 curated MIDI pairs. It also explains why the labels and thresholds must be interpreted cautiously. Section 5 concludes by summarizing what the project achieved and what remains outside its scope. Section 6 provides a final reflection on the law-and-computation lessons of the project.

The main argument of the report is that local alignment is better suited than strict global comparison for fragment-based melody disputes, but only if its result is embedded in a legal reasoning structure. Computation is useful when it clarifies what it measures, exposes its assumptions, and leaves room for human legal judgment. It becomes dangerous when a score is presented as a substitute for doctrine. Our prototype is designed around this distinction.

## 2. Background

### 2.1 Music copyright and substantial similarity

Copyright infringement analysis generally requires more than showing that two works resemble each other. In simplified terms, a claimant must show copying of protected expression. Because direct evidence of copying is often unavailable, disputes frequently rely on indirect evidence such as access and similarity. In music cases, the similarity inquiry can be especially difficult because musical works are multi-dimensional. A song includes melody, rhythm, harmony, lyrics, arrangement, timbre, production, performance, and recording choices. A legal analysis must decide which aspects are relevant and whether the resemblance concerns protectable expression rather than generic musical building blocks.

The legal standard of substantial similarity is intentionally flexible. It allows courts and fact-finders to evaluate musical works in context, but that flexibility also creates uncertainty. The same musical resemblance may look important to one expert and trivial to another. Some cases involve clear melodic borrowing; others concern style, groove, production, or a short common pattern. The result is a field where legal decisions, settlements, and negotiated credits can be difficult to predict and difficult to explain.

Case law illustrates why the prototype must separate similarity from legal judgment. Arnstein v. Porter links copying analysis to access and substantial similarity [8]. Feist emphasizes that copyright protects original expression, not unprotectable material [9]. Music-specific decisions such as Skidmore and Gray also show that access or audible resemblance does not remove the need to examine protectability, scope, and the legally relevant work [10], [11].

This creates a natural space for computational support. A computational method can provide a consistent measure of resemblance under defined assumptions. It can show where two melodies align, where they diverge, and whether a claimed fragment is exceptional or weak. However, a computational method also risks giving false precision. If the method hides its assumptions or ignores legal context, it may make a score appear more legally decisive than it is.

### 2.2 Why focus on melody?

The project focuses on melody for both practical and legal reasons. Practically, melody can be represented as a sequence of pitches or intervals. This allows the use of dynamic programming methods originally developed for sequence comparison. Legally, melody has historically been one of the central elements in music copyright disputes. It is often easier to isolate and discuss than timbre or production style, and it is closer to the traditional notion of musical composition.

This focus is also a limitation. Many contemporary disputes are not melody-only disputes. They may involve sampling, sound recordings, production aesthetics, chord progressions, rhythmic grooves, or the general "vibe" of a song. A melody-only tool should not be used to decide those cases. For that reason, our legal rule layer includes a variable called melody_scope. If the dispute is not meaningfully about melody, the prototype should say that the case falls outside its intended scope.

### 2.3 Prior computational approaches

Several computational approaches have been proposed to compare melodies in copyright or plagiarism contexts. Mongeau and Sankoff adapted sequence comparison methods to musical sequences, treating melodies as ordered objects that can be aligned and transformed [1]. Mullensiefen and Pendzich studied court decisions on music plagiarism and compared predictive performance across similarity algorithms, emphasizing that actual legal decisions depend on more than a fixed number of corresponding notes [2]. Savage, Cronin, Mullensiefen, and Atkinson applied Percent Melodic Identity (PMI) to music copyright cases and argued that transparent quantitative methods can supplement traditional musicological analysis [3].

These works support the premise that melodic similarity can be measured in a structured way. They also support the caution that similarity metrics should not be treated as complete legal tests. The strongest computational contribution is not simply to output a number, but to make the comparison inspectable. This is particularly important in legal settings, where parties must be able to challenge evidence, understand assumptions, and explain why a result matters.

### 2.4 Global and local alignment

Our computational methods draw on dynamic programming alignment. Needleman-Wunsch alignment was developed for global sequence alignment [4]. It aligns two complete sequences and is useful when the question is whether the sequences resemble each other overall. Smith-Waterman alignment was developed for local sequence alignment [5]. It identifies a high-scoring matching subsequence and is useful when the important similarity is embedded within longer unrelated material.

This distinction maps naturally onto music copyright reasoning. A whole-excerpt comparison asks whether the two melodies resemble each other overall. A local comparison asks whether there is a strong shared fragment. In legal disputes, both questions can matter. Whole-work resemblance may support a claim of broad copying, but a short, recognizable, and protectable fragment can also be important. A global score can miss such cases because unrelated surrounding material lowers the overall percentage. A local score can reveal the fragment, but it can also be over-inclusive if it treats any short match as legally important. This is why our prototype includes a hybrid score and a legal interpretation layer.

### 2.5 Research gap

The research gap is therefore not only computational. Better algorithms are useful, but they do not solve the legal problem by themselves. What is needed is a narrow techno-legal structure that connects a transparent similarity measure to legal interpretation. The prototype addresses this gap by combining four elements:

1. a curated corpus of music copyright disputes;
2. an interval-based representation of melody;
3. global, local, and hybrid PMI scores;
4. a minimal legal rule layer that prevents raw scores from being read as legal judgments.

The project is exploratory. It does not claim statistical validation, and it does not claim that its thresholds generalize beyond the current dataset. Its value lies in showing how a law-and-computation prototype can be built responsibly: define the scope, implement a transparent method, report results, and explicitly state what remains for human legal evaluation.

## 3. Methodologies and Approach

### 3.1 Corpus construction

The master corpus contains 128 music copyright disputes stored in `data/master_case.csv`. Each row includes a case identifier, plaintiff song, defendant song, year, jurisdiction, binary label, notes, and source information. The binary label was confirmed by the team as a broad outcome label:

- `1` means a claimant-favourable outcome, including a settlement, songwriting credit, royalties, a court finding, or another form of recognition.
- `0` means a non-claimant-favourable outcome, such as dismissal, defendant-favourable ruling, withdrawal, no settlement, or no clear claimant success.

This label is not a pure court judgment label. Many cases in the corpus are settlements or negotiated credits rather than final judicial decisions. This matters for evaluation. If a model appears to match the labels, it is not necessarily predicting court decisions. It is comparing similarity scores to a broad dispute outcome variable.

The computational evaluation uses a subset of 15 cases. These were selected because they were the cases for which the team had two usable MIDI files. This is a practical availability criterion rather than a statistically balanced sampling method. The subset therefore cannot support broad claims about accuracy across music copyright disputes. It can, however, support an exploratory comparison of global, local, and hybrid similarity behavior on well-known melody-dispute pairs.

### 3.2 MIDI acquisition and preparation

The MIDI files were collected from public MIDI sources, mainly mididb.com and bitmidi.com. After collection, the files were edited using signalmidi.app to remove irrelevant layers and keep the relevant melody. This step is important because many MIDI files contain multiple tracks or accompaniment layers. The prototype compares melody, not full audio production or polyphonic arrangement. The input to the similarity pipeline is therefore a curated monophonic melody excerpt for each song.

This manual preparation improves the relevance of the comparison, but it also introduces a limitation. The result depends on which melodic line is selected and how the excerpt is cleaned. A future version should document excerpt boundaries, track selection rules, and any manual edits case by case. For the present project, the report treats the MIDI preparation as a necessary curation step for an exploratory prototype.

### 3.3 Melody representation

Each melody is represented as an interval sequence. Given a pitch sequence:

`P = [p1, p2, ..., pn]`

the interval sequence is:

`I = [p2 - p1, p3 - p2, ..., pn - p(n-1)]`

For example, if the pitch sequence is `[60, 62, 65, 64]`, the interval sequence is `[+2, +3, -1]`.

The interval representation has three advantages. First, it is transposition-invariant: the same melodic contour in a different key produces the same intervals. Second, it focuses on melodic movement rather than absolute pitch. Third, it is simple enough to explain to a legal audience. This makes it appropriate for a decision-support prototype where interpretability is part of the objective.

The representation also has limitations. It does not directly encode rhythm, note duration, harmony, timbre, lyrics, production, or performance. It also reduces melodic identity to contour, which may miss aspects of perception that matter musically. These omissions are acceptable only because the prototype is explicitly scoped to melody-focused disputes.

### 3.4 Global PMI

The baseline method computes a global PMI score. The implemented global alignment follows a Needleman-Wunsch-style dynamic programming structure over interval sequences. It aligns the two full sequences and counts exact interval matches. The score is calculated as:

`Global PMI = exact interval matches / aligned length`

reported as a percentage.

The global score answers a conservative question: how similar are the two melodies as whole excerpts? This is useful because it resists overreacting to a short match. If two songs share only a brief fragment but differ elsewhere, the global score remains low. That makes global PMI a useful baseline. However, this same property can be a weakness in fragment-based disputes, where the legally relevant material may be a short but recognizable passage.

### 3.5 Local PMI

The local method is designed to identify stronger fragment resemblance. The team described the final local approach as finding the best matching fragment and ignoring unrelated surrounding material. In implementation terms, this corresponds to a Smith-Waterman-style local alignment with tolerant matching. Exact interval matches receive stronger support, near matches within a small interval difference are tolerated, and mismatches or gaps reduce the local alignment score.

The local PMI score is then computed over the locally aligned fragment. A tolerant match counts when the aligned intervals are equal or close enough under the selected tolerance. In the implemented version, the tolerance used by the local PMI function is one semitone of interval difference:

`abs(a - b) <= 1`

This is intended to capture small melodic variation, ornamentation, or near-copying that a strict exact-match score would miss.

The legal rationale is that music copyright disputes often concern recognizable fragments, not only full-melody duplication. A defendant may reuse or adapt a hook while changing surrounding material. A local alignment is better suited to reveal that kind of resemblance. The risk is that local scores may be over-inclusive, because short patterns can recur by chance or because common melodic gestures may be weakly protectable. The legal layer is therefore necessary to interpret local scores responsibly.

### 3.6 Hybrid PMI

The hybrid score combines global and local evidence:

`Hybrid PMI = 0.5 * Global PMI + 0.5 * Local PMI`

The rationale is to balance two intuitions. Global PMI is conservative and captures whole-excerpt resemblance. Local PMI is sensitive and captures fragment resemblance. The hybrid score avoids relying entirely on a single local fragment, while still allowing a strong fragment to raise concern when the global score is low.

The current weighting is exploratory. The 0.5/0.5 combination is transparent and easy to explain, but it is not statistically calibrated. A future version could tune the weight on a larger balanced dataset and report uncertainty.

### 3.7 Legal variables and rule layer

The project proposes a minimal legal rule layer with four variables:

- `access`: whether there is evidence or plausible support that the defendant had access to the plaintiff's work;
- `melody_scope`: whether the dispute is meaningfully about melody rather than lyrics, sampling, timbre, groove, production, or overall style;
- `protectable_material`: whether the similar material appears to concern distinctive protectable expression rather than generic or trivial material;
- `context_override`: whether the legal or procedural context makes the computational score unreliable in isolation.

The rule layer is not a liability test. It is an interpretation framework. Its purpose is to prevent a raw score from being treated as a legal conclusion. For example, if melody_scope is no, the prototype should output that the case is outside its intended melodic scope. If access is absent, even a high similarity score should be treated with caution. If the score is high but the shared material is generic, the output should flag similarity in weakly protectable material rather than prima facie concern. If context_override is yes, the output should require manual legal review.

In the project dataset, the legal variables are documented but not fully populated in the master CSV. This is an important limitation. The legal layer should therefore be described as an exploratory coding and rule-trace framework rather than a completed annotated legal dataset. For the final system, the next step would be to validate legal annotations and rule traces on the 15 MIDI cases before expanding to the full 128-case corpus.

## 4. Results and Discussion

### 4.1 Dataset summary

The master corpus contains 128 cases. The labels are distributed as follows:

| Label | Meaning | Count |
|---|---|---:|
| 1 | Claimant-favourable outcome, broadly defined | 93 |
| 0 | Non-claimant-favourable or no clear claimant success | 35 |

The MIDI evaluation subset contains 15 cases. This subset is strongly imbalanced: 13 cases have label `1` and 2 cases have label `0`. This imbalance reinforces the exploratory nature of the evaluation. The subset is useful for comparing how scoring methods behave on known disputes, but it is not sufficient for robust classification accuracy.

### 4.2 Score results

The following table reports the computed scores for the 15 curated MIDI pairs. Global PMI measures whole-excerpt resemblance. Local PMI measures best-fragment resemblance. Hybrid PMI averages the two.

\begin{center}
{\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\begin{tabular}{@{}r p{0.43\linewidth} r r r r@{}}
\hline
\textbf{ID} & \textbf{Melody pair} & \textbf{Global} & \textbf{Local} & \textbf{Hybrid} & \textbf{Label}\\
\hline
120 & The Last Time / Bitter Sweet Symphony & 26.95 & 77.54 & 52.24 & 1\\
125 & Anybody Seen My Baby / Constant Craving & 5.01 & 93.08 & 49.04 & 1\\
127 & All You Need Is Love / In the Mood & 12.85 & 95.05 & 53.95 & 1\\
13 & Oops Up Side Your Head / Uptown Funk & 6.58 & 62.90 & 34.74 & 1\\
28 & Greatest Love of All / If You Could Read My Mind & 21.10 & 93.23 & 57.16 & 0\\
29 & Sweet Little Sixteen / Surfin' U.S.A. & 18.62 & 93.70 & 56.16 & 1\\
32 & I Won't Back Down / Stay With Me & 7.76 & 88.89 & 48.32 & 1\\
39 & No Scrubs / Shape of You & 8.39 & 92.12 & 50.25 & 1\\
4 & I'm Not Alone / Yeah 3x & 3.61 & 0.00 & 1.81 & 1\\
40 & Teach the World to Sing / Shakermaker & 12.90 & 89.46 & 51.18 & 1\\
80 & Under Pressure / Ice Ice Baby & 2.78 & 33.33 & 18.06 & 1\\
81 & Every Breath You Take / I'll Be Missing You & 23.01 & 93.35 & 58.18 & 1\\
87 & All Day and All of the Night / Hello, I Love You & 12.74 & 93.94 & 53.34 & 1\\
92 & I Want a New Drug / Ghostbusters & 9.91 & 85.00 & 47.45 & 1\\
96 & When I Was Your Man / Flowers & 36.10 & 89.43 & 62.77 & 0\\
\hline
\end{tabular}
}
\end{center}

The average scores are:

| Score | Minimum | Maximum | Mean |
|---|---:|---:|---:|
| Global PMI | 2.78 | 36.10 | 13.89 |
| Local PMI | 0.00 | 95.05 | 78.73 |
| Hybrid PMI | 1.81 | 62.77 | 46.31 |

\newpage

Under the exploratory thresholds used for the poster-stage analysis:

| Threshold | Flagged cases |
|---|---:|
| Global PMI > 20% | 4 / 15 |
| Local PMI > 80% | 11 / 15 |
| Hybrid PMI > 50% | 9 / 15 |

The main empirical finding is therefore:

Local PMI flags more of the 15 curated melody-dispute pairs under the exploratory threshold than global PMI.

This formulation is intentionally cautious. The dataset is small and imbalanced, the thresholds are exploratory, and the labels are broad dispute outcomes rather than pure court decisions. The result should not be presented as statistical validation. It should be read as evidence that local alignment is more sensitive to fragment-based resemblance than global alignment in this curated subset.

### 4.3 Interpretation of global PMI

Global PMI is conservative. It captures whether two entire melody excerpts resemble each other across their full aligned length. This makes it useful as a baseline because it reduces the risk of overvaluing a short fragment. In the results, however, global PMI flags only 4 of 15 pairs above 20%. Several well-known disputes with claimant-favourable outcomes have low global scores. Examples include:

- Anybody Seen My Baby / Constant Craving: global 5.01, local 93.08;
- I Won't Back Down / Stay With Me: global 7.76, local 88.89;
- No Scrubs / Shape of You: global 8.39, local 92.12;
- I Want a New Drug / Ghostbusters: global 9.91, local 85.00.

These examples illustrate why whole-excerpt comparison can be too rigid for fragment-based disputes. If the legally relevant similarity is a hook, motif, or short passage, then unrelated surrounding material will lower the global score even though the disputed fragment remains recognizable.

This does not mean global PMI is useless. On the contrary, it provides an important conservative reference point. It helps identify cases where resemblance is broad rather than local. It also helps restrain local overreach. A high local score combined with a very low global score should invite careful legal interpretation: is the shared fragment protectable, central, and plausibly copied, or is it a common musical gesture?

### 4.4 Interpretation of local PMI

Local PMI is much more sensitive in the current subset. It flags 11 of 15 cases above 80%. This is consistent with the project's legal intuition: many melody disputes are not about entire songs being globally similar, but about a recognizable fragment appearing in both works.

The local method performs especially well as an explanatory tool. It can show why a low global score does not necessarily make a dispute irrelevant. For example, No Scrubs / Shape of You has a low global score but a high local score. The legal point is not that the songs are globally identical, but that the disputed material may involve a recognizable local melodic relationship. Similarly, I Won't Back Down / Stay With Me has low global resemblance but high local resemblance, matching the public understanding that the case centered on a specific musical resemblance rather than whole-song copying.

The weakness of local PMI is over-inclusion. Greatest Love of All / If You Could Read My Mind has label 0 but local 93.23 and hybrid 57.16. When I Was Your Man / Flowers also has label 0 but high local and hybrid scores. These are not simply errors in the computational sense. They show the legal gap. A high local score may identify musical resemblance, but the dispute outcome can still depend on settlement posture, protectability, access, procedural choices, or whether the claim was actually pursued. In other words, local PMI may be good at detecting resemblance but not sufficient for predicting legal outcomes.

The I'm Not Alone / Yeah 3x case points in the opposite direction. It has label 1 but local 0.00 and hybrid 1.81 in the current results. This suggests either that the selected MIDI excerpts do not capture the disputed material, that the algorithm is sensitive to preprocessing choices, or that the case involved musical/legal factors not represented by the interval sequence. This is an important diagnostic case. It shows why data curation and case-specific review are necessary before treating scores as evidence.

### 4.5 Interpretation of hybrid PMI

Hybrid PMI averages global and local PMI. It flags 9 of 15 cases above 50%. This makes it less sensitive than local PMI but more sensitive than global PMI. That balance is useful for decision support. It allows a strong local match to influence the score, while still accounting for whole-excerpt dissimilarity.

The hybrid score is most persuasive when both global and local evidence point in the same direction. For example, Every Breath You Take / I'll Be Missing You has global 23.01, local 93.35, and hybrid 58.18. The result suggests that there is both some whole-excerpt resemblance and a very strong local fragment resemblance. The hybrid score is also useful when local PMI is high but global PMI is low, because it produces a moderate score rather than allowing the local score alone to dominate the interpretation.

However, the 0.5/0.5 weighting is not calibrated. It is a design choice made for transparency. A more developed model would learn or justify the weighting using a larger and more balanced dataset. It might also report separate global and local scores rather than collapsing them, because legal interpretation often needs to know whether similarity is broad or fragment-specific.

### 4.6 Legal interpretation

The legal lesson of the results is that similarity scores should be read as evidence, not decisions. The computational layer can answer questions such as:

- Are the full melody excerpts similar under global alignment?
- Is there a strong locally matching fragment?
- Does the hybrid score suggest both broad and fragment evidence?
- Which cases require closer legal review?

It cannot answer by itself:

- Did the defendant actually copy?
- Was there access?
- Is the shared material protectable?
- Is the dispute mainly about melody?
- Does the procedural posture explain the outcome?

This is why the legal variables are central to the prototype. A case with high local PMI but no access should not be treated the same as a case with high local PMI and clear access. A case involving sampling, production, or lyrics should not be treated as a melody case simply because a melody score is available. A case involving generic musical material should be treated cautiously even if the score is high.

The legal rule layer therefore translates score-based evidence into structured review categories. Its strongest role is negative and interpretive: it prevents misuse. It says when the tool should stop, when the score is weak, when the score may concern non-protectable material, and when manual legal review is required. That is a valuable contribution for law and computation because it connects formalization to institutional responsibility.

### 4.7 Limitations

The project has several important limitations.

First, the dataset is small for computational evaluation. The master corpus has 128 cases, but only 15 have two usable MIDI melody files. This prevents robust statistical validation. The result should be framed as an exploratory prototype rather than a benchmark.

Second, the evaluation subset is imbalanced. Thirteen of the fifteen MIDI cases have claimant-favourable labels. This makes classification metrics such as accuracy potentially misleading. The report therefore focuses on threshold behavior and qualitative interpretation rather than claiming predictive accuracy.

Third, the labels are broad dispute outcomes, not pure judicial findings. Settlements, credits, royalties, withdrawals, and court decisions are grouped into binary labels. This is reasonable for a first corpus, but future work should separate settlement outcomes from judicial infringement findings.

Fourth, the legal variables are not fully annotated in the current master CSV. Access, melody scope, protectability, and context are documented as a framework, but they remain exploratory. Future work should validate annotations and rule traces for at least the 15 MIDI cases.

Fifth, MIDI curation affects results. The selected melody line, excerpt boundaries, and removal of other tracks can change the interval sequence. A future version should document each curation decision and preserve intermediate files.

Sixth, the model is melody-only. It does not model rhythm, duration, harmony, lyrics, timbre, sampling, arrangement, production, or listener perception. This is appropriate for the project's scope, but it means the tool should not be generalized to all music copyright disputes.

Seventh, the thresholds are exploratory. Global > 20%, local > 80%, and hybrid > 50% are useful for poster-stage comparison, but they are not legally or statistically validated thresholds. A future model should calibrate thresholds on a larger dataset and report uncertainty.

### 4.8 Why the project remains valuable

These limitations do not undermine the project. They define its proper contribution. The prototype is valuable because it demonstrates a responsible structure for computational legal support. It begins with a bounded legal problem, implements transparent methods, reports results, and explicitly separates evidence from judgment.

For a legal audience, the key value is explainability. A black-box classifier that predicts "infringement" or "no infringement" would be difficult to trust and difficult to challenge. By contrast, this prototype can say: the whole-excerpt resemblance is low, the best-fragment resemblance is high, the hybrid score is moderate, and legal factors must still be checked. That output is more consistent with legal reasoning because it supports argument rather than replacing it.

For a computational audience, the key value is the global/local distinction. A single similarity score hides important structure. Two songs can have low global resemblance but high local resemblance. In a legal dispute, that distinction may be decisive. The prototype makes that distinction visible.

For a law-and-computation course, the project illustrates a broader principle: formalization should be humble. It should not pretend that legal standards can always be converted into complete algorithms. Instead, it should identify the part of a legal problem that can be made explicit, compute it transparently, and show where legal judgment must re-enter.

## 5. Conclusion

This project built an explainable decision-support prototype for melody-focused music copyright disputes. The goal was not to automate copyright adjudication, but to make one evidence layer clearer: whether two songs share a whole-excerpt resemblance, a strong local melodic fragment, or both.

The prototype uses curated MIDI melody excerpts, converts them into interval sequences, and compares them with global, local, and hybrid PMI scores. On the 15 available MIDI pairs, global PMI flags 4 cases under the exploratory threshold, local PMI flags 11, and hybrid PMI flags 9. This supports the project's central claim: local melodic alignment is better suited than strict global comparison for detecting fragment-based resemblance in melody disputes.

At the same time, the results show why computation cannot decide the legal question alone. High local similarity can appear in cases without claimant-favourable outcomes. Some claimant-favourable cases may score low because the selected MIDI excerpts or the melody-only representation do not capture the disputed material. Labels may reflect settlements rather than judicial findings. Access, protectability, melody scope, and context remain essential.

The project's contribution is therefore best understood as a transparent evidence and interpretation layer. Global PMI provides a conservative whole-excerpt baseline. Local PMI identifies fragment resemblance. Hybrid PMI balances the two. The legal rule framework explains how these scores should be interpreted cautiously.

Future work should expand the MIDI dataset, document curation decisions, separate settlements from court decisions, validate legal annotations, calibrate thresholds, and add musical dimensions such as rhythm, harmony, and sampling where relevant. The most important future step is not simply adding complexity, but preserving explainability. In legal contexts, a useful computational system must be inspectable, contestable, and bounded.

The final takeaway is that computation can clarify one part of copyright reasoning. It can make melodic resemblance more visible and more structured. But it should remain a support for human legal judgment, not a substitute for it.

## 6. Final Reflection

The project changed our understanding of what it means to formalize law. At the beginning, it was tempting to imagine a broader pipeline that would take copyright disputes, compute similarity, apply legal rules, and output a decision-like result. That ambition was useful because it gave the project direction, but the implementation process showed why responsible formalization requires narrowing the scope.

The most important lesson is that the difficult part is not only coding. The legal meaning of the data is often harder than the algorithm. A binary label sounds simple, but in this corpus it includes settlements, credits, royalties, withdrawals, and court decisions. Treating all of these as the same kind of ground truth would be misleading. Similarly, a high similarity score sounds persuasive, but its legal meaning depends on access, protectability, scope, and context. The project therefore forced us to distinguish computational outputs from legal conclusions.

Another lesson is that explainability is not an extra feature. It is the core requirement. A legal user needs to understand what a score measures, what it ignores, and why a case has been flagged. For that reason, the global/local distinction became the strongest part of the project. It is simple enough to explain, technically meaningful, and legally relevant. Global alignment asks whether the full melodies resemble each other. Local alignment asks whether there is a strong shared fragment. That distinction maps well onto the way many music disputes are argued.

The project also showed the importance of data preparation. MIDI files are not neutral inputs. They may contain multiple tracks, arrangements, or irrelevant layers. Selecting the relevant melody is a legal and musical judgment as much as a technical step. This means the pipeline can never be fully separated from human interpretation. Rather than hiding that fact, a responsible report should document it.

Finally, the project clarified the role of law-and-computation work. The best version of the prototype is not a system that claims to decide infringement. It is a system that helps humans reason better by turning a vague similarity claim into structured evidence. It shows the score, the method, the limits, and the points where legal judgment remains necessary. That is a modest contribution, but it is a defensible and useful one.

## References

[1] M. Mongeau and D. Sankoff, "Comparison of musical sequences," Computers and the Humanities, vol. 24, no. 3, pp. 161-175, 1990.

[2] D. Mullensiefen and M. Pendzich, "Court decisions on music plagiarism and the predictive value of similarity algorithms," Musicae Scientiae, vol. 13, no. 1_suppl, pp. 257-295, 2009.

[3] P. E. Savage, C. Cronin, D. Mullensiefen, and Q. D. Atkinson, "Quantitative evaluation of music copyright infringement," in Proceedings of the 8th International Workshop on Folk Music Analysis, Thessaloniki, Greece, 2018, pp. 61-66.

[4] S. B. Needleman and C. D. Wunsch, "A general method applicable to the search for similarities in the amino acid sequence of two proteins," Journal of Molecular Biology, vol. 48, no. 3, pp. 443-453, 1970.

[5] T. F. Smith and M. S. Waterman, "Identification of common molecular subsequences," Journal of Molecular Biology, vol. 147, no. 1, pp. 195-197, 1981.

[6] R. J. S. Cason and D. Mullensiefen, "Singing from the same sheet: Computational melodic similarity measurement and copyright law," International Review of Law, Computers & Technology, vol. 26, no. 1, pp. 25-36, 2012.

[7] J. P. Fishman, "Music as a matter of law," Harvard Law Review, vol. 131, pp. 1861-1923, 2018.

[8] Arnstein v. Porter, 154 F.2d 464 (2d Cir. 1946).

[9] Feist Publications, Inc. v. Rural Telephone Service Co., 499 U.S. 340 (1991).

[10] Skidmore v. Led Zeppelin, 952 F.3d 1051 (9th Cir. 2020).

[11] Gray v. Hudson, 28 F.4th 87 (9th Cir. 2022).
