"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    Link: https://neetcode.io/problems/meeting-schedule-ii?list=neetcode250
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        min_heap = []

        for interval in intervals:

            if min_heap and min_heap[0] <= interval.start:
                # a new meeting started and the old one should finish
                # pop off the heap
                heapq.heappop(min_heap) # remove the free room to use
            
            # push the end time, to track the earliest end time
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
        