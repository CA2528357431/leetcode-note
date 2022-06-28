class Solution:
    def minimumTotal(self, triangle):

        # 动规A

        '''
        res = [[99999]*len(x) for x in triangle]

        # 不能直接copy
        # copy出的li中的子li和triangle同址

        res[0][0] = triangle[0][0]
        for x in range(0, len(res) - 1):
            for y in range(len(res[x])):
                res[x + 1][y] = min(res[x + 1][y], res[x][y] + triangle[x + 1][y])
                res[x + 1][y + 1] = min(res[x + 1][y + 1], res[x][y] + triangle[x + 1][y + 1])
        return min(res[-1])
        '''

        # 动规A+

        '''
        res = [[0] * len(x) for x in triangle]
        res[0][0] = triangle[0][0]
        for x in range(1, len(res)):
            res[x][0] = res[x - 1][0] + triangle[x][0]
            for y in range(1, len(res[x]) - 1):
                res[x][y] = min(res[x - 1][y], res[x - 1][y - 1]) + triangle[x][y]
                # 减少min步骤，对res初态无要求
            res[x][-1] = res[x - 1][-1] + triangle[x][-1]
        return min(res[-1])
        '''

        # 空间优化
        # 其实就是滚动法
        # 举fib数列例子类比就是
        # 普通动规[1,1,2,3,5,....]逐步后推
        # 滚动法 1,1   1,2   2,3   3,5

        last = [0]*len(triangle)
        last[0] = triangle[0][0]
        cur = last.copy()
        for x in range(1, len(triangle)):
            cur[0] = last[0] + triangle[x][0]
            for y in range(1, x):
                cur[y] = min(last[y], last[y - 1]) + triangle[x][y]
                # 减少min步骤，对res初态无要求
            cur[x] = last[x - 1] + triangle[x][-1]
            last = cur.copy()
        return min(cur)

