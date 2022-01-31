class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        li1 = s1.split()
        li2 = s2.split()

        dic1 = {}
        for w in li1:
            if w not in dic1:
                dic1[w] = 0
            dic1[w] += 1
        dic2 = {}
        for w in li2:
            if w not in dic2:
                dic2[w] = 0
            dic2[w] += 1

        res = []
        for w in dic1:
            if dic1[w] == 1 and w not in dic2:
                res.append(w)
        for w in dic2:
            if dic2[w] == 1 and w not in dic1:
                res.append(w)

        return res