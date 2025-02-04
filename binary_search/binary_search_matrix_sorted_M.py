class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1

        # find the row where the target is located
        while top <=bot:
            row = (top+bot)//2
            
            if target < matrix[row][0]:
                bot  = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        # after finding the row where the target is located, we perform binary search on that row
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            index = (l + r) // 2

            if matrix[row][index] == target:
                return True
            if target > matrix[row][index]:
                l = index + 1
            elif target < matrix[row][index]:
                r = index - 1
        
        return False

        
        
            
        
