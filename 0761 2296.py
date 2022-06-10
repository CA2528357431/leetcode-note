class Node:

    def __init__(self, ch=''):
        self.prev = None
        self.next = None
        self.ch = ch

    def insert(self, node):
        node.prev = self
        node.next = self.next
        node.prev.next = node
        if node.next:
            node.next.prev = node

    def remove(self) -> None:
        self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class TextEditor:
    def __init__(self):
        self.root = Node()
        self.cur = self.root

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur.insert(Node(ch))
            self.cur = self.cur.next

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            self.cur.next.remove()
            k -= 1
        return k0 - k

    def text(self) -> str:
        s = []
        k, cur = 10, self.cur
        while k and cur:
            s.append(cur.ch)
            cur = cur.prev
            k -= 1
        s.reverse()
        return ''.join(s)

    def cursorLeft(self, k: int) -> str:
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.cur.next:
            self.cur = self.cur.next
            k -= 1
        return self.text()