class Solution:
    def minimumWhiteTiles(self, floor: str, n: int, carpetLen: int) -> int:
        m = len(floor)
        f = [[0] * m for _ in range(n + 1)]
        f[0][0] = int(floor[0])
        for i in range(1, m):
            f[0][i] = f[0][i - 1] + int(floor[i])
        for i in range(1, n + 1):
            # j < carpetLen 的 f[i][j] 均为 0
            for j in range(carpetLen, m):
                f[i][j] = min(f[i][j - 1] + int(floor[j]), f[i - 1][j - carpetLen])
        return f[n][m - 1]
    # https://leetcode-cn.com/problems/minimum-white-tiles-after-covering-with-carpets/solution/by-endlesscheng-pa3v/



