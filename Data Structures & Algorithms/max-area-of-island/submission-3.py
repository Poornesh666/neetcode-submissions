class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        def dfs(r,c):
            depth = 1
            if not (0<=r<rows and 0<=c<cols):
                return 0

            grid[r][c] = 0
            for i,j in moves:
                nr, nc = r+i, c+j
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1):
                    depth += dfs(nr,nc)

            return depth

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))

        return res