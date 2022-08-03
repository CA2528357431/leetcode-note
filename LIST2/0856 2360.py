class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        res = [-1] * n
        used = [False] * n

        def do(i, cur):

            if i < 0:
                return
            if used[i]:
                for x in cur:
                    used[x] = True
                    return

            if i in cur and cur[i] == 2:
                l = 0
                for x in cur:
                    if cur[x] == 2:
                        l += 1
                for x in cur:
                    if cur[x] == 2:
                        res[x] = l
                    used[x] = True
                return

            cur[i] = cur.get(i, 0) + 1
            do(edges[i], cur)

        for i in range(n):
            if not used[i]:
                do(i, {})

        return max(res)
