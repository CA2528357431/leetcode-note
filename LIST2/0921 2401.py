class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        n = len(nums)

        j = 0
        for i in range(n):
            while nums[i] & cur != 0:
                cur -= nums[j]
                j += 1
            cur = cur | nums[i]
            res = max(res, i - j + 1)
        return res
        # 滑动窗口