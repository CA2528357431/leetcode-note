class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for w, l in matches:
            if w not in dic:
                dic[w] = 0
            if l not in dic:
                dic[l] = 0
            dic[l] += 1
        res = [[], []]
        for i in range(1, 10 ** 5 + 1):
            if i in dic:
                if dic[i] == 0:
                    res[0].append(i)
                if dic[i] == 1:
                    res[1].append(i)
        return res
