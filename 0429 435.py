class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        end = intervals[0][1]
        num = 1
        for i in range(1,n):
            s,e = intervals[i]
            if s>=end:
                num+=1
                end = e
            # 为了获取最长序列
            # 对于一组相交的区间，必须取end最小的一个
        return n-num