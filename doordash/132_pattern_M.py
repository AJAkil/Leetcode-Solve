"""
PROBLEM: 132 Pattern (LeetCode 456 - Medium)
---------------------------------------------
Find if there exists i < j < k such that nums[i] < nums[k] < nums[j].
Return true if such pattern exists.

Example:
Input: [3,1,4,2]
Output: true (1 < 2 < 4)

KEY INSIGHT: Monotonic stack scanning from right to left.
- Maintain decreasing stack
- Track nums[k] as the largest value popped
- If we find nums[i] < nums[k], we found the pattern
"""

from collections import deque
class Solution:
    """
    APPROACH: Monotonic Decreasing Stack (Right to Left)
    
    INTUITION:
    - Scan right to left, looking for nums[i] (smallest)
    - Maintain decreasing stack containing potential nums[j] values
    - When we find larger nums[i], pop smaller values as nums[k]
    - If current < nums[k], we found i < k < j pattern
    
    TIME: O(n)
    SPACE: O(n)
    """
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
        