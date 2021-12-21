class Solution:
    def dayOfYear(self, date: str) -> int:
        dic = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        li = date.split("-")
        y,m,d = int(li[0]),int(li[1]),int(li[2])
        if (y%400==0) or (y%100!=0 and y%4==0):
            dic[2]+=1
        res = d
        for i in range(1,m):
            res+=dic[i]
        return res