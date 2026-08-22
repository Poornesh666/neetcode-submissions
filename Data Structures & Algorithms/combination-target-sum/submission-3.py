class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, running_sum, path):
            if running_sum == target:
                res.append(path.copy())
                return

            if running_sum > target:
                return

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i, running_sum+nums[i], path) 
                path.pop()
                

        backtrack(0, 0, [])
        return res