class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d1 = defaultdict()
        # d2 = defaultdict()

        # for c in s:
        #     d1[c] += 1

        # for c in t:
        #     d2[c] += 1

        return sorted(s) == sorted(t)