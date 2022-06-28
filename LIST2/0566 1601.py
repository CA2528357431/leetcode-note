class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        total = len(requests)

        def dfs(i, cur, res):
            if i == total:
                for num in res:
                    if num != 0:
                        return 0
                return cur
            into, out = requests[i]
            yes = dfs(i + 1, cur, res)

            res[into] -= 1
            res[out] += 1
            nop = dfs(i + 1, cur + 1, res)

            res[into] += 1
            res[out] -= 1

            return max(yes, nop)

        res = dfs(0, 0, [0] * n)
        return res