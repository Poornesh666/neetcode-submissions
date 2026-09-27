class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, currSum, path):
            if currSum == target:
                res.append(path.copy())
                return

            if currSum > target:
                return

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i, currSum+nums[i], path)
                path.pop()

        backtrack(0, 0, list())
        return res