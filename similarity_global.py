# baseline_pmi.py

def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=0, gap_penalty=-1):
    n = len(seq1)
    m = len(seq2)

    # Initialize score matrix
    score = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize borders
    for i in range(n + 1):
        score[i][0] = i * gap_penalty
    for j in range(m + 1):
        score[0][j] = j * gap_penalty

    # Fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                s = match_score
            else:
                s = mismatch_score

            diag = score[i - 1][j - 1] + s
            up = score[i - 1][j] + gap_penalty
            left = score[i][j - 1] + gap_penalty

            score[i][j] = max(diag, up, left)

    # Traceback
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
            aligned2.append('-')
            i -= 1
        else:
            aligned1.append('-')
            aligned2.append(seq2[j - 1])
            j -= 1

    return aligned1[::-1], aligned2[::-1]


def compute_pmi(aligned1, aligned2):
    matches = 0
    total = len(aligned1)

    for a, b in zip(aligned1, aligned2):
        if a == b:
            matches += 1

    if total == 0:
        return 0

    return matches / total


def melody_similarity(seq1, seq2):
    aligned1, aligned2 = needleman_wunsch(seq1, seq2)
    similarity = compute_pmi(aligned1, aligned2)
    return similarity, aligned1, aligned2


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    # Example melodies (can be MIDI pitches or note names)
    melody1 = ["C", "D", "E", "F", "G"]
    melody2 = ["C", "E", "F", "A"]

    sim, aligned1, aligned2 = melody_similarity(melody1, melody2)

    print("Aligned Melody 1:", aligned1)
    print("Aligned Melody 2:", aligned2)
    print("PMI Similarity:", round(sim, 3))