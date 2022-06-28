class Node:
    def __init__(self):
        self.next = {}

    # 字典树


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.next:
                cur = cur.next[c]
            else:
                cur.next[c] = Node()
                cur = cur.next[c]
        cur.next[None] = Node()

    def search(self, word: str) -> bool:
        curs = [self.root]
        for c in word:
            neo = []
            if c == ".":
                for cur in curs:
                    neo.extend(list(cur.next.values()))
            else:
                judge = False
                for cur in curs:
                    if c in cur.next:
                        judge = True
                        neo.append(cur.next[c])

                if not judge:
                    return False
            del curs
            curs = neo
        for cur in curs:
            if None in cur.next:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)