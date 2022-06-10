class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            li = []

            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    li.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    li.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = li
        return nums[0]