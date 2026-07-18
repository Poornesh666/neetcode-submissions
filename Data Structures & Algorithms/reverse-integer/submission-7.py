class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            last = x % 10
            if rev > (2**31 - 1) // 10 or \
               (rev == (2**31 - 1) // 10 and last > 7):
                return 0
            rev = rev*10 + last
            x //= 10

        rev *= sign
        if -2**31 <= rev <= 2**31-1:
            return rev
        return 0