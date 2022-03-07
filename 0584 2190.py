class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dic = {}
        for i in range(len(nums)-1):
            if nums[i]!=key:
                continue
            dic[nums[i+1]] = dic.get(nums[i+1],0)+1
        res = 0
        for k in dic:
            if res==0 or dic[k]>dic[res]:
                res = k
        return res