# hybrid_similarity.py

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


def local_align(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    max_score = 0
    max_pos = (0, 0)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            diff = abs(seq1[i - 1] - seq2[j - 1])
            
            if diff == 0:
                score = 2
            elif diff == 1:
                score = 1
            else:
                score = -1
            
            match = dp[i - 1][j - 1] + score
            delete = dp[i - 1][j] - 1
            insert = dp[i][j - 1] - 1
            
            dp[i][j] = max(0, match, delete, insert)
            
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_pos = (i, j)
    
    aligned1 = []
    aligned2 = []
    
    i, j = max_pos
    
    while i > 0 and j > 0 and dp[i][j] > 0:
        diff = abs(seq1[i - 1] - seq2[j - 1])
        
        if diff == 0:
            score = 2
        elif diff == 1:
            score = 1
        else:
            score = -1
        
        if dp[i][j] == dp[i - 1][j - 1] + score:
            aligned1.append(seq1[i - 1])
            aligned2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] - 1:
            aligned1.append(seq1[i - 1])
            aligned2.append(None)
            i -= 1
        else:
            aligned1.append(None)
            aligned2.append(seq2[j - 1])
            j -= 1
    
    aligned1.reverse()
    aligned2.reverse()
    
    return aligned1, aligned2

def tolerant_pmi(aligned1, aligned2):
    matches = 0
    length = len(aligned1)
    
    for a, b in zip(aligned1, aligned2):
        if a is not None and b is not None:
            if abs(a - b) <= 1:
                matches += 1
                
    return (matches / length) if length > 0 else 0

def hybrid_similarity(seq1, seq2, group_size=10, alpha=0.5):
    """
    Improved hybrid similarity:
    - global: LCS-style (your version)
    - local: tolerant local alignment (colleague-style)
    """

    # --- GLOBAL (unchanged) ---
    aligned1, aligned2 = needleman_wunsch(seq1, seq2)
    global_score = compute_pmi(aligned1, aligned2)

    # --- LOCAL (REPLACED WITH TOLERANT VERSION) ---
    local_scores = []
    n = len(seq1)

    for start in range(0, n, group_size):
        end = start + group_size

        group1 = seq1[start:end]
        group2 = seq2[start:end]

        if group1 and group2:
            # use local alignment instead of global
            aligned_l1, aligned_l2 = local_align(group1, group2)
            score = tolerant_pmi(aligned_l1, aligned_l2)  # normalize to [0,1]
            local_scores.append(score)

    local_score = sum(local_scores) / len(local_scores) if local_scores else 0

    # --- HYBRID ---
    hybrid_score = alpha * global_score + (1 - alpha) * local_score

    return hybrid_score, global_score, local_score
