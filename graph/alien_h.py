def foreignDictionary(self, words: List[str]) -> str:
    '''
    Link: https://neetcode.io/problems/foreign-dictionary?list=neetcode250
    '''

    # first make the graph
    adj = {c: set() for word in words for c in word}

    # build the graph in pairs first
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))

        # Handle the edge case if two words share same prefix but the first word is longer
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        # else construct the graph via adjacancy list
        for i in range(min_len):
            if w1[i] != w2[i]:
                adj[w1[i]].add(w2[i])
                break 
        
    res = []
    visited = {} # will keep track of nodes visited but need to reset it to false to consider it has not been processed from the parent
    # since another parent can lead upto this node:
    # A - B - C with A - C as well
    
    def dfs(char):

        # first handle the base case
        # if we have processed it we return T/F (the visited state) but we need to reset
        if char in visited:
            return visited[char]

        # now we mark it as visited
        visited[char] = True 

        for nei in adj[char]:
            dfs_res = dfs(nei)

            # if the dfs result is true, it means we hit upon a node we visited before
            # so it is a cycle. The node we hit upon is in the current chain of the dfs
            if dfs_res:
                return True # we got a cycle
        
        # this is the important part
        # we mark the node visited as False for now so that if we visit this from other parent node, we can use it
        visited[char] = False 

        # post dfs
        res.append(char)
    
    # perform the dfs from each node
    for char in adj:
        if dfs(char): # if any dfs return T, we found a loop
            return ""
    
    res.reverse()
    return "".join(res)