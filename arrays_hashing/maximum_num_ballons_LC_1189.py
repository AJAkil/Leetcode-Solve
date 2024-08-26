class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)

        for c in text:
            freq[c] = 1 + freq.get(c, 0)

        temp = min(freq['l']//2, freq['o']//2)

        if (freq['b'] >= temp and
        freq['a'] >= temp and
        freq['n'] >= temp):
            return temp
        else:
            min_ = min(freq['a'], freq['b'], freq['n'])

            return min_

        