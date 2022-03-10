class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for x in nums:
            dic[x] = dic.get(x,0)+1
        for k in dic:
            if dic[k]>n//2:
                return k