class Solution:
    def thirdMax(self, nums) -> int:
        if len(nums)<3:
            return max(nums)

        a = None
        b = None
        c = None
        for n in nums:
            if a is None or n>a:
                a,b,c = n,a,b
            elif b is None or n>b:
                b,c = n,b
            else:
                c = n
        if a==b or b==c:
            return a
        else:
            return c
sol = Solution()
x = sol.thirdMax([3,2,1])
print(x)