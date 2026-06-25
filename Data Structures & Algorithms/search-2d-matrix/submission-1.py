class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols

        st, end = 0, total - 1

        while st <= end:
            mid = st + ((end-st) // 2)

            row = mid // cols
            col = mid % cols
            value = matrix[row][col]

            if value > target:
                end = mid - 1
            elif value < target:
                st = mid + 1
            else:
                return True

        return False