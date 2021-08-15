class Solution:
    def integerBreak(self, n: int) -> int:
        res = [0]*(n+1)
        res[1]=1
        for x in range(2,n+1):
            for y in range(1,x//2+1):
                a = max(res[y],y)
                b = max(res[x-y],x-y)
                res[x] = max(res[x],a*b)
        return res[-1]

# res[x]表示对x求最大乘积
# 取因数的时候 如 x = a+b
#  max(a,res[a])    max(b,res[b])
# res中的数字至少拆分为两个因数，而作为因数的时候可以不拆分