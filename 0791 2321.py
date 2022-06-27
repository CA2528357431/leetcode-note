class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        delta1 = [0] * n
        for i in range(n):
            delta1[i] = nums2[i] - nums1[i]

        dp = [0] * n
        dp[0] = delta1[0]
        for i in range(1, n):
            dp[i] = max(delta1[i], delta1[i] + dp[i - 1])
        res1 = max(max(dp), 0) + sum(nums1)

        delta2 = [0] * n
        for i in range(n):
            delta2[i] = nums1[i] - nums2[i]

        dp = [0] * n
        dp[0] = delta2[0]
        for i in range(1, n):
            dp[i] = max(delta2[i], delta2[i] + dp[i - 1])
        res2 = max(max(dp), 0) + sum(nums2)

        return max(res1, res2)