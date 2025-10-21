from collections import deque
def count_number_of_islands(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    def get_neighbors(node):
        row, col = node
        row_dir = [-1, 0, 1, 0]
        col_dir = [0, 1, 0, -1]
        res = []

        for i in range(len(row_dir)):
            n_row = row + row_dir[i]
            n_col = col + col_dir[i]

            if 0 <= n_row < rows and 0 <= n_col < cols:
                res.append((n_row, n_col))
        return res 
    
    def bfs(root):
        Q = deque([root])

        while len(Q) > 0:
            node = Q.popleft()

            for neighbor in get_neighbors(node):
                n_row, n_col = neighbor 

                if grid[n_row][n_col] == 0:
                    continue 

                Q.append(neighbor)
                grid[n_row][n_col] = 0

    island = 0 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue 
            bfs((r,c))
            island += 1
    
    return island

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
