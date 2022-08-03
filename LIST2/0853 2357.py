class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        while nums[-1]>0:
            res+=1
            i = 0
            while nums[i]==0:
                i+=1
            x = nums[i]
            for j in range(i,n):
                nums[j]-=x
        return res