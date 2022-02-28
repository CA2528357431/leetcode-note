class MinStack:

    def __init__(self):
        self.li = []
        self.sm = []
        # 利用sm栈记录min，sm[i]为有i+1个数字时的最小值


    def push(self, val: int) -> None:
        self.li.append(val)
        if not self.sm:
            self.sm.append(val)
        else:
            self.sm.append(min(val,self.sm[-1]))


    def pop(self) -> None:
        self.li.pop()
        self.sm.pop()


    def top(self) -> int:
        return self.li[-1]


    def getMin(self) -> int:
        return self.sm[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()