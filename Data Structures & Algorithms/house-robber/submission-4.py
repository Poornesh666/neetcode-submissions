class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        if n == 1:
            return nums[0]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            take = dp[i-2]+nums[i]
            skip = dp[i-1]
            dp[i] = max(take, skip)

        return dp[n-1]
        

        # cache = [-1]*len(nums)
        # def calculate(idx):
        #     if idx >= len(nums):  
        #         return 0
        #     if cache[idx] != -1:
        #         return cache[idx]

        #     rob = nums[idx] + calculate(idx+2)
        #     skip = calculate(idx+1)
        #     cache[idx] = max(rob, skip)
        #     return cache[idx]

        # return calculate(0)