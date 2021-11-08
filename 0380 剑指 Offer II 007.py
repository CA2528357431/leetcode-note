class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=2:
            return []

        nums.sort()

        res = []

        n = len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a = nums[i]

            if i<n-2 and a+nums[i+1]+nums[i+2]>0:
                break

            l = i+1
            r = n-1
            while l<r:
                if a+nums[l]+nums[r]==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif a+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return res