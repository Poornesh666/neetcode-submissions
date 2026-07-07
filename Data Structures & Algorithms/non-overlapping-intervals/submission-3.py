class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        res = []
        intervals.sort()

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if interval[0] < res[-1][1]:
                    res[-1] = [res[-1][0], min(res[-1][1], interval[1])]
                    count += 1
                else:
                    res.append(interval)

        return len(intervals) - len(res)
