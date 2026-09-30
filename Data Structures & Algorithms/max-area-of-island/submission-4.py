class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        area = 0
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r, c):
            depth = 1
            if not(0 <= r < row and 0 <= c < col and grid[r][c] == 1):
                return 0

            grid[r][c] = 0
            for i,j in moves:
                nr, nc = r+i, c+j
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                    depth += dfs(r+i, c+j)
        
            return depth

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))


        return area