from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = defaultdict(int)
        max_window = 0

        for r, elem in enumerate(s):
            freq[elem] += 1

            # the invalid condition to move the left pointer
            while len(freq) > k: # cause we need <=k
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    freq.pop(s[l]) # we remove it from the entire dict

                l += 1
            
            # since we want max/largest
            max_window = max(max_window, r - l + 1)
        
        return max_window


        