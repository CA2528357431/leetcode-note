class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        n = len(nums)
        if n<3:
            return 0
        dp =[0]*n
        for x in range(2,n):
            if nums[x]-nums[x-1]==nums[x-1]-nums[x-2]:
                dp[x] = 1+dp[x-1]
        return sum(dp)
        '''

        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        dp = 0
        for x in range(2, n):
            if nums[x] - nums[x - 1] == nums[x - 1] - nums[x - 2]:
                dp = 1 + dp
            else:
                dp = 0
            ans+=dp
        return dp
