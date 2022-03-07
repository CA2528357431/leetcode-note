class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        fromal = ord(s[0])
        toal = ord(s[3])
        fromnum = int(s[1])
        tonum = int(s[4])
        res = []
        for a in range(fromal, toal + 1):
            alpha = chr(a)
            for num in range(fromnum, tonum + 1):
                res.append(alpha + str(num))
        return res

