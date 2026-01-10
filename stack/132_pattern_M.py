from collections import deque
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num_k = -1* float('inf') # set the nums[k]
        stack = deque()

        for num_i in nums[::-1]:
            if num_i < num_k:
                # this takes care of the first condition
                return True
            
            while len(stack) > 0 and stack[-1] < num_i:
                num_k = stack[-1]
                stack.pop() # keep popping to maintain the decreasing one
                '''
                The reason to keep a monotonically decreasing stack is to make sure when we 
                pop the number off, we can srt the nums[k] value immedietly. the decreasing stack
                would contain numbers that are greater than nums[k] but in a decreasing order.
                Since its decreasing, when we pop it off, we can just set the latest one to be nums[k]
                '''
            
            stack.append(num_i)
        
        return False
        