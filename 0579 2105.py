class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants)-1
        lcur = capacityA
        rcur = capacityB
        res = 0
        while l<r:
            if plants[l]>lcur:
                res+=1
                lcur = capacityA
            if plants[r]>rcur:
                res+=1
                rcur = capacityB
            lcur-=plants[l]
            rcur-=plants[r]
            l+=1
            r-=1
        if l==r:
            if plants[l]>lcur and plants[l]>rcur:
                res+=1
        return res