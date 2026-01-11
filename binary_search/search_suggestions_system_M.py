class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        # sort the products first lexicographically
        products.sort() # (O(nlogn))

        l, r = 0, len(products) - 1
        res = []

        # now go thorugh each character of the searchword
        for i in range(len(searchWord)): # O(m)
            c = searchWord[i] # the ith character of searchWord

            # Two pointer is O(nW)
            while l <= r and (i >= len(products[l]) or products[l][i] != c):
                # i >= len(products[l]) -> the l pointed word is smaller than ith index so we cant go to that index
                # products[l][i] != c -> the ith character of the l pointed word is not matching with the current character c
                l += 1
            
            while l <= r and (i >= len(products[r]) or products[r][i] != c):
                r -= 1
            
            window = r - l + 1
            res.append([])

            for j in range(min(3, window)):
                res[-1].append(products[l + j])
            
        
        return res
    
# Binary Search Solution
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() # O(nlogn)
        n = len(products)
        res = []
        prefix = ""

        for ch in searchWord:
            temp = []
            prefix += ch
            starting_index = self.binary_search(products, prefix) # used to find starting index from which we can look      
            # this loop looks for 3 words from starting index
            for i in range(starting_index, min(starting_index + 3, n)): # cause we need at most 3 words and the product list can be exhausted
                if products[i].startswith(prefix):
                    temp.append(products[i])

            res.append(temp)
        return res
        
    def binary_search(self, array, target):
        l = 0
        r = len(array)

        while l < r:
            mid = (l + r) // 2
            if array[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        # we return the starting index after the binary search cause we need the next 3 words
        return l

# solution with Trie

class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            
            node = node.children[char]
        
        node.is_word = True
    
    def getPrefixNode(self, prefix):
        node = self

        for char in prefix:
            if char not in node.children:
                return None 
            
            node = node.children[char]
        
        return node

    def dfs_from_prefix_node(self, node, res, word):
        # base case handled here
        if len(res) == 3:
            return
        
        if node.is_word:
            res.append(word)
            if len(res) == 3:
                return res
        
        # now go through all alphabet characters from 'a' to 'z' that might be in the trie
        for char in "abcdefghijklmnopqrstuvwxyz": # maintains the lexicographical order
            if char in node.children:
                self.dfs_from_prefix_node(node.children[char], res, word + char)
                if len(res) == 3:
                    return

    def searchSuggestedWords(self, prefix):
        res = []
        prefix_node = self.getPrefixNode(prefix)

        if prefix_node is None:
            return res
        
        # else we found the prefix node
        # we start preorder traversal from this node till we find 3 words
        self.dfs_from_prefix_node(prefix_node, res, prefix) 

        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        # first insert all the words
        for product in products:
            trie.insert(product)
        
        res = []
        prefix = ''

        for char in searchWord:
            prefix += char
            res.append(trie.searchSuggestedWords(prefix))
        

        return res
