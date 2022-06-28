class Solution:
    def isHappy(self, n: int) -> bool:
        def next(num):
            s=0
            while num>0:
                s+=(num%10)*(num%10)
                num=num//10
            return s
        s=next(n)
        f=next(s)
        while f!=s:
            f=next(f)
            f=next(f)
            s=next(s)
        if f==1:
            return True
        return False