from collections import Counter
class Solution:
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