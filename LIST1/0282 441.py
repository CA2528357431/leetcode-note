class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n//2+1
        while l<r:
            mid = (l+r)//2+1
            if (1+mid)*mid//2<n:
                l = mid
            elif n<(1+mid)*mid//2:
                r = mid-1
            else:
                return mid
        return l