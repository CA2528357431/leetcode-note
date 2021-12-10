class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def getdic(word):
            dic = {}
            for c in word:
                if "a" <= c <= "z":
                    if c not in dic:
                        dic[c] = 0
                    dic[c] += 1
            return dic

        def judge(d1, d2):
            delta = 0
            for c in d1:
                if c in d2 and d2[c] >= d1[c]:
                    delta += (d2[c] - d1[c])
                else:
                    return -1
            for c in d2:
                if c not in d1:
                    delta += d2[c]
            return delta

        neo = licensePlate.lower()
        oridic = getdic(neo)
        cur = 100
        res = -1
        for i in range(len(words)):
            word = words[i]
            nxt = judge(oridic, getdic(word))
            if 0 <= nxt < cur:
                cur = nxt
                res = i
        return words[res]