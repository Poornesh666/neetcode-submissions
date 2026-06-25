class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr: List[int], target):
            st = 0
            end = len(arr) - 1

            while st <= end:
                mid = st + ((end-st) // 2)
                if arr[mid] > target:
                    end = mid - 1
                elif arr[mid] < target:
                    st = mid + 1
                else:
                    return True

            return False

        for row in matrix:
            res = binarySearch(row, target)
            if res:
                return True

        return False  