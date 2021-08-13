class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        par = -1
        for l in t:
            if l == s[par + 1]:
                par += 1
            if par == (len(s) - 1):
                return True
        return False