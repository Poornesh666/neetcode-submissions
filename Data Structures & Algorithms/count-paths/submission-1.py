from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = [(0,1), (1,0)]

        @lru_cache(None)
        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            
            if row == m-1 and col == n-1:
                return 1

            res = 0

            for i,j in moves:
                res += dfs(row+i, col+j)

            return res

        return dfs(0, 0)