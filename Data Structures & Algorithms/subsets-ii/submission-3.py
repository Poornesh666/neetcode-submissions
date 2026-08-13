class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(idx, subset):
            res.append(subset[::])            

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0, [])
        return res