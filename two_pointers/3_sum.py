# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sol = set()

#         for i, a in enumerate(nums):
#             t = set()
#             for j, b in enumerate(nums):
#                 if i!=j:
#                     third = 0 - (b + a)
#                     if third not in t:
#                         t.add(b)
#                     else:
#                         # print(a,b,third)
#                         sol.add(tuple(sorted((a , b , third))))

#         return list(sol)        
#         -4 -1 -1 0 1 2  


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue # skip duplicates [ -1, -1, 0, 1, 2]
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = nums[l] + nums[r] + a

                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.add(tuple(sorted((a, nums[l], nums[r]))))
                    l += 1
                    r -= 1


        return list(res)