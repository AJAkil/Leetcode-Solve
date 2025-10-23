"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(n,r,c):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
            
            if all_same:
                return Node(grid[r][c], True, None, None, None, None)
            
            # divide 
            n = n//2

            top_l = dfs(n, r, c)
            top_r = dfs(n, r, c + n)
            bottom_l = dfs(n, r + n, c)
            bottom_r = dfs(n, r + n, c + n)

            return Node(1, False, top_l, top_r, bottom_l, bottom_r)
        
        return dfs(len(grid), 0, 0)
            