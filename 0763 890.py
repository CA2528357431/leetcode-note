class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        def cmp(w1,w2):
            dic = {}
            used = set()
            for i in range(n):
                if w2[i] in dic:
                    if dic[w2[i]]!=w1[i]:
                        return False
                else:
                    if w1[i] in used:
                        return False
                    else:
                        dic[w2[i]]=w1[i]
                        used.add(w1[i])
            return True
        res = []
        for w in words:
            if cmp(w,pattern):
                res.append(w)
        return res