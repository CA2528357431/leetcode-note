class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (right+left)//2
            if target<nums[mid]:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
        return -1

    # while条件：
    # 最后一次查询是 l=r
    # 如还不成功则tar不存在