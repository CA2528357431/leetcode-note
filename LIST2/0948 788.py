class Solution:
    def rotatedDigits(self, n: int) -> int:
        yes = {}
        same = {"0", "1", "8"}
        yes = {"2", "5", "6", "9"}

        res = 0

        def do(cur, judge):
            nonlocal res
            for i in same:
                neo = cur + i

                if int(neo) <= n:
                    if judge:
                        res += 1
                        do(neo, judge)
                    else:
                        do(neo, judge)
            for i in yes:
                neo = cur + i

                if int(neo) <= n:
                    res += 1
                    do(neo, True)

        for x in same:
            if x == "0":
                continue
            do(x, False)
        for x in yes:
            do(x, True)
            if int(x) <= n:
                res += 1

        return res


