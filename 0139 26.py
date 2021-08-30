class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        w = 1
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                nums[w] = nums[r]
                w += 1
        return w