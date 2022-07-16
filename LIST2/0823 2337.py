class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = "".join(start.split("_"))
        t = "".join(target.split("_"))
        if s != t:
            return False

        n = len(start)
        j = -1
        for i in range(n):
            c = target[i]
            if c == "_":
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