class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = -1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            # left side sorted search there
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                # the right side is sorted, search there
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        return -1

        
