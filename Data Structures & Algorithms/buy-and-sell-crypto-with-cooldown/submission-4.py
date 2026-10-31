class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0:
            return 0

        dp = [[0]*2 for _ in range(n+2)]
        # 0 -> no holding, 1 -> holding 
        for i in range(n-1, -1, -1):
            # choice 1 -> not holding any stock 
            # go to next day or buy today's stock
            dp[i][0] = max(dp[i+1][0], -prices[i]+dp[i+1][1])
            # choice 2 -> i have a stock
            # hold and move to next day or sell today and buy 2 days later
            dp[i][1] = max(dp[i+1][1], prices[i]+dp[i+2][0])

        return dp[0][0]