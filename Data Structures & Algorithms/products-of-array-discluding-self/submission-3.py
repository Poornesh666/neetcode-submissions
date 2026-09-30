class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = suffix = 1

        for i,num in enumerate(nums):
            res[i] = prefix
            prefix *= num

        for i,num in enumerate(reversed(nums)):
            res[len(nums)-1-i] *= suffix
            suffix *= num

        return res