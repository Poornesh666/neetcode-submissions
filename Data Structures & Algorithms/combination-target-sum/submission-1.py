class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        choice = []

        def backtrack(running_sum, idx):
            if running_sum == target:
                res.append(choice.copy())
                return

            if running_sum > target:
                return

            for i in range(idx, len(nums)):
                choice.append(nums[i])
                backtrack(nums[i]+running_sum, i)
                choice.pop()

        backtrack(0, 0)
        return res