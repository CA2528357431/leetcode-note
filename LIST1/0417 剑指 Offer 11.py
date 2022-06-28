class Solution:
    def minArray(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            while nums[l] == nums[r] and l < r:
                r -= 1

            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            elif nums[l] <= nums[mid]:
                l = mid + 1

        return nums[l]