class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # row, col = set(), set()
        first_col_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0: first_col_zero = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 #row
                    matrix[0][j] = 0 #col
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0: 
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
