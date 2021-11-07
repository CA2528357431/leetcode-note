class Solution:
    def mySqrt(self, x: int) -> int:
        cur = 1
        while cur*cur<=x:
            cur = (cur+x//cur)//2
            print(cur)
        return cur-1
sol = Solution()
sol.mySqrt(4)