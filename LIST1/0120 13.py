class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        res = 0
        i = 0
        while i < len(s):
            if i <= len(s) - 2:
                cur = s[i] + s[i + 1]
                if cur in dic:
                    i += 2
                    res += dic[cur]
                    continue

            res += dic[s[i]]
            i += 1
        return res