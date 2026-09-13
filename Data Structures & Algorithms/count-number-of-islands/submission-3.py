class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        def dfs(r,c):
            if not (0<=r<rows and 0<=c<cols):
                return

            grid[r][c] = "0"
            for i,j in moves:
                nr, nc = r+i, c+j
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1"):
                    dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1

        return res