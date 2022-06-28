class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(0, len(nums) // 2):
            nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]

        for i in range(0, k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        for i in range(k, (len(nums) + k) // 2):
            nums[i], nums[k + len(nums) - 1 - i] = nums[k + len(nums) - 1 - i], nums[i]

        return nums

    # 交换 整体的两个部分 的次序？
    # 不妨先把整体反转 再反转局部