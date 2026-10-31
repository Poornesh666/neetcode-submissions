class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, memo = len(prices), {}

        def solve(i, holding):
            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                memo[(i, holding)] = max(solve(i+1, True), prices[i]+solve(i+2, False))
                return memo[(i, holding)]
            else:
                memo[(i, holding)] = max(-prices[i]+solve(i+1, True), solve(i+1, False))
                return memo[(i, holding)]

        return solve(0, False)