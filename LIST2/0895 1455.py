class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def do(w):
            if len(w)<len(searchWord):
                return False
            for i in range(len(searchWord)):
                if searchWord[i]!=w[i]:
                    return False
            return True
        li = sentence.split()
        for i in range(len(li)):
            if do(li[i]):
                return i+1
        return -1