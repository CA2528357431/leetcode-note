class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    res+=1
        return res