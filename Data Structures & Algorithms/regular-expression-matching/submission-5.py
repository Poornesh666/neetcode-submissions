from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        @lru_cache(None)
        def recurse(i, j):
            if j == n2:
                return i == n1

            first_match = (i<n1 and (s[i] == p[j] or p[j] == '.'))

            if j+1 < n2 and p[j+1] == '*':
                return (recurse(i, j+2) or (first_match and recurse(i+1, j)))

            return (first_match and recurse(i+1, j+1))

        return recurse(0,0)