class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        mod = 10 ** 9 + 7

        def judge(num):
            upper = int(num ** 0.5)
            for i in range(2, upper + 1):
                if num % i == 0:
                    return False
            return True

        a = 0
        for i in range(2, n + 1):
            if judge(i):
                a += 1
        b = n - a
        res = 1
        for i in range(1, a + 1):
            res *= i
            res %= mod
        for i in range(1, b + 1):
            res *= i
            res %= mod
        res %= mod
        return res