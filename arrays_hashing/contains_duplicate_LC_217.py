class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate.add(nums[i])
            else:
                return True
        
        return False
        