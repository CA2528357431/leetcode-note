class StockPrice:

    def __init__(self):
        self.dic = {}

        self.cur = 0

        self.big = []
        self.small = []

    def update(self, timestamp: int, price: int) -> None:

        self.dic[timestamp] = price

        if timestamp > self.cur:
            self.cur = timestamp

        heapq.heappush(self.big, (-price, timestamp))
        heapq.heappush(self.small, (price, timestamp))
        # 此时暂时不处理堆中的过期数据

    def current(self) -> int:
        return self.dic[self.cur]

    def maximum(self) -> int:
        while True:
            # 开始处理错误数据
            p, t = -self.big[0][0], self.big[0][1]
            # 如果heap中的 时间价格 与dic中的不相符合，则删除
            if self.dic[t] == p:
                return p

            heapq.heappop(self.big)


    def minimum(self) -> int:
        while True:
            p, t = self.small[0][0], self.small[0][1]
            if self.dic[t] == p:
                return p

            heapq.heappop(self.small)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()