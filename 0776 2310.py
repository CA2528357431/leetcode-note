class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        for i in range(1, 11):
            num -= k
            if num < 0:
                return -1
            if num % 10 == 0:
                return i
        return -1
