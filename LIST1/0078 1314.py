class Solution:
    def matrixBlockSum(self, mat, k):

        # 暴力法
        # 因重复计算超时

        '''
        res = [[0]*len(mat[0]) for _ in range(len(mat))]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                left = max(y-k,0)
                right = min(y+k,len(mat[0])-1)
                top = max(x-k,0)
                bottom = min(x+k,len(mat)-1)
                for m in range(top,bottom+1):
                    for n in range(left, right+1):
                        res[x][y]+=mat[m][n]
        return res
        '''

        # 提前计算，一次计算多次复用

        cal = [[0] * len(mat[0]) for _ in range(len(mat))]
        for x in range(len(mat)):
            ans = 0
            for y in range(len(mat[0])):
                ans += mat[x][y]
                cal[x][y] = ans
        for y in range(len(mat[0])):
            ans = 0
            for x in range(len(mat)):
                ans += cal[x][y]
                cal[x][y] = ans

        res = [[0] * len(mat[0]) for _ in range(len(mat))]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                left = max(y - k, 0)
                right = min(y + k, len(mat[0]) - 1)
                top = max(x - k, 0)
                bottom = min(x + k, len(mat) - 1)

                # 不想要这么多if
                # cal加一行一列
                # 见 0080 304

                if left != 0 and top != 0:
                    res[x][y] = cal[bottom][right] - cal[top - 1][right] - cal[bottom][left - 1] + cal[top - 1][left - 1]
                elif left != 0:
                    res[x][y] = cal[bottom][right] - cal[bottom][left - 1]
                elif top != 0:
                    res[x][y] = cal[bottom][right] - cal[top - 1][right]
                else:
                    res[x][y] = cal[bottom][right]
        return res


sol = Solution()
sol.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
