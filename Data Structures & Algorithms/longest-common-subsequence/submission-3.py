from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def backtrack(idx1, idx2, count):
            if idx1 == len(text1) or idx2 == len(text2):
                return count
            
            if text1[idx1] == text2[idx2]:
                count += 1
                return backtrack(idx1+1, idx2+1, count)
            else:
                return max(backtrack(idx1+1, idx2, count), backtrack(idx1, idx2+1, count))

        return backtrack(0, 0, 0)