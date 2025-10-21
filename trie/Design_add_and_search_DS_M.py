class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # move the current node ahead
            curr = curr.children[char]
        
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(start_idx, root):
            curr = root

            for i in range(start_idx, len(word)):
                char = word[i]

                if char == ".":
                    # look through the children of current node
                    for child in curr.children.values():
                        dfs_res = dfs(i+1, child)        

                        if dfs_res: # need a single match
                            return True
                    return False # missed this case 
                else:
                    if not char in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.is_word
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)