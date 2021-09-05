class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def addStrings(num1, num2):
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

        res = ""
        for i in range(len(num1))[::-1]:
            re = "0" * (len(num1)-1-i)
            pro = 0
            a1 = int(num1[i])
            for j in range(len(num2))[::-1]:
                a2 = int(num2[j])
                s = a1 * a2 + pro
                pro = s // 10
                re = str(s % 10) + re
            if pro:
                re = str(pro)+re
            res = addStrings(res, re)
        return res

sol = Solution()
sol.multiply("123","456")