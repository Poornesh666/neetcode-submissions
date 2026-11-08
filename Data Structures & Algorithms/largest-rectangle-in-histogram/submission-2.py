class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store (start_idx, height)
        maxi = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                prev_idx, prev_h = stack.pop()
                maxi = max(maxi, prev_h*(i-prev_idx))
                start = prev_idx

            stack.append((start, h))
        
        n = len(heights)
        for idx, h in stack:
            maxi = max(maxi, h*(n-idx))


        return maxi