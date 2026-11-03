from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)

        @lru_cache(None)
        def dp(i,j):
            if i+1 == j:
                return 0

            ans = 0
            for k in range(i+1, j):
                coins = nums[i]*nums[k]*nums[j] + dp(i,k) + dp(k,j)
                ans = max(ans, coins)

            return ans

        return dp(0,n-1)