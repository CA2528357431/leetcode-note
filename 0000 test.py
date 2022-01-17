from heapq import *
def maxRunTime(n: int, batteries) -> int:
    if n > len(batteries):
        return 0
    res = 0
    heap = [-x for x in batteries]
    heapify(heap)

    while len(heap) > n:
        neo = [0] * n
        for i in range(n):
            neo[i] = -heappop(heap)
        limit = -heap[0]
        if limit == 0:
            return res + neo[-1]
        else:
            sub = neo[-1] - (limit - 1)
            res += sub
            for i in range(n):
                if neo[i] - sub > 0:
                    heappush(heap, -(neo[i] - sub))
    if len(heap)==n:
        res -= max(heap)
    print(res,heap)
    return res

b = [3,3,3]
maxRunTime(2,b)