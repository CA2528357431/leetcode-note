class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid
                r = mid
        if nums[l] != target:
            return [-1, -1]

        while l - 1 >= 0 and nums[l - 1] == target:
            l -= 1
        while r + 1 < len(nums) and nums[r + 1] == target:
            r += 1
        return [l, r]
        '''

        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        # get r range
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

        # get l range
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

