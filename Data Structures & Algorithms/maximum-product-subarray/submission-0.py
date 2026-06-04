class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j] 
                maxi = max(maxi, curr)

        return maxi