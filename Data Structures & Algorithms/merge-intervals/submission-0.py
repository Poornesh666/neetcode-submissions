class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        i = 0
        while i < len(intervals):
            if not res:
                res.append((intervals[i]))  
            else:
                curr = res[-1]
                nxt = intervals[i]
                if nxt[0] <= curr[1]:
                    res[-1] = [curr[0], max(curr[1], nxt[1])]
                else:
                    res.append(intervals[i])
            

            i += 1

        return res 
