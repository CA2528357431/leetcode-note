class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        dele = False
        res = 0
        i = 0
        while i + res < n - 1:
            if i % 2 == 0:
                if nums[i + res] != nums[i + 1 + res]:
                    i += 2
                else:
                    res += 1
            else:
                i += 1
        if (n - res) % 2 == 1:
            res += 1
        return res

