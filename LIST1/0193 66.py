class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        l = len(digits)
        for i in range(l - 1, 0, -1):
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i - 1] += 1

        if digits[0] >= 10:
            res = []
            res.append(1)
            res.append(digits[0] - 10)
            for i in range(1, l):
                res.append(digits[i])
            return res
        else:
            return digits

