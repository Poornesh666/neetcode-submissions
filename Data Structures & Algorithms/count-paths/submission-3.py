class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        moves = [(0,-1),(-1,0)]
        dp[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if (i,j) == (1,1):
                    continue
                    
                for r,c in moves:
                    dp[i][j] += dp[r+i][c+j]

        return dp[m][n]