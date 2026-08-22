class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]

        def isSafe(row, col):
            #left
            r, c = row, col-1
            while c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1
            #upperDiag
            r, c = row-1, col-1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1 
            #lowerDiag
            r, c = row+1, col-1
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False 
                r += 1
                c -= 1

            return True

        def backtrack(col):
            if col == n:
                temp = ["".join(row) for row in board]
                res.append(temp)
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    backtrack(col+1)
                    board[row][col] = "."

        backtrack(0)
        return res