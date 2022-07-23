class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for k,t in queries:
            neo = [int(x[-t:]) for x in nums]
            dic = {}
            for i in range(len(neo)):
                n = neo[i]
                if n not in dic:
                    dic[n] = []
                dic[n].append(i)
            neo.sort()
            tar = neo[k-1]
            t = k-1
            while t>0 and neo[t]==neo[t-1]:
                t-=1
            length = k-1-t
            re = dic[tar][length]
            res.append(re)
        return res