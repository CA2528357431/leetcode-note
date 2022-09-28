class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        dic = {}
        n = len(s)
        for i in range(n):
            c = s[i]
            if c in dic:
                res = max(i - dic[c] - 1, res)
            else:

                dic[c] = i
        return res

