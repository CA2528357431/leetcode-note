class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        cur = 0
        res = -1

        zero = 0
        one = 0
        for c in s:
            if c=="0":
                zero+=1
            else:
                one+=1


        for i in range(n-1):
            c = s[i]
            if c=="0":
                cur+=1
            ones = one-(i+1-cur)
            res = max(res,cur+ones)
        return res
