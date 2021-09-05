class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pro = 0
        res = ""
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:

            a1 = 0
            if i >= 0:
                a1 = int(num1[i])
            a2 = 0
            if j >= 0:
                a2 = int(num2[j])

            s = a1 + a2 + pro
            pro = s // 10
            res = str(s % 10) + res

            i -= 1
            j -= 1

        if pro:
            res = "1" + res
        return res