import heapq


class Solution:
    def maxmiumScore(self, cards, cnt: int) -> int:
        for i in range(len(cards)):
            cards[i] = -cards[i]

        heapq.heapify(cards)
        single = []
        double = []
        snum = 0
        s = 0
        while cards:
            neo = -heapq.heappop(cards)
            if neo % 2 == 0:
                double.append(neo)
            else:
                s += neo
                snum += 1
                if snum == 2:
                    single.append(s)
                    s = 0
                    snum = 0
        res = 0
        si = 0
        di = 0
        while cnt > 1:
            if (di + 1 >= len(double) and si < len(single)) or single[si] >= double[di] + double[di + 1]:
                res += single[si]
                si += 1
                cnt -= 2
            elif (di + 1 < len(double) and si >= len(single)) or single[si] < double[di] + double[di + 1]:
                res += double[di] + double[di + 1]
                di += 2
                cnt -= 2
            else:
                return 0

        if cnt == 1:
            if di >= len(double):
                return 0
            else:
                return res + double[di]

        else:
            return res

sol = Solution












