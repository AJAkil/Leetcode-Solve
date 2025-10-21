class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen_cell = set() # to track which cell we already visited

        def dfs(i, r, c):

            if board[r][c] != word[i]:
                return False

            # end condition when we find the word
            if i == len(word) - 1:
                return True 
            
            
            seen_cell.add((r,c))
            moves = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            # get the edges
            for next_r, next_c in moves:
                # pruning condition
                if ((next_r, next_c) not in seen_cell and
                    (0 <= next_r < ROWS) and
                    (0 <= next_c < COLS)):
                    if dfs(i+1, next_r, next_c):
                        return True
            seen_cell.remove((r,c))
            return False

        # now call dfs from each cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        return False
        