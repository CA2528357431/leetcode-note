class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60:
            return 0

        def deal(string):
            hs, ms = string.split(":")
            h = int(hs)
            m = int(ms)
            return h * 60 + m

        li = [deal(x) for x in timePoints]
        li.sort()

        res = li[0] + 24 * 60 - li[-1]
        for i in range(len(li) - 1):
            res = min(res, li[i + 1] - li[i])
        return res

    # 最小差一定出现于大小相邻的两个之间