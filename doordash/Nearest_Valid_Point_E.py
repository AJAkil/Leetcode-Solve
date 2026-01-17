"""
PROBLEM: Find Nearest Point That Has the Same X or Y Coordinate (LeetCode 1779 - Easy)
---------------------------------------------------------------------------------------
Given your position (x,y) and array of points, find the index of the nearest valid point.
Valid point: shares same x OR same y coordinate with your position.
Nearest: minimum Manhattan distance.

Example:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2 (point [2,4] shares y=4, distance = 1)

KEY INSIGHT: Filter valid points, track minimum distance.
"""

class Solution:
    """
    APPROACH: Linear Scan with Distance Tracking
    
    INTUITION:
    - Iterate through points
    - Skip if neither coordinate matches
    - Calculate Manhattan distance for valid points
    - Track minimum distance and corresponding index
    
    TIME: O(n)
    SPACE: O(1)
    """
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