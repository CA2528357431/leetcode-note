class Solution:
    def appealSum(self, s: str) -> int:
        se = set()
        n = len(s)
        res = 0
        cur = 0
        dic = {}
        for i in range(n):
            c = s[i]
            if c not in se:
                neo = cur + 1 + i
                dic[c] = i
            else:
                neo = cur + 1 + (i - (dic[c] + 1))
                dic[c] = i
            cur = neo
            res += cur
            se.add(s[i])

        return res