class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)

        used = set()
        res = -1
        for i in range(n):
            cur = nums[i]
            if cur in used:
                continue
            l = 0
            while cur not in used:
                used.add(cur)
                l += 1
                cur = nums[cur]
            res = max(res, l)

        return res