from collections import deque
def shortestRestaurent(i,j, grid):
    Q = deque()
    visited = set()
    ROWS = len(grid)
    COLS = len(grid[0])
    res = []

    
    Q.append((i,j))
    visited.add((i,j))
    dirs = [
        (-1, 0),
    (0, -1),            (0, 1),
        (1, 0)
    ]
    
    dist = 1
    while Q:

        n = len(Q)

        for _ in range(n):
            # for all the nodes now, the level / dist = 1
            r,c = Q.popleft()

            for dir_r, dir_c in dirs:
                n_r = r + dir_r 
                n_c = c + dir_c 

                if 0 <= n_r < ROWS and 0 <= n_c < COLS:
                    if (n_r, n_c) in visited:
                        continue
                    if grid[n_r][n_c] == 1:
                        res.append(dist) 

                    Q.append((n_r, n_c))
                    visited.add((n_r, n_c))

        dist += 1
    
    return res




