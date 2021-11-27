class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic1 = {}
        for word in words1:
            if word not in dic1:
                dic1[word] = 0
            dic1[word]+=1
        dic2 = {}
        for word in words2:
            if word not in dic2:
                dic2[word] = 0
            dic2[word]+=1
        res = 0
        for w in dic1:
            if dic1[w]==1 and w in dic2 and dic2[w]==1:
                res+=1
        return res