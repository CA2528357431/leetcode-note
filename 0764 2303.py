class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        if income <= brackets[0][0]:
            return income * brackets[0][1] / 100

        res = brackets[0][0] * brackets[0][1]

        for i in range(1, len(brackets)):
            u, r = brackets[i]
            pu, _ = brackets[i - 1]
            if u >= income:
                res += (income - pu) * r
                break
            else:
                res += (u - pu) * r

        return res / 100