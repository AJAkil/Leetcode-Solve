from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo: dict[int, int] = {}
    
        def dfs(sum):
            if sum == amount:
                return 0 # no other way to get to the sum 

            if sum > amount:
                return inf

            if sum in memo:
                return memo[sum]

            ways = inf 
            for coin in coins:
                # we take each type 
                ways = min(ways, 1 + dfs(sum + coin))

            memo[sum] = ways # the minimum possible way we got through aggregation
            return ways
                
        result = dfs(0)

        return result if result != inf else -1
        