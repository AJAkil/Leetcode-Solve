"""
Problem: Longest Increasing Path in a Matrix (LeetCode 329) - HARD
========================================================================

Given an m x n matrix, find the length of the longest strictly increasing path.
You can move in 4 directions (up, down, left, right) from each cell.

Example:
    Input: matrix = [[9,9,4],
                     [6,6,8],
                     [2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9] or [1, 6, 6, 9]

Example 2:
    Input: matrix = [[3,4,5],
                     [3,2,6],
                     [2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]


APPROACH: DFS with Memoization + Path Reconstruction
========================================================================

INTUITION:
----------
- We can start a DFS from ANY cell and explore all 4 directions
- From each cell, we only move to neighbors with STRICTLY greater values
- This naturally prevents cycles (can't revisit a cell in same path)
- Since subproblems overlap (same cell visited from different starting points),
  we use memoization to avoid recomputation
- To track the actual path, we store not just the length, but also the NEXT cell
  that leads to the longest increasing path from current cell

ALGORITHM STEPS:
----------------
1. DFS Function (returns tuple: (max_length, next_cell)):
   - Base case: out of bounds or not increasing -> return (0, None)
   - Check memo: if already computed, return cached result
   - Try all 4 directions and find which gives longest path
   - Store the direction (next_cell coordinates) that gives best result
   - Cache and return (length, next_cell)

2. Find Starting Point:
   - Try DFS from every cell in the matrix
   - Track which cell gives the overall longest path
   - Save the coordinates of this starting cell

3. Path Reconstruction:
   - Start from the cell that has the longest increasing path
   - Follow the "next_cell" chain stored in memo
   - Keep adding cells to path until next_cell is None (end of path)
   - This gives us the actual sequence of cells forming longest path

PATH RECONSTRUCTION DETAILS:
-----------------------------
The memo stores: memo[(r,c)] = (length_from_here, next_best_cell)
- length_from_here: longest increasing path starting at (r,c)
- next_best_cell: the neighbor that leads to this longest path
  * If no valid neighbor exists (dead end), next_best_cell = None

To reconstruct:
1. Start at (starting_row, starting_col) - the cell with global max length
2. Look up memo to find which neighbor to go to next
3. Follow this chain: current -> next -> next -> ... -> None
4. Build the path list as we follow the chain

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(m * n)
- Each cell is visited once by DFS (memoization prevents revisits)
- For each cell, we explore 4 directions: O(4) = O(1) per cell
- Total: O(m * n) cells × O(1) = O(m * n)
- Path reconstruction: O(length of path) = O(m * n) worst case
- Overall: O(m * n)

Space Complexity: O(m * n)
- Memo dictionary stores entry for each cell: O(m * n)
- Recursion stack depth in worst case: O(m * n) for a path visiting all cells
- Path list: O(m * n) worst case
- Overall: O(m * n)

Edge Cases:
- Single cell matrix: length = 1, path = [(0,0)]
- All equal values: length = 1 from any cell
- Already sorted increasing: path length = m * n
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = dict()  # memo[(r,c)] = (max_length_from_here, next_cell_in_path)

        
        def dfs(r, c, prev):
            """
            DFS to find longest increasing path starting from (r, c).
            
            Args:
                r, c: current cell coordinates
                prev: value of previous cell (to ensure strictly increasing)
            
            Returns:
                (length, next_cell): length of longest path and next cell to follow
            """
            # Base case: out of bounds or not strictly increasing
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0, None

            # Return cached result if already computed
            if (r,c) in memo:
                return memo[(r,c)]

            # Explore all 4 directions
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            dfs_res = 1  # At minimum, current cell forms a path of length 1
            next_path = None  # Track which neighbor gives the longest path
            
            for r_dir, c_dir in dirs:
                new_r = r + r_dir
                new_c = c + c_dir

                # Recursively get length from neighbor
                dfs_new_len, dfs_new_next = dfs(new_r, new_c, matrix[r][c])
                dfs_new_res = 1 + dfs_new_len  # Current cell + path from neighbor

                # Update if this direction gives a longer path
                if dfs_new_res > dfs_res:
                    dfs_res = dfs_new_res
                    next_path = (new_r, new_c)  # Remember which neighbor to follow

            # Cache result: (length from this cell, next cell in longest path)
            memo[(r,c)] = (dfs_res, next_path)
            return dfs_res, next_path
        
        # Find the starting cell with the longest increasing path
        res = 0
        starting_row = -1
        starting_col = -1
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs_curr_res, next_path = dfs(r, c, float('-inf'))
                if res < dfs_curr_res:
                    res = dfs_curr_res
                    starting_row = r
                    starting_col = c
        
        # === PATH RECONSTRUCTION ===
        # Start from the cell that has the globally longest increasing path
        current = (starting_row, starting_col)
        path = [current]

        # Follow the chain of "next_cell" pointers stored in memo
        while current in memo:
            length, next_cell = memo[current]

            # If no next cell (end of path), stop
            if next_cell is None:
                break 
            
            # Add next cell to path and move to it
            path.append(next_cell)
            current = next_cell

        # Return both the length and the actual path
        return res, path