"""
PROBLEM: Koko Eating Bananas (LeetCode 875 - Medium)
-----------------------------------------------------
Koko eats bananas at speed k bananas/hour. Given piles and h hours,
find minimum k such that Koko can finish all piles within h hours.
(If pile has < k bananas, she finishes in 1 hour and doesn't eat more)

Example:
Input: piles = [3,6,7,11], h = 8
Output: 4

KEY INSIGHT: Binary search on eating speed.
- Range: [1, max(piles)]
- For each speed k, calculate hours needed
- Find minimum k where hours <= h
"""

class Solution:
    """
    APPROACH: Binary Search on Answer
    
    INTUITION:
    - Search space: k from 1 to max(piles)
    - For each k, calculate time: sum(ceil(pile/k))
    - If time <= h, try smaller k (search left)
    - If time > h, need larger k (search right)
    
    TIME: O(n log m) where m = max(piles)
    SPACE: O(1)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        res = k
        while l <= r:
            k = (l + r)//2
            total = 0

            for pile in piles:
                total += math.ceil(float(pile)/k)

            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res