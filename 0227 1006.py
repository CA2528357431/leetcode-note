class Solution:
    def clumsy(self, n: int) -> int:
        i = 0
        pos = True
        re = n
        res = 0
        for x in range(n-1,0,-1):
            if i%4==0:
                re *= x
            elif i%4==1:
                re //= x
                if pos:
                    res+=re
                    pos = False
                else:
                    res-=re

            elif i%4==2:
                res += x
            else:
                re = x
            i+=1

        i-=1
        if i%4==0 or i%4==3:
            if pos:
                res += re
            else:
                res -= re

        return res
sol = Solution()
x = sol.clumsy(3)
print()
print(x)