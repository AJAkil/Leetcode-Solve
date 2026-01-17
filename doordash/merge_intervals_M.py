"""
PROBLEM: Merge Intervals (LeetCode 56 - Medium)
------------------------------------------------
Given intervals array where intervals[i] = [start, end],
merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

KEY INSIGHT: Sort by start time, then merge greedily.
"""

class Solution:
    """
    APPROACH: Sort + Greedy Merge
    
    INTUITION:
    - Sort intervals by start time
    - Iterate: if current overlaps with last merged (curr.start <= last.end)
      -> merge by extending last.end = max(last.end, curr.end)
    - Otherwise add as separate interval
    
    TIME: O(n log n)
    SPACE: O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals by the start time
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        # then we iterate over the sorted intervals
        for curr_int in intervals[1:]:
            if res[-1][1] >= curr_int[0]:
                # we found an overlapping interval
                start_time = res[-1][0]
                end_time = max(res[-1][1], curr_int[1])

                # you replace the latest one that is pushed
                # because two are merged together
                res[-1] = [start_time, end_time]
            else:
                # non overlapping interval, no need to merge
                res.append(curr_int)
        
        return res
