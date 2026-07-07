class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for interval in intervals:
            if inserted:
                res.append(interval)
            else:
                if interval[1] < newInterval[0]:
                    res.append(interval)
                elif interval[0] > newInterval[1]:
                    res.append(newInterval)
                    res.append(interval)
                    inserted = True
                else:
                    newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                
            
        if not inserted:
            res.append(newInterval)
            
        return res 
            