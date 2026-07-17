class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            bit = n & 1
            ans <<= 1 
            ans |= bit
            n >>= 1

        return ans