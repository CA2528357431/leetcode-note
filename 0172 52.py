class Solution:
    def totalNQueens(self, n: int) -> int:
        line = []
        minus = []
        plus = []

        res = 0

        def do(x):

            nonlocal res

            if x == n:
                res+=1
                return
            for y in range(n):
                if (y in line) or (x + y in plus) or (x - y in minus):
                    continue
                line.append(y)
                plus.append(x + y)
                minus.append(x - y)
                do(x + 1)
                line.pop()
                plus.pop()
                minus.pop()

        do(0)
        return res