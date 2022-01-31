class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)

        zero = [0] * n
        if nums[0] == 0:
            zero[0] = 1
        for i in range(1, n):
            num = nums[i]
            if num == 0:
                zero[i] = zero[i - 1] + 1
            else:
                zero[i] = zero[i - 1]

        ones = [0] * n
        if nums[-1] == 1:
            ones[-1] = 1
        for i in range(n - 2, -1, -1):
            num = nums[i]
            if num == 1:
                ones[i] = ones[i + 1] + 1
            else:
                ones[i] = ones[i + 1]

        res = [0]
        cur = 0 + ones[0]
        for i in range(1, n):
            neo = zero[i - 1] + ones[i]
            if neo == cur:
                res.append(i)
            elif neo > cur:
                res = [i]
                cur = neo
        neo = zero[n - 1] + 0
        if neo == cur:
            res.append(n)
        elif neo > cur:
            res = [n]
        return res


