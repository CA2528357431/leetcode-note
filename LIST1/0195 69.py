class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        r = x // 2 + 1
        l = 1
        while l < r:
            mid = (l + r) // 2 + 1
            neo = mid * mid
            if neo == x:
                return mid
            if neo < x:
                l = mid
            else:
                r = mid - 1
        return l
