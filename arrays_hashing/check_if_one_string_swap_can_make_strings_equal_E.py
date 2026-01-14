"""
Check If One String Swap Can Make Strings Equal (LeetCode 1790)

PROBLEM:
Given two strings s1 and s2 of equal length, return true if you can swap at most one pair 
of characters in one of the strings so that both strings become equal.

SOLUTION APPROACH:

STEP 1: Quick check - if strings are already equal, return True (no swap needed)

STEP 2: Verify anagrams - check if both strings have the same character frequencies
  - If frequencies differ, it's impossible to make them equal with a swap
  - Intuition: A swap only changes positions, not the set of characters. If they don't 
    have the same characters, no swap can help.

STEP 3: Count position differences - find how many positions differ between s1 and s2
  - If more than 2 positions differ: impossible (a single swap fixes exactly 2 positions)
  - If exactly 2 positions differ: possible IF swapping those positions in one string 
    makes them equal
  - If 0 positions differ: already equal (handled in step 1)
  - Intuition: A single character swap affects exactly 2 positions

STEP 4: Verify the swap works - if 2 positions differ at indices i and j, check if 
  swapping s1[i] with s1[j] makes s1 equal to s2
  - This is guaranteed if s1[i] == s2[j] and s1[j] == s2[i]

TIME: O(n)  SPACE: O(1) - only using character frequency counters
"""

from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        freq_s1 = Counter(s1)
        freq_s2 = Counter(s2)

        # if they are anagram and differ by exactly two posuitions, we can make a single swap
        # else we cant
        diff = False

        for k, v in freq_s1.items():
            if k in freq_s2:
                if freq_s1[k] != freq_s2[k]:
                    diff = True
                    break
                else:
                    diff = False
            else:
                return False
        
        if diff:
            return False

        # next we count the position difference as diff is False - so they are anagrams
        pos = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                pos += 1
            
            if pos > 2:
                return False
        
        if pos == 2:
            return True
        

# ============================================================================
# CLEANER SOLUTION (More Elegant Approach)
# ============================================================================
"""
SIMPLER INTUITION:
Instead of checking frequencies first, just collect all differences. A valid swap must satisfy:
1. Exactly 0 or 2 positions differ
2. If 2 positions differ at indices i and j, then s1[i]==s2[j] and s1[j]==s2[i]

This naturally handles the anagram constraint because if frequencies differ, we'll have 
either odd number of differences or the swap condition will fail.
"""

class SolutionClean:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Collect all positions where strings differ
        differences = [i for i in range(len(s1)) if s1[i] != s2[i]]
        
        # Valid if no differences (already equal)
        if len(differences) == 0:
            return True
        
        # Valid if exactly 2 differences that can be swapped to match
        if len(differences) == 2:
            i, j = differences[0], differences[1]
            # Check if swapping s1[i] and s1[j] would make them equal to s2
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # Any other case (1 difference or more than 2) is impossible
        return False
        

        

        


        
        