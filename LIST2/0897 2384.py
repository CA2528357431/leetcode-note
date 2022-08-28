class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic = {}
        mid = ""
        pre = []
        for c in num:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        ks = list(dic.keys())
        ks.sort(reverse=True)

        if len(ks) == 1 and ks[0] == "0":
            return "0"

        for c in ks:
            if not pre and c == "0":
                continue
            if dic[c] % 2 == 0:
                if dic[c] // 2 > 0:
                    pre.append(c * (dic[c] // 2))
            else:
                if dic[c] // 2 > 0:
                    pre.append(c * (dic[c] // 2))
                if not mid:
                    mid = c
        pres = "".join(pre)
        res = pres + mid + pres[::-1]
        return res
