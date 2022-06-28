class Solution:
    def sumScores(self, s: str) -> int:

        # 扩展kmp算法
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        z[0] = n
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                    # 更新z[i]
            # 更新 l r
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return sum(z)