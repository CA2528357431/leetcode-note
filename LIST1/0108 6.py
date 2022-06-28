class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for x in range(numRows)]
        cur = 0
        par = 0
        judge = 1
        for char in s:
            if judge == 1:
                res[cur] += char
                if cur < numRows - 1:
                    cur += 1
                else:
                    judge = 0
                    cur -= 1

            else:
                res[cur] += char
                if cur > 0:
                    cur -= 1
                else:
                    judge = 1
                    cur += 1
        re = ""
        for x in res:
            re += x

        return re