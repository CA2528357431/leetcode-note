class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = "".join(start.split("X"))
        t = "".join(end.split("X"))
        if s != t:
            return False

        n = len(start)
        j = -1
        for i in range(n):
            c = end[i]
            if c == "X":
                continue
            elif c == "R":
                j += 1
                while start[j] != "R":
                    j += 1
                if i < j:
                    return False
            else:
                j += 1
                while start[j] != "L":
                    j += 1
                if i > j:
                    return False
        return True