class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        choices = []
        candidates.sort()
        def backtrack(running_sum, idx):
            if running_sum == target:
                res.append(choices.copy())
                return 

            for i, num in enumerate(candidates[idx:], start = idx):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if running_sum + num > target:
                    break                
                choices.append(num)
                backtrack(running_sum+num, i+1)
                choices.pop()

        backtrack(0, 0)
        return res