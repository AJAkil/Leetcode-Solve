from collections import Counter
class Solution:
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
        
        
