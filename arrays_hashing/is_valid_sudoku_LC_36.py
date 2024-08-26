class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                current = board[r][c]

                if (current in row[r] or
                current in col[c] or
                current in sub[r//3 * 3 + c//3]):

                    return False

                row[r].add(current)
                col[c].add(current)
                sub[r//3 * 3 + c//3].add(current)
        
        return True


        