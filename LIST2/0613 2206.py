class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for c in nums:
            if c not in dic:
                dic[c] = 0
            dic[c]+=1
        for k in dic:
            if dic[k]%2!=0:
                return False
        return True