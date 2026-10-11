class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[float("inf")]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                skip = dp[i-1][j]
                if coins[i-1] <= j:
                    take = 1 + dp[i][j-coins[i-1]]
                    dp[i][j] = min(take, skip)
                else:
                    dp[i][j] = skip

        flag = dp[n][amount] == float("inf")
        return dp[n][amount] if not flag else -1