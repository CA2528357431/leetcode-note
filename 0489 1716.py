class Solution:
    def totalMoney(self, n: int) -> int:
        base=(1+7)*7//2
        week=n//7
        start=week+1
        res=(base*2+(week-1)*7)*week//2
        for i in range(n%7):
            res+=start
            start+=1
        return res