class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num = [[0] * n for _ in range(m)]
        c2, c5 = [0] * 1001, [0] * 1001

        for i in range(2, 1001):
            if i % 2 == 0:
                c2[i] = c2[i // 2] + 1
            if i % 5 == 0:
                c5[i] = c5[i // 5] + 1

        two = [[0] * n for _ in range(m)]
        five = [[0] * n for _ in range(m)]
        for i in range(m):
            two[i][0] = c2[grid[i][0]]
            five[i][0] = c5[grid[i][0]]
        for i in range(m):
            for j in range(1, n):
                two[i][j] = two[i][j - 1] + c2[grid[i][j]]
                five[i][j] = five[i][j - 1] + c5[grid[i][j]]

        res = -99999
        for j in range(n):
            cur2 = 0
            cur5 = 0
            for i in range(m):
                add2 = c2[grid[i][j]]
                add5 = c5[grid[i][j]]
                cur2 += add2
                cur5 += add5

                l2 = cur2 - add2 + two[i][j]
                l5 = cur5 - add5 + five[i][j]

                r2 = cur2 + two[i][-1] - two[i][j]
                r5 = cur5 + five[i][-1] - five[i][j]

                res = max(res, min(l2, l5), min(r2, r5))

            cur2 = 0
            cur5 = 0
            for i in range(m - 1, -1, -1):
                add2 = c2[grid[i][j]]
                add5 = c5[grid[i][j]]
                cur2 += add2
                cur5 += add5

                l2 = cur2 - add2 + two[i][j]
                l5 = cur5 - add5 + five[i][j]

                r2 = cur2 + two[i][-1] - two[i][j]
                r5 = cur5 + five[i][-1] - five[i][j]

                res = max(res, min(l2, l5), min(r2, r5))
        return res

