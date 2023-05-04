class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        cur = ""
        for c in s:
            if c != cur:
                if c == "1":
                    cnt += 1
                cur = c
            # print(cnt)

        return cnt < 2
