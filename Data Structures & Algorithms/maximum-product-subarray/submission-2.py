class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            temp = num * currMax
            currMax = max(temp, num*currMin, num)
            currMin = min(temp, num*currMin, num)
            maxi = max(maxi, currMax)

        return maxi