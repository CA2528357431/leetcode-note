class MyCircularDeque:

    def __init__(self, k: int):
        self.li = [0]*k
        self.k = k
        self.l = 0
        self.r = 1
        self.cnt = 0


    def insertFront(self, value: int) -> bool:
        if self.cnt==self.k:
            return False
        neol = (self.l+self.k-1)%self.k
        self.li[self.l] = value
        self.l = neol
        self.cnt+=1
        return True


    def insertLast(self, value: int) -> bool:
        if self.cnt==self.k:
            return False
        neor = (self.r+1)%self.k
        self.li[self.r] = value
        self.r = neor
        self.cnt+=1
        return True


    def deleteFront(self) -> bool:
        if self.cnt==0:
            return False
        neol = (self.l+1)%self.k
        self.l = neol
        self.cnt-=1
        return True


    def deleteLast(self) -> bool:
        if self.cnt==0:
            return False
        neor = (self.r+self.k-1)%self.k
        self.r = neor
        self.cnt-=1
        return True


    def getFront(self) -> int:
        if self.cnt==0:
            return -1
        neol = (self.l+1)%self.k
        return self.li[neol]


    def getRear(self) -> int:
        if self.cnt==0:
            return -1
        neor = (self.r+self.k-1)%self.k
        return self.li[neor]


    def isEmpty(self) -> bool:
        return self.cnt==0


    def isFull(self) -> bool:
        return self.cnt==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()