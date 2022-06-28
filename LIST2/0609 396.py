class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        big = 0
        n = len(nums)
        for i in range(n):
            big+=i*nums[i]
        cur = big
        for i in range(n-1,0,-1):
            cur = cur+s-n*nums[i]
            big = max(big,cur)
        return big
