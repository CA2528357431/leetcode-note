class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        child = {}
        for i in range(len(parents)):
            if parents[i] not in child:
                child[parents[i]] = [i]
            else:
                child[parents[i]].append(i)
        child.pop(-1)
        # 建立图

        findres = [0] * n
        # 对于子树大小预处理
        def find(x):
            if x not in child:
                findres[x] = 1
                return 1
            elif len(child[x]) == 2:
                l = find(child[x][0])
                r = find(child[x][1])
                findres[x] = 1 + l + r
                return 1 + l + r
            else:
                l = find(child[x][0])
                findres[x] = 1 + l
                return 1 + l
            # 边递归边更新

        find(0)

        def judge(x):
            if x not in child:
                return n - 1
            elif len(child[x]) == 2:
                l = findres[child[x][0]]
                r = findres[child[x][1]]
                m = n - l - r - 1
                if m == 0:
                    m = 1
                return l * r * m
            else:
                c = findres[child[x][0]]
                if c == n - 1:
                    return n - 1
                else:
                    return c * (n - 1 - c)

        res = -1
        num = 0
        for x in range(n):
            neo = judge(x)
            if neo > res:
                res = neo
                num = 1
            elif neo == res:
                num += 1

        return num




