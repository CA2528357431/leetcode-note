class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False



        v = s // 2
        dp = [[False] * (n + 1) for _ in range(v + 1)]

        # n件商品
        # v的容积
        # dp[vv][ii]表示考虑ii件物品，能否凑出vv重量

        for i in range(n + 1):
            dp[0][i] = True

        for vv in range(1, v + 1):
            for ii in range(1, n + 1):
                weight = nums[ii - 1]
                if vv >= weight and dp[vv - weight][ii - 1]:
                    dp[vv][ii] = True
                if dp[vv][ii - 1]:
                    dp[vv][ii] = True
        return dp[-1][-1]

