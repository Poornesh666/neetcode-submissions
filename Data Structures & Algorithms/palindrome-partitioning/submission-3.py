class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPallindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(idx, path):
            if idx == len(s):
                res.append(path.copy())
                return

            for end in range(idx, len(s)):
                if isPallindrome(idx, end):
                    path.append(s[idx:end+1])
                    backtrack(end+1, path)
                    path.pop()


        backtrack(0, [])
        return res