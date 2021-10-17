class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def getlength():

            used = [2] * n
            used[0] = 1
            # 获取第x的路径：
            # 任意节点只能访问x次

            dic = [[] for _ in range(n)]
            for x, y in edges:
                dic[x - 1].append(y)
                dic[y - 1].append(x)

            judge = False
            big = 0
            cur = {1}

            l = 0
            while True:
                l += 1
                neo = set()
                for node in cur:
                    li = dic[node - 1]
                    for x in li:
                        if x in neo or used[x - 1] == 0:
                            continue
                        neo.add(x)
                        used[x - 1] -= 1
                        if x == n:
                            if not judge:
                                judge = True
                                big = l
                            else:
                                if l > big:
                                    return l

                cur = neo

        def gettime(l):
            res = 0
            for i in range(l):
                res += time
                if i != l - 1:
                    if (res // change) % 2 == 1:
                        res = (res // (2 * change) + 1) * (2 * change)
            return res

        l = getlength()
        t = gettime(l)
        return t


