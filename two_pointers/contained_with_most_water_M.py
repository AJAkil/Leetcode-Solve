class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = -1 * float('inf')

        while l < r:
            temp_l = l
            temp_r = r
            if height[l] < height[r]:
                bottle = height[l]
                l += 1
            elif height[l] > height[r]:
                bottle = height[r]
                r -= 1
            else:
                bottle = height[l]
                l += 1
                r -= 1
            
            area = max(area, bottle * (temp_r - temp_l))
        
        return area




        