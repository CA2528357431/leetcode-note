class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        cur = 0
        for i in range(len(timeSeries)):
            if cur<=timeSeries[i]:
                res+=duration
            else:
                neo = timeSeries[i]+duration-cur
                res+=neo

            cur = timeSeries[i]+duration
        return res