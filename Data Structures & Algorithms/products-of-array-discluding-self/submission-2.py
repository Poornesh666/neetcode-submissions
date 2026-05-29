class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 

        prefix_sum = suffix_sum = 1

        for i, num in enumerate(nums):
            res[i] = prefix_sum
            prefix_sum *= num 

        for i,num in enumerate(reversed(nums)):
            res[len(nums)-1-i] *= suffix_sum
            suffix_sum *= num
        
        return res