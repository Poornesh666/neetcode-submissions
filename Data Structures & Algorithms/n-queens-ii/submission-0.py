class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [['.']*n for i in range(n)]
        rows = set()
        upperDiag = set()
        lowerDiag = set()

        def backtrack(col):
            nonlocal res
            if col == n:
                res += 1
                return

            for row in range(n):
                if isSafe(row, col):
                    #choose
                    board[row][col] = "Q"
                    rows.add(row)
                    upperDiag.add(row+col)
                    lowerDiag.add(row-col)
                    #backtrack
                    backtrack(col+1)
                    #undo
                    lowerDiag.remove(row-col)
                    upperDiag.remove(row+col)
                    rows.remove(row)
                    board[row][col] = "."

        def isSafe(row, col):
            return row not in rows and row+col not in upperDiag and row-col not in lowerDiag

        backtrack(0)
        return res