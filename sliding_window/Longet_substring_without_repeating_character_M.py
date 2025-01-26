class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        l, r = 0, 0
        res = 0
        m = {}

        while r < len(s):
            if s[r] in m: # if the character is already in the window then update the left pointer
                l = max(m[s[r]] + 1, l) # update the left pointer to start from the next of the duplicate
                
            m[s[r]] = r # store the right pointer index
            res = max(res, r - l + 1)
            
            r += 1

        return res
