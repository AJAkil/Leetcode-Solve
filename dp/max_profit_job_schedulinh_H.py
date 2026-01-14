"""
Maximum Profit in Job Scheduling (LeetCode 1235)

PROBLEM:
Given n jobs with startTime[i], endTime[i], and profit[i], find the maximum profit
you can earn by scheduling non-overlapping jobs. A job cannot be scheduled if it
overlaps with another (i.e., if one starts before another ends).

SOLUTION INTUITION:
This is a classic DP problem with a "take it or leave it" pattern for each job.

KEY DECISIONS:

1. Sort by start time:
   - Allows us to process jobs in chronological order
   - Makes it possible to use binary search to find the next compatible job
   - Creates a clear decision boundary: for job i, all compatible jobs are at index j >= i

2. Use index array instead of sorting jobs directly:
   - Preserves original indices to access profit[], startTime[], endTime[] correctly
   - Avoids creating new sorted arrays or tuples
   - Memory efficient while maintaining clean code

3. DFS with memoization (Top-down DP):
   - Natural recursion: for each job i, recursively decide for job i+1
   - Memoization prevents recalculating overlapping subproblems
   - Cleaner than bottom-up DP for this problem structure

4. Two choices at each step:
   - Skip job i: move to dfs(i+1)
   - Take job i: add profit[i] and jump to next compatible job using binary search
   - Return max of both choices

5. Binary search for next compatible job:
   - After taking job i (ends at endTime[i]), find the earliest job j where
     startTime[j] >= endTime[i]
   - O(log n) lookup vs O(n) linear search
   - Critical for overall O(n log n) time complexity

TIME: O(n log n) - sorting + n recursive calls each with O(log n) binary search
SPACE: O(n) - recursion stack + memoization
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        index = list(range(n))
        index.sort(key=lambda i: startTime[i])
        memo = {}

        def dfs(i):
            # base case
            if i == n:
                return 0 # return 0 profit upon reaching end
            
            if i in memo:
                return memo[i]
            
            # we dont take the i-th job
            res = dfs(i+1)

            # if we take the ith job, we have to find out a job that doesnt overlap
            l, r , j = i + 1, n, n

            while l < r:
                mid = (l+r) // 2
                if startTime[index[mid]] >= endTime[index[i]]:
                    j = mid
                    r = mid
                else:
                    l = mid + 1

            res = max(res, profit[index[i]] + dfs(j))
            memo[i] = res

            return res
        
        return dfs(0)