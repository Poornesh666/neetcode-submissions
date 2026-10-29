from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def backtrack(idx):
            if idx == len(s):
                return 1

            if s[idx] == '0':
                return 0

            res = backtrack(idx+1)
            if (idx+1 < len(s)) and (s[idx] == '1' or (s[idx] == '2' and s[idx+1] < '7')):
               res += backtrack(idx+2)

            return res

        return backtrack(0)