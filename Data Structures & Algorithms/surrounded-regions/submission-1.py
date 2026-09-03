class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        boundaries = set()
        for r in range(rows):
            boundaries.add((r,0))
        for c in range(cols):
            boundaries.add((0,c))
        for r in range(rows):
            boundaries.add((r,cols-1))
        for c in range(cols):
            boundaries.add((rows-1,c))

        q = deque()
        for r,c in boundaries:
            if board[r][c] == "O":
                board[r][c] = "S"
                q.append((r,c))

        while q:
            r,c = q.popleft()

            for i,j in moves:
                nr,nc = r+i,c+j
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        