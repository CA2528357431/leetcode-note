class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # https://leetcode-cn.com/problems/k-inverse-pairs-array/solution/kge-ni-xu-dui-shu-zu-by-leetcode-solutio-0hkr/

        '''
        li = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            li[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                cur = 0
                for num in range(1, i + 1):
                    if j - (i - num) >= 0:
                        p = li[i - 1][j - (i - num)]
                        cur += p
                li[i][j] = cur
        return li[-1][-1] % (1000000007)
        '''

        # 优化逻辑
        '''
        li = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            li[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                cur = 0
                # 优化计数算法
                for num in range(0, i):
                    if j - num >= 0:
                        p = li[i - 1][j - num]
                        cur += p
                li[i][j] = cur
        return li[-1][-1] % (1000000007)
        '''

        # 优化算法
        '''
        li = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            li[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                a = li[i][j-1]
                c = li[i-1][j]
                b = 0
                if j-i>=0:
                    b = li[i-1][j-i]
                li[i][j] = a-b+c
        return li[-1][-1] % (1000000007)
        '''

        # 滚动优化
        li = [0] * (k+1)
        li[0] = 1

        for i in range(1, n + 1):
            neo = [0] * (k+1)
            neo[0] = 1
            for j in range(1, k + 1):
                a = neo[j-1]
                c = li[j]
                b = 0
                if j-i>=0:
                    b = li[j-i]
                neo[j] = a-b+c
            li = neo
        return li[-1] % (1000000007)