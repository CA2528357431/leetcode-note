class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        mat = [0] * forget
        mat[0] = 1
        s = 0
        for _ in range(n - 1):
            s = s - mat[-1]
            for i in range(forget - 1, 0, -1):
                mat[i] = mat[i - 1] % mod
            s = s + mat[delay]
            mat[0] = s

        return sum(mat) % mod
