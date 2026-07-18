class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            last = x % 10
            rev = rev*10 + last
            x //= 10

        if -2**31 <= rev <= 2**31-1:
            return -1 * rev if sign == -1 else rev
        return 0