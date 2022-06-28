class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        start,end = intervals[0]
        for s,e in intervals:
            if s<=end:
                end = max(e,end)
            else:
                res.append([start,end])
                start,end = s,e
        res.append([start, end])
        return res