class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(x, y):
            if p[y] == "." or p[y] == s[x]:
                return True
            else:
                return False

        res = [[False] * (1 + len(p)) for _ in range(len(s) + 1)]
        res[0][0] = True

        for x in range(1,len(s)+1):
            if p[x-1]=="*":
                res[x][0] = res[x-2][0]

        for x in range(1,len(s) + 1):
            for y in range(1, len(p) + 1):
                if p[y - 1] == "*":
                    if res[x][y - 2]:
                        res[x][y] = True
                    if match(x - 1, y - 2):
                        if res[x - 1][y]:
                            res[x][y] = True
                else:

                    if match(x - 1, y - 1):
                        res[x][y] = res[x - 1][y - 1]
        return res[-1][-1]