class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * len(nums)
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        left = [0] * len(nums)
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])

        res = 0
        for i in range(1, n - 1):
            if nums[i] > left[i - 1] and nums[i] < right[i + 1]:
                res += 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                res += 1
        return res