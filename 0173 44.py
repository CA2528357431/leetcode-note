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
                    if gaint[y-1][x] or gaint[y][x-1]:
                        gaint[y][x]=True
                    # 如果*为空串则无*也匹配，看gaint[y-1][x]
                    # 如果*不为空串则，删除s的最后一个，也一定匹配(最坏也就是*空)。看gaint[y][x-1]

        return gaint[-1][-1]
        '''


        # 滚动优化
        gaint = [False] * (len(s) + 1)
        gaint[0] = True

        for y in range(1, len(p) + 1):
            neo = [False] * (len(s) + 1)
            if p[y - 1] == "*" and gaint[0]:
                neo[0] = True
            else:
                neo[0] = False

            for x in range(1, len(s) + 1):
                if s[x - 1] == p[y - 1] or p[y - 1] == "?":
                    neo[x] = gaint[x - 1]
                elif p[y - 1] == "*":
                    if gaint[x] or neo[x - 1]:
                        neo[x] = True

            gaint = neo
        return gaint[-1]