class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        
        indegree = [[0]*col for _ in range(row)]
        q = deque()

        for r in range(row):
            for c in range(col):
                for i, j in moves:
                    nr, nc = i+r, j+c
                    if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1

                if indegree[r][c] == 0:
                    q.append((r,c))

        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
            
                for i, j in moves:
                    nr, nc = i+r, j+c
                    if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr,nc))

        return res
