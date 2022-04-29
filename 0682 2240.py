class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cnt = 0

        one = 0
        while True:
            neo = total-cost1*one
            if neo<0:
                return cnt
            cnt+=neo//cost2+1
            one+=1