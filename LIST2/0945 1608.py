class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            bigger = n - i
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] < bigger <= nums[i] or i == 0 and bigger <= nums[i]:
                return bigger

        return -1
