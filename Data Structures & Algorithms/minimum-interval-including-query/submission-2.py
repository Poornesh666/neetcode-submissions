class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        res = [0]*len(queries)
        intervals.sort(key = lambda interval:interval[0])
        queries_sorted = []

        for i, q in enumerate(queries):
            queries_sorted.append((q, i))

        queries_sorted.sort(key = lambda q:q[0])

        i = 0
        for q, idx in queries_sorted:
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][0]
                r = intervals[i][1]
                length = r - l + 1
                heapq.heappush(heap,(length, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if not heap:
                res[idx] = -1
            else:
                res[idx] = heap[0][0]

        return res