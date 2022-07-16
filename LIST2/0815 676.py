class MagicDictionary:

    def __init__(self):
        self.li = []


    def buildDict(self, dictionary: List[str]) -> None:
        self.li = dictionary


    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for w in self.li:
            if n!=len(w):
                continue
            cnt = 0
            for i in range(n):
                if searchWord[i]!=w[i]:
                    cnt+=1
                    if cnt==2:
                        break
            if cnt==1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)