class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # 二分法思想

        if dividend == 0:
            return 0

        on = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            on = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        r = 1
        lr = r
        d = divisor
        ld = d

        neo = 0

        while d <= dividend:
            ld = d
            lr = r
            if d == dividend:
                neo = r * on
                break

            else:
                r = r + r
                d = d + d
        if neo==0:
            neo = (self.divide(dividend - ld, divisor) + lr) * on
        if neo < -2 ** 31:
            return -2 ** 31
        elif neo > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return neo