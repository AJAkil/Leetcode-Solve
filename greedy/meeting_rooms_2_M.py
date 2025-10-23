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
        '''
        Each heap element = one ongoing meeting = one room occupied
        '''

        '''
        Why only check min_heap[0]?

        We only need to check the earliest ending meeting
        If the earliest one hasn't ended, none of the others have either (they're in a min heap!)
        If the earliest one HAS ended, we can reuse that room
        '''

        for interval in intervals:
            # check if the earliest ending meeting has been done and a new meeting wills tart
            # if so, we create space for that meeting that came next!
            if min_heap and min_heap[0] <= interval.start:
                # a new meeting started and the old one should finish
                # pop off the heap
                heapq.heappop(min_heap) # remove the free room to use
            
            # push the end time, to track the earliest end time
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
        