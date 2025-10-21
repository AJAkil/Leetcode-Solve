class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        Link: https://neetcode.io/problems/foreign-dictionary?list=neetcode250
        '''

        adj = {c: set() for word in words for c in word}

        # build the graph first
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            # handle the edge case related to lexicographical ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            # base case first
            if char in visited:
                return visited[char]
            
            visited[char] = True
            
            for nei in adj[char]:
                dfs_res = dfs(nei)
                if dfs_res:
                    return True
            
            visited[char] = False # for another path, it can be unvisited
            # post dfs
            res.append(char)
        
        for char in adj:
            if dfs(char):
                # we found a loop
                return ""
        
        res.reverse()
        return "".join(res)