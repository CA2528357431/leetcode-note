class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        cur = 1
        res = 0
        j = 0
        n = len(nums)
        for i in range(n):
            cur = cur * nums[i]
            while cur >= k and j <= i:
                cur = cur / nums[j]
                j += 1
            res += i + 1 - j
        return res

