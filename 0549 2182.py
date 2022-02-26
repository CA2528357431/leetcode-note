class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        def get(c):
            return ord(c) - ord("a")

        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        li = list(dic.keys())
        li.sort(key=lambda x: -get(x))

        if len(li) == 1:
            return s[0] * min(repeatLimit, len(s))

        res = []
        cur = 0
        i = 0
        j = 1
        while i < len(li):

            if cur == repeatLimit:
                if j == len(li):
                    break
                elif dic[li[i]] == 0:
                    cur = 0
                    i += 1
                    j += 1
                else:
                    cur = 0
                    ch = li[j]
                    res.append(ch)
                    dic[ch] -= 1
                    if dic[ch] == 0:
                        j += 1
            else:
                ch = li[i]
                if dic[ch] == 0:
                    cur = 0
                    while i < len(li) and dic[li[i]] == 0:
                        i += 1
                    if i == len(li):
                        break
                    j = i + 1
                else:
                    res.append(ch)
                    cur += 1
                    dic[ch] -= 1

        return "".join(res)