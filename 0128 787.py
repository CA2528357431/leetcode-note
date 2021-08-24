class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # 不可遍历————存在大量重复导致超时
        '''
        li = [(src, 0)]
        res = 999999
        for _ in range(k + 1):
            if not li:
                break
            neo = []
            for cur, price in li:
                for start, end, cost in flights:

                    if start == cur:
                        if end == dst:
                            res = min(res, cost + price)
                        else:
                            neo.append((end, price + cost))
            li = neo
        for end, cost in li:
            if end == dst:
                res = min(res, cost)
        if res == 999999:
            return -1
        else:
            return res
        '''

        # 动规
        '''
        big = float("inf")
        square = [[big] * n for _ in range(k + 2)]
        square[0][src] = 0
        for x in range(1, k + 2):
            for start, end, cost in flights:
                square[x][end] = min(square[x - 1][start] + cost, square[x][end])
        res = min(li[dst] for li in square)
        if res == big:
            return -1
        return res
        '''

        big = float("inf")
        square = [big] * n
        square[src] = 0

        for x in range(1, k + 2):
            last = square.copy()
            for start, end, cost in flights:
                square[end] = min(last[start] + cost, square[end])
        res = square[dst]
        if res == big:
            return -1
        return res



