class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n]+=1
        res = 0
        for n in dic.keys():
            if n-1 in dic:
                res = max(res,dic[n]+dic[n-1])
        return res