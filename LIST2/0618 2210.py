class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        cur = nums[0]
        up = 0
        for i in range(1,len(nums)):
            num = nums[i]
            if num>cur:
                if up == -1:
                    res+=1
                up = 1
            elif num<cur:
                if up==1:
                    res+=1
                up = -1
            cur = num
        return res