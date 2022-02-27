class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def do(t):
            res = 0
            for x in time:
                res += t // x
            return res

        l = 1
        r = max(time) * totalTrips

        while l < r:
            mid = (l + r) // 2
            tt = do(mid)
            if tt < totalTrips:
                l = mid + 1
            else:
                r = mid
        return l