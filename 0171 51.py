class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        line = []
        minus = []
        plus = []

        res = []

        def do(x):
            if x == n:
                res.append(line.copy())
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

        squares = []

        for item in range(len(res)):
            square = []
            for x in range(n):
                neo = ["."] * n
                neo[res[item][x]] = "Q"
                square.append("".join(neo))
            squares.append(square)

        return squares