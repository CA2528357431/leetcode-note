class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def get(x, y):
            a = 1
            aa = 1
            for i in range(y):
                a *= (x - i)
                aa *= (i + 1)

            return a // aa

        n = len(nums)
        res = 0
        for i in range(n):
            neo = get(n - 1, i) * nums[i]
            res += neo
        res = res % 10
        return res
