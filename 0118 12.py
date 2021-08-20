class Solution:
    def intToRoman(self, num: int) -> str:
        ori = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        sthnum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        res = ""
        for x in range(12):
            sth = num // sthnum[x]
            res += sth * ori[x]
            num = num % sthnum[x]
        res += num * "I"
        return res

    # 把900、400等也当作一个位
