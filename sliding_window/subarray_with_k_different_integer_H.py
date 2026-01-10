from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l_near, l_far = 0, 0
        n = len(nums)
        res = 0

        for r, elem in enumerate(nums):
            freq[elem] += 1

            # there are two cases where we expand the near pointer
            while len(freq) > k: # the invalid case: valid case is: len(freq) == k
                freq[nums[l_near]] -= 1

                if freq[nums[l_near]] == 0:
                    freq.pop(nums[l_near])
                
                l_near += 1
                l_far = l_near
            
            # we also shift the left pointer if number pointer by the l_near is > 1
            while freq[nums[l_near]] > 1:
                freq[nums[l_near]] -= 1
                l_near += 1
            
            if len(freq) == k:
                res += l_near - l_far + 1
        
        return res
                

        