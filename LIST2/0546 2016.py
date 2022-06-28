class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        res=-1
        for j in range(1,n):
            neo=nums[j]-nums[i]
            if neo>0:
                res=max(res,neo)
            if nums[i]>nums[j]:
                i=j
        return res