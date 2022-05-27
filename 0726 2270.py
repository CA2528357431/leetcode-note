class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        cur = 0
        res = 0
        for i in range(n - 1):
            cur += nums[i]
            if cur * 2 >= s:
                res += 1

        return res