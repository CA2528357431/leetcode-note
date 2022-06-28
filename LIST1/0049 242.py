class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for x in s:
            if x not in dic1:
                dic1[x] = 1
            else:
                dic1[x] += 1
        for x in t:
            if x not in dic2:
                dic2[x] = 1
            else:
                dic2[x] += 1
        return dic1==dic2