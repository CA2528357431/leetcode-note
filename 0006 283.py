class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        f = 0
        s = 0
        while f < len(nums):
            if nums[f] != 0:
                nums[f], nums[s] = nums[s], nums[f]
                s += 1
            f +=1

        # s之前的数是排好的非零数
        # f捕获非零数，扔到s处即可


