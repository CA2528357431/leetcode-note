class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        re = 1
        res = [0] * (n + 1)
        res[1] = 1
        for x in range(2, n + 1):
            if x % 2 == 0:
                res[x] = res[x // 2]
                re = max(res[x], re)
            else:
                res[x] = res[x // 2] + res[x // 2 + 1]
                re = max(res[x], re)
        return re
