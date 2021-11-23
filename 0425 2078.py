class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dic = {}
        res = 0
        for i in range(len(colors)):
            if colors[i] not in dic:
                dic[colors[i]] = i
            for c in dic.keys():
                if c == colors[i]:
                    continue
                res = max(res, i - dic[c])
        return res
