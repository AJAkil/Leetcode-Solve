class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = dict()

        
        def dfs(r, c, prev):
            # prev -> the value at the previous cell

            # check the base case here
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0

            # memo case here
            if (r,c) in memo:
                return memo[(r,c)]


            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            dfs_res = 1
            for r_dir, c_dir in dirs:
                new_r = r + r_dir
                new_c = c + c_dir

                dfs_res = max(dfs_res, 1 + dfs(new_r, new_c, matrix[r][c]))

            memo[(r,c)] = dfs_res
            return dfs_res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c,float('-inf'))) # cause finding longest
        
        return res
        



            
        