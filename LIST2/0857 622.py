class MyCircularQueue:

    def __init__(self, k: int):
        self.li = [-1] * (k + 1)
        self.s = 0
        self.e = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.li[self.e] = value
        self.e = (self.e + 1) % len(self.li)
        # print(self.li,self.s,self.e)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.s = (self.s + 1) % len(self.li)
        # print(self.li,self.s,self.e)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.li[self.s]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.li[(self.e - 1 + len(self.li)) % len(self.li)]

    def isEmpty(self) -> bool:
        return self.s == self.e

    def isFull(self) -> bool:
        res = (self.e - self.s + len(self.li)) % len(self.li)
        return res == len(self.li) - 1

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()