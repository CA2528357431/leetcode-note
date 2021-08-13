class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:


        # 动态规划
        # 很难想

        '''
        up = [1] * len(nums)
        down = [1] * len(nums)


        # https://leetcode-cn.com/problems/wiggle-subsequence/solution/zheng-ming-wei-shi-yao-dong-tai-gui-hua-97d4m/


        for x in range(1, len(nums)):
            if nums[x] > nums[x - 1]:
                up[x] = max(down[x - 1] + 1, up[x - 1])
                down[x] = down[x - 1]
            elif nums[x] < nums[x - 1]:
                down[x] = max(down[x - 1], up[x - 1] + 1)
                up[x] = up[x - 1]
            else:
                up[x] = up[x - 1]
                down[x] = down[x - 1]

        return max(up[-1], down[-1])
        '''

        # 贪心

        # 捕捉拐点

        res = 1
        trend = 0
        for x in range(1, len(nums)):
            if nums[x-1]<nums[x] and trend<=0:
                trend=1
                res+=1
            elif nums[x-1]>nums[x] and trend>=0:
                trend=-1
                res+=1
        return res
