class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        w = 0
        s = 0

        while r < len(nums):
            if nums[r] >= target: return 1
            
            s += nums[r]

            while s - nums[l] >= target: # if the running sum - the left pointer is greater than or equal to the target
                s -= nums[l] # remove the left pointer from the window
                l += 1 # move the left pointer to the right by 1
            
            if s >= target:
                w = r - l + 1
            
            # print(s)
            # print(w)
            # print('l ', l)
            # print('r ', r)
 
            if w > 0: 
                s -= nums[l]
                l += 1
            
            r += 1
        
        return w

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        w = float('inf')
        s = 0

        while r < len(nums):
            if nums[r] >= target: return 1
            
            s += nums[r]

            while s >= target:
                w = min(w, r - l + 1)
                s -= nums[l]
                l += 1
            
            r += 1
        
        return 0 if w == float('inf') else w

        