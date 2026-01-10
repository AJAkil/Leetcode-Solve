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
            for i in range(starting_index, min(starting_index + 3, n)):
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
