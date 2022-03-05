class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        def deal(x):
            res = 0
            for i in quantities:
                res+=i//x
                if i%x!=0:
                    res+=1
            return res<=n

        while l<r:
            mid = (l+r)//2
            if deal(mid):
                r = mid
            else:
                l = mid+1
        return r