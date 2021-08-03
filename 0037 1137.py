class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            ll = 0
            la = 1
            cur = 1
            p = 2
            while p<n:
                p+=1
                ll,la,cur=la,cur,ll+la+cur
            return cur
