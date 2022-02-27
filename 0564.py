class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires.sort(key=lambda x: (x[0], x[1]))

        curr = tires[0][1]
        ntires = [tires[0]]

        for i in range(1, len(tires)):
            f, r = tires[i]
            if f == tires[i - 1][0]:
                continue
            if r >= curr:
                continue

            curr = r
            ntires.append([f, r])

        single = [9999999999999] * (numLaps + 1)
        single[0] = 0
        # single[i]只用一个轮胎走i圈的最短时间

        for f, r in ntires:
            x = 1
            t = f
            s = 0
            while t < changeTime + f:
                s += t
                single[x] = min(single[x], s)
                x += 1
                t *= r

        res = [9999999999999] * (numLaps + 1)
        res[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(1, i + 1):
                res[i] = min(res[i], res[i - j] + single[j] + changeTime)

        return res[-1] - changeTime
        # 第一个轮胎不需要changeTime
