# solution 1
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        temp_arr = []
        
        for index, num in enumerate(arr):
            if num == 0:
                temp_arr.append(0)
                temp_arr.append(0)
            else:
                temp_arr.append(num)
        
        for index in range(len(arr)):
            arr[index] = temp_arr[index]


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        
        for i, num in enumerate(arr):
            if num == 0:
                zeros += 1
        
        i = len(arr) - 1
        j = len(arr) + zeros - 1
        print(i,j)
        
        while(i != j):
            arr = self.insert(arr, i, j)
            j -= 1
            
            if arr[i] == 0:
                arr = self.insert(arr, i, j)
                j -= 1
                
            i -= 1
            
            
    
    def insert(self, arr, i, j):
        if j < len(arr):
            print(i,j)
            arr[j] = arr[i]
            print(arr)
        return arr

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        length = len(arr)
        
        if length == 0:
            return
        
        i = 0
        
        while i < length:
            if arr[i] == 0:
                for j in reversed(list(range(length))):
                    if j <=i: break
                    
                    arr[j] = arr[j-1]
                i+=1
            i+=1 
    
            
        
            
        
