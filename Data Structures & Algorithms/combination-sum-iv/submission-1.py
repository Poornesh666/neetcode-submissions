class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0

        dp = [-1]*(target+1)

        def solve(sum):
            ans = 0
            if sum == target:
                return 1
            
            if sum > target:
                return 0

            if dp[sum] != -1:
                return dp[sum]

            for i in range(len(nums)):
                ans += solve(sum+nums[i])
            
            dp[sum] = ans
            return ans

        return solve(0)