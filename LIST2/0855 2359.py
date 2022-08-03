class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def do(cur, cost, li):
            if li[cur] >= 0:
                return
            li[cur] = cost
            if edges[cur] < 0:
                return
            do(edges[cur], cost + 1, li)

        li1 = [-1] * n
        li2 = [-1] * n

        do(node1, 0, li1)
        do(node2, 0, li2)

        res = -1
        for i in range(n):
            if li1[i] < 0 or li2[i] < 0:
                continue
            if res < 0:
                res = i
            else:
                if max(li1[i], li2[i]) < max(li1[res], li2[res]):
                    res = i
        if res > n:
            return -1
        return res
