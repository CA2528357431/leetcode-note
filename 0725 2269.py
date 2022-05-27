class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        res = 0
        for i in range(n-k+1):
            snum = int(s[i:i+k])
            if snum==0:
                continue
            if num%snum==0:
                res+=1
        return res