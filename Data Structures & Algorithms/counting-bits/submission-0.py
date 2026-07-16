class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i, num in enumerate(range(n+1)):
            binary = self.decToBin(num)
            res[i] = self.count(binary)
        return res

    def decToBin(self, n: int) -> str:
        if n == 0: return "0"
        res = ""
        while n > 0:
            digit = n % 2
            res = str(digit) + res
            n //= 2

        return res

    def count(self, binary: str) -> int:
        res = 0
        for ch in binary:
            if ch == "1": res += 1

        return res