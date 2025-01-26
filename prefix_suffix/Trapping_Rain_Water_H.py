class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = height[0]

        # calculate prefix
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        
        suffix[n - 1] = height[n - 1]

        # calculate suffix
        for i in range(len(height) - 2, -1 , -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        # for each index, calculate the water trapped by taking the min of prefix and suffix and subtracting the height of the building
        res = 0
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]
        
        return res