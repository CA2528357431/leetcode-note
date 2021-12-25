class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0

        def getnext(sma):
            ne = [0] * len(sma)
            cur = 0
            i = 1
            while i < len(sma):
                if sma[cur] == sma[i]:
                    cur += 1
                    ne[i] = cur
                    i += 1
                else:
                    if cur == 0:
                        i += 1
                    else:
                        cur = ne[cur - 1]
            return ne

        ne = getnext(b)
        i = 0
        j = 0

        lim = (len(b) // len(a) + 2) * len(a)
        # 重复次数的最大值为 len(b) // len(a) + 2
        # i的最大值为 次数*len(a)

        while j < len(b):
            if a[i % len(a)] == b[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = ne[j - 1]
            if i == lim:
                return -1
            # 跳出条件

        if i % len(a) == 0:
            i -= 1
        return i // len(a) + 1

    # 本质上是 判断 "b 是否是 a*无穷 的子串"