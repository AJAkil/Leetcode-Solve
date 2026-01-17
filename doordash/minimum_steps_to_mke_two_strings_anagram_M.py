"""
PROBLEM: Minimum Steps to Make Two Strings Anagram (LeetCode 1347 - Medium)
---------------------------------------------------------------------------
Given two strings s and t of same length, return minimum steps to make t anagram of s.
One step = replace one character in t.

Example:
Input: s = "bab", t = "aba"
Output: 1 (replace one 'a' in t with 'b')

KEY INSIGHT: Count frequency difference.
- Characters in t but not in s (or excess) need to be replaced
"""

from collections import Counter
class Solution:
    """
    APPROACH: Frequency Counting
    
    INTUITION:
    - Count char frequencies in both strings
    - For each char in t: if excess compared to s, count the difference
    - Sum all excesses = steps needed
    
    TIME: O(n)
    SPACE: O(1) - at most 26 chars
    """
    def minSteps(self, s: str, t: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(t)
        steps = 0

        for key, value in freq_t.items():
            if key in freq_s:
                steps += max(0, freq_t[key] - freq_s[key])
            else:
                print(value)
                steps += value
        
        return steps