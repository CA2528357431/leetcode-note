class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            res = piles[0] // h
            if piles[0] % h:
                res += 1
            return res
        r = max(piles)
        l = 1
        while l < r:
            mid = (l + r) // 2
            cur = 0
            for x in piles:
                cur += x // mid
                if x % mid:
                    cur += 1
            if cur <= h:
                r = mid
            else:
                l = mid + 1
        return l
