class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i]+=1
        a,b = 0,0
        for k in dic:
            v = dic[k]
            a+=v//2
            b+=v%2
        return [a,b]