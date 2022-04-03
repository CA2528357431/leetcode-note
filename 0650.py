class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.k2v = {}
        self.v2k = {}
        for i in range(len(keys)):
            k = keys[i]
            v = values[i]
            self.k2v[k] = v
            if v not in self.v2k:
                self.v2k[v] = []
            self.v2k[v].append(k)

        self.tree = {}
        for w in dictionary:
            cur = self.tree
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = None

    def encrypt(self, word1: str) -> str:
        li = list(word1)
        for i in range(len(word1)):
            k = li[i]
            li[i] = self.k2v[k]

        return "".join(li)

    def decrypt(self, word2: str) -> int:
        n = len(word2) // 2
        ll = [""] * n
        for i in range(n):
            ll[i] = word2[i * 2:i * 2 + 2]

        li = [self.tree]
        for i in range(n):
            neo = ll[i]
            if neo not in self.v2k:
                return 0
            nxt = []
            for x in self.v2k[neo]:

                for l in li:
                    if x not in l:
                        continue
                    nxt.append(l[x])
            li = nxt
        cnt = 0
        for x in li:
            if "" in x:
                cnt += 1
        return cnt

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)