class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        if k == 1:
            return min(wage)

        n = len(quality)
        li = [i for i in range(n)]
        li.sort(key=lambda i: -quality[i] / wage[i])

        heap = []
        cur = 0
        res = 1000000000
        for i in range(n):
            neo = li[i]
            if len(heap) < k - 1:
                heapq.heappush(heap, -quality[neo])
                cur += quality[neo]
            else:
                res = min(res, cur * wage[neo] / quality[neo] + wage[neo])

                if -heap[0] > quality[neo]:
                    x = -heapq.heappop(heap)
                    cur -= x
                    heapq.heappush(heap, -quality[neo])
                    cur += quality[neo]

        return res

