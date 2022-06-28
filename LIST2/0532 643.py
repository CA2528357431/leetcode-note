class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        cur = res
        n = len(nums)

        for i in range(1, n - k + 1):
            cur = cur + nums[i + k - 1] - nums[i - 1]
            res = max(cur, res)

        return res / k