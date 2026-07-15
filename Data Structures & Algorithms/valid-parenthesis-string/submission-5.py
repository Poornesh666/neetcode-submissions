class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == '(': low, high = low+1, high+1
            elif c == ')': low, high = low-1, high-1
            else: low, high = low-1, high+1

            if high < 0: return False
            low = max(low, 0)

        return low == 0