class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        '''
        s = s.upper()
        res = ""
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                res = s[i] + res
                count += 1
                if count > 0 and count % k == 0:
                    res = "-" + res
        if len(res) > 0 and res[0] == "-":
            return res[1:]

        return res
        '''

        s = s.upper()
        res = []
        cur = ""
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                cur = s[i] + cur
                count += 1
                if count > 0 and count % k == 0:
                    res.append(cur)
                    cur = ""
        if cur:
            res.append(cur)

        return "-".join(res[::-1])

