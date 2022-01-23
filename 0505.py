class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        judge = [False] * n

        def find(cur, i):
            if i == n:
                deal(cur)
                return
            find(cur, i + 1)

            cur[i] = True
            find(cur, i + 1)
            cur[i] = False

        def deal(li):
            cur = set()
            for j in range(n):

                judge = li[j]
                if judge:
                    for c in cur:
                        if statements[c][j] == 0:
                            return
                        if statements[j][c] == 0:
                            return
                    cur.add(j)
            for i in range(n):
                for j in range(n):
                    if i in cur and j not in cur and statements[i][j] == 1:
                        return
            nonlocal res
            res = max(res, len(cur))
            return

        find(judge, 0)
        return res