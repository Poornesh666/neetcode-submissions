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

        def backtrack(idx, path):
            if idx == len(s):
                res.append(path.copy())
                return

            for end in range(idx, len(s)):
                curr = s[idx:end+1]
                if isPallindrome(curr):
                    path.append(curr)
                    backtrack(end+1, path)
                    path.pop()


        backtrack(0, [])
        return res