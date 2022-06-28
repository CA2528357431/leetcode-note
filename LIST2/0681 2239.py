class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        cur = nums[0]
        for num in nums:
            if abs(num)<abs(cur):
                cur = num
            elif abs(num)==abs(cur):
                cur = max(cur,num)
        return cur