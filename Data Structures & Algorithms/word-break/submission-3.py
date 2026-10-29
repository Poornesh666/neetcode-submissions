class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def recurse(idx):
            if idx == len(s):
                return True

            if idx in memo:
                return memo[idx]

            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring in wordDict:
                    memo[idx] = recurse(i+1)
                    if memo[idx]:
                        return True

            return False

        return recurse(0)