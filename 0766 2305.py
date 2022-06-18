class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        kid = [0] * k
        n = len(cookies)
        res = sum(cookies)

        def do(i):
            nonlocal res
            if i == n:
                res = min(res, max(kid))
                return
            if max(kid) >= res:
                return
            for j in range(k):
                kid[j] += cookies[i]
                do(i + 1)
                kid[j] -= cookies[i]

        do(0)
        return res