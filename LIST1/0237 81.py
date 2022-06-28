class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        n = len(nums)
        if n==1:
            return nums[0]==target
        l = 0
        r = 0
        if nums[0]>=nums[-1]:
            l = 0
            while l+1<n-1 and nums[l]<=nums[l+1]:
                l+=1
            r = l+1
        def tran(x):
            if x >= r:
                return r + len(nums) - 1 - x
            else:
                return 0 + l - x

        neol = 0
        neor = len(nums)-1
        while neol < neor:
            neomid = (neol + neor) // 2
            mid = tran(neomid)
            if nums[mid] > target:
                neol = neomid + 1
            elif target > nums[mid]:
                neor = neomid - 1
            else:
                return True
        return nums[tran(neol)]==target
        '''

        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            # 要么 r<=l<=mid 要么 mid<=l<=r
            if nums[l]==nums[mid]==nums[r]:
                l+=1
                r-=1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return nums[l]==target


    # https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-ii-by-l-0nmp/