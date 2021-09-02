class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        num = len(words)
        l = len(words[0])

        res = []

        for p in range(len(s) - l * num + 1):
            diccpy = dic.copy()
            for x in range(p, p + l * num, l):
                neo = s[x:x + l]
                if neo in diccpy:
                    diccpy[neo] -= 1
                    if diccpy[neo] == 0:
                        diccpy.pop(neo)
                else:
                    break
            else:
                res.append(p)
        return res