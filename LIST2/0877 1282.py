class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        res = []
        for i in range(len(groupSizes)):
            c = groupSizes[i]
            if c not in dic:
                dic[c] = []
            dic[c].append(i)
            if len(dic[c]) == c:
                res.append(dic[c])
                dic[c] = []
        return res


