class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(idx, curr):
            nonlocal res
            if idx == len(nums):
                res += curr
                return

            # Include
            backtrack(idx+1, curr^nums[idx])
            # Exclude
            backtrack(idx+1, curr)

        backtrack(0, 0)
        return res
