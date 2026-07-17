class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            res.append(self.count(num))

        return res

    def count(self, n: int):
        count = 0
        while n > 0:
            count += n&1
            n >>= 1

        return count