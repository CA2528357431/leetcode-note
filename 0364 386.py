class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(cur):
            res.append(cur)
            for x in range(10):
                now = cur*10+x
                if now<=n:
                    dfs(now)
                else:
                    break
        for x in range(1,min(n+1,10)):
            dfs(x)
        return res

    # 这也能dfs