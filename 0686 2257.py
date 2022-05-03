class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(m)]

        for x, y in walls:
            mat[x][y] = -1
        for x, y in guards:
            mat[x][y] = -2
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for x, y in guards:
            for dx, dy in d:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if mat[nx][ny] < 0:
                            break
                        if mat[nx][ny] == 0:
                            mat[nx][ny] = 1
                    else:
                        break
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res += 1
        return res
