from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        GATE = 0
        visited = set()
        Q = deque()
        ROWS = len(rooms)
        COLS = len(rooms[0])


        def get_nei(node):
            res = []
            row, col = node 
            row_dirs = [-1, 0, 1, 0]
            col_dirs = [0, 1, 0, -1]

            for i in range(len(row_dirs)):
                new_row = row + row_dirs[i]
                new_col = col + col_dirs[i]

                if 0 <= new_row < ROWS and 0 <= new_col < COLS and rooms[new_row][new_col] != INF:
                    res.append((new_row, new_row))
        
            return res 
    
        # get the gates first
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == GATE:
                    Q.append((i,j))
                    visited.add((i,j))
        

        # do BFS
        dist = 0
        while len(Q) > 0:
            n = len(Q)
            
            for _ in range(n):
                node = Q.popleft()
                
                # we process the node after we pop it out
                rooms[node[0]][node[1]] = dist # the gates will have 0 distance

                for nei_node in get_nei(node):
                    if nei_node in visited:
                        continue
                
                    # else, we mark them as visited and add them to the Q
                    Q.append(nei_node)
                    visited.add(nei_node)

                dist += 1
    
            