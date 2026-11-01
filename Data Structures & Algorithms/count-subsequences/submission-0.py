from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        
        if n1 < n2:
            return 0
        @lru_cache(None)
        def recurse(i, j):
            if j == n2:
                return 1
            
            if i == n1:
                return 0

            if s[i] == t[j]:
                return recurse(i+1, j+1)+recurse(i+1, j)
            else:
                return recurse(i+1, j)

        return recurse(0, 0)
