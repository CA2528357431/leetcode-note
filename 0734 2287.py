class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        def getdic(w):
            dic = {}
            for c in w:
                if c not in dic:
                    dic[c] = 0
                dic[c] += 1
            return dic
        dic1 = getdic(s)
        dic2 = getdic(target)
        res = len(s)
        for c in dic2:
            if c not in dic1:
                return 0
            res = min(res,dic1[c]//dic2[c])
        return res