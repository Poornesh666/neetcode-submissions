
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def solve(i, holding):

            if i >= n:
                return 0

            if holding:
                # Continue holding OR sell today
                return max(
                    solve(i+1, True),
                    prices[i] + solve(i+2, False)
                )

            else:
                # Buy today OR skip today
                return max(
                    -prices[i] + solve(i+1, True),
                    solve(i+1, False)
                )

        return solve(0, False)
