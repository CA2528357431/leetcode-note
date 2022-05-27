class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n=len(words)
        i1=-1
        i2=-1
        res=n
        for i in range(n):
            w=words[i]
            if w==word1:
                i1=i
                if i2>=0:
                    res=min(abs(i1-i2),res)
            elif w==word2:
                i2=i
                if i1>=0:
                    res=min(abs(i1-i2),res)
        return res