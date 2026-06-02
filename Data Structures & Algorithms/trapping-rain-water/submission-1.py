class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        if n == 0:
            return 0


        for i in range(n):
            left_max = right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i+1, n):
                right_max = max(right_max, height[j])

            res += min(left_max, right_max) - height[i]

        return res