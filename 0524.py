class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        def do(m, s):
            m1 = m // 10
            m2 = m % 10
            s1 = s // 10
            s2 = s % 10

            moves = 0
            pushs = 0

            if m1 != 0:
                pushs = 4
                if startAt != m1:
                    moves += 1
                if m1 != m2:
                    moves += 1
                if m2 != s1:
                    moves += 1
                if s1 != s2:
                    moves += 1
            elif m2 != 0:
                pushs = 3
                if startAt != m2:
                    moves += 1
                if m2 != s1:
                    moves += 1
                if s1 != s2:
                    moves += 1
            elif s1 != 0:
                pushs = 2
                if startAt != s1:
                    moves += 1
                if s1 != s2:
                    moves += 1
            else:
                pushs = 1
                if startAt != s2:
                    moves += 1

            return moves * moveCost + pushs * pushCost

        minute1 = targetSeconds // 60
        second1 = targetSeconds % 60

        minute2 = minute1 - 1
        second2 = second1 + 60

        res = 9999999
        if minute1 < 100:
            neo = do(minute1, second1)
            res = min(res, neo)

        if second2 <= 99 and minute2 >= 0:
            neo = do(minute2, second2)
            res = min(res, neo)

        return res