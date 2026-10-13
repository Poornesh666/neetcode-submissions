class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (abs(target) > total) or ((target+total) % 2) != 0:
            return 0

        subset_target = (total+target)//2
        dp = [0]*(total+1)
        dp[0] = 1

        for num in nums:
            for i in range(total, num-1, -1):
                dp[i] += dp[i-num]

        return dp[subset_target]