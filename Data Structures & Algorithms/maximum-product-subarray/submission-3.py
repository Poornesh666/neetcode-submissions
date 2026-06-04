class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            temp1 = num*currMax
            temp2 = num*currMin
            currMax = max(temp1, temp2, num)
            currMin = min(temp1, temp2, num)
            maxi = max(maxi, currMax)

        return maxi