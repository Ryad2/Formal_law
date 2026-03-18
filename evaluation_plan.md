# Evaluation Plan: Melody Similarity

## 1. Baseline Similarity Method

The baseline method follows the **Pitch Matching Index (PMI)** approach.

### Procedure:
1. Represent melodies as sequences of pitches.
2. Apply global alignment using the Needleman–Wunsch algorithm.
3. Compare aligned sequences and count matching notes.
4. Compute similarity:

PMI = (number of matching notes) / (average length of sequences)

### Goal:
Provide a simple global measure of similarity for comparison.

---

## 2. Improved Similarity Method

The improved method introduces a **hybrid similarity score** that combines global and local similarity.

### Procedure:
1. Perform global alignment (same as baseline).
2. Convert aligned sequences into a binary match sequence:
   - 1 = match
   - 0 = mismatch or gap

3. Compute:
   - Global similarity:
     S_global = mean of the match sequence

   - Local similarity:
     - Apply a sliding window (size 10–20)
     - Compute similarity within each window
     - Select the top 20% highest-scoring windows
     - Compute their average:
       S_local = average of top windows

4. Combine:
   S = 0.5 × S_global + 0.5 × S_local

### Goal:
Capture both overall similarity and strong local similarities within melodies.

---

## 3. Evaluation Metrics

The methods will be evaluated using the following criteria:

### 3.1 Score Comparison
Compare similarity scores produced by the baseline and improved methods on the same melody pairs.

### 3.2 Ranking Consistency
Given multiple candidate melodies, compare how each method ranks similarity.

### 3.3 Sensitivity to Local Similarity
Evaluate cases where:
- melodies share short but strong similar segments
- global similarity is low but local similarity is high

The improved method is expected to better capture such cases.

### 3.4 (Optional) Classification Accuracy
If labeled data is available, evaluate how well each method distinguishes similar vs non-similar melody pairs.

---

## 4. Working Baseline (Deadline: 18 Mar)

The baseline is considered complete if:

- Needleman–Wunsch alignment is implemented
- The system can input two melodies and output aligned sequences
- PMI similarity score is correctly computed
- Results are reasonable (e.g., identical melodies produce high similarity)

---

## 5. Working Improved Method (Deadline: 1 Apr)

The improved method is considered complete if:

- Baseline system is fully functional
- Sliding window computation is implemented
- Local similarity (top 20% windows) is computed correctly
- Hybrid similarity score is produced
- The method shows improved sensitivity to local similarity compared to the baseline