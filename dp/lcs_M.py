def lcs(dasher_1, dasher_2):
    m, n = len(dasher_1), len(dasher_2)

    # need to find the longest common subssequence between the dasheers,
    # since skipping is allowed 

    # why dp? cause the substring calculated so far, can be reused to find substring for the next larger subsequence
    # also subproblems essentially overlaps, where a subseq upto a certain (i,j) can be part of ther subsequnces, so we can just reuse that


    dp = [[0] *(n+1) for _ in range(n+1)]

    end_pos = 0 # only needed if we are doing substring
    maximum = 0

    for i in range(1, m+1):
        for j in range(1, n + 1):
            if dasher_1[i-1] == dasher_2[j-1]:
                # if the res are the same, both dashers can pick from it
                dp[i][j] = dp[i-1][j-1] + 1 # since i,j stores the max length of the common subseq upto that point

            else:
                # no match, we can skip
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # choose the max to propagate if no match occurs, essentially skipping for one of the dashers list
            
            # if dp[i][j] > maximum: - for lcs
            #     maximum = dp[i][j]
            #     end_pos = i 

    # # Extract the actual substring
    # start_pos = end_pos - max_length
    # result = dasher1[start_pos:end_pos]

    result = []
    i,j = m,n # the last entry has the length, so we start from there

    while i > 0 and j > 0:
        if dasher_1[i-1] == dasher_2[j-1]:
            result.append(dasher_1[i-1]) # add any one
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            # dasher 1 is contributing more to the lcs, so we backtrack on that path
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], result[::-1]


def longest_common_substring_all(dasher1, dasher2):
    """
    Find ALL longest common substrings (if there are ties).
    
    Returns list of all substrings with maximum length.
    """
    m, n = len(dasher1), len(dasher2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    end_positions = []  # Store all positions where max length occurs
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dasher1[i-1] == dasher2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_positions = [i]  # New max, reset list
                elif dp[i][j] == max_length:
                    end_positions.append(i)  # Another substring with same length
    
    # Extract all substrings
    results = []
    for end_pos in end_positions:
        start_pos = end_pos - max_length
        results.append(dasher1[start_pos:end_pos])
    
    return max_length, results