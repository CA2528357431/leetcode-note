class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def hdiv(dividend, divisor):
            a = dividend
            b = divisor
            flag = 1
            if (a > 0 and b > 0) or (a < 0 and b < 0):
                flag = 1
            else:
                flag = -1

            a = abs(a)
            b = abs(b)

            quotient = a // b
            remainder = a % b

            if remainder == 0:
                return str(quotient * flag)

            ans = [str(quotient), '.']
            repeats = dict()
            i = 2
            for _ in range(10000):
                a = remainder * 10
                quotient = a // b
                remainder = a % b
                if a in repeats:
                    ans.insert(repeats[a], '(')
                    ans.append(')')
                    break
                ans.append(str(quotient))
                repeats[a] = i
                if remainder == 0:
                    break
                i += 1

            if flag == -1:
                return '-' + ''.join(ans)
            return ''.join(ans)

        return hdiv(numerator, denominator)