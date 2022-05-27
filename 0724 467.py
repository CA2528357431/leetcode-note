class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def con(a, b):
            return (ord(b) - ord(a) + 26) % 26 == 1

        dic = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for c in alpha:
            dic[c] = 0
        dic[p[0]] = 1

        n = len(p)
        cur = 1
        for i in range(1, n):

            if con(p[i - 1], p[i]):
                cur += 1
            else:
                cur = 1
            dic[p[i]] = max(dic[p[i]], cur)

        s = 0
        for c in alpha:
            s += dic[c]
        return s

        s = 0
        for c in alpha:
            s += dic[c]
        return s