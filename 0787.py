class Solution:
    def distinctSequences(self, n: int) -> int:

        if n == 1:
            return 6

        dic = {}
        mod = 10 ** 9 + 7

        def do(n, a, b):
            if n == 2:
                if gcd(a, b) == 1 and a != b:
                    return 1
                else:
                    return 0
            if (n, a, b) in dic:
                return dic[(n, a, b)]
            if gcd(a,b)!=1:
                return 0
            res = 0
            for c in range(1, 7):
                if a != b and b != c and c != a and gcd(a, b) == 1 and gcd(b, c) == 1:
                    neo = do(n - 1, b, c)
                    res += neo
                    res = res % mod
            dic[(n, a, b)] = res % mod
            return res

        res = 0
        for i in range(1, 7):
            for j in range(1, 7):
                res += do(n, i, j) % mod
        return res % mod