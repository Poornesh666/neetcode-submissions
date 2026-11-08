class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [] #to store indexes
        maxi = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height_idx = stack.pop()
                height = heights[height_idx]

                width = i if not stack else i-stack[-1]-1
                area = height*width
                maxi = max(maxi, area)
            
            stack.append(i)
        
        heights.pop()
        return maxi