class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0

        def dfs(r, c):
            depth = 1
            if r<0 or r>=row or c<0 or c>=col or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            for i,j in moves:
                depth += dfs(r+i, c+j)
                

            return depth

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res