class Solution:
    def calPoints(self, ops: List[str]) -> int:
        li = []
        for s in ops:
            if s=="+":
                li.append(li[-1]+li[-2])
            elif s=="D":
                li.append(li[-1]*2)
            elif s=="C":
                li.pop()
            else:
                li.append(int(s))
        return sum(li)