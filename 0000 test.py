class Solution:
    def firstMissingPositive(self, nums) -> int:
        for x in range(len(nums)):
            if nums[x]<=len(nums) and nums[x]>=1:
                i = nums[x]
                nums[i-1],nums[x] = nums[x],nums[i-1]
                print(nums,x,i)
        for x in range(len(nums)):
            if nums[x]!=x+1:

                return x+1
        print(nums)
        return len(nums)+1





sol = Solution()
sol.firstMissingPositive([3,4,-1,1])