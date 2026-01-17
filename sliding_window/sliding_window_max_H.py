"""
PROBLEM: Sliding Window Maximum (LeetCode 239 - Hard)
------------------------------------------------------
Given an array nums and a sliding window of size k which is moving from the very left 
of the array to the very right, return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

from collections import deque

# ==================== APPROACH 1: BRUTE FORCE ====================
class Solution:
    """
    INTUITION:
    - For each window position, scan all k elements to find the maximum
    - Simple but inefficient - recalculates max for overlapping elements
    
    STEPS:
    1. Initialize left pointer at 0, right pointer at k
    2. For each window position:
       - Scan k elements starting from left pointer
       - Track the maximum value
       - Add max to result
       - Slide window by incrementing both pointers
    
    TIME COMPLEXITY: O(n * k)
    - We have n-k+1 windows
    - For each window, we scan k elements
    
    SPACE COMPLEXITY: O(1)
    - Only using constant extra space (excluding output array)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        l = 0
        r = l + k # upto k - 1 index starting from l (0)
        res_arr = []

        while r <= n:
            res = float('-inf')
            for i in range(k):
                res = max(res, nums[l + i])
            
            res_arr.append(res)

            l += 1
            r += 1
        
        return res_arr

    

# ==================== APPROACH 2: MAX HEAP ====================
class Solution:
    """
    INTUITION:
    - Use a max heap to efficiently track the maximum element
    - Store (value, index) pairs to know when elements are out of window
    - Lazy deletion: only remove elements when they're at top and out of window
    
    STEPS:
    1. For each element, push (-value, index) to heap (negative for max heap)
    2. Once we have k elements (i >= k-1):
       - Remove elements from top if their index is outside current window
       - The top element is the max for current window
       - Add to result
    
    TIME COMPLEXITY: O(n log n)
    - Push n elements to heap: O(n log n)
    - In worst case, we might pop all elements: O(n log n)
    
    SPACE COMPLEXITY: O(n)
    - Heap can store up to n elements (in worst case like sorted array)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i)) # store the index as well, it will be used to push out the out of window elements from the current heap
            if i >= k - 1:
                # i has crossed the first window
                # 0 1 2 3 4 5 -> only consider 4 5 and kick out the element at 3 for k = 2 and i = 5
                while heap[0][1] <= i - k:
                    # if the index at the top of the max heap is <= the indices inside the current window
                    heapq.heappop(heap) # we pop it out
                
                res.append(-heap[0][0])
        
        return res


# ==================== APPROACH 3: MONOTONIC DEQUE (OPTIMAL) ====================
class Solution:
    """
    INTUITION:
    - Use a deque to maintain indices of potentially useful elements
    - Keep deque monotonically decreasing (values at indices)
    - Front of deque always contains index of maximum in current window
    - Remove smaller elements from back - they can never be max if current element exists
    - Remove elements from front if they're outside the window
    
    STEPS:
    1. For each element (right pointer):
       - Remove smaller elements from back of deque (they're useless now)
       - Add current index to back of deque
       - Remove front element if it's outside window (index < left pointer)
       - If window is valid size (r+1 >= k), add max to result and move left pointer
    
    TIME COMPLEXITY: O(n) ⭐
    - Each element is pushed to deque exactly once: O(n)
    - Each element is popped from deque at most once: O(n)
    - Total operations: O(n) + O(n) = O(n)
    - KEY INSIGHT: Even though we have while loops, across all iterations:
      * Each of n elements enters deque once (append operation)
      * Each of n elements exits deque at most once (pop from either end)
      * Therefore, total pop operations (from both while loops combined) <= n
    
    SPACE COMPLEXITY: O(k)
    - Deque stores at most k indices at any time
    - In the worst case (all elements decreasing), deque has k elements
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # q of index monotonically decreasing Q

        l = r = 0

        while r < len(nums):
            # first we check if the current num is greater than the rightmost q element        
            while q and nums[q[-1]] <= nums[r]:
                q.pop()  # Remove smaller elements - they can't be max anymore
            
            # next we push the right index
            q.append(r)

            # we also check if the left pointer has proceeded and q has element from past windows
            # this is done by comparing leftmost element of the q with l pointer
            if l > q[0]:
                q.popleft() # we pop element from the q from the left
            
            # we also check if we have reached atleast the minimum window size
            if (r + 1) >= k:
                res.append(nums[q[0]])  # Front of deque is the max for this window
                l += 1 # proceed l by 1 only when window is valid and we got a max
            
            r += 1
            
        return res

        