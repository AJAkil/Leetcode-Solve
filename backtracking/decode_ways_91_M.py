class Solution:
    def numDecodings(self, s: str) -> int:
        memo: dict[int, int] = {}
        
        def dfs(start_index):
            # end condition
            if start_index == len(s):
                return 1 

            # do memo later here 
            if start_index in memo:
                return memo[start_index]

            ans = 0

            # get the edges
            # if something starts with a 0, we return what we have so far
            if s[start_index].startswith("0"):
                return ans 

            # two possible ways to decode - taking 1 digit at a time 
            ans += dfs(start_index + 1)

            # or take two digits at a time
            # check if I can take two digits 
            if 10 <= int(s[start_index: start_index + 2]) <= 26:
                ans += dfs(start_index + 2)

            memo[start_index] = ans

            return ans
        
        return dfs(0)

        