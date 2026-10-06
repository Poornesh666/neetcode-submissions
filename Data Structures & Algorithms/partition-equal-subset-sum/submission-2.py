class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        halfSum = sum(nums) // 2

        dp = [False]*(halfSum+1)
        dp[0] = True

        for num in nums:
            for j in range(halfSum, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[halfSum]