class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        cur = 0

        if n < 1 + 2 * k:
            return res
        for i in range(0, 2 * k):
            cur += nums[i]

        for i in range(k, n - k):
            cur = cur + nums[i + k]
            res[i] = cur
            cur = cur - nums[i - k]
        for i in range(n):
            if res[i] != -1:
                res[i] = res[i] // (2 * k + 1)
        return res