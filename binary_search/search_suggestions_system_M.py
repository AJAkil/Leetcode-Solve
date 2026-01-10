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
