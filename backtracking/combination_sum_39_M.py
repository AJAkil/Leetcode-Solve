class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, res, target, path):

            # end case 
            if target == 0:
                res.append(path[:])
                return

            # get the edges
            for i, num in enumerate(nums):
                # prune step here / invalid step here
                if target - num < 0:
                    continue 

                path.append(num)
                dfs(nums[i:], res, target - num, path)
                path.pop()

            return res
            
    
        res = []
        path = []
        candidates.sort()
        return dfs(candidates, res, target, path)