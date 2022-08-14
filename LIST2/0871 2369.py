class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            res = False
            if nums[i - 1] == nums[i - 2]:
                res = res or dp[i - 2]
            if i >= 3:
                if i == n:
                    print(nums[i - 1] == nums[i - 2] + 1)
                    print(nums[i - 2] == nums[i - 3] + 1)
                if nums[i - 1] == nums[i - 2] == nums[i - 3]:
                    res = res or dp[i - 3]
                if nums[i - 1] == nums[i - 2] + 1 and nums[i - 2] == nums[i - 3] + 1:
                    # print(111111)
                    res = res or dp[i - 3]
            dp[i] = res

        return dp[-1]
