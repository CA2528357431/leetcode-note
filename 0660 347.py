class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1
        heap = []
        for n in dic:
            heapq.heappush(heap, (-dic[n], n))

        res = []
        for i in range(k):
            t, n = heapq.heappop(heap)
            res.append(n)
        return res