class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s=sum(nums)
        res=[]
        cur=0
        for c in nums:
            cur+=c
            res.append(c)
            if cur*2>s:
                return res