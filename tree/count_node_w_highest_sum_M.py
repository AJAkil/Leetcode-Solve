"""
PROBLEM: Count Nodes With Highest Score (LeetCode 2581 - Medium)
-----------------------------------------------------------------
You are given a tree where each node's parent is given in the parents array.
- parents[i] = -1 if node i is the root
- parents[i] = j if node i's parent is j

When you remove a node, the tree splits into connected components:
- Each child subtree becomes separate
- The parent's side (rest of tree) becomes separate

The score of a node is the PRODUCT of sizes of all resulting components.
(If a component has size 0, it contributes factor of 0 to the product)

Return the count of nodes with the HIGHEST score.

Example:
Input: parents = [-1,2,0,2,0]
Tree structure:
    0 (root)
   / \
  2   4
 /
1
3 is also child of 2

When removing node 2: components are [0,4] (size 2), [1] (size 1), [3] (size 1)
Score = 2 * 1 * 1 = 2

KEY INSIGHT: For each node, the score = (size of left subtree) * (size of right subtree) * (size of rest)
- Use DFS postorder to calculate subtree sizes
- For each node, multiply: left_size * right_size * (n - subtree_size)
- Note: For root, "rest" = 0, which is treated as factor 0 or excluded
"""

class Solution:
    """
    APPROACH: DFS Postorder Traversal with Subtree Size Calculation
    
    INTUITION:
    - Build adjacency list for children of each node
    - Use DFS to calculate subtree sizes from bottom-up
    - For each node, score = product of component sizes after removal
    - Track the maximum score and count of nodes achieving it
    
    TIME COMPLEXITY: O(n)
    - Visit each node once: O(n)
    - Each node processed in O(1) time (fixed number of children)
    
    SPACE COMPLEXITY: O(n)
    - children dictionary: O(n)
    - Recursion stack: O(h) where h is tree height, worst case O(n)
    """
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        n = len(parents)
        # Build adjacency list: children[i] = list of node i's children
        children = {i: [] for i in range(n)}

        for i in range(n):
            if parents[i] != -1:
                children[parents[i]].append(i)
        
        res = 0  # Maximum score found so far
        count_nodes = 0  # Count of nodes with max score
        
        def dfs(node):
            """
            Returns the size of subtree rooted at node.
            Calculates node's score and updates global max.
            """
            nonlocal res, count_nodes
            
            sub = 1  # Subtree size (including current node)
            score = 1  # Score initialized to 1 (identity element for multiplication)

            # Process left child (if exists)
            if len(children[node]) >= 1:
                l = dfs(children[node][0])
                sub += l
                score *= l
            
            # Process right child (if exists)
            if len(children[node]) == 2:
                r = dfs(children[node][1])
                sub += r
                score *= r
            
            # Calculate remaining nodes (parent's side of tree)
            rest = n - sub

            # Include rest in score only if it's > 0
            # For root node, rest = 0, so we don't multiply by 0
            if rest > 0:
                score *= rest
            
            # Update maximum score and count
            if score > res:
                res = score
                count_nodes = 1
            elif score == res:
                count_nodes += 1

            return sub
        
        dfs(0)
        return count_nodes