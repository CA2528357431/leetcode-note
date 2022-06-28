class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        r = 1
        cur = 0
        if s[0] == "+":
            cur = 1
        elif s[0] == "-":
            cur = 1
            r = -1
        neo = 0
        for x in range(cur, len(s)):
            if s[x] in "1234567890":
                neo = neo * 10 + int(s[x])
            else:
                break

        neo = r * neo
        if -2 ** 31 <= neo <= 2 ** 31 - 1:
            return neo
        elif neo > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return -2 ** 31
