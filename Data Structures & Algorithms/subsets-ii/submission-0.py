class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        nums.sort()
        def backtrack(idx):
            if idx == len(nums):
                res.add(tuple(subset.copy()))
                return

            subset.append(nums[idx])
            backtrack(idx+1)
            subset.pop()
            backtrack(idx+1)

        backtrack(0)
        return [list(t) for t in res]