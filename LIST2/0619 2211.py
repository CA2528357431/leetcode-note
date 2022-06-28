class Solution:
    def countCollisions(self, directions: str) -> int:

        def dol(s):
            i = 0
            while i < len(s) and s[i] == "L":
                i += 1
            return i

        def dor(s):
            i = len(s) - 1
            while i >= 0 and s[i] == "R":
                i -= 1
            return i

        l = dol(directions)
        r = dor(directions)
        s = directions[l:r + 1]
        li = s.split("RL")
        res = (len(li) - 1) * 2
        for ss in li:
            ll = ss.split("S")
            for sss in ll:
                res += len(sss)

        return res
