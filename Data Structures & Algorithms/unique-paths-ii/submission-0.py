class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        target = (row-1, col-1)
        moves = [(1,0),(0,1)]
        memo = defaultdict(int)
        
        def solve(r, c):
            if not (0 <= r < row and 0 <= c < col and obstacleGrid[r][c] == 0):
                return 0

            if (r,c) == target:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            paths = 0
            for i, j in moves:
                nr, nc = i+r, j+c
                memo[(r,c)] += solve(nr, nc)

            return memo[(r,c)]
        return solve(0,0)