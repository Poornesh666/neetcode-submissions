class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = n*(n+1)//2

        for i in range(max_sum + 1):
            if i not in nums:
                return i