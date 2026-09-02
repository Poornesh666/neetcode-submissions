class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            depth = 1
            if not(0<=r<rows and 0<=c<cols and grid[r][c]==1):
                return 0

            grid[r][c] = 0
            for i,j in moves:
                depth += dfs(r+i,c+j)

            return depth

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = max(area, dfs(i,j))
        
        return area