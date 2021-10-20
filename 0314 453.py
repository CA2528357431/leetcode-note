class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mid=min(nums)
        res=0
        for x in nums:
            res+=abs(x-mid)
        return res