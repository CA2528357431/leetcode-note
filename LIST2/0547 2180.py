class Solution:
    def countEven(self, num: int) -> int:
        def judge(x):
            cur = 0
            while x:
                cur+=x%10
                x//=10
            if cur%2==0:
                return True
            else:
                return False
        res = 0
        for i in range(1,num+1):
            if judge(i):
                res+=1
        return res