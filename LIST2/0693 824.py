class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        w = [list(x) for x in sentence.split()]
        n = len(w)
        li = "AEIOUaeiou"
        for i in range(n):
            if w[i][0] in li:
                w[i].append("ma")
            else:
                w[i].append(w[i][0])
                w[i][0] = ""
                w[i].append("ma")
            w[i].append("a"*(i+1))
        ww = ["".join(x) for x in w]
        s = " ".join(ww)
        return s