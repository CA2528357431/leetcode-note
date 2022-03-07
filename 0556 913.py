class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        dic = {}
        def dfs(m, c, i):
            """
            极大极小博弈，
            老鼠尽量找自己获胜的，其次接受平局
            猫尽量找自己获胜的，其次接受平局

            :param m: 老鼠的位置
            :param c: 猫的位置
            :param i: 回合
            """
            if i > 100:
                return 0
            if not m:
                return -1
            if c == m:
                return 1
            res = (-1) ** i
            if i % 2:
                for nxt in graph[c]:
                    if nxt:
                        neo = 0
                        if (m, nxt, (i + 1)) not in dic:
                            neo = dfs(m, nxt, i + 1)
                        else:
                            neo = dic[(m, nxt, (i + 1))]
                        res = max(res, neo)
                    if res == 1:
                        break
            else:
                for nxt in graph[m]:
                    neo = 0
                    if (nxt, c, (i + 1)) not in dic:
                        neo = dfs(nxt, c, i + 1)
                    else:
                        neo = dic[(nxt, c, (i + 1))]
                    res = min(res, neo)
                    if res == -1:
                        break
            dic[(m, c, i)] = res
            # 记录，防止重复运算
            return res
        return ans if not (ans:=dfs(1, 2, 0)) else (1 if ans == -1 else 2)