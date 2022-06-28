class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a) - 1
        lb = len(b) - 1
        res = ""
        judge = False
        while la >= 0 or lb >= 0:
            neo = 0
            if judge:
                neo += 1
                judge = False

            if la >= 0:
                neo += int(a[la])
                la -= 1

            if lb >= 0:
                neo += int(b[lb])
                lb -= 1

            if neo >= 2:
                judge = True
                neo -= 2
                res = str(neo) + res
            else:
                res = str(neo) + res
        if judge:
            res = "1" + res
        return res