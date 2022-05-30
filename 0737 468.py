class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP)>4*8+7:
            return "Neither"
        if "." in queryIP:
            # ip4
            li = queryIP.split(".")
            if len(li)!=4:
                return "Neither"
            for s in li:
                if s.isdigit() and int(s)<=255 and str(int(s))==s:
                    continue
                return "Neither"
            return "IPv4"

        else:
            li = queryIP.split(":")
            if len(li)!=8:
                return "Neither"
            for s in li:
                if len(s)>4 or len(s)<1:
                    return "Neither"
                for c in s:
                    if c not in "abcdefABCDEF1234567890":
                        return "Neither"

            return "IPv6"
