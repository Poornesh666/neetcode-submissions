class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def solve(start, end):
            prev2, prev1 = nums[start], max(nums[start], nums[start+1])

            for i in range(start+2, end+1):
                take = prev2+nums[i]
                skip = prev1

                curr = max(take, skip)

                prev2, prev1 = prev1, curr

            return prev1

        return max(solve(0, n-2), solve(1, n-1))
            