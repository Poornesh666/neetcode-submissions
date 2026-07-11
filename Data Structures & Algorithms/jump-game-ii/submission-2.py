class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return 0

            ans = float("+inf")

            end = min(len(nums)-1, i+nums[i])
            for j in range(i+1,end+1):
                ans = min(ans, 1 + dfs(j))

            memo[i] = ans
            return ans

        return dfs(0)