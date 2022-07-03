class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        near = {}
        gas = {}
        for i in range(len(stations)):
            if i == 0:
                near[0] = stations[0][0]
            else:
                near[stations[i - 1][0]] = stations[i][0]
            gas[stations[i][0]] = stations[i][1]

        cnt = 0

        heap = []
        s = 0

        cur = startFuel
        sp = 0

        while True:

            if cur + sp >= target:
                return cnt

            if sp not in near:
                nxt = target
                dis = nxt - sp

                if s + cur < dis:
                    return -1

                while dis > cur:
                    neo = -heappop(heap)
                    cur += neo
                    cnt += 1
                    s -= neo
                return cnt

            nxt = near[sp]
            dis = nxt - sp

            if s + cur < dis:
                return -1

            while dis > cur:
                neo = -heappop(heap)
                cur += neo
                cnt += 1
                s -= neo
            cur -= dis
            heappush(heap, -gas[nxt])
            s += gas[nxt]
            sp = nxt

