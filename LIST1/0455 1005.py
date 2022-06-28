class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg = 0
        for num in nums:
            if num<0:
                neg+=1
        res = 0
        if neg>=k:
            nums.sort()
            for num in nums:
                if k>0:
                    res-=num
                    k-=1
                else:
                    res+=num
        else:
            k = (k-neg)%2
            if not k:
                for num in nums:
                    res+=abs(num)
            else:
                nums.sort(key=lambda x:abs(x))
                for i in range(1,len(nums)):
                    res+=abs(nums[i])
                res-=abs(nums[0])


        return res