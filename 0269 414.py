class Solution:
    def thirdMax(self, nums) -> int:
        if len(nums)<3:
            return max(nums)

        a = None
        b = None
        c = None
        for n in nums:
            if n==a or n==b or n==c:
                continue
            if a is None or n>a:
                a,b,c = n,a,b
            elif b is None or n>b:
                b,c = n,b
            elif c is None or n>c:
                c = n
        if b is None or c is None:
            return a
        else:
            return c