class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        choices = []
        candidates.sort()
        def backtrack(running_sum, idx):
            if running_sum == target:
                res.append(choices.copy())
                return 

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                if running_sum + candidates[i] > target:
                    break

                choices.append(candidates[i])
                backtrack(running_sum + candidates[i], i + 1)
                choices.pop()

        backtrack(0, 0)
        return res