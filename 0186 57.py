class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        x, y = newInterval
        judge = False
        for i in range(len(intervals)):
            xx, yy = intervals[i]
            if y < xx:
                if not judge:
                    res.append([x, y])
                    judge = True
                res.append(intervals[i])
                # 对于区间完全在右侧，若new尚未加入则将其加入
                # 再直接加入区间
            elif yy < x:
                res.append(intervals[i])
                # 对于区间完全在左侧，直接加入区间
            else:
                x = min(x, xx)
                y = max(y, yy)
                # 有重合则更新new

        if not judge:
            res.append([x, y])
        # 最后有可能未加入new，则加入
        return res