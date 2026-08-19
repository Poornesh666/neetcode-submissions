class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)

        def backtrack(i, j, idx):
            if idx == w:
                return True

            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[idx]:
                return False
        
            char = board[i][j]
            board[i][j] = '#'

            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                r, c = i+i_off, j+j_off
                if backtrack(r, c, idx+1):
                    return True

            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False