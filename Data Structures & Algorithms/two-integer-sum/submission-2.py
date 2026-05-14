class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in h:
                return [h[diff], i]
            h[nums[i]] = i
            
            
