class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom-up
        n = len(nums)
        dp = [0]*2
        if n == 1:
            return nums[0]

        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            take = prev2+nums[i]
            skip = prev1

            curr = max(take, skip)
            
            prev2 = prev1
            prev1 = curr

        return prev1
        
        # top-down
        # cache = [-1]*len(nums)
        # def calculate(idx):
        #     if idx >= len(nums):  
        #         return 0
        #     if cache[idx] != -1:
        #         return cache[idx]

        #     rob = nums[idx] + calculate(idx+2)
        #     skip = calculate(idx+1)
        #     cache[idx] = max(rob, skip)
        #     return cache[idx]

        # return calculate(0)