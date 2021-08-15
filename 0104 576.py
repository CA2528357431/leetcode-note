class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):


        '''
        mat = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)]
        for i in range(1,maxMove+1):
            for x in range(m):
                for y in range(n):
                    for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if (xx >= m or xx < 0) or (yy >= n or yy < 0):
                            mat[i][x][y]+=1
                        else:
                            mat[i][x][y]+=mat[i-1][xx][yy]
        return mat[-1][startRow][startColumn]%(1000000007)
        '''

        # 优化
        cur = [[0] * n for _ in range(m)]
        for _ in range(maxMove):
            neo = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if (xx >= m or xx < 0) or (yy >= n or yy < 0):
                            neo[x][y] += 1

                        else:
                            neo[x][y] += cur[xx][yy]
            cur = neo

        return cur



sol = Solution()
sol.findPaths(2, 2, 2, 0, 0)