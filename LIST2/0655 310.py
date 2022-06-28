class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dic = {}
        for a, b in edges:
            if a not in dic:
                dic[a] = []
            if b not in dic:
                dic[b] = []
            dic[a].append(b)
            dic[b].append(a)
        ps = [-1] * n

        def count(x):
            used = {x}
            cur = [x]
            h = 0
            while cur:
                h += 1
                nxt = []
                for x in cur:
                    for y in dic[x]:
                        if y in used:
                            continue
                        used.add(y)
                        nxt.append(y)
                        ps[y] = x
                if not nxt:
                    return cur[0]
                cur = nxt

        x = count(0)
        y = count(x)
        path = [y]
        cur = y
        while cur != x:
            path.append(ps[cur])
            cur = ps[cur]
        length = len(path)
        if length % 2 == 1:
            return [path[length // 2]]
        else:
            return [path[length // 2], path[length // 2 - 1]]

# https://leetcode-cn.com/problems/minimum-height-trees/solution/zui-xiao-gao-du-shu-by-leetcode-solution-6v6f/