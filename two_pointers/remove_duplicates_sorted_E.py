class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)

        while r < n :

            
            while r < n and nums[l] == nums[r]:
                r += 1
            
            l += 1
            
            if r < n:
                nums[l] = nums[r]

        
        return l
        

