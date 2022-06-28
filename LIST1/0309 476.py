class Solution:
    def findComplement(self, num: int) -> int:
        neo = bin(num)
        l = len(neo) - 2
        order = 2 ** l - 1

        return order ^ num