from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def backtrack(idx):
            if idx >= len(nums):
                return 0

            take = nums[idx] + backtrack(idx+2)
            skip = backtrack(idx+1)
            return max(take, skip)

        return backtrack(0)