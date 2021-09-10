class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        gaint = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        gaint[0][0] = True

        for x in range(1, len(p) + 1):
            if gaint[x - 1][0] and p[x - 1] == "*":
                gaint[x][0] = True
            else:
                break

        for y in range(1, len(p) + 1):
            for x in range(1, len(s) + 1):
                if s[x - 1] == p[y - 1] or p[y - 1] == "?":
                    gaint[y][x] = gaint[y - 1][x - 1]
                elif p[y - 1] == "*":
                    for xx in range(x + 1):
                        if gaint[y - 1][xx]:
                            gaint[y][x] = True
                            break

        return gaint[-1][-1]
        '''