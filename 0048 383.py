class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {}
        dic2 = {}
        for x in ransomNote:
            if x not in dic1:
                dic1[x] = 1
            else:
                dic1[x] += 1
        for x in magazine:
            if x not in dic2:
                dic2[x] = 1
            else:
                dic2[x] += 1
        for x in dic1:
            if x not in dic2 or dic2[x] < dic1[x]:
                return False

        return True
