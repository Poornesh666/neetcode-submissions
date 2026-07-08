"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        canAttend = True

        i = 0
        j = 1

        while j < len(intervals):
            curr = intervals[i]
            nextt = intervals[j]

            if nextt.start < curr.end:
                canAttend = False
                break

            i += 1
            j += 1

        return canAttend

             