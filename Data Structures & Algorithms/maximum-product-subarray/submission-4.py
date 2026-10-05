class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxi = mini = 1
        for num in nums:
            temp1 = num*maxi
            temp2 = num*mini
            maxi = max(num, temp1, temp2)
            mini = min(num, temp1, temp2)
            res = max(res, maxi)

        return res