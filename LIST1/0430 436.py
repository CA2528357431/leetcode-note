class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(intervals)):
            s,e = intervals[i]
            dic[s] = i
        ss = list(dic.keys())
        ss.sort()
        def find(tar):
            if tar>ss[-1]:
                return -1
            if tar in dic:
                return dic[tar]
            l = 0
            r = len(ss)-1
            while l<r:
                mid = (l+r)//2
                if ss[mid]<tar:
                    l = mid+1
                elif ss[mid]>tar:
                    r = mid
            return dic[ss[l]]
        res = [find(x[1]) for x in intervals]
        return res