class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def add(l,r,li):
            if l==n:
                li = [x+")"*(n-r) for x in li]
                return li
            else:
                if l==r:
                    li = [x+"(" for x in li]
                    return add(l+1,r,li)
                else:
                    li1 = [x+")" for x in li]
                    li2 = [x+"(" for x in li]
                    return add(l+1,r,li2)+add(l,r+1,li1)
        res = add(0,0,[""])
        return res