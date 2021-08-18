class Solution:
    def reverse(self, x: int) -> int:
        neo = 0
        r = 1
        if x < 0:
            r = -1
            x = -x
        while x != 0:
            temp = x % 10
            x = x // 10
            neo = neo * 10 + temp

        if -2 ** 31 <= neo <= 2 ** 31 - 1:
            return neo * r
        else:
            return 0
