class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1 = 1
        dp2 = 0

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = dp1
            
            if (i+1 < n) and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                curr += dp2

            dp2 = dp1
            dp1 = curr 
            
        return dp1
