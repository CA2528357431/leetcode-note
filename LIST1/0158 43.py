class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        if num1 == "0" or num2 == "0":
            return "0"

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
            re = "0" * (len(num1) - 1 - i)
            pro = 0
            a1 = int(num1[i])
            for j in range(len(num2))[::-1]:
                a2 = int(num2[j])
                s = a1 * a2 + pro
                pro = s // 10
                re = str(s % 10) + re
            if pro:
                re = str(pro) + re
            res = addStrings(res, re)
        return res
        '''

        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        li = [0]*(m+n)
        for x in range(m)[::-1]:
            xx = int(num1[x])
            for y in range(n)[::-1]:
                li[x+y+1] += xx*int(num2[y])
        for i in range(m+n)[::-1]:
            li[i-1] += li[i]//10
            li[i] = li[i]%10
        if li[0]!=0:
            return "".join(str(x) for x in li)
        else:
            return "".join(str(x) for x in li[1:])