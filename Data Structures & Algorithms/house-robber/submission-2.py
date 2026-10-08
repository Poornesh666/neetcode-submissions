class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        def calculate(idx):
            if idx >= len(nums):  
                return 0
            if cache[idx] != -1:
                return cache[idx]

            rob = nums[idx] + calculate(idx+2)
            skip = calculate(idx+1)
            cache[idx] = max(rob, skip)
            return cache[idx]

        return calculate(0)