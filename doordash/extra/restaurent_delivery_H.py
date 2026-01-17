from collections import deque

def heatmap_bfs(n, restaurants):
    dirs = [
        (-1,-1), (-1, 0), (1, -1),
        (0, -1),        (0,1),
        (1,-1), (1, 0), (1,1)
    ]

    res = [[0] * n for i in range(n)]

    best_range_seen = [[0]*n for i in range(n)]

    q = deque()

    # add the sources first
    for (i,j,r,d) in restaurants:
        if 0<= i < n and 0<= j < n:
            q.append(i,j,r,d)
            best_range_seen[r][c] = r
    

    # start the BFS 
    while q:
        # get the node first
        r,c, r, d = q.popleft()

        # set the deliveries here
        res[r][c] += d

        # spread if range is > 0
        if r > 0:
            for dir_r, dir_c in dirs:
                n_r = r + dir_r 
                n_c = c + dir_c 

                if 0 <= n_r < n and 0 <= n_c < n:
                    # now check for new range
                    new_range = r - 1 # this is the new range for the current new cell

                    # we check if the new range is higher than the best range so far for that cell

                    if new_range > best_range_seen[n_r][n_c]:
                        # we update the new range here
                        best_range_seen[n_r][n_c] = new_range 
                        q.append((n_r, n_c, new_range, d))

    
    return res
