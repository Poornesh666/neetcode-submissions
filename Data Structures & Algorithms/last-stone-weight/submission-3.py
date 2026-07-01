class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            diff = heapq.heappop(stones) - heapq.heappop(stones)

            if diff:
                heapq.heappush(stones, diff)

        return -heapq.heappop(stones) if stones else 0
        