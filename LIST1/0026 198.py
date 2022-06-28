class Solution:
    def rob(self, nums):

        # 递归

        '''
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        else:
            a = self.rob(nums[:len(nums)//2])
            b = self.rob(nums[len(nums)//2+1:])

            c = self.rob(nums[:len(nums)//2-1])
            d = self.rob(nums[len(nums)//2+2:])

            return max(a+b, c+d+nums[len(nums)//2] )
        '''


        # 动态规划

        # 递归是大数需要小数支持，因此计算小数
        # f(n) = f(n-1)+f(n-2)
        # f(n-1) = ...   f(n-2) = ...
        # 动规是先计算小数，有小数逐层推出大数
        # f(1) = ...   f(2) = ...
        # f(n-1) = ...   f(n-2) = ...
        # f(n) = f(n-1)+f(n-2)


        # res[r]
        # 表示劫掠0-r房子的max收益

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        res = [0]*len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            res[i] = max(res[i-2]+nums[i],res[i-1])
        return res[-1]

sol = Solution()
print(sol.rob([1,2,3,1]))


