class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        st = 1000000007
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1
        heap = [(n, dic[n]) for n in dic]
        heapq.heapify(heap)
        while k:
            n, t = heapq.heappop(heap)
            if not heap:
                a = k // t
                b = k % t
                return pow((n + a), (t - b), st) * pow((n + a + 1), b, st) % st
            la, tt = heap[0]

            if (la - n) * t > k:
                res = 1
                a = k // t
                b = k % t
                res = res * pow((n + a), (t - b), st) % st
                res = res * pow((n + a + 1), b, st) % st
                for np, tp in heap:
                    res = res * pow(np, tp, st) % st
                return res

            k = k - (la - n) * t
            heapq.heappop(heap)
            heapq.heappush(heap, (la, tt + t))

        res = 1
        for np, tp in heap:
            res = res * pow(np, tp, st) % st
        return res