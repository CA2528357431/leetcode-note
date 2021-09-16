class Trie:
    def __init__(self):
        self.children = {}
        self.word = ""
        self.count = 0

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                neo = Trie()
                cur.children[c] = neo
            cur = cur.children[c]
            cur.count += 1
        cur.word = word

    def pop(self, word):
        cur = self
        for c in word:
            neo = cur.children[c]
            neo.count -= 1
            if neo.count == 0:
                cur.children.pop(c)
                return
            cur = neo
        cur.word = ""

t = Trie()
li = ["a","aa"]
for i in li:
    t.insert(i)
for i in li:
    t.pop(i)
print(t.children)
