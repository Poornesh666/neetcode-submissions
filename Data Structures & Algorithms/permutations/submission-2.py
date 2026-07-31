class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = nums.copy()

        def backtrack(idx):
            if idx == len(nums):
                res.append(temp.copy())
                return

            for i in range(idx, len(nums)):
                temp[i], temp[idx] = temp[idx], temp[i]
                backtrack(idx+1)
                temp[i], temp[idx] = temp[idx], temp[i]


        backtrack(0)
        return res                