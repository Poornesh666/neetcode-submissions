class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for st in range(len(nums)):
            for end in range(st, len(nums)):
                temp = sum(nums[st:end+1])
                maxSum = max(maxSum, temp)

        return maxSum