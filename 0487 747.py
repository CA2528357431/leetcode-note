class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        big = -1
        small = -1
        for i in  range(len(nums)):
            if big == -1:
                big = i
            elif small == -1:
                if nums[big]>nums[i]:
                    small = i
                else:
                    small = big
                    big = i
            else:
                if nums[i]>nums[big]:
                    small = big
                    big = i
                elif nums[i]>nums[small]:
                    small = i
        if nums[big]>=nums[small]*2:
            return big
        else:
            return -1