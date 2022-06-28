class Solution:
    def solveEquation(self, equation: str) -> str:
        li = equation.split("=")
        l = li[0]
        r = li[1]

        def deal(string):
            xnum = 0
            nnum = 0
            cur = 0
            add = 1
            ty = 1
            for i in range(len(string)):
                c = string[i]
                if c == "+":

                    if ty == 0:
                        xnum += cur * add
                    else:
                        nnum += cur * add
                    cur = 0
                    add = 1
                    ty = 1
                elif c == "-":

                    if ty == 0:
                        xnum += cur * add
                    else:
                        nnum += cur * add
                    cur = 0
                    add = -1
                    ty = 1

                elif c == "x":
                    if cur == 0 and not (i - 1 >= 0 and string[i - 1] == "0"):
                        cur = 1
                    ty = 0

                else:
                    cur = cur * 10 + int(c)
            if ty == 0:
                xnum += cur * add
            else:
                nnum += cur * add

            return xnum, nnum

        xl, nl = deal(l)
        xr, nr = deal(r)

        xres = xl - xr
        nres = nr - nl

        if xres == 0:
            if nres == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return "x=" + str(nres // xres)