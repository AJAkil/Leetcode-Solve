class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2
            
            if nums[m] < nums[r]:
                r = m  # look to the left
            elif nums[l] <= nums[m]:
                l = m + 1  # look to the right and cases where l == r we increment l to break the loop
            
            # essentially 
            """
            if l == m:
                break
            """
            
        
        return nums[m]
        