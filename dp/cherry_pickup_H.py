class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(n)]

        def dfs(r1, c1, r2):
            # compute c2 here
            # because r1+c1 = r2 + c2 = t at any step or time t
            c2 = r1 + c1 - r2

            # check out of bounds for dfs
            if r1 >=n or c1 >=n or r2>=n or c2>=n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -10000
            

            # check if we are the end states
            # if we are we will return whatever there is on the grid if there is a cherry
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            

            # the memo step
            if dp[r1][c1][r2] != float('-inf'):
                return dp[r1][c1][r2]
            
            # the dp choice step

            res = dfs(r1, c1+1, r2)
            res = max(res, dfs(r1, c1+1, r2+1))
            res = max(res, dfs(r1+1, c1, r2))
            res = max(res, dfs(r1+1, c1, r2+1))         
            # add the current grid cherry value for person 1
            res += grid[r1][c1]

            # add the current grid cherry value for person 2
            if (r1,c1)!=(r2,c2):
                res += grid[r2][c2]
            
            # save the value for the dp state
            dp[r1][c1][r2] = res
            return res
    

        return max(0, dfs(0,0,0))


        