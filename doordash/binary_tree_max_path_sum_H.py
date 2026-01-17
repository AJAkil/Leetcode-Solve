"""
PROBLEM: Binary Tree Maximum Path Sum (LeetCode 124 - Hard)
------------------------------------------------------------
Find the maximum path sum in a binary tree. Path can start/end at any node,
must follow parent-child connections, and each node appears at most once.

Example:
    -10
    /  \
   9   20
      /  \
     15   7
Output: 42 (15 -> 20 -> 7)

KEY INSIGHT: At each node, decide whether to include left/right subtree.
- Path can "turn" at any node (include both left + right + node)
- But return value to parent can only include ONE side
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    APPROACH: DFS with Global Maximum Tracking
    
    INTUITION:
    - At each node, calculate max path going through it (left + node + right)
    - Update global max with this value
    - Return to parent: node + max(left, right) - can only go one direction
    - Use max(0, subtree) to ignore negative paths
    
    TIME: O(n)
    SPACE: O(h) recursion stack
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            # base case
            nonlocal res
            if not node:
                return 0
            
            left_path_val = max(0, dfs(node.left))
            right_path_val = max(0, dfs(node.right))

            # update the global res
            res = max(res, node.val + left_path_val + right_path_val)

            return node.val + max(left_path_val, right_path_val)

        
        dfs(root)
        return res

        