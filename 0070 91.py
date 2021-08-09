class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)

        if n == 1:
            return 1

        la = 1
        if s[0] == "0":
            cur = 0
        else:
            cur = 1

        for x in range(1, n):
            neo = 0
            if s[x] != "0":
                neo += cur
            if s[x - 1] != "0" and int(s[x - 1:x + 1]) <= 26:
                neo += la
            la, cur = cur, neo

        return cur