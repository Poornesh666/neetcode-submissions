class Solution:
    def permute(self, nums):
        res = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(nums.copy())
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]

                backtrack(idx + 1)

                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return res