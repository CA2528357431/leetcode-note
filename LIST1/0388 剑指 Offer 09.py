class CQueue:

    def __init__(self):
        self.last = []
        self.first = []

    def appendTail(self, value: int) -> None:
        self.last.append(value)

    def deleteHead(self) -> int:
        if not self.first and not self.last:
            return -1

        if not self.first:
            while self.last:
                neo = self.last.pop()
                self.first.append(neo)

        return self.first.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()