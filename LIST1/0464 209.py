class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        cur = 0
        n = len(nums)

        res = 0
        while r<n or l<n:
            if cur<target:
                if r==n:
                    return res
                cur+=nums[r]
                r+=1
            else:
                if res==0:
                    res = r-l
                else:
                    res = min(res,r-l)
                cur-=nums[l]
                l+=1
        return res