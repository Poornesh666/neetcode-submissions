class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x: float, n:int) -> float:
            if n == 0: return 1
            half = power(x*x, n//2)
            return half if n%2==0 else x*half
        
        res = power(x, abs(n))
        return res if n>=0 else 1/res