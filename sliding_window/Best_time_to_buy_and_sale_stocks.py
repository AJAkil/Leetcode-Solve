class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        p = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                p = max(p, prices[r] - prices[l])
            else:
                l = r # reset the left pointer to the right pointer if the right pointer is less than the left pointer
            
            r += 1
        
        return p