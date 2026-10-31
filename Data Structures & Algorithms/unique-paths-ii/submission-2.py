class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        target = (row - 1, col - 1)

        memo = {}

        def solve(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if (r, c) == target:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = solve(r + 1, c) + solve(r, c + 1)

            return memo[(r, c)]

        return solve(0, 0)