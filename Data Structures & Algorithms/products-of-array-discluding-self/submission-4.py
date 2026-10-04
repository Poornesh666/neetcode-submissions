class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 

        prefix_sum = suffix_sum = 1

        for i, num in enumerate(nums):
            res[i] = prefix_sum
            prefix_sum *= num 

        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix_sum
            suffix_sum *= nums[i]
        
        return res