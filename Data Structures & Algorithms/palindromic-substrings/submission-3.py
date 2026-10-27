class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0

        for i in range(n):
            # odd
            l, r = i, i
            while l>=0 and r<n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res