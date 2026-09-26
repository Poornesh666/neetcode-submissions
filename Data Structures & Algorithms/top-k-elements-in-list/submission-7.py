class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
    
        max_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, num))

        res = []
        for i in range(k):
            freq, num = heapq.heappop(max_heap)
            res.append(num)

        return res
        