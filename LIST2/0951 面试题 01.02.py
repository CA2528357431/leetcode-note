class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        def get(w):
            dic = {}
            for c in w:
                if c not in dic:
                    dic[c] = 0
                dic[c] += 1
            return dic

        if len(s1) != len(s2):
            return False

        dic1 = get(s1)
        dic2 = get(s2)
        if len(dic1) != len(dic2):
            return False

        for c in dic1:
            if c not in dic2 or dic1[c] != dic2[c]:
                return False
        return True



