class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1: return [[s]]

        res = []

        def isPallindrome(substr):
            l, r = 0, len(substr) - 1
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(idx, substr):
            if idx == len(s):
                res.append(substr.copy())
                return

            pal_str = ""
            for i in range(idx, len(s)):
                pal_str += s[i]
                if isPallindrome(pal_str):
                    substr.append(pal_str)
                    backtrack(i+1, substr)
                    substr.pop()


        backtrack(0, [])
        return res