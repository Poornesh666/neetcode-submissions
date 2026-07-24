class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while top<=bottom and l<=r:
            #left to right
            for i in range(l, r+1):
                res.append(matrix[top][i])
            top += 1
            #top to bottom
            for i in range(top, bottom+1):
                res.append(matrix[i][r])
            r -= 1
            if not (top<=bottom and l<=r): break
            #right to left
            for i in range(r, l-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            #bottom to top
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res