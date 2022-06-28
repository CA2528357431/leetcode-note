class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        cur = -999999
        res = 0
        for x in nums:
            if x > cur + k:
                res += 1
                cur = x

        return res

