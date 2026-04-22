# --- GLOBAL ALIGNMENT (MODIFIED SCORING ONLY) ---
def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=0, gap_penalty=0):
    n = len(seq1)
    m = len(seq2)

    # Initialize score matrix
    score = [[0] * (m + 1) for _ in range(n + 1)]

    # No gap penalty → borders stay 0 (important change)
    # (previous version had initialization with gap penalties)

    # Fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                s = match_score
            else:
                s = mismatch_score  # now 0

            diag = score[i - 1][j - 1] + s
            up = score[i - 1][j] + gap_penalty   # now 0
            left = score[i][j - 1] + gap_penalty # now 0

            score[i][j] = max(diag, up, left)

    # Traceback (unchanged)
    aligned1 = []
    aligned2 = []
    i, j = n, m

    while i > 0 or j > 0:
        current = score[i][j]

        if i > 0 and j > 0:
            if seq1[i - 1] == seq2[j - 1]:
                s = match_score
            else:
                s = mismatch_score

            if current == score[i - 1][j - 1] + s:
                aligned1.append(seq1[i - 1])
                aligned2.append(seq2[j - 1])
                i -= 1
                j -= 1
                continue

        if i > 0 and current == score[i - 1][j] + gap_penalty:
            aligned1.append(seq1[i - 1])
            aligned2.append(None)
            i -= 1
        else:
            aligned1.append(None)
            aligned2.append(seq2[j - 1])
            j -= 1

    return aligned1[::-1], aligned2[::-1]


# --- PMI (MODIFIED DENOMINATOR) ---
def compute_pmi(aligned1, aligned2):
    matches = 0

    for a, b in zip(aligned1, aligned2):
        if a is not None and b is not None and a == b:
            matches += 1

    # IMPORTANT CHANGE: use average length (like your colleague)
    length = (len(aligned1) + len(aligned2)) / 2

    return matches / length if length > 0 else 0





def melody_similarity(seq1, seq2):
    aligned1, aligned2 = needleman_wunsch(seq1, seq2)
    similarity = compute_pmi(aligned1, aligned2)
    return similarity, aligned1, aligned2



# -------------------------
# Example usage
# -------------------------
