class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1:
            return []
        cur = 2
        res = []
        while True:
            if finalSum<cur*2+2:
                res.append(finalSum)
                return res
            else:
                res.append(cur)
                finalSum-=cur
                cur+=2
        return finalSum