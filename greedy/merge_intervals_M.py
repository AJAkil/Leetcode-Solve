class Solution:
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
