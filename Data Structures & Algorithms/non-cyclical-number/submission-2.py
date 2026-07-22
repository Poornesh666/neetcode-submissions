class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.squareSum(n)

        while slow != fast:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))

        return slow == 1        

    def squareSum(self, n):
        res = 0
        while n!=0:
            digit = n%10
            res += digit*digit
            n //= 10

        return res