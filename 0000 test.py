import time


class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        if n==1:
            return nums[0] == target

        l = 0
        while l+1<n-1 and nums[l]<=nums[l+1]:
            l+=1
        r = l+1
        if nums[-1] < target < nums[0] or target > nums[l] or target < nums[r]:
            return False

        rr = n - 1
        ll = 0
        if target <= nums[-1]:
            ll = r
        else:
            rr = l



        while ll < rr:
            mid = (ll + rr) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                ll = mid + 1
            else:
                rr = mid - 1

        return nums[ll] == target
sol = Solution()
x = sol.search([1,1],2)
print(x)