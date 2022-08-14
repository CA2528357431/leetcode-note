class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        n = len(nums)
        j = 0
        k = 0
        for i in range(n):
            while j < n and nums[j] < nums[i] + diff:
                j += 1
            if j == n:
                return res
            if nums[j] == nums[i] + diff:
                while k < n and nums[k] < nums[j] + diff:
                    k += 1
                if k == n:
                    return res
                if nums[k] == nums[j] + diff:
                    res += 1

        return res
