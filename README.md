## Formalizing the Law

### Project Overview
This project is focused on building an explainable, decision-support prototype for melody-focused music copyright disputes. The goal is not full formal verification, but a rigorous, transparent system combining melody similarity analysis with a minimal legal rule layer, threshold calibration, and clear outputs (scorecard + rule trace).

### Objectives
- Develop a prototype that integrates melody similarity metrics and legal rules to support decision-making in copyright cases.
- Calibrate thresholds for similarity and legal concern.
- Provide transparent, explainable outputs for each case.
- Evaluate the system quantitatively and qualitatively.

### Research Question
Can an explainable prototype combining melody similarity and minimal legal rules reproduce and explain outcomes in melody-focused music copyright disputes better than similarity scoring alone?

### Scope
**In scope:**
- Curated case corpus
- Melody representation and extraction
- Baseline and improved similarity methods
- Threshold calibration
- Minimal legal rule layer
- Scorecard and rule trace outputs
- Quantitative evaluation and qualitative error analysis
- Poster and final report

**Out of scope:**
- Full formal verification
- Large feature families or full audio pipeline
- Heavy web app or broad legal survey
- Rhythm/timbre/chords as core features

### Methodology
1. **Corpus Construction:** Each case includes plaintiff/defendant melody excerpts, final label, and four legal variables:
	- access (yes/no/unclear)
	- melody_scope (yes/no)
	- protectable_material (yes/no/unclear)
	- context_override (yes/no)
2. **Similarity Pipeline:**
	- Baseline: global melody similarity
	- Improvement: local melody similarity
3. **Decision Logic:**
	- Minimal legal rule layer applied to similarity scores and legal variables
	- Transparent output: scorecard and rule trace
4. **Evaluation:**
	- Quantitative metrics and qualitative error analysis

### Project Structure
- `data/master_case.csv`: Main case corpus
- `songs/`: Melody excerpts
- `src/`: Code for data loading, similarity computation, and decision logic
- `results/`: Output tables and figures
- `docs/`: Project scope, research question, legal variables, dataset card, evaluation plan, contribution and AI-use statements
- `poster/` and `report/`: Presentation and final report materials

### Usage
1. Clone the repository and ensure all required files are present.
2. Run the data loader and similarity scripts in `src/` to process the corpus and generate results.
3. Review outputs in `results/` and figures in `figures/`.
4. Refer to the scorecard and rule trace for case-by-case explanations.

### Contact
For questions, please contact the project contributors or refer to the documentation in `docs/`.
