class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get(w):
            dic = {}
            for c in w:
                if c not in dic:
                    dic[c] = 0
                dic[c] += 1
            return dic
        n = len(words)
        cur = get(words[0])
        res = [words[0]]
        for i in range(1,n):
            neo = get(words[i])
            if neo!=cur:
                cur = neo
                res.append(words[i])
        return res