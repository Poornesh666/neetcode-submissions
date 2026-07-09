class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0]*len(queries)
        heap = []

        sorted_queries = []

        for i, q in enumerate(queries):
            sorted_queries.append((i,q))

        sorted_queries.sort(key = lambda q:q[1])
        intervals.sort(key = lambda interval:interval[0])

        i = 0
        for idx, q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][0]
                r = intervals[i][1]
                heapq.heappush(heap, (r-l+1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if not heap:
                res[idx] = -1
            else:
                res[idx] = heap[0][0]

        return res 