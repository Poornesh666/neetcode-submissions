class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(i, open):
            if (i, open) in memo:
                return memo[(i, open)]
            
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == '(':
                ans = dfs(i+1, open+1)
                memo[(i,open)] = ans 
                return ans
            elif s[i] == ')': return dfs(i+1, open-1)
            else: return (dfs(i+1, open) or dfs(i+1, open+1) or dfs(i+1, open-1))

        return dfs(0,0)