"""
PROBLEM: Rotting Oranges (LeetCode 994 - Medium)
-------------------------------------------------
Grid with 0 (empty), 1 (fresh orange), 2 (rotten orange).
Every minute, rotten oranges make adjacent (4-directional) fresh oranges rotten.
Return minimum minutes until no fresh oranges remain, or -1 if impossible.

Example:
Input: [[2,1,1],
        [1,1,0],
        [0,1,1]]
Output: 4

KEY INSIGHT: Multi-source BFS - all rotten oranges spread simultaneously.
- Similar to: Walls and Gates, 01 Matrix
- Track fresh count to determine if all oranges can rot
"""

from collections import deque
class Solution:
    """
    APPROACH: Multi-Source BFS
    
    INTUITION:
    - Start BFS from ALL rotten oranges simultaneously (not one by one)
    - Process level by level - each level = 1 minute passed
    - Decrement fresh count when orange rots
    - If fresh > 0 at end, return -1
    
    TIME: O(m*n)
    SPACE: O(m*n)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        Q = deque()

        # add the rotten oranges and count the fresh ones
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    Q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0 , -1)]

        while len(Q) > 0 and fresh > 0:
            
            for _ in range(len(Q)):  # <--- The main thing in multi source BFS - process all sources at the same level
                r,c = Q.popleft()
                for d_r, d_c in dirs:
                    n_r = r + d_r
                    n_c = c + d_c

                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                        fresh -= 1 # decrease the fresh count by 1
                        Q.append((n_r, n_c))
                        grid[n_r][n_c] = 2
            
            time += 1

        return time if fresh == 0 else -1

        