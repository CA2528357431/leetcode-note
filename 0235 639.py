class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        la = 1
        cur = 0
        if s[0] == "0":
            cur = 0
        elif s[0] == "*":
            cur = 9
        else:
            cur = 1

        for x in range(1, n):
            neo = 0
            if s[x] == "0":
                pass
            elif s[x] == "*":
                neo += cur * 9
            else:
                neo += cur

            if s[x - 1] == "*":
                if s[x] == "*":
                    neo += la * 15
                elif s[x] in "0123456":
                    neo += la * 2
                else:
                    neo += la
            elif s[x - 1] in "123456789":
                if s[x] == "*":
                    if s[x - 1] == "1":
                        neo += la * 9
                    elif s[x - 1] == "2":
                        neo += la * 6
                elif int(s[x - 1:x + 1]) <= 26:
                    neo += la

            la, cur = cur, neo

        return cur % (10 ** 9 + 7)