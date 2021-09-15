class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                return mid

            if mid < 0 or nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                r = mid

        return l


