class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        n = len(paragraph)
        s = set(banned)
        dic = {}
        cur = []
        for x in range(n):
            c = paragraph[x]
            if not c.isalpha():
                w = "".join(cur)
                w = w.lower()
                if w and w not in s:
                    if w not in dic:
                        dic[w] = 0
                    dic[w] += 1
                cur = []
            else:
                cur.append(c)
        if cur:
            w = "".join(cur)
            w = w.lower()
            if w and w not in s:
                if w not in dic:
                    dic[w] = 0
                dic[w] += 1

        ll = list(dic.keys())
        ll.sort(key=lambda x: -dic[x])
        return ll[0]