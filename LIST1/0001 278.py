class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    # 二分法
    # right = mid 无加一，mid可能是最终结果
    # while条件控制 无等号，最终条件是 l = r
    #