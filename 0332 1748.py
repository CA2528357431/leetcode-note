class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = {}
        res = 0
        for x in nums:
            if x not in s:
                s[x] = 1
                res+=x
            else:
                if s[x]==1:
                    s[x]=2
                    res-=x
                else:
                    s[x]+=1
        return res