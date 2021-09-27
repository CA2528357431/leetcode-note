class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        l = 0
        r = 0
        if nums[0]>nums[-1]:
            l = 0
            r = len(nums) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid

        for x in range(0, (l - 0) // 2 + 1):
            nums[x], nums[0 + l - x] = nums[0 + l - x], nums[x]
        for x in range(r, (len(nums) - 1 + r) // 2 + 1):
            nums[x], nums[r + len(nums) - 1 - x] = nums[r + len(nums) - 1 - x], nums[x]



        def tran(x):
            if x >= r:
                return r + len(nums) - 1 - x
            else:
                return 0 + l - x

        ll = 0
        rr = len(nums) - 1
        while ll < rr:
            mid = (ll + rr) // 2
            if nums[mid] > target:
                ll = mid + 1
            elif target > nums[mid]:
                rr = mid - 1
            else:
                ll = mid
                break
        if nums[ll] == target:
            return tran(ll)
        else:
            return -1
        '''


        '''
        l = 0
        r = 0
        if nums[0]>nums[-1]:
            l = 0
            r = len(nums) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid

        def tran(x):
            if x >= r:
                return r + len(nums) - 1 - x
            else:
                return 0 + l - x

        neol = 0
        neor = len(nums)-1
        while neol <= neor:
            neomid = (neol + neor) // 2
            mid = tran(neomid)
            if nums[mid] > target:
                neol = neomid + 1
            elif target > nums[mid]:
                neor = neomid - 1
            else:
                return mid
        return -1
        '''

        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        if nums[l]==target:
            return l
        else:
            return -1