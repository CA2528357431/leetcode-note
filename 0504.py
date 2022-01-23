class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        nums.sort()
        n = len(nums)
        res = []

        cur = nums[0]
        nxt = nums[1]
        if cur + 1 < nxt:
            res.append(cur)

        for i in range(1, n - 1):
            pre = nums[i - 1]
            cur = nums[i]
            nxt = nums[i + 1]
            if cur - 1 > pre and cur + 1 < nxt:
                res.append(cur)

        pre = nums[-2]
        cur = nums[-1]
        if cur - 1 > pre:
            res.append(cur)

        return res