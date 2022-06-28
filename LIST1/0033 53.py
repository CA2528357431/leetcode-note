class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # 原始的递归

        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        left = self.maxSubArray(nums[:len(nums) // 2])
        right = self.maxSubArray(nums[len(nums) // 2:])

        rp = len(nums) // 2
        lp = len(nums) // 2 - 1
        lm = nums[len(nums) // 2 - 1]
        l = nums[len(nums) // 2 - 1]
        rm = nums[len(nums) // 2]
        r = nums[len(nums) // 2]

        while lp >= 1:
            lp -= 1
            l += nums[lp]
            lm = max(lm, l)
        while rp <= len(nums) - 2:
            rp += 1
            r += nums[rp]
            rm = max(rm, r)
        mid = lm + rm

        return max(left, mid, right)
        '''

        # 动态规划

        # 所求的last表示以i为结尾的最大值

        last = nums[0]
        ma = nums[0]
        for i in range(1, len(nums)):
            last = max(last + nums[i], nums[i])
            ma = max(ma, last)
        return ma