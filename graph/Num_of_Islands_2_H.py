'''
Tutorial Solution: https://algo.monster/liteproblems/305
'''

class UF:
    def __init__(self, n):
        self.parent = list(range(0, n)) # each node is its own parent for now
        self.size = [1] * n # size = 1

    def find(self, x):
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        # we do union by rank or size
        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

        return True

def get_neighbors(row, col, grid):
    row_dir = [-1, 0, 1, 0]
    col_dir = [0, 1, 0, -1]
    res = []

    for i in range(len(row_dir)):
        new_row = row + row_dir[i]
        new_col = col + col_dir[i]

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
            res.append((new_row, new_col))
        
    return res

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UF(m*n) # we treat entire grid for unionfind

        grid = [[0] * n for _ in range(m)]

        result = []

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        count = 0

        for row, col in positions:

            if grid[row][col] == 1:
                # keep count same already 1
                result.append(count)
                continue
            
            # first set the grid to 1
            grid[row][col] = 1
            count += 1

            # check neihbors
            for new_row, new_col in get_neighbors(row, col, grid):
                # do the union find operations
                # first convert 2d coordinate to 1d one
                curr_idx = row * n + col
                neighbor_idx = new_row * n + new_col

                if uf.union(curr_idx, neighbor_idx):
                    count -= 1 # since we combined the two islands

            # after all processing we add it to the results list
            result.append(count)
        
        return result
        