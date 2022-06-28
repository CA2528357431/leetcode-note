class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        ln = 1
        lx = x

        cn = 1
        cx = x
        while cn + cn < n:
            ln = cn
            lx = cx

            cn = cn + cn
            cx = cx * cx
        # 用乘方来快速逼近

        if cn == n:
            return cx

        neo = self.myPow(x, n - ln)
        return lx * neo