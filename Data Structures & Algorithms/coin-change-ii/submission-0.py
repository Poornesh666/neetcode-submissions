class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp =[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                skip = dp[i-1][j]
                if coins[i-1] <= j:
                    take = dp[i][j-coins[i-1]]
                    dp[i][j] = take+skip
                else:
                    dp[i][j] = skip

        return dp[n][amount]