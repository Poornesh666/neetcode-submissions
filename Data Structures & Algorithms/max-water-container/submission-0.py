class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, i, j = 0, 0, len(heights) - 1

        while i < j:
            curr_area = min(heights[i], heights[j]) * (j-i) 
            area = max(curr_area, area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return area