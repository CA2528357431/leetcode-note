class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c]+=1
        li = [[dic[c],c] for c in dic]
        li.sort(key=lambda x:x[0],reverse=True)
        res = []
        for time,c in li:
            res.extend([c]*time)
        return "".join(res)
        '''

        # 桶排序
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        buck = [[] for _ in range(len(s) + 1)]
        for c in dic:
            buck[dic[c]].append(c)

        res = []
        for time in range(len(s), 0, -1):
            for c in buck[time]:
                res.extend([c] * time)
        return "".join(res)