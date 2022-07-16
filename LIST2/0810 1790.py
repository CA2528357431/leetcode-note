class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        ch = -1
        for i in range(n):
            if s1[i] != s2[i]:
                if ch == -1:
                    ch = i
                elif ch == n:
                    return False

                else:
                    if s1[i] == s2[ch] and s1[ch] == s2[i]:
                        ch = n
                    else:
                        return False
        if ch == -1 or ch == n:
            return True
        return False