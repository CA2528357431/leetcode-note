class Solution:
    def bitwiseComplement(self, n: int) -> int:
        neo = bin(n)
        l = len(neo) - 2
        order = 2 ** l - 1

        return order ^ n