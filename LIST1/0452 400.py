class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        mult = 9
        while n > i * mult:
            n -= (i * mult)
            mult *= 10
            i += 1
        start = 10 ** (i - 1) - 1
        nums = n // i
        cur = nums + start
        res = n % i
        if res == 0:
            return cur % 10
        else:
            cur += 1

            for _ in range(i - res):
                cur //= 10
            return cur % 10