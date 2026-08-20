class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]
        rows = set()
        upperDiag = set()
        lowerDiag = set()

        def isSafe(row, col):
            if row in rows:
                return False

            if row+col in upperDiag:
                return False

            if row-col in lowerDiag:
                return False

            return True

        def backtrack(col):
            if col == n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    #choose
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

        backtrack(0)
        return res