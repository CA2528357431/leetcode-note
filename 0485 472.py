
class Trie:
    def __init__(self):
        self.next = {}

    def insert(self, word: str):
        cur = self.next
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur[""] = None
    def judge(self,word):
        if not word:
            return False
        def find(cur,i,j):
            if i==len(word):
                if j and "" in cur:
                    return True
                else:
                    return False
            up = False
            down = False
            if word[i] in cur:
                down = find(cur[word[i]],i+1,j)
            if "" in cur:
                up = find(self.next,i,True)
            return up or down
        return find(self.next,0,False)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        tree = Trie()
        for word in words:
            if word:
                tree.insert(word)
        res = []
        for word in words:
            if tree.judge(word):
                res.append(word)
        return res
        '''

        tree = Trie()
        words.sort(key=lambda x:len(x))
        # 先加小词
        res = []
        for word in words:
            if not word:
                continue
            elif tree.judge(word):
                res.append(word)
                # 一个连接词无需加入树中
            else:
                tree.insert(word)