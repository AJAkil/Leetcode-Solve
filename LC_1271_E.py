class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        sorted_array = [0] * n
        squared = [num**2 for num in nums]
        left = 0
        right = n - 1
        
        
        index = n - 1
        
        while index >= 0:
            if squared[left] >= squared[right]:
                sorted_array[index] = squared[left]
                left += 1
            else:
                sorted_array[index] = squared[right]
                right -= 1
            
            index -= 1
        
        return sorted_array
                
            
            
        