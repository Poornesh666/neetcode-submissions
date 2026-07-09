class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []

        for q in queries:
            cur = -1
            for l, r in intervals:
                if l <= q <= r:
                    length = r - l + 1
                    if cur == -1 or length < cur:
                        cur = length
                    
            res.append(cur)

        return res