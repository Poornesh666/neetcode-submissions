class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append("".join(path))
                return

            if openN < n:
                path.append("(")
                backtrack(openN+1, closedN, path)
                path.pop()

            if closedN < openN:
                path.append(")")
                backtrack(openN, closedN+1, path)
                path.pop()

        backtrack(0, 0, [])
        return res