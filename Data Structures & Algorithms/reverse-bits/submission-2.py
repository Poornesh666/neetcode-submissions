class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            last_bit = n&1
            res |= last_bit
            n >>= 1

        return res