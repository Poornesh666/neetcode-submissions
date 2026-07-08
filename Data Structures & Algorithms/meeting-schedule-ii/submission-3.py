    """
    Definition of Interval:
    class Interval(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
    """

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        if len(intervals) == 1:
            return 1 
            
        intervals.sort(key=lambda interval:interval.start)
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)


        for i in range(1, len(intervals)): 
            curr = intervals[i]
            if min_heap[0] <= curr.start:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, curr.end)
            else:
                heapq.heappush(min_heap, curr.end)

        return len(min_heap)
                              

