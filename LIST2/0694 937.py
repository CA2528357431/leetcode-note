class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort(s):
            li = s.split()
            res1 = 0
            res2 = ""
            res3 = ""
            if li[1].isnumeric():
                res1 = 1
            else:
                res2 = " ".join(li[1:])
                res3 = li[0]
            return (res1,res2,res3)
        logs.sort(key=sort)
        return logs
