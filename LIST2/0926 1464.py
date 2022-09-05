class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for ii in range(n):
            if nums[ii] > nums[i]:
                i = ii
        j = 0
        if i == 0:
            j = 1
        for ii in range(n):
            if ii == i:
                continue
            if nums[ii] > nums[j]:
                j = ii
        # print(i,j)

        return (nums[i] - 1) * (nums[j] - 1)

