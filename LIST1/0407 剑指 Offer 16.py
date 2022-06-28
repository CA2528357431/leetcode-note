class Solution:
    def myPow(self, x: float, n: int) -> float:
        def get(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            if n < 0:
                x = 1 / x
                n = -n

            last = x
            lasttimes = 1
            cur = x
            times = 1
            while times < n:
                last = cur
                lasttimes = times

                cur = cur * cur
                times = times * 2

            if times == n:
                return cur
            else:
                rest = get(x, n - lasttimes)
                return last * rest

        return get(x, n)