class Solution:
    def countHousePlacements(self, n: int) -> int:
        dic = {}
        mod = 10 ** 9 + 7

        def do(i, j):
            if i == 1:
                return 1
            if i == 2:
                if j == True:
                    return 1
                else:
                    return 2
            if (i, j) in dic:
                return dic[(i, j)]

            res = -1
            if j == True:
                res = do(i - 1, False)
            else:
                res = do(i - 1, False) + do(i - 1, True)
            dic[(i, j)] = res % mod
            return res % mod

        return ((do(n, True) + do(n, False)) ** 2) % mod