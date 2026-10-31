class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2, memo = len(word1), len(word2), {}
        def solve(i, j):
            if i == n1:
                return n2 - j

            if j == n2:
                return n1 - i

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                memo[(i,j)] = solve(i+1, j+1)
                return memo[(i,j)]

            if word1[i] != word2[j]:
                memo[(i,j)] = 1 + min(solve(i+1, j+1), solve(i, j+1), solve(i+1, j))
                return memo[(i,j)]

        return solve(0, 0)