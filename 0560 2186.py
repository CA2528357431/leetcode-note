class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def getdic(word):
            dic = {}
            for x in word:
                if x not in dic:
                    dic[x] = 0
                dic[x] += 1
            return dic

        dic1 = getdic(s)
        dic2 = getdic(t)

        li = set(dic1.keys()) | set(dic2.keys())

        res = 0

        for c in li:
            res += abs(dic1.get(c, 0) - dic2.get(c, 0))
        return res
