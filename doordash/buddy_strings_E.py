"""
PROBLEM: Buddy Strings (LeetCode 859 - Easy)
---------------------------------------------
Given two strings s and goal, return true if you can swap two letters in s
so it equals goal.

Example:
Input: s = "ab", goal = "ba"
Output: true

KEY INSIGHT: Check character frequencies and position differences.
- Must have same character frequencies (anagram)
- Either exactly 2 positions differ (and swappable)
- Or 0 positions differ AND has duplicate char (swap duplicates)
"""

from collections import Counter
class Solution:
    """
    APPROACH: Frequency Count + Position Diff Count
    
    INTUITION:
    - If lengths differ -> false
    - If char frequencies differ -> false
    - Count position differences:
      * diff == 2: can swap to match
      * diff == 0: need duplicate char to swap with itself
      * otherwise: false
    
    TIME: O(n)
    SPACE: O(1)
    """
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        s_char_freq = Counter(s)
        goal_char_freq = Counter(goal)

        if s_char_freq != goal_char_freq:
            return False
        
        # count the difference of characters between them
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        
        # now if the difference is 2 we can do an easy swap
        if diff == 2:
            return True
        
        # now if the difference is 0, so they are identical but there is atleast one char that has a freq > 1 - we can swap that and it would be true
        if diff == 0 and any(count > 1 for count in s_char_freq.values()):
            return True
        
        return False
        
        
