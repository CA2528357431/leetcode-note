class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        res = [-1 for i in range(n)]
        li = [[] for i in range(n)]

        for r, p in richer:
            li[p].append(r)

        def dfs(p):
            res[p] = p
            for r in li[p]:
                if res[r] < 0:
                    dfs(r)
                    # 如果每求过就dfs
                if quiet[res[r]] < quiet[res[p]]:
                    res[p] = res[r]
            # 比p富的安静者，一定是他自己或者他相邻富有的人的安静者
            # 递归时保存数据

        for i in range(n):
            if res[i] < 0:
                dfs(i)
        return res