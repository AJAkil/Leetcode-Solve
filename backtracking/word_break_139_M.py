class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo: dict[int, bool] = {}
        
        def dfs(start_index):
            # end condition
            if start_index == len(s):
                return True

            # add memo call here
            if start_index in memo:
                return memo[start_index]

            ans = False
            # get the edges
            for word in wordDict:
                if s[start_index:].startswith(word):
                    # we continue since we found a matching prefix
                    ans = ans or dfs(start_index + len(word))
                    
            memo[start_index] = ans 
            return ans
        
        return dfs(0)
        