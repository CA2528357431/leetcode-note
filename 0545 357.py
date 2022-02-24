class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        nums = [0 for _ in range(n + 1)]
        nums[0] = 1
        for i in range(1, n + 1):
            cur = 9
            for j in range(i-1):
                cur *= 9-j
            # cur 为j位的数位互不相同的数的个数
            nums[i] = nums[i-1]+cur
        return nums[n]