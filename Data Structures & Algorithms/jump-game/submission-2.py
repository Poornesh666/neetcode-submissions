class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        
        for i in range(1, len(nums)):
            if i > reach:
                return False
            new_reach = i + nums[i]
            reach = max(reach, new_reach)

        return True