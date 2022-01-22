class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)

        c = 0
        j = n - 1
        while c < 2 and j >= 0:
            if corridor[j] == "S":
                c += 1
            j -= 1
        if c < 2:
            return 0
        last = j

        def deal(i):
            if i >= last:
                return 1
            cur = 0
            while cur < 2 and i <= last:
                if corridor[i] == "S":
                    cur += 1
                i += 1
            if cur < 2:
                return 0
            mul = 1
            while corridor[i] == "P" and i <= last:
                mul += 1
                i += 1
            return mul * deal(i)

        i = 0
        while corridor[i] == "P":
            i += 1

        return deal(i) % (1000000007)