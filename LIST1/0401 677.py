class node:
    def __init__(self,char=""):
        self.char = char
        self.val = 0
        self.next = {}


class MapSum:

    def __init__(self):
        self.root = node()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.next:
                cur.next[c] = node(c)
            cur = cur.next[c]
        cur.next[""] = node()
        cur = cur.next[""]
        cur.val = val


    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.next:
                return 0
            cur = cur.next[c]
        res = 0
        li = [cur]
        while li:
            neo = []
            for nn in li:
                for n in nn.next.values():
                    if n.char == "":
                        res+=n.val
                    else:
                        neo.append(n)
            li = neo
        return res



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)