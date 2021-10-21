class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dic = {}
        s = 0
        for num in nums:
            if num+k in dic:
                s+=dic[num+k]
            if num-k in dic:
                s+=dic[num-k]
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        return s