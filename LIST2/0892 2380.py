class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        connect = 0
        tar = 0
        res = 0
        for i in range(n):

            if s[i] == "1":
                if i == tar:
                    tar += 1
                    continue
                connect += 1
                neo = i - tar + (connect - 1)
                res = max(res, neo)
                tar += 1
            else:
                connect -= 1
                if connect < 0:
                    connect = 0

        return res