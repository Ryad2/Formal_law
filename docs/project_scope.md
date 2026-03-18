# Project Scope

We are not building a full formal-verification system for music copyright disputes. Instead, we are building a small, rigorous, and explainable decision-support prototype focused on melody-based copyright disputes.

Our prototype combines four elements: a melody-similarity pipeline, threshold calibration, a minimal legal rule layer, and a transparent output in the form of a scorecard and rule trace. The goal is not to replace legal decision-making, but to structure and explain how computational similarity measures may support legal analysis in a narrow and carefully bounded setting.

The project is intentionally limited in scope. We focus on a curated corpus of melody-focused disputes, one main melodic representation, one baseline similarity method, one improved similarity method, and a small set of legally relevant variables. We do not aim to model the full complexity of copyright doctrine, nor do we attempt to build a production-level adjudication tool.

What we want to test is whether a narrow, explainable techno-legal prototype can reproduce and clarify some outcomes in melody-focused copyright disputes better than similarity scoring alone. The value of the project lies in the combination of computational scoring and explicit legal reasoning, not in raw predictive ambition.

In scope are: a curated case corpus, melody similarity computation, threshold calibration, a minimal legal rule layer, a scorecard and rule trace output, quantitative evaluation, and qualitative error analysis.

Out of scope are: full formal verification in the strong sense, large multi-feature audio pipelines, timbre/rhythm/chord modeling as core features, heavy web interfaces, large-scale benchmark expansion, and broad comparative doctrinal mapping across jurisdictions.