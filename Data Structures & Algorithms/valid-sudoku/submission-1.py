class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSeen = set()

        for row in range(9):
            seen = set()
            for col in range(9):
                curr = board[row][col]
                if curr != '.':
                    if curr in seen:
                        return False
                
                    seen.add(curr)

        for col in range(9):
            seen = set()
            for row in range(9):
                curr = board[row][col]
                if curr != '.':
                    if curr in seen:
                        return False
                
                    seen.add(curr)
            

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        curr = board[r][c]
                        if curr != '.':
                            if curr in seen:
                                return False
                
                            seen.add(curr)

        return True