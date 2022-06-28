class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    res+=1
        return res