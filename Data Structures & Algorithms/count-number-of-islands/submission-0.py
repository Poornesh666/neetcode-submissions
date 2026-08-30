class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
                return 

            grid[r][c] = "0"
            for i, j in moves:
                dfs(r+i, c+j)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res