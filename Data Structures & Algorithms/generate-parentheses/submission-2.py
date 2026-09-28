class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closeN, temp):
            if openN == closeN == n:
                res.append("".join(temp))
                return

            if openN < n:
                temp.append('(')
                backtrack(openN+1, closeN, temp)
                temp.pop()

            if closeN < openN:
                temp.append(')')
                backtrack(openN, closeN+1, temp)
                temp.pop()

        backtrack(0,0,[])
        return res