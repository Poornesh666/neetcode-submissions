class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        moves = [(0,1),(1,0)]
        target = (r-1, c-1)

        memo = {}

        def backtrack(row, col):
            if not (0<=row<r and 0<=col<c):
                return float("inf")

            if (row,col) == target:
                return grid[row][col]

            if (row,col) in memo:
                return memo[(row,col)]

            right = backtrack(row, col+1)
            down = backtrack(row+1, col)

            memo[(row,col)] = grid[row][col] + min(right, down)
            return memo[(row,col)]

        return backtrack(0,0)