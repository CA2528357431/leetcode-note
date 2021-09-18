class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in used:
                dic[s[i]] = t[i]
                used.add(t[i])
            elif s[i] not in dic and t[i] in used:
                return False
            elif s[i] in dic and t[i] not in used:
                return False
            else:
                if dic[s[i]] != t[i]:
                    return False

        return True