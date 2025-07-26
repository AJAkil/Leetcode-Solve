def dfs(res, path, n, nums, track):

    # end case here 
    if len(path) == n:
        res.append(path[:])
        return


    # get the edges here
    for num in nums:
        # prune first
        if num in track:
            continue 

        path.append(num)
        track.add(num)

        dfs(res, path, n, nums, track)

        track.remove(num)
        path.pop()

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        track = set()
        dfs(res, path, n, nums, track)
        return res
        