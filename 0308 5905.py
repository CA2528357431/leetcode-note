class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def getlength():
            dic = [[] for _ in range(n)]
            for x, y in edges:
                dic[x - 1].append(y)
                dic[y - 1].append(x)

            judge = False
            big = 0
            cur = {1}
            la = {}
            l = 0
            while True:
                l += 1
                neo = set()
                for node in cur:
                    li = dic[node - 1]
                    for x in li:
                        neo.add(x)
                        if x == n:
                            if not judge:
                                judge = True
                                big = l
                            else:
                                if l > big:
                                    return l
                la = cur
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