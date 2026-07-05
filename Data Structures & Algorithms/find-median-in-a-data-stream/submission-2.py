class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []  

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return 

        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            move = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, move)

        if len(self.min_heap) > len(self.max_heap):
            move = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, move)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            mid = (-self.max_heap[0] + self.min_heap[0]) / 2
            return mid
