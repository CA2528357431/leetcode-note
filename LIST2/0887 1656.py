class OrderedStream:

    def __init__(self, n: int):
        self.dic = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey] = value
        res = []

        pre = ""
        while self.ptr in self.dic:
            if self.dic[self.ptr] > pre:
                res.append(self.dic[self.ptr])
                self.ptr += 1
            else:
                break
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)