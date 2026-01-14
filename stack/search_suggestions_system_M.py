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
    


# ref: https://leetcode.com/problems/search-suggestions-system/discuss/436674/C++JavaPython-Sort-and-Binary-Search-the-Prefix
# approach 1: sort then binary search
# 1. sort input array
# 2. use binary search to find first index
# 3. check the following 3 words
# time: O(nlogn) ---> python timsort
# space: O(n) ---> might need to scan the entire input array

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort() # time O(nlogn)
        array_len = len(products)
        ans = []
        input_char = ""

        for chr in searchWord:
            tmp = []
            input_char += chr
            insertion_index = self.binary_search(products, input_char) # find where input_char can be inserted in-order in the products array
            for word_ind in range(insertion_index, min(array_len, insertion_index+3)): # check the following 3 words, if valid
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target): # bisect.bisect_left implementation
        lo = 0
        hi = len(array)

        while lo < hi:
            mid = (lo + hi) //2
            if array[mid] < target: lo = mid + 1
            else: hi = mid
        return lo