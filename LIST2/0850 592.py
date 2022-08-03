class Solution:
    def fractionAddition(self, expression: str) -> str:

        if expression[0] not in "+-":
            expression = "+" + expression
        cura, curb = 0, 1
        sign = 1

        i = 0
        while i < len(expression):
            if expression[i] == "+":
                sign = 1
            else:
                sign = -1
            i += 1
            a = 0
            b = 0
            while expression[i] != "/":
                a = a * 10 + int(expression[i])
                i += 1
            i += 1
            while i < len(expression) and expression[i] not in "+-":
                b = b * 10 + int(expression[i])
                i += 1

            neoa = cura * b + curb * a * sign
            neob = b * curb

            if neoa != 0:
                div = gcd(abs(neoa), neob)
                neoa //= div
                neob //= div
            else:
                neob = 1

            cura = neoa
            curb = neob
        return str(cura) + "/" + str(curb)




