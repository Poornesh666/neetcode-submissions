class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        choices = []

        def backtrack(running_sum, idx):
            # base conditions
            if running_sum == target:
                res.append(choices.copy())
                return
            
            if running_sum > target:
                return

            for i, num in enumerate(nums[idx:], start = idx):
                choices.append(num)
                backtrack(running_sum+num, i)
                choices.pop()    


        backtrack(0, 0)
        return res