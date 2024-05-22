class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = m = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            if arr[i] > m:
                m = arr[i]
            
            arr[i] = temp
            temp = m

        return arr

# second solution
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp =  -1

        for i in range(len(arr)-1, -1, -1):
            m = max(temp, arr[i])
            arr[i] = temp
            temp = m

        return arr
        
        