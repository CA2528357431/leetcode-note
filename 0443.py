class Solution:
    def minimumBuckets(self, street: str) -> int:

        n = len(street)

        for i in range(n):
            if street[i] == "H" and (i - 1 < 0 or street[i - 1] == "H") and (i + 1 >= n or street[i + 1] == "H"):
                return -1

        res = 0
        i = 0
        while i < n:

            if street[i] == "H":
                res += 1
                if i + 2 < n and street[i + 2] == "H":
                    i += 3
                else:
                    i += 1
            else:
                i += 1
        return res
