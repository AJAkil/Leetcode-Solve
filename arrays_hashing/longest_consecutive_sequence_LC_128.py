class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make a hash set of the numbers
        has_start = set(nums)
        
        max_l = 0

        for num in has_start:
            
            # for each number in the set, check if the number - 1 is not in the set, if not then we have a start of a sequence
            if (num - 1) not in has_start:
                temp_l = 1
                
                # check if the number + 1 is in the set, if it is then we have a sequence and we increment the length of the sequence
                while (num + temp_l) in has_start:
                    temp_l += 1
                
                # update the max length of the sequence when we finish checking the sequence
                max_l = max(max_l, temp_l)
        
        return max_l