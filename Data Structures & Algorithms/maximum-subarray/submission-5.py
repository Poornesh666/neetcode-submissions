class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for st in range(len(nums)):
            curr = 0
            for end in range(st, len(nums)):
                curr += nums[end]
                maxSum = max(maxSum, curr)

        return maxSum