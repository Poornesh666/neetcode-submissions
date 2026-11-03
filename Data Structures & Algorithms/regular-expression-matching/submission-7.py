from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[n1][n2] = True

        for i in range(n1, -1, -1):
            for j in range(n2-1, -1, -1):
                first_match = (i<n1 and (s[i]==p[j] or p[j] == '.'))

                if j+1 < n2 and p[j+1] == '*':
                    dp[i][j] = (dp[i][j+2] or (first_match and dp[i+1][j]))
                else:
                    dp[i][j] = (first_match and dp[i+1][j+1])

        return dp[0][0]