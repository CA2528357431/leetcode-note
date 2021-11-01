class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events1 = events.copy()
        events1.sort(key=lambda x: x[0])
        events2 = events.copy()
        events2.sort(key=lambda x: x[1])

        i = 0
        big = 0
        res = 0

        for s, e, v in events1:
            while events2[i][1] < s:
                big = max(big, events2[i][2])
                # 在当前事件开始前的事件的最大val
                i += 1
            res = max(res, big + v)
            # 更新val

        return res