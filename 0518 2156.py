class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashcurue: int) -> str:

        def getcur(c):
            return ord(c) - ord("a") + 1

        t = pow(p, k - 1, m)

        cur = 0
        res = 0

        for i in range(k):
            cur = cur + getcur(s[len(s) - 1 - i]) * pow(p, k - 1 - i, m) % m
            cur = cur % m
        if cur == hashcurue:
            res = len(s) - k

        for i in range(len(s) - 1, k - 1, -1):
            cur = cur - getcur(s[i]) * t % m
            cur = cur % m
            cur = cur * p
            cur = cur % m
            cur = cur + getcur(s[i-k])
            cur = cur % m
            if cur == hashcurue:
                res = i - k
        return s[res:res + k]
