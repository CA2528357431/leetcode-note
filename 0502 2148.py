class Solution:
    def countElements(self, nums: List[int]) -> int:
        low = min(nums)
        up = max(nums)
        res = 0
        for n in nums:
            if n!=low and n!=up:
                res+=1
        return res