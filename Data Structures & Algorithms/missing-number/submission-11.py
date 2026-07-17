class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i, num in enumerate(nums):
            xorr ^= i ^ num

        return xorr