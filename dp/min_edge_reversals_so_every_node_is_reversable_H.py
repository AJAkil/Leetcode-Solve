class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Useful Link I used to understand the problem:
        https://algo.monster/liteproblems/2858
        '''

        min_reversals = [0] * n # the answer array

        adj_list = [[] for _ in range(n)]

        for s, d in edges:
            adj_list[s].append((d, 1)) # original edge direction s->d with k = 1
            adj_list[d].append((s,-1)) # reverse edge direction d-> with k = -1
        

        def dfs_root(node, parent):
            for neigh, edge_weight in adj_list[node]:
                if neigh!=parent:

                    # if edge weight < 0 we add it to the result array for 0th node
                    min_reversals[0] += int(edge_weight < 0)
                    dfs_root(neigh, node)
        
        # call the dfs_1 from the root
        dfs_root(0, -1)

        def dfs_2(node, parent):
            for neigh, edge_weight in adj_list[node]:
                if neigh!=parent:
                    # if edge weight = 1, moving the root to neighbor means originally we had root->neighbor so we need 1 reversal of edge
                    # if w = -1, it means there was an edge from neigh -> root so if we use root's computed value we need 1 less value than that.
                    min_reversals[neigh] = min_reversals[node] + edge_weight

                    dfs_2(neigh, node)
        
        dfs_2(0,-1)

        return min_reversals

                    
        