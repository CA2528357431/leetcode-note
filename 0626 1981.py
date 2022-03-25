class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])
        for x in mat:
            x.sort()
        big = 0
        for i in range(m):
            big += mat[i][-1]
        if big <= target:
            return target - big

        small = 0
        for i in range(m):
            small += mat[i][0]
        if small >= target:
            return small - target

        # 为什么用2*target
        # 可达最小值小于target大于0，决定了最终结果小于target
        # 因此遍历的t无需考虑大于 2*t-可达最小值 的数字

        dp = [[False] * (target * 2 + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for l in range(1, m + 1):
            for t in range(1, target * 2 + 1):
                for x in mat[l - 1]:
                    if t - x < 0:
                        break
                    if dp[l - 1][t - x]:
                        dp[l][t] = True
                        break
        low = 999999
        for t in range(target, -1, -1):
            if dp[-1][t]:
                low = target - t
                break
        up = 999999
        for t in range(target, target * 2 + 1):
            if dp[-1][t]:
                up = t - target
                break

        return min(low, up)