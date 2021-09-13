class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        x = intervals[0][0]
        y = intervals[0][1]
        for xx, yy in intervals:
            if xx > y:
                res.append([x, y])
                x = xx
                y = yy
            else:
                if yy > y:
                    y = yy
        res.append([x, y])
        return res