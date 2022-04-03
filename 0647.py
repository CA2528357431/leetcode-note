class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def get(s):
            h,m = s.split(":")
            minute = int(h)*60+int(m)
            return minute
        mincu = get(current)
        minco = get(correct)
        delta = minco-mincu
        do = 0
        do+=delta//60
        delta %= 60
        do+=delta//15
        delta %= 15
        do+=delta//5
        delta %= 5
        do+=delta
        return do