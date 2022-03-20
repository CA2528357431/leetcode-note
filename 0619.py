class Solution:
    def countCollisions(self, directions: str) -> int:
        li = directions.split("S")

        def dol(s):
            i = 0
            while i < len(s) and s[i] == "L":
                i += 1
            return i

        def dor(s):
            i = len(s) - 1
            while i >= 0 and s[i] == "R":
                i -= 1
            return len(s) - 1 - i

        def dom(s, ls, rs):
            if rs > 0:
                s = s[ls:-rs]
            else:
                s = s[ls:]
            if not s:
                return 0
            lis = s.split("RL")
            num = (len(lis) - 1) * 2
            for liss in lis:
                num += len(liss)
            return num

        if len(li) == 1:
            r0 = dor(li[0])
            l0 = dol(li[0])
            return dom(li[0], l0, r0)

        r0 = dor(li[0])
        l0 = dol(li[0])
        m0 = dom(li[0], l0, r0)

        ln = dol(li[-1])
        rn = dor(li[-1])
        mn = dom(li[-1], ln, rn)
        res = r0 + ln + m0 + mn

        for i in range(1, len(li) - 1):
            l = dol(li[i])
            r = dor(li[i])

            m = dom(li[i], l, r)
            res += l + r + m
        return res
