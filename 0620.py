class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        li = [[i, aliceArrows[i] + 1] for i in range(12)]
        resu = 0
        re = []

        def do(i, cur, res, li0):

            if cur < 0:
                return 0
            if i == 12:
                nonlocal resu
                nonlocal re
                if cur > 0:
                    li0[0] += cur
                if res > resu:
                    re = li0
                    resu = res
                return res
            p, a = li[i]

            liy = li0.copy()
            liy[i] = a
            yes = do(i + 1, cur - a, res + p, liy)
            lin = li0.copy()
            no = do(i + 1, cur, res, lin)

            return max(yes, no)

        a = do(0, numArrows, 0, [0] * 12)
        return re