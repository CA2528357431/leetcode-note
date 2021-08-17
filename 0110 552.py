class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        if n == 2:
            return 8

        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 2
        f[2] = 4
        f[3] = 7



        for x in range(4, n + 1):
            f[x] = (f[x - 1] * 2 - f[x - 4])# %1000000009
        res = f[-1]
        for x in range(n):
            res += f[x] * f[n - x - 1]
        return res  # %1000000009
        # https://leetcode-cn.com/problems/student-attendance-record-ii/solution/xue-sheng-chu-qin-ji-lu-ii-by-leetcode/