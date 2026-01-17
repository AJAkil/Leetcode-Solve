class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = dict()

        
        def dfs(r, c, prev):
            # prev -> the value at the previous cell

            # check the base case here
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0, None

            # memo case here
            if (r,c) in memo:
                return memo[(r,c)]


            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            dfs_res = 1
            next_path = None
            for r_dir, c_dir in dirs:
                new_r = r + r_dir
                new_c = c + c_dir

                dfs_new_len, dfs_new_next = dfs(new_r, new_c, matrix[r][c])
                dfs_new_res = 1 + dfs_new_len

                if dfs_new_res > dfs_res:
                    dfs_res = dfs_new_res
                    next_path = (new_r, new_c)

            memo[(r,c)] = (dfs_res, next_path)
            return dfs_res, next_path
        
        res = 0
        starting_row = -1
        starting_col = -1
        dfs_curr_res = 0
        for r in range(ROWS):
            for c in range(COLS):
                dfs_curr_res, next_path = dfs(r,c,float('-inf'))
                if res < dfs_curr_res:
                    res =  dfs_curr_res
                    starting_row = r
                    starting_col = c
        
        current = (starting_row, starting_col)
        path = [current]

        while current in memo:
            length, next_cell = memo[current]

            if next_cell is None:
                break 
                
            path.append(next_cell)
            current = next_cell

        
        return res, path
        



            
        