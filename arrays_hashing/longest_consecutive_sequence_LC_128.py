class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has_start = set(nums)
        
        max_l = 0

        for num in has_start:
            
            if (num - 1) not in has_start:
                temp_l = 1
                
                while (num + temp_l) in has_start:
                    temp_l += 1
                
                max_l = max(max_l, temp_l)
        
        return max_l