class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        if n == 0:
            return 0

        prefix_arr = [0]*n
        suffix_arr = [0]*n
        maxi1 = height[0]
        maxi2 = height[n-1]

        for i in range(n):
            maxi1 = max(maxi1, height[i])
            suffix_arr[i] = maxi1

        for i in range(n-1, -1, -1):
            maxi2 = max(maxi2, height[i])
            prefix_arr[i] = maxi2

        for i in range(n):
            res += min(suffix_arr[i], prefix_arr[i]) - height[i]

        return res