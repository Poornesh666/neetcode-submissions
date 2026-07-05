class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)          
        self.arr.sort()

    def findMedian(self) -> float:
        if len(self.arr) % 2 != 0:
            mid = len(self.arr)//2
            return float(self.arr[mid])
        else:
            mid = len(self.arr)//2
            median = (self.arr[mid] + self.arr[mid-1]) / 2
            return median