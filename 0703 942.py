class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        used = set()
        n = len(s)
        res = [0]*(n+1)
        big = n
        small = 0

        for i in range(n):
            if s[i]=="D":
                res[i] = big
                big-=1
            else:
                res[i] = small
                small+=1

        res[-1] = small

        return res
# https://leetcode-cn.com/problems/di-string-match/solution/zeng-jian-zi-fu-chuan-pi-pei-by-leetcode-jzm2/