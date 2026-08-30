class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        res = 0
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                return 0

            area = 1
            grid[r][c] = 0
            for i, j in moves:
                area += dfs(i+r,j+c)
            
            return area
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
                

        return res
