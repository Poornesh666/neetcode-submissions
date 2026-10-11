from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def backtrack(idx, curr_sum):
            if curr_sum == amount:
                return 0
                
            if curr_sum > amount:
                return float("inf")   
            
            min_coins = float("inf")

            for i in range(idx, len(coins)):
                res = backtrack(i, coins[i]+curr_sum)
                
                if res != float("inf"):
                    min_coins = min(min_coins, 1+res)

            return min_coins

        res = backtrack(0, 0)

        return res if res != float("inf") else -1
