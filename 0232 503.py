class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 编辑距离
        '''
        mat = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for x in range(len(word1) + 1):
            mat[0][x] = x
        for x in range(len(word2) + 1):
            mat[x][0] = x

        for x in range(1, len(word2) + 1):
            for y in range(1, len(word1) + 1):
                change = mat[x - 1][y - 1]
                if word2[x - 1] != word1[y - 1]:
                    change += 2
                a = mat[x][y - 1] + 1
                b = mat[x - 1][y] + 1

                mat[x][y] = min(a, b, change)
        return mat[-1][-1]
        '''

        # 编辑距离 滚动优化
        '''
        mat = [x for x in range(len(word1) + 1)]

        for y in range(1, len(word2) + 1):

            la = mat
            mat = [y for _ in range(len(word1) + 1)]

            for x in range(1, len(word1) + 1):
                c = la[x - 1]
                if word1[x - 1] != word2[y - 1]:
                    c += 2
                a = mat[x - 1] + 1
                b = la[x] + 1
                mat[x] = min(a, b, c)

        return mat[-1]
        '''

        # 最长公共串
        '''
        mat = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for x in range(1, len(word2) + 1):
            for y in range(1, len(word1) + 1):
                if word2[x - 1] == word1[y - 1]:
                    mat[x][y] = mat[x - 1][y - 1] + 1
                else:
                    mat[x][y] = max(mat[x - 1][y], mat[x][y - 1])
        longest = mat[-1][-1]

        return len(word1) + len(word2) - longest * 2
        '''

        # 最长公共串 滚动优化
        mat = [0 for _ in range(len(word1) + 1)]

        for y in range(1, len(word2) + 1):

            la = mat
            mat = [0 for _ in range(len(word1) + 1)]

            for x in range(1, len(word1) + 1):
                if word1[x - 1] == word2[y - 1]:
                    mat[x] = la[x - 1] + 1
                else:
                    mat[x] = max(mat[x - 1], la[x])
        longest = mat[-1]

        return len(word1) + len(word2) - longest * 2

