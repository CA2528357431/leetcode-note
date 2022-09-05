class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dis = endPos - startPos
        if abs(dis) > k:
            return 0

        if (k - abs(dis)) % 2 == 1:
            return 0

        pos = (k + dis) // 2

        # print(pos)
        def do(a, b):
            mod = 10 ** 9 + 7
            res = 1
            for i in range(b):
                res *= (a - i)
                res = res
            for i in range(b):
                res //= (i + 1)
            return res % mod

        return do(k, pos)



