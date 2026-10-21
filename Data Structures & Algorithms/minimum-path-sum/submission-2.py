class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        dp = [[0]*c for _ in range(r)]
        dp[r-1][c-1] = grid[r-1][c-1]

        for j in range(c-2, -1, -1):
            dp[r-1][j] = grid[r-1][j] + dp[r-1][j+1]

        for i in range(r-2, -1, -1):
            dp[i][c-1] = grid[i][c-1] + dp[i+1][c-1]

        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])

        return dp[0][0]