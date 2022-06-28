class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1 = num1.split("+")
        n2 = num2.split("+")

        n1[-1] = n1[-1][:-1]
        n2[-1] = n2[-1][:-1]

        for i in range(2):
            n1[i] = int(n1[i])
            n2[i] = int(n2[i])

        res1 = n1[0] * n2[0] - n1[1] * n2[1]
        res2 = n1[1] * n2[0] + n1[0] * n2[1]

        return str(res1) + "+" + str(res2) + "i"