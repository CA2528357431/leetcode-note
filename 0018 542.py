import collections


class Solution:
    def updateMatrix(self, mat):

        # 多源BFS

        '''
        res = [[0] * len(mat[0]) for _ in range(len(mat))]

        li = []
        used = set()
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    li.append((x, y))
                    used.add((x, y))

        i = 1
        while li:
            neo = []
            for x, y in li:
                for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= xx < len(mat) and 0 <= yy < len(mat[0]):
                        if (xx, yy) not in used:
                            res[xx][yy] = i
                            neo.append((xx, yy))
                            used.add((xx, yy))
            li = neo
            i += 1

        return res
        '''



        # 这个是重点
        # 动态规划

        '''
        res = [[999999] * len(mat[0]) for _ in range(len(mat))]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    res[x][y] = 0

        # 由左上开始
        
        # 如果在找0的过程中只能向左、向上
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if x - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x - 1][y] + 1)
                if y - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x][y - 1] + 1)

        # 从右下开始
        for x in range(0,len(mat))[::-1]:
            for y in range(len(mat[0]))[::-1]:
                if x + 1 < len(mat):
                    res[x][y] = min(res[x][y], res[x + 1][y] + 1)
                if y + 1 < len(mat[0]):
                    res[x][y] = min(res[x][y], res[x][y + 1] + 1)

        # 由左下开始
        for x in range(len(mat))[::-1]:
            for y in range(len(mat[0])):
                if x - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x - 1][y] + 1)
                if y + 1 < len(mat):
                    res[x][y] = min(res[x][y], res[x][y + 1] + 1)

        # 从右上开始
        for x in range(0, len(mat)):
            for y in range(len(mat[0]))[::-1]:
                if x + 1 < len(mat):
                    res[x][y] = min(res[x][y], res[x + 1][y] + 1)
                if y - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x][y - 1] + 1)

        return res
        '''

        # 动态规划--优化
        # 事实上，只需要从两个对角开始

        res = [[999999] * len(mat[0]) for _ in range(len(mat))]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    res[x][y] = 0

        # 由左上开始
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if x - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x - 1][y] + 1)
                if y - 1 >= 0:
                    res[x][y] = min(res[x][y], res[x][y - 1] + 1)

        # 从右下开始
        for x in range(0, len(mat))[::-1]:
            for y in range(len(mat[0]))[::-1]:
                if x + 1 < len(mat):
                    res[x][y] = min(res[x][y], res[x + 1][y] + 1)
                if y + 1 < len(mat[0]):
                    res[x][y] = min(res[x][y], res[x][y + 1] + 1)








