class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ele = len(nums)
        missing = sum(nums)
        for nums in range(max_ele+1):
            missing -= nums

        return abs(missing)
    
