class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        res = [0]*len(nums)
        u = len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[u] = nums[l]**2
                l += 1
            else:
                res[u] = nums[r]**2
                r -= 1
            u -= 1
        return res

    # 如果知道结果数组的大小，不妨先开辟空间，再赋值
    # 避免反转操作？  用另一个指针从后往前赋值