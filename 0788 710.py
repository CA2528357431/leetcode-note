class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.dic = {}
        st = n-len(blacklist)
        self.st = st
        w = st
        blacklist = set(blacklist)
        for b in blacklist:
            if b<st:
                while w in blacklist:
                    w+=1
                self.dic[b] = w
                w+=1
    def pick(self) -> int:
        x = randint(0,self.st-1)
        if x not in self.dic:
            return x
        else:
            return self.dic[x]
