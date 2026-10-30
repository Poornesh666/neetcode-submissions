class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        memo = {}
        def dfs(r, c):
            res = 1

            if (r,c) in memo:
                return memo[(r,c)]

            for i, j in moves:
                nr, nc = r+i, c+j
                if (0 <= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]):         
                    res = max(res, 1+dfs(nr, nc))

            memo[(r,c)] = res
            return res

        ans = 0
        for r in range(row):
            for c in range(col):
                ans = max(ans, dfs(r,c))

        return ans