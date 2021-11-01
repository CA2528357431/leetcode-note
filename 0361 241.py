class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        def deal(l,r):
            if "+" not in expression[l:r+1] and "-" not in expression[l:r+1] and "*" not in expression[l:r+1] :
                return [int(expression[l:r+1])]
            res = []
            for i in range(l,r):
                if expression[i] not in "+-*":
                    continue
                ll = deal(l,i-1)
                rr = deal(i+1,r)
                for x in ll:
                    for y in rr:
                        if expression[i]=="+":
                            res.append(x+y)
                        elif expression[i]=="-":
                            res.append(x-y)
                        else:
                            res.append(x*y)
            return res
        return deal(0,n-1)