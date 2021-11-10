class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                return nums[i]
            else:
                used.add(nums[i])