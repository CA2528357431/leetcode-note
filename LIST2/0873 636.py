class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        cur = []
        res = [0]*n
        pre = 0
        for x in logs:
            sth,do,t = x.split(":")

            sth = int(sth)
            t = int(t)

            if len(do)==5:
                if not cur:
                    cur = [sth]
                    pre = t
                else:
                    res[cur[-1]] += t-pre
                    cur.append(sth)
                    pre = t
            else:
                cur.pop()
                res[sth] += t-pre+1
                pre = t+1


        return res