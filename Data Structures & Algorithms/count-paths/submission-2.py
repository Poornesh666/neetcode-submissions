from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = [(0,1), (1,0)]
        mem_map = {}
        
        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            
            if row == m-1 and col == n-1:
                return 1

            if (row, col) in mem_map:
                return mem_map[(row, col)]

            res = 0

            for i,j in moves:
                res += dfs(row+i, col+j)
                mem_map[(row, col)] = res

            return res

        return dfs(0, 0)