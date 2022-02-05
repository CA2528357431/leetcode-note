class Solution:
    def minimumSum(self, num: int) -> int:
        li = [0]*4
        for i in range(4):
            neo = num%10
            li[i] = neo
            num = num//10
        li.sort()
        res1 = (li[0]+li[1])*10+li[2]+li[3]
        res2 = li[0]*100+li[1]*10+li[2]+li[3]
        return min(res1,res2)