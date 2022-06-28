class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = {}

        n = len(values)
        for i in range(n):
            b, s = equations[i]

            if s in dic:
                dic[s][b] = values[i]
            else:
                dic[s] = {}
                dic[s][b] = values[i]

            if b in dic:
                dic[b][s] = 1 / values[i]
            else:
                dic[b] = {}
                dic[b][s] = 1 / values[i]
        res = []
        for query in queries:
            a, b = query
            if b not in dic or a not in dic:
                res.append(-1)
                continue
            if a == b:
                res.append(1)
                continue
            used = set()
            cur = {b: 1}
            num = 1
            find = False
            while cur:
                neo = {}
                for x in cur.keys():
                    for k in dic[x].keys():
                        if k in used:
                            continue
                        elif k == a:
                            res.append(dic[x][k] * cur[x])
                            find = True
                            break
                        else:
                            used.add(k)
                            neo[k] = dic[x][k] * cur[x]
                    if find:
                        break
                if find:
                    break
                cur = neo
            if not find:
                res.append(-1)
        return res


        # 构建图 广度优先