"""
PROBLEM: Making A Large Island (LeetCode 827 - Hard)
-----------------------------------------------------
Given a binary grid (0 = water, 1 = land), you can change at most ONE 0 to 1.
Return the size of the largest island you can create.

Example:
Input: [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect the two separate islands.

KEY INSIGHT: DFS to label islands + check 0s to see potential connections.
- Label each island with unique ID and store its area
- For each 0, check which unique islands it touches
- Island size = 1 + sum of unique neighbor island areas
"""

class Solution:
    """
    APPROACH: Island Labeling + Greedy Selection
    
    INTUITION:
    - Phase 1: DFS to label each island with unique ID (2, 3, 4...)
    - Store {island_id: area} mapping
    - Phase 2: For each 0, check 4 neighbors and collect unique island IDs
    - New island size = 1 + sum(areas of unique neighbors)
    - Track maximum
    
    TIME: O(m*n)
    SPACE: O(m*n)
    """
    def largestIsland(self, grid: List[List[int]]) -> int:
        # first label the islands with dfs

        ROWS = len(grid)
        COLS = len(grid[0])
        island_id = 2
        id_to_area = {}


        def dfs(node, island_id):
            # returns an area
            r,c = node

            dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            area = 1
            grid[r][c] = island_id

            for dir_r, dir_c in dirs:
                n_r = r + dir_r
                n_c = c + dir_c

                if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                    area += dfs((n_r, n_c), island_id)
            
            return area


        #modify the grid itself to label it with the island id and also track the area of the island
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    id_to_area[island_id] = dfs((i,j), island_id)
                    island_id += 1
        
        largest = max(id_to_area.values()) if id_to_area else 0
        
        # now start from the 0 and check the neighbors
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    # see all the neighbors
                    neighbors = set()
                    dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]

                    for dir_r, dir_c in dirs:
                        n_r = i + dir_r
                        n_c = j + dir_c

                        if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c]>1:
                            neighbors.add(grid[n_r][n_c]) # ad the island id
                    
                    # then get the best
                    largest = max(largest, 1 + sum(id_to_area[id] for id in neighbors))
        
        return largest