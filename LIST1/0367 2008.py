class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dic = {}
        for ride in rides:
            s,e,v = ride
            if e not in dic:
                dic[e] = {}
            if s not in dic[e]:
                dic[e][s] = v+(e-s)
            else:
                dic[e][s] = max(dic[e][s],v+(e-s))
        res = [-1]*(n+1)
        res[1] = 0
        for i in range(2,n+1):
            res[i] = res[i-1]
            if i in dic:
                for s,v in dic[i].items():
                    res[i] = max(res[s]+v,res[i])

        return res[-1]