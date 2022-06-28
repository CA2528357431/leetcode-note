class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        delta = [0] * n
        for i in range(1, n):
            delta[i] = security[i] - security[i - 1]
        inc = [0] * n
        dec = [0] * n
        for i in range(1, n):
            if delta[i] <= 0:
                dec[i] = dec[i - 1] + 1
            else:
                dec[i] = 0
        for i in range(n - 1, 0, -1):
            if delta[i] >= 0:
                inc[i - 1] = inc[i] + 1
            else:
                inc[i - 1] = 0
        res = []

        for i in range(n):
            if inc[i] >= time and dec[i] >= time:
                res.append(i)
        return res