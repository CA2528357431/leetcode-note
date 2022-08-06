class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        def do(x, lim):
            a = x // lim
            b = x % lim
            if b == 0:
                return a - 1, lim
            else:
                aa = x // (a + 1)
                bb = x % (a + 1)
                return a, aa

        res = 0
        n = len(nums)
        lim = nums[-1]

        for i in range(n - 2, -1, -1):
            times, neo = do(nums[i], lim)
            res += times
            lim = neo
        return res