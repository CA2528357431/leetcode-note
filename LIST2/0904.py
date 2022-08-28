class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowConditions = {tuple(x) for x in rowConditions}
        colConditions = {tuple(x) for x in colConditions}

        def getmap(li):
            dic = [[] for _ in range(k + 1)]
            cnt = [0] * (k + 1)
            for f, t in li:
                dic[f].append(t)
                cnt[t] += 1
            return dic, cnt

        def sort(dic, cnt):
            li = []
            for _ in range(k):
                for i in range(1, k + 1):
                    if cnt[i] == 0:
                        li.append(i)
                        cnt[i] = -1
                        for x in dic[i]:
                            cnt[x] -= 1
                        break
            return li

        def do(li):
            lmap, lcnt = getmap(li)
            sl = sort(lmap, lcnt)
            if len(sl) != k:
                return []
            res = [-1] * (k + 1)
            for i in range(k):
                neo = sl[i]
                res[neo] = i
            return res

        row = do(rowConditions)
        col = do(colConditions)
        if not row or not col:
            return []
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            x = row[i]
            y = col[i]
            res[x][y] = i
        return res

