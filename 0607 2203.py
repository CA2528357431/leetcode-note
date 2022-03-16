class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        way = [{} for i in range(n)]
        for i in range(n):
            way[i][i] = 0
        for f, t, w in edges:
            way[f][t] = min(w, way[f].get(t, 9999999999999))

        def deal(li, i):
            heap = [(0, i)]
            while heap:
                dis, to = heapq.heappop(heap)
                if dis <= li[to]:

                    for j in way[to]:

                        neo = way[to][j] + li[to]
                        if neo >= 9999999999999:
                            continue
                        if neo < li[j]:
                            heappush(heap, (neo, j))
                            li[j] = neo

        to1 = [9999999999999] * n
        to1[src1] = 0
        to2 = [9999999999999] * n
        to2[src2] = 0
        deal(to1, src1)
        deal(to2, src2)

        wayb = [{} for i in range(n)]
        for i in range(n):
            wayb[i][i] = 0
        for f, t, w in edges:
            wayb[t][f] = min(w, wayb[t].get(f, 9999999999999))

        def dealb(li, i):
            heap = [(0, i)]
            while heap:
                dis, to = heapq.heappop(heap)
                if dis <= li[to]:

                    for j in wayb[to]:
                        neo = wayb[to][j] + li[to]

                        if neo >= 9999999999999:
                            continue
                        if neo < li[j]:
                            heappush(heap, (neo, j))
                            li[j] = neo

        to3 = [9999999999999] * n
        to3[dest] = 0
        dealb(to3, dest)

        res = 9999999999999
        for i in range(n):
            res = min(res, to1[i] + to2[i] + to3[i])
        if res >= 9999999999999:
            return -1
        return res


