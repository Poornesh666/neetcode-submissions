class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)

        dp[target] = 1

        for total in range(target - 1, -1, -1):
            for num in nums:
                if total + num <= target:
                    dp[total] += dp[total + num]

        return dp[0]
