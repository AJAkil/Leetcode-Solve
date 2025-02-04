class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # start with two pointers at the ends of the array
        l, r = 0, len(arr) - 1
        
        # we look at subarrays upto k elements and shrink the window upto k elements
        while r - l >= k:
            if abs(arr[l] - x) <= abs(arr[r] - x): # if the left element is closer to x than the right element
                r -= 1 # remove the right element from the window and shrink the window
            else:
                l += 1 # remove the left element from the window and shrink the window
        
        return arr[l:r+1] # return the subarray


        