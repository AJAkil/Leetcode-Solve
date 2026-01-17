class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest_dist = 10000000
        idx = -1
        res = -1

        for i in range(len(points)):
            a,b = points[i]

            if a != x and b != y:
                continue
            
            # valid point found
            dist = abs(x - a) + abs(y - b)

            prev_dist = smallest_dist
            smallest_dist = min(smallest_dist, dist)

            if prev_dist > smallest_dist:
                idx = i
        
        return idx