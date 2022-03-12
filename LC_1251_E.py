class Solution(object):
    
    def count_digits(self, num):
        if num == 0:
            return 0
    
        return 1 + self.count_digits(num//10)
    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            if self.count_digits(nums[i]) % 2 == 0:
                counter += 1
        
        return counter
        

# Alternative
class Solution(object):
    
    def count_digits(self, num):
        if num == 0:
            return 0
    
        return 1 + self.count_digits(num//10)
    
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            if len(str(nums[i])) & 1 == 0:
                counter += 1
        
        return counter
        