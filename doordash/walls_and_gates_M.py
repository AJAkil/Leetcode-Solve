"""
PROBLEM: Walls and Gates (LeetCode 286 - Medium)
-------------------------------------------------
Given a 2D grid with:
- INF (2147483647): empty room
- 0: gate
- -1: wall

Fill each empty room with distance to nearest gate. If impossible to reach, leave as INF.

Example:
Input:  INF  -1   0  INF
        INF INF INF  -1
        INF  -1 INF  -1
          0  -1 INF INF

Output:   3  -1   0   1
          2   2   1  -1
          1  -1   2  -1
          0  -1   3   4

KEY INSIGHT: Multi-source BFS from all gates simultaneously.
- Start BFS from ALL gates at once (not one by one)
- Level-by-level expansion ensures shortest distance
- Similar to: Rotting Oranges, 01 Matrix
"""

from collections import deque
class Solution:
    """
    APPROACH: Multi-Source BFS
    
    INTUITION:
    - Instead of BFS from each room to find nearest gate (slow)
    - Do ONE BFS starting from ALL gates simultaneously
    - Distance increments level by level naturally giving shortest paths
    
    TIME: O(m*n) - visit each cell once
    SPACE: O(m*n) - queue can hold all cells
    """
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        GATE = 0
        visited = set()
        Q = deque()
        ROWS = len(rooms)
        COLS = len(rooms[0])


        def get_nei(node):
            res = []
            row, col = node 
            row_dirs = [-1, 0, 1, 0]
            col_dirs = [0, 1, 0, -1]

            for i in range(len(row_dirs)):
                new_row = row + row_dirs[i]
                new_col = col + col_dirs[i]

                if 0 <= new_row < ROWS and 0 <= new_col < COLS and rooms[new_row][new_col] != INF:
                    res.append((new_row, new_row))
        
            return res 
    
        # get the gates first
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == GATE:
                    Q.append((i,j))
                    visited.add((i,j))
        

        # do BFS
        dist = 0
        while len(Q) > 0:
            n = len(Q)
            
            for _ in range(n):
                node = Q.popleft()
                
                # we process the node after we pop it out
                rooms[node[0]][node[1]] = dist # the gates will have 0 distance

                for nei_node in get_nei(node):
                    if nei_node in visited:
                        continue
                
                    # else, we mark them as visited and add them to the Q
                    Q.append(nei_node)
                    visited.add(nei_node)

                dist += 1
    
            