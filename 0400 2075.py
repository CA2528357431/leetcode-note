class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        lines = n // rows
        if n % rows != 0:
            lines += 1
        li = [[" "] * lines for _ in range(rows)]
        for i in range(n):
            x = i // lines
            y = i % lines
            li[x][y] = encodedText[i]

        res = []
        for x in range(lines):
            for y in range(rows):
                if x + y >= lines:
                    break
                xx = x + y
                yy = y
                res.append(li[yy][xx])
        return "".join(res).rstrip()