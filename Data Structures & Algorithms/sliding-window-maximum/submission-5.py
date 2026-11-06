class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        rightMax = [0]*n
        leftMax = [0]*n

        for i in range(n):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(nums[i], leftMax[i-1])

        for i in range(n-1, -1, -1):
            if (i+1) % k == 0 or i == n-1:
                rightMax[i] = nums[i]
            else:
                rightMax[i] = max(nums[i], rightMax[i+1])

        res = []
        for i in range(n-k+1):
            res.append(max(rightMax[i], leftMax[i+k-1]))

        return res