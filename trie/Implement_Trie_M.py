class Trie:

    def __init__(self):
        self.children = {}
        self.freq = 0
        self.end_of_word = False
        

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            # if the char is not a child
            if char not in node.children:
                # create a new Trie node
                node.children[char] = Trie()
            
            # proceed the trie node
            node = node.children[char]
            node.freq += 1
        node.end_of_word = True
        

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            # proceed to the next node
            node = node.children[char]
        
        return node.end_of_word
        

        

    def startsWith(self, prefix: str) -> bool:
        node = self

        for char in prefix:
            # if char do not exist return False
            if char not in node.children:
                return False 
            
            node = node.children[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)