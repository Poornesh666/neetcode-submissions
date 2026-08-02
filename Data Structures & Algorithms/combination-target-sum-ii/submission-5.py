class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(running_sum, idx, subset):
            if running_sum == target:
                res.append(subset.copy())
                return

            if running_sum > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                # if running_sum + candidates[i] > target:
                #     break

                subset.append(candidates[i])
                backtrack(running_sum+candidates[i], i+1, subset)
                subset.pop()

        backtrack(0, 0, [])
        return res
