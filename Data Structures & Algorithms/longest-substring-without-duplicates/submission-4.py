class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, i, max_len = set(), 0, 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            max_len = max(max_len, j-i+1)


        return max_len