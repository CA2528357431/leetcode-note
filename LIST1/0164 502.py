import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        '''
        length = len(profits)

        def do(k, w):
            if k == 0:
                return w

            big = None
            for i in range(length):
                if w >= capital[i]:
                    if big is None:
                        big = i
                    else:
                        if profits[i] > profits[big]:
                            big = i

            if big is None:
                return w

            w += profits[big]
            profits[big] = 0
            k -= 1
            return do(k, w)

        res = do(k, w)

        return res
        '''

        # 快速查找

        # w足够大的话直接挑最大的即可
        if w >= max(capital):

            '''
            heap = [-x for x in profits]
            heapq.heapify(heap)
            for _ in range(k):
                w+=-heapq.heappop(heap)
            '''

            return w + sum(heapq.nlargest(k, profits))

        length = len(profits)
        cur = 0

        # 根据cap排序来便于确定比较范围
        li = [(capital[i], profits[i]) for i in range(length)]
        li.sort(key=lambda x: x[0])
        heap = []

        for x in range(k):
        # 用heap排序高速找出max
            while cur < length and li[cur][0] <= w:
                heapq.heappush(heap, -li[cur][1])
                cur += 1
            if not heap:
                break
            neo = -heapq.heappop(heap)
            w += neo

        return w

sol = Solution()
sol.findMaximizedCapital(2,0,[1,2,3],[0,1,1])