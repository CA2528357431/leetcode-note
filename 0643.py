class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        li = start^goal
        cnt = 0
        i = 1
        while i<=li:
            if i&li:
                cnt+=1
            i = i*2
        return cnt