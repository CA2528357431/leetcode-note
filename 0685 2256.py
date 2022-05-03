class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        n = len(nums)
        cal = nums.copy()
        for i in range(1, n):
            cal[i] += cal[i - 1]
        s = cal[-1]
        res = 0
        cur = 9999999
        for i in range(n):
            l = cal[i] // (i + 1)
            r = 0
            if i != n - 1:
                r = (s - cal[i]) // (n - i - 1)
            de = abs(l - r)
            if de < cur:
                res = i
                cur = de
        return res

