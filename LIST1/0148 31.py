class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        i = len(nums) - 2
        while nums[i] >= nums[i + 1] and i >= 0:
            i -= 1
        if i < 0:
            for r in range(0, (len(nums) - 1) // 2 + 1):
                nums[r], nums[len(nums) - 1 - r] = nums[len(nums) - 1 - r], nums[r]

        else:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

            for r in range(i + 1, (len(nums) - 1 + i + 1) // 2 + 1):
                nums[r], nums[len(nums) - 1 + i + 1 - r] = nums[len(nums) - 1 + i + 1 - r], nums[r]


    # https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/