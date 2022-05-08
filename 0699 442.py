class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [nums[i] for i in range(n) if nums[i] != i + 1]

    # 数据在1-n，因此尝试将num放到对应的index处，最后num与index不一致的数字是答案


