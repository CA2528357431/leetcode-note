class Solution:
    def binaryGap(self, n: int) -> int:
        string = bin(n)[2:]
        res = 0
        n = len(string)
        pre = -1
        for i in range(n):
            if string[i]=="1":
                pre=i
                break
        if pre<0:
            return 0
        for i in range(pre+1,n):
            c = string[i]
            if c=="1":
                res = max(res,i-pre)
                pre = i
        return res