'''

class Trie:
    def __init__(self):
        self.root = {}

    def add(self,w):
        cur = self.root
        for c in w:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[""] = None
    def start(self,w):
        cur = self.root
        n = len(w)
        for i in range(n):
            if "" in cur:
                return w[:i]
            c = w[i]
            if c not in cur:
                return w
            cur = cur[c]
        return w


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        root = Trie()
        for w in dictionary:
            root.add(w)
        li = sentence.split()
        res = [root.start(w) for w in li]

        return " ".join(res)

'''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def add(cur, w):
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = None

        def start(cur, w):
            n = len(w)
            for i in range(n):
                if "" in cur:
                    return w[:i]
                c = w[i]
                if c not in cur:
                    return w
                cur = cur[c]
            return w

        root = {}
        for w in dictionary:
            add(root, w)
        li = sentence.split()
        res = [start(root, w) for w in li]

        return " ".join(res)
