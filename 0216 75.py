class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        for num in nums:
            if num==0:
                r+=1
            elif num==1:
                w+=1
        for i in range(len(nums)):
            if r:
                r-=1
                nums[i] = 0
            elif w:
                w-=1
                nums[i] = 1
            else:
                nums[i] = 2