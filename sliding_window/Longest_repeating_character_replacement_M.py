class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            #  (r - l + 1) - max(count.values()) is the number of characters that need to be replaced
            # we replace with the most frequent character in the window
            # the relation between the number of characters that need to be replaced and k is given by:
            # (r - l + 1) - max(count.values()) <= k -> invariant

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 # remove the leftmost character from the window
                l += 1 # move the left pointer to the right by 1


            res = max(res, r - l + 1) # update the result
        
        return res
