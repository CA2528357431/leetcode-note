class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, r = 1, x
        while l < r:
            mid = (l + r) // 2 + 1

            if mid * mid > x:
                r = mid - 1
            else:
                l = mid
        return l