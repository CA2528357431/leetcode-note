class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and k % 2 == 1:
            return -1
        elif n == 1:
            return nums[0]

        big = nums.copy()
        for i in range(1, n):
            big[i] = max(big[i], big[i - 1])

        if k > n:
            return big[n - 1]
        if k == n:
            return big[n - 2]
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]

        # 结果一定是0 - n-2的最大项或者n项
        return max(big[k - 2], nums[k])