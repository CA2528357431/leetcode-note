class node:
    def __init__(self, c=0):
        self.count = c
        self.li = set()
        self.pre = None
        self.nxt = None

    def add(self, c):
        neo = node(c)
        if self.nxt:
            self.nxt.pre = neo
            neo.nxt = self.nxt
            neo.pre = self
            self.nxt = neo
        else:
            neo.pre = self
            self.nxt = neo

    def remove(self):
        if self.nxt:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre
        else:
            self.pre.nxt = None


class AllOne:

    def __init__(self):
        self.root = node()
        self.s = self.root
        self.e = self.root
        self.dic = {}

    # def show(self):
    #     cur = self.root
    #     while cur:
    #         print(cur.count, cur.li)
    #         cur = cur.nxt

    def inc(self, key: str) -> None:

        if key not in self.dic:
            cur = self.root
            i = cur.count + 1
            if not cur.nxt or cur.nxt.count != i:
                cur.add(i)
            cur.nxt.li.add(key)
            self.s = self.root.nxt
            if self.e == self.root:
                self.e = self.root.nxt
            self.dic[key] = self.root.nxt

        else:
            cur = self.dic[key]

            cur.li.remove(key)

            i = cur.count + 1
            if not cur.nxt or cur.nxt.count != i:
                cur.add(i)
            cur.nxt.li.add(key)

            if cur == self.e:
                self.e = self.e.nxt
            if cur == self.s and not self.s.li:
                self.s = self.s.nxt
            self.dic[key] = cur.nxt
            if not cur.li:
                cur.remove()
        # self.show()
        # print("inc")
        # print()

    def dec(self, key: str) -> None:

        cur = self.dic[key]
        cur.li.remove(key)

        i = cur.count - 1
        if i > 0:
            if cur.pre.count != i:
                cur.pre.add(i)
            cur.pre.li.add(key)

            if cur == self.e and not self.e.li:
                self.e = self.e.pre

            if cur == self.s:
                self.s = self.s.pre

            self.dic[key] = cur.pre

        else:
            if self.e == cur and not cur.li:
                self.e = self.root
            if self.s == cur and not cur.li:
                if cur.nxt:
                    self.s = cur.nxt
                else:
                    self.s = self.root
            self.dic.pop(key)
        if not cur.li:
            cur.remove()
        # self.show()
        # print("inc")
        # print()

    def getMaxKey(self) -> str:

        if self.e.count == 0:
            return ""
        neo = self.e.li.pop()
        self.e.li.add(neo)
        return neo

    def getMinKey(self) -> str:
        if self.e.count == 0:
            return ""
        neo = self.s.li.pop()
        self.s.li.add(neo)
        return neo

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()