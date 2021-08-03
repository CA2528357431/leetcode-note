class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:

            la = 0
            cur = 1
            p = 1
            while p < n:
                la, cur = cur, la + cur
                p += 1
        return cur