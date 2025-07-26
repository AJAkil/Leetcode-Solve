class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_index, nums, res, path):

            res.append(path[:])

            # get the edges
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, nums, res, path)
                path.pop()
            
            return
        
        res = []
        path = []
        nums.sort()
        dfs(0, nums, res, path)

        return res

        # Alternative Approach
        # def dfs(start_index, nums, res, path):

        #     # end condition
        #     if start_index == len(nums):
        #         return 

        #     # get the edges
        #     for i, num in enumerate(nums[start_index:]):
        #         path.append(num)
        #         res.append(path[:]) # copy the path 

        #         dfs(start_index + i + 1, nums, res, path)
        #         path.pop()
            
        #     return
    
        # res = []
        # path = []
        # nums.sort()
        # dfs(0, nums, res, path)
        # res.append([])
        
        # return res