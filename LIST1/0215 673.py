class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1]*n
        num = [1]*n

        l = 1
        res = 1

        for i in range(1,n):
            for ii in range(i):
                if nums[ii]<nums[i]:
                    if length[ii]+1==length[i]:
                        num[i]+=num[ii]
                    elif length[ii]+1>length[i]:
                        num[i]=num[ii]
                        length[i]=length[ii]+1
            if length[i]==l:
                res += num[i]
            elif length[i]>l:
                res = num[i]
                l = length[i]

        return res