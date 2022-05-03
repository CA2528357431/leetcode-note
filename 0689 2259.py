class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        big = -1
        for i in range(len(number)):
            if number[i] == digit:
                cpy = list(number)
                cpy.pop(i)
                big = max(big, int("".join(cpy)))
        return str(big)
