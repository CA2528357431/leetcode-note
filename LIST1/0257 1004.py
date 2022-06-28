class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = 0

        s = 0

        l = 0
        r = 0
        while r<n:
            if nums[r]==0:
                s+=1
            r+=1

            while s>k:
                if nums[l]==0:
                    s-=1
                l+=1
            res = max(r-l,res)
        return res