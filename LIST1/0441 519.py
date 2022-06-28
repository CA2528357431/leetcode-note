class Solution:

    # https://leetcode-cn.com/problems/random-flip-matrix/solution/pythonjavajavascriptgo-jiang-wei-ha-xi-b-8ipu/
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.change = {}
        # 用于指向被替换后某 数字 被替换成了什么 新数字
        self.cur = m * n - 1

    def flip(self) -> List[int]:
        x = random.randint(0, self.cur)

        neo = x
        if neo in self.change:
            neo = self.change[neo]
        # 如果目标位置被替换，就用替换后的数字

        last = self.cur
        if last in self.change:
            last = self.change[last]
        self.change[x] = last
        # 如果末尾位置被替换，就用末尾指向后的数字

        self.cur -= 1

        return [neo // self.n, neo % self.n]

    def reset(self) -> None:
        self.change = {}
        self.cur = self.m * self.n - 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()