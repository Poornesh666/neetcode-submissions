class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1

        if s == "":
            return 0
        if len(s) == 1:
            return 1

        seen = set()
        i = 0
        j = 1
        max_len = 0

        while j < len(s):
            seen.add(s[i])
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j += 1
            max_len = max(max_len, j - i)


        return max_len