# ** 字典树 **

'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        y = len(board)
        x = len(board[0])

        res = set()

        for word in words:

            def check(i, j, word, length):

                if length == len(word) - 1:
                    if word[-1] == board[i][j]:
                        if word not in res:
                            res.add(word)
                    return
                if board[i][j] != word[length]:
                    return

                ch = board[i][j]
                board[i][j] = ""
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ii < y and 0 <= jj < x:
                        check(ii, jj, word, length + 1)

                board[i][j] = ch

            for i in range(y):
                for j in range(x):
                    check(i, j, word, 0)
        return list(res)
'''


# ** 字典树 **

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
                # 不能break，递归的其他分支在用cur，因此需要对cur之后的节点进行处理
            cur = neo
        cur.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        y = len(board)
        x = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []

        def dfs(cur, i, j):
            ch = board[i][j]
            if ch not in cur.children:
                return

            ne = cur.children[ch]
            if ne.word:
                res.append(ne.word)
                trie.pop(ne.word)

            board[i][j] = ""

            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ii < y and 0 <= jj < x:
                    dfs(ne, ii, jj)

            board[i][j] = ch

        for i in range(y):
            for j in range(x):
                dfs(trie, i, j)

        return res