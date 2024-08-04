class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sec_elem_to_idx = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in sec_elem_to_idx:
                return [sec_elem_to_idx[diff], i]
            sec_elem_to_idx[n] = i
        