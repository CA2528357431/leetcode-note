class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        nums.sort()
        ave = nums[n//2]
        res = 0
        for i in nums:
            res+=abs(i-ave)
        return res
        # 中位数