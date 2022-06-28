class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """

        mat = [[-1] * n for _ in range(n)]
        for x in range(n):
            for y in range(n - 1):
                mat[x][preferences[x][y]] = y

        total = 0

        for p1 in range(len(pairs)):

            x, y = pairs[p1]
            judgex = False
            judgey = False
            for p2 in range(len(pairs)):

                if p1 != p2:
                    u, v = pairs[p2]
                    if ((mat[x][u] < mat[x][y] and mat[u][x] < mat[u][v]) or (
                            mat[x][v] < mat[x][y] and mat[v][x] < mat[v][u])) and not judgex:
                        total += 1
                        judgex = True
                    if ((mat[y][u] < mat[y][x] and mat[u][y] < mat[u][v]) or (
                            mat[y][v] < mat[y][x] and mat[v][y] < mat[v][u])) and not judgey:
                        total += 1
                        judgey = True

        return total


sol = Solution()
sol.unhappyFriends(4,[[1,2,3],[3,2,0],[3,1,0],[1,2,0]],[[0,1],[2,3]])