class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        idx, length = 0, 0

        for i in range(n):
            # odd
            l, r = i, i
            while l>=0 and r<n and s[l] == s[r]:
                if (r-l+1) > length:
                    idx = l
                    length = r-l+1
                l -= 1
                r += 1

            #even
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if (r-l+1) > length:
                    idx = l
                    length = r-l+1
                l -= 1
                r += 1

        return s[idx:idx+length]