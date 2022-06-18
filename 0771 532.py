class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()
        cnt = 0
        n = len(nums)
        j = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < n and (j <= i or nums[j] < nums[i] + k):
                j += 1
            if j < n and nums[j] == nums[i] + k:
                cnt += 1
        return cnt

