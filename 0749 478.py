class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        lli = [x.split("@") for x in emails]
        l = [x[0] for x in lli]
        g = [x[1] for x in lli]
        def deal(s):
            ii = -1
            for i in range(len(s)):
                if s[i]=="+":
                    ii = i
                    break
            if ii>=0:
                s = s[:ii]
            li = s.split(".")
            res = "".join(li)
            return res
        l = [deal(x) for x in l]

        s = set()
        for i in range(len(l)):
            s.add(l[i]+"@"+g[i])
        return len(s)