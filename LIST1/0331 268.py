class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        re = (n+1)*n//2
        s = sum(nums)
        return re-s