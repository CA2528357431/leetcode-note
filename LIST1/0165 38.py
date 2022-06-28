class Solution:
    def countAndSay(self, n: int) -> str:
        la = "1"

        for x in range(n - 1):
            cur = la[0]
            num = 1
            neo = ""
            for r in range(1, len(la)):
                if la[r] != cur:
                    neo += str(num)
                    neo += cur
                    cur = la[r]
                    num = 1
                else:
                    num += 1
            neo += str(num)
            neo += cur

            la = neo
        return la