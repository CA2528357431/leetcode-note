class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        res = len(s1)
        n = len(s1)

        li1 = list(s1)
        li2 = list(s2)

        def do(i, cur):

            if i == n:
                nonlocal res
                res = min(res, cur)
                return
            if cur >= res:
                return

            sth = 0
            for ii in range(i, n):
                if li1[ii] != li2[ii]:
                    sth += 1
            neo = sth // 2 + sth % 2
            if cur + neo >= res:
                return

            if li1[i] == li2[i]:
                do(i + 1, cur)
            else:
                for ii in range(i + 1, n):
                    if li2[ii] != li1[i]:
                        continue
                    li2[i], li2[ii] = li2[ii], li2[i]

                    do(i + 1, cur + 1)

                    li2[i], li2[ii] = li2[ii], li2[i]

        do(0, 0)

        return res