class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        # get r
        l = 0
        r = len(nums) - 1
        while l < r :
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        if nums[l]!=target:
            return [-1,-1]

        # get l
        ll = 0
        rr = len(nums) - 1
        while ll < rr :
            mid = (ll + rr) // 2
            if target <= nums[mid]:
                rr = mid
            else:
                ll = mid + 1
        if nums[rr]!=target:
            return [-1,-1]

        return [rr, r]

sol = Solution()
x = sol.searchRange([5,7,7,8,8,10],6)
print(x)