class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            take = nums[i]+prev2
            skip = prev1
            
            curr = max(take, skip)
            prev2 = prev1
            prev1 = curr

        return prev1