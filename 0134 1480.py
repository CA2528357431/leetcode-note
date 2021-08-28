class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for x in range(1,len(res)):
            res[x] = res[x-1]+nums[x]
        return res