class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return left


        # left = 3 right = 4 mid = 3
        # left = 4 right = 4 mid = 4
        # left = 4 right = 3
        # insert 到4
        # left