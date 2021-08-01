class Solution:
    def climbStairs(self, n: int) -> int:

        # 乘法递归

        # 取n//2
        # res = f(n//2)*f(n-n//2)
        # 不取n//2 --- 必然走n//2-1、n//2+1
        # res = f(n//2-1)*f(n-n//2-1)


        '''
        if n == 1:
            return 1
        elif n == 0:
            return 1
        else:
            return self.climbStairs(n//2) * self.climbStairs(n - n//2) + self.climbStairs(n//2-1) * self.climbStairs(n - n//2-1)
        '''

        # 滚动法
        p = 1
        la = 1
        cur = 1
        while p<n:
            p+=1
            la,cur = cur,la+cur
        return cur