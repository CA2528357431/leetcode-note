class Solution:
    def maxSubarraySumCircular(self, nums):

        cur = nums[0]
        big = cur
        for x in range(1, len(nums)):
            cur = max(nums[x], nums[x]+cur)
            big = max(big,cur)
        # 不分两部分

        if big<=0:
            return big

        # 问题出在
        # small的求值时，有可能把整个数组都加进去，导致sum-small为空组
        # 只有整个数组全<=0时才可能如上
        # 此时当且仅当big<=0

        cur = nums[0]
        small = cur
        for x in range(1, len(nums)):
            cur = min(nums[x], nums[x] + cur)
            small = min(small, cur)

        return max(small,big)


sol = Solution()
sol.maxSubarraySumCircular([5,-3,5])